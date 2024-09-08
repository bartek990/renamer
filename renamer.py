import os

LINE = ('-' * 80)

def main():
    # names = load_names()
    # create_files('names')
    list_of_files = get_list_of_files()
    show_names(list_of_files)
    extension = input('Wybierz rozszerzenie plików do edycji : ')
    # remove_from_list(list_of_files, [0, 10, 11, 12, 13])
    # os.system('export TERM=xterm-256color')
    # os.system('clear')
    list_of_files = pick_file_extension(list_of_files, extension)
    show_names(list_of_files)

    # new_names = remove_word(names, '_xvid')
    # new_names = remove_word(new_names, '_001')
    # commands = ''
    
    # for index in range(len(names)):
        # name = names[index]
        # name = name.replace('_xvid','')
        # name = name.replace('_001','')
        # name = name.replace('Dekalog ','')
        # name_arr = name.split()

        # new_names.append(f"Dekalog S01E0{roman_to_int(name_arr[0])} - {name}")

    # print(in_string_after_add(new_names[0], 'Dekalog', 'S01E0 -'))
    #
    # commands = make_commands(names, new_names)

    # print(commands)
    # export_commands(commands)

def load_names(file: str) -> []:
    """Returns an array of names from **file**"""
    names = []

    f = open(file, "r")
    while True:
        content = f.readline().replace('\n','')
        if not content:
            break
        names.append(content)
    f.close()
    return names

def create_files(files_names: str) -> None:
    """Creates empty files from **file** with *file_names*"""
    names = load_names(files_names)
    for n in names:
        f = open(n, 'w')
        f.close()

def get_list_of_files(my_path: str = os.getcwd()) -> [str]:
    """Returns an array with names of files from active directory or *my_path*"""
    files = [f for f in os.listdir(my_path) if os.path.isfile(os.path.join(my_path, f))]
    files.sort()
    return files

def show_names(name_list: [str]) -> None:
    """Shows numbered list of names"""
    print(LINE)
    if len(name_list) == 0:
        print('BRAK')
        return None

    for n in range(len(name_list)):
        print(f'{n + 1}.\t{name_list[n]}')

def remove_from_list(name_list: [str], num_arr: [int]) -> None:
    """Removes names from list"""


    if num_arr is None:
        show_names(name_list)
        numbers = input('Podaj numery nazw do usunięcia z listy: ')
        numbers = numbers.split(', ')
        num_arr = [int(n) - 1 for n in numbers if n.isnumeric()]

    rem_arr = [name_list[n] for n in num_arr]
    for r in rem_arr:
        name_list.remove(r)

def remove_word(old_names: [str], word:str) -> [str]:
    """Returns new_names array from given old_names array and word to remove or None"""
    new_names = []
    for index in range(len(old_names)):
        new_names.append(old_names[index].replace(word, ''))
    return new_names

def pick_file_extension(files_list: [str], extension: str) -> []:
    """Returns a **list** from *files_list* only with *extensions*"""
    new_list = [n for n in files_list if n.endswith(extension)]
    show_names(new_list)
    choice = input('Zatwierdzić listę? [t/N]: ')
    if choice.lower() == 't':
        return new_list
    return files_list

def in_string_after_add(string: str, after_word: str, add_word: str) -> str:
    """Adds add_word after after_word in given old_name and returns a string"""
    string = string.split()
    new_string = []
    for index in range(len(string)):
        new_string.append(string[index])
        if string[index] == after_word:
            new_string.append(add_word)

    return ' '.join(new_string)

def make_commands(old_names: [str], new_names: [str]) -> str | None:
    """Returns a string with "mv 'old_name' 'new_name'" commands or empty string"""
    commands = ''

    if len(old_names) != len(new_names):
        return None

    for index in range(len(old_names)):
        commands = commands + f"mv '{old_names[index]}' '{new_names[index]}'\n"

    return commands

def export_commands(all_commands: str, file: str = 'commands') -> None:
    """Writes commands to a file (default 'commands')"""
    f = open(file, 'w')
    f.write(all_commands)
    f.close()

def roman_to_int(s: str) -> int:
    """Returns int from given roman number"""
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for numeral in reversed(s):
        current_value = roman_values[numeral]

        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value

        prev_value = current_value

    return total

if __name__ == '__main__':
    main()