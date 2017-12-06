def decorator_func(inner_function):
     def showing_n(n):
         print(str(n))
         inner_function(n)

     return showing_n


@decorator_func
def untouchable_function(n):
     if n == 0:
         return
     untouchable_function(n - 1)


if __name__ == '__main__':
    untouchable_function(100)