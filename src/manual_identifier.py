import json
from urllib.parse import urlparse

REGEX_ANY_SUBSTRING = '([^/]+)'
REGEX_ANY_NUMBER = '(\d+)'
REGEX_FILE_PATH = './assets/domain_profile_url_regex.py'
COMMON_FORMAT_PATH = './assets/common_formats.json'

def load_json(path):
    with open(path, 'r') as f: return json.load(f)

class ManualIdentifier:
    def __init__(self, output_path) -> None:
        self.output_path = output_path
        self.common_formats = load_json(COMMON_FORMAT_PATH)
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
            'single_article_date',
            'single_article_title',
            'single_article_description',
            'single_article_url',
        ]
        self.non_selector_fields = ['outlet_name','url']

    
    def handle_regex_based_on_input(self, url):
        domain = urlparse(url).netloc
        url_regex = url.replace('.','\.')
        if input('About to enter REGEX information. Enter s to SKIP.') == 's': return
        string_fields = input('[REGEX GENERATION] Enter string field text (delimiter: space): ')
        numeric_fields = input('[REGEX GENERATION] Enter numeric field text (delimiter: space): ')
        string_fields, numeric_fields = string_fields.split(' '), numeric_fields.split(' ')
        for field in string_fields:     
            if field: url_regex = url_regex.replace(field, REGEX_ANY_SUBSTRING)
        for field in numeric_fields:    
            if field: url_regex = url_regex.replace(field, REGEX_ANY_NUMBER)
        url_regex += '$'
        newline_to_write = '\t' + f"'{domain}'" + ' : ' + 'r' + f"'{url_regex}'" + ',\n'
        filelines = []
        with open(REGEX_FILE_PATH, 'r') as f: filelines = f.readlines()
        filelines.insert(-1, newline_to_write)
        with open(REGEX_FILE_PATH, 'w') as f: f.write(''.join(filelines))


    def remove_substring_loop(self, string):
        while True:
            user_input = input('Substring to remove? (ENTER to skip): ').replace('\n','')
            if user_input in [' ', '']:
                return string
            string = string.replace(user_input, '')

    def start(self):
        counter = 0
        broken = False
        outlet_name, url = None, None
        while not broken:
            used_common_format = False
            res = {'selectors':{}, 'post_selectors': {}, 'selectors_type': 'css'}
            print('\nDIRECTION: ENTER if field is None, -s to stop')
            for field in self.fields:
                user_input = input(f'{field}: ').replace('\n','')
                if field == 'outlet_name': outlet_name = user_input
                if field == 'url': url = user_input
                if 'article' in field:
                    user_input = self.remove_substring_loop(user_input)
                if user_input in self.common_formats:
                    res = self.common_formats[user_input]
                    used_common_format = True
                    break
                if field == 'url': self.handle_regex_based_on_input(user_input)
                if len(user_input) == 0: user_input = None
                if (not user_input and field == 'outlet_name') or (user_input == '-s'):
                    broken = True
                    break
                if field in self.non_selector_fields:
                    res[field] = user_input
                else:
                    res['selectors'][field] = user_input

            entering_post_selectors = True
            while entering_post_selectors and not used_common_format:
                post_selector_input = input("Enter a post-selector (ENTER to skip): ")
                if post_selector_input in self.common_formats:
                    res = self.common_formats[user_input]
                    used_common_format = True
                    break
                if post_selector_input:
                    post_selector_input = post_selector_input.split(' ', 1)
                    if len(post_selector_input) < 2:
                        print('Invalid input. Needs at least 1 space.')
                    res['post_selectors'][post_selector_input[0]] = post_selector_input[1]
                else:
                    entering_post_selectors = False

            if used_common_format: res['outlet_name'], res['url'] = outlet_name, url
            if not broken: self.write_to_output(res)
            counter += 1
        print(f'Finished! {counter - 1} new items added!')

    def write_to_output(self, item : dict):
        with open(self.output_path, '+a') as f:
            json_line = json.dumps(item, indent=4)
            f.write(json_line + '\n')