import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():

    my_file = open("dictionary.txt")

    dictionary_list = []

    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)

    my_file.close()

    print("--- Linear Search ---")

# --- Linear search

    my_alice = open("AliceInWonderLand200.txt")

    for line in my_alice:
        word_list = split_line(line)

    current_list_position = 0

    while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word_list:

        current_list_position += 1

    if current_list_position < len(dictionary_list):
        print("The name is at position", current_list_position)
    else:
        print("The name was not in the list.")


main()
