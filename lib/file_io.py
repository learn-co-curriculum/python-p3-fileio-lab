def write_file(file_name, file_content):
    with open(file_name, mode='w', encoding='utf-8') as write_file:
        write_file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name, mode='a', encoding='utf-8') as append_file:
        append_file.write(append_content)

def read_file(file_name):
    with open(file_name, mode='r', encoding='utf-8') as read_file:
        return read_file.read()

