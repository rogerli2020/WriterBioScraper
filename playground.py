import json
import re

# Load JSON content from file
with open('./assets/domain_profile_url_regex.json', 'r') as json_file:
    data = json.load(json_file)

# Get the regex pattern from the JSON
regex_pattern = data.get('www.cityandstateny.com', '')

# Compile the regex pattern
compiled_regex = re.compile(regex_pattern)

# Test the regex with a sample URL
sample_url = 'https://www.cityandstateny.com/voices/fuck_you/163462345/'
match = compiled_regex.match(sample_url)

if match:
    print("URL matches the pattern!")
else:
    print("URL does not match the pattern.")
