def add(word_ru, word_en):
    with open(name_file, 'a', 'utf-8') as file:
        file.append(f"{word_ru} {word_en}\n")


def get_list():
    with open(name_file, 'r', 'utf-8') as file:
        resutl = [row for row in file]
        return result


print('COMMANDS:')
print('  L - learning words')
print('  A - add the word')
print('  R - remove the word')
print('  list - list of words')
print('  exit - if you want to leave')

name_file = "list.txt"

command = ""

while command != "exit":
    if command == "L":
        print(get_list())
    elif command == "A":
        word_ru, word_en = input().split()
        add(word_ru, word_en)
    elif command == "R":
        remove()
    elif command == "list":
        list_of_words()

    command = input()
