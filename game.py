def run_lvl1(s: str):
    print(f"""
        LVL1 
        1) .upper() делает все буквы заглавными
        s.upper() = {s.upper()}
        2) .lower() делает все буквы строчными
        s.lower() = {s.lower()}
        3) .capitalize() Делает первую букву заглавной, а остальные строчными
        s.capitalize = {s.capitalize()}
    """)

def run_lvl2(s: str):
    print(f"""
        LVL2
        1) Символ 'Ч' есть в вашей строке, значит .find и .index 
        будут работать одинаково:
        s.find('ч') = {s.find('ч')}
        s.index('ч') = {s.index('ч')}

        Но если символа нет в строке, то .index вызовет ошибку, а .find вернёт -1
        s.find('z') = {s.find(s[0])}
        s.index('z') = ValueError

        2) Первый индекс вхождения "круто" в s = {s.find('круто')}
        3) Количество букв "о" в строке s = {s.lower().count('о')}
        4) Изменяем подстроку "круто" на свою >> "{s.replace('круто', 'обязательно')}"
    """) 

def run_lvl3(s: str):
    print(f"""
        LVL3
        .split(sep: str, maxsplit: int) возвращает разделенную на подстроки строку в формате списка
        sep: str - разделитель
        maxsplit: int - максимальное количество делений
        s.split(sep=',', maxsplit=3) = {s.split(sep=',', maxsplit=-1)}

        'sep'.join(obj) возвращает строку, состоящую из последовательных строк из obj,
        разделённых строкой sep
        ' '.join(['1', '2', '3', '4', '5']) = "{' '.join(['1', '2', '3', '4', '5'])}"
    """)

def run_lvl4(s: str):
    print(f"""
        LVL4
        .isdigit() возвращает True, если строка состоит из цифр и содержит >= 1 символа, иначе - False 
        '123'.isdigit() = {'123'.isdigit()}
        s.isdigit() = {s.isdigit()}

        .isalpha() работает аналогично, только множество не цифр, а букв
        '123'.isalpha() = {'абв'.isalpha()}
        s.isalpha() = {s.isalpha()}

        .strip(chars) возвращает искомую строку без ведущих символов из chars с обеих сторон
        ' 123'.strip(' ') = "{' 123'.strip()}"
        s.strip('_') = "{s.strip()}"

        * lstrip и rstrip - left и right strip, соответственно убирают символы только с этих сторон
        '_1'.lstrip('_') = "{'_1'.lstrip('_')}"
        '_1'.rstrip('_') = "{'_1'.rstrip('_')}"
    """)

def run_lvl5(s: str):
    print(f"""
        LVL5
        s.strip('_ ;').capitalize().replace(';', ' ') = "{s.strip('_ ;').capitalize().replace(';', ' ')}"
    """)

run_lvl1("прИвЕт_МИР")
run_lvl2("Ботать_-_это круто. Очень круто!")
run_lvl3("1,2,3,4,5")
run_lvl4("_ПП__")
run_lvl5("__PyTHOn;is;AweSOMe;____")

