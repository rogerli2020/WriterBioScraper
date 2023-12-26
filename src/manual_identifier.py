import json

class ManualIdentifier:
    def __init__(self, output_path) -> None:
        self.output_path = output_path
        self.fields = [
            'outlet_name',
            'url',
            'name',
            'title',
            'desc',
            'email',
            'twitter',
            'linkedin',
            'facebook',
            'instagram',
            'phone',
            'pfp',
            'single_article',
            'single_article_title',
            'single_article_description',
            'single_article_date',
            'single_article_url',
        ]
        self.non_selector_fields = ['outlet_name','url']


    def start(self):
        counter = 0
        broken = False
        while not broken:
            res = {'selectors':{}, 'post_selectors': {}}
            print('\nDIRECTION: ENTER if field is None, -s to stop')
            for field in self.fields:
                user_input = input(f'{field}:').replace('\n','')
                if len(user_input) == 0: user_input = None
                if (not user_input and field == 'outlet_name') or (user_input == '-s'):
                    broken = True
                    break
                if field in self.non_selector_fields:
                    res[field] = user_input
                else:
                    res['selectors'][field] = user_input

            entering_post_selectors = True
            while entering_post_selectors:
                post_selector_input = input("Enter a post-selector (ENTER to skip): ")
                if post_selector_input:
                    post_selector_input = post_selector_input.split(' ', 1)
                    if len(post_selector_input) < 2:
                        print('Invalid input. Needs at least 1 space.')
                    res['post_selectors'][post_selector_input[0]] = post_selector_input[1]
                else:
                    entering_post_selectors = False

            if not broken: self.write_to_output(res)
            counter += 1
        print(f'Finished! {counter - 1} new items added!')

    def write_to_output(self, item : dict):
        with open(self.output_path, '+a') as f:
            json_line = json.dumps(item, indent=4)
            f.write(json_line + '\n')