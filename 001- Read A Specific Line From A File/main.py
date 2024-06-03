
def read_line_in_file():
    filename = input("File: ")
    line_number = int(input("Line: "))

    try:
        # open a file 
        file = open(filename, 'r')

        # red file lines as list []
        # ex: ['Line 1.\n', 'Line 2.\n', 'Line 3.\n', 'Line 4.\n', 'Line 5.']
        lines = file.readlines()

        # close the file
        file.close()
    except:
        print('Error reading the file.')
        return

    # print(f'file->{file}')
    # print(f'lines->{lines}')

    # get the length of the lines list
    total_lines = len(lines)

    if line_number > total_lines:
        print(str(total_lines) + " file lines.")
        print("Can't read line " + str(line_number) + "!")
    else:
        line = lines[line_number - 1].rstrip('\n')
        print(line)

def main():
    read_line_in_file()

main()
