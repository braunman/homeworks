# Work with files
base_file_name = "text.txt"


def write_to_file(text, mode_type="w", filename=base_file_name):
    print("Write text to file '{}'".format(filename))
    with open(filename, mode=mode_type) as f:
        f.write(text)


def read_file_data(filename=base_file_name):
    print("Read file '{}':".format(filename))
    with open(filename) as f:
        return f.read()

if __name__ == '__main__':
    write_to_file("Hi, I'm new file\n")
    write_to_file("Second line", mode_type="a")
    print(read_file_data())
