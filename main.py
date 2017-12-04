

def init():
    int_input = input("[Введите число]--> ")

    if int(int_input) % 3 == 0:
        print('True')
    else:
        print('False')

    return init()


if __name__ == '__main__':
    init()
