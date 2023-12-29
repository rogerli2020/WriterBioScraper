import re


class Node:
    def __init__(self, data : str, layer) -> None:
        self.data = data
        self.layer = layer
        self.children = []
        self.weight = 0
    
    def add_child(self, node):
        self.children.append(node)


class Layer:
    def __init__(self, layer_depth, parent=None) -> None:
        self.layer_depth = layer_depth
        self.parent = parent
        self.nodes = []
        self.weight = 0
        self.cur_index = 0
    
    def add_node(self, node : Node):
        self.nodes.append(node)

    def add_weight(self, weight):
        def add_weight_to_parents(layer, weight):
            if not layer.parent: return
            layer.parent.weight += weight / 2
            add_weight_to_parents(layer.parent, weight / 2)
        self.weight += weight
        add_weight_to_parents(self, weight)
    
    def get_next_node(self) -> Node:
        if len(self.nodes) == 0: 
            return None
        if self.is_done(): 
            return None
        next_node = self.nodes[self.cur_index]
        self.cur_index += 1
        print(f'\t[Node Selected] {next_node.data}\tDEPTH {self.layer_depth}\tLAYER_WEIGHT {self.weight}')
        return next_node

    def is_done(self):
        return self.cur_index >= len(self.nodes)
    
    def is_empty(self):
        return len(self.nodes) == 0


class CrawlerTree:
    def __init__(self, outlet : str, root_url : str, profile_url_regex) -> None:
        self.outlet = outlet
        self.root_url = root_url
        self.profile_url_regex = profile_url_regex
        self.layers : list[Layer] = []
        self.visited = set()
        self.captured = set()
        self.finished = False
        self._initiate()


    def _initiate(self):
        first_layer = Layer(layer_depth=0, parent=None)
        self.layers.append(first_layer)
        first_node = Node(data=self.root_url, layer=first_layer)
        self.insert_new_node(first_node, 0)


    def get_layer_by_depth(self, depth : int):
        if depth <= len(self.layers) - 1:
            return self.layers[depth]
        return None
    

    def insert_new_node(self, node, layer_depth):
        if node.data in self.visited: return
        self.visited.add(node.data)
        self.get_layer_by_depth(layer_depth).add_node(node)
    

    def update_node_weight(self, node : Node):
        weight = 0
        for child in node.children:
            if re.match(self.profile_url_regex, child.data): 
                if child.data not in self.captured:
                    with open('./output/captured_urls.txt', '+a') as f:
                        f.write(child.data + '\n')
                    self.captured.add(child.data)
                weight += 1
        node.weight = weight
        node.layer.add_weight(weight)


    # def update_layer_weight(self, layer : Layer):
    #     def update_parent_layer_weight(child_layer, child_weight):
    #         if not child_layer.parent: return
    #         child_layer.parent.weight += child_weight / 2
    #         update_parent_layer_weight(child_layer.parent, child_weight / 2)
    #     weight = 0
    #     for node in layer.nodes: weight += node.weight
    #     layer.weight = weight
    #     update_parent_layer_weight(layer, 1)
        # print(f'Layer weight updated: DEPTH {layer.layer_depth}, WEIGHT {weight}, SIZE {len(layer.nodes)}')


    def get_next_layer(self) -> Layer:
        unfinished_layers = []
        for layer in self.layers: 
            if not layer.is_done() and not layer.is_empty(): unfinished_layers.append(layer)
        if len(unfinished_layers) == 0: return None
        same_weight_across = True
        first_weight = unfinished_layers[0].weight
        for layer in unfinished_layers:
            if layer.weight != first_weight:
                same_weight_across = False
                break
        if same_weight_across:
            return unfinished_layers[-1]
        return max(unfinished_layers, key=lambda layer: layer.weight)


    def get_next_node(self):
        next_layer = self.get_next_layer()
        if not next_layer: 
            print('No more layers to process...')
            return None
        return next_layer.get_next_node()
    

    def add_new_layer(self, depth : int) -> Layer:
        new_layer = Layer(depth, parent=self.layers[-1])
        self.layers.append(new_layer)
        # print(f'New layer added! Depth {depth}')
        return new_layer


    def generate_and_add_child_nodes(self, node : Node, urls : list[str]):
        parent_node_layer_depth = node.layer.layer_depth
        child_node_layer_depth = parent_node_layer_depth + 1
        child_layer : Layer = self.get_layer_by_depth(child_node_layer_depth)
        if not child_layer: 
            child_layer = self.add_new_layer(child_node_layer_depth)
        for url in urls:
            if url in self.visited: continue
            new_node = Node(data=url, layer=child_layer)
            child_layer.add_node(new_node)
            node.add_child(new_node)
            self.visited.add(url)
        self.update_node_weight(node)
        # self.update_layer_weight(node.layer)
        print(f'\t[Node Updated] #CHILD {len(node.children)}\tWEIGHT {node.weight}')