from manual_identifier import ManualIdentifier

LOCAL_FILE_PATH = "./regex.csv"

def generate_regex_from_local_file(file_path=LOCAL_FILE_PATH):
    lines = []
    with open(file_path, 'r') as f:
        lines = [line.rstrip() for line in f]
    lines = [line.split(',') for line in lines]
    for line in lines:
        my_url = line[2]
        my_string_fields = line[3]
        my_numeric_fields = line[4]
        print(my_url,my_string_fields,my_numeric_fields)
        if not my_url: continue
        manual_identifier = ManualIdentifier('./o')
        manual_identifier.handle_regex_based_on_input(
            my_url, 
            False, 
            my_string_fields, 
            my_numeric_fields
        )

generate_regex_from_local_file()