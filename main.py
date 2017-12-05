# Описание задачи:
# На вход программа получает текст (файл с текстом (работа с файлами - усложненная вещь)), в каждом слове, где кол-во букв >6 сделать первую букву заглавной. На выходе нужно вывести на экран обработанный текст (записывать изменения в файл и сохранить).
#
# Повышения режима сложности за счет работы с файлами.
#
# Удачи.
#
# Напомню, если вы решаете новый модуль, то и загружать надо в новую ветку, пример: oappot/[Task]2

filename = 'text.txt'


def init(filename):
    f = open('text.txt', 'r', encoding="utf-8")
    list_words = f.read().split()

    list_upper_words = []

    for el in list_words:
        if len(el) > 6 and el[6] != ',' and el[6] != '.':
            list_upper_words.append(el.title())
        else:
            list_upper_words.append(el)

    new_text = str(" ".join(list_upper_words))
    print(new_text)

    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(new_text)  # python will convert \n to os.linesep
        f.close()


if __name__ == '__main__':
    init(filename)
