def untouchable_function(n):
    if n == 0:
        return
    untouchable_function(n-1)


if __name__ == '__main__':
    untouchable_function(100)