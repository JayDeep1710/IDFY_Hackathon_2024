def print_dict_in_color(data_dict):
    red = '\033[91m'  # Red color for keys
    green = '\033[92m'  # Green color for values
    reset = '\033[0m'  # Reset color to default

    max_key_length = max(len(str(key)) for key in data_dict.keys())
    
    print(f'{"PII Type".ljust(max_key_length)} | Found')
    print('-' * (max_key_length + 8))

    for key, value in data_dict.items():
        print(f'{red}{str(key).ljust(max_key_length)}{reset} | {green}{value}{reset}')