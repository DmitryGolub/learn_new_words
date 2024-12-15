import random


def add(word_ru, word_en):
    with open(name_file, 'a', encoding='utf-8') as file:
        file.write(f"{word_ru}{separator}{word_en}\n")


def get_words():
    with open(name_file, 'r', encoding='utf-8') as file:
        pairs = [row for row in file]
        list_ru_to_en = [pair.strip().split(separator) for pair in pairs]
        dict_ru_to_en = {}
        for pair in list_ru_to_en:
            dict_ru_to_en[pair[0]] = pair[1]
        return dict_ru_to_en


def remove():
    ...


print('COMMANDS:')
print('  learn - learning words')
print('  add - add the word')
print('  remove - remove the word')
print('  list - list of words')
print('  exit - if you want to leave')

name_file = "list.txt"
separator = "-"

command = ""

while command != "exit":
    if command == "learn":
        words = get_words()
        ru_words = list(words.keys())
        random.shuffle(ru_words)

        counter = 0
        
        for ru_word in ru_words:
            answer = input(f'{ru_word} > ')
            if answer.lower() == words[ru_word]:
                print('Yes')
                counter += 1
            else:
                print(f'No. {words[ru_word]}')

        print(f'{counter} from {len(ru_words)}')

    elif command == "add":
        word_ru, word_en = input("Russian word: "), input("English word: ")
        add(word_ru, word_en)
    elif command == "remove":
        remove()
    elif command == "list":
        print(get_words())

    command = input()
