def helper(n: int, s: int):  # this function prints n to s in one line
    if n == s:
        print()
        return
    print(n, end=' ')
    helper(n + 1, s)


def helper_rev(n: int, s: int):  # this function prints lines of decreasing numbers
    if n == s:
        return
    helper(n, s)
    helper_rev(n, s - 1)


def helper_forward(n: int, s: int):  # this function prints lines of increasing numbers
    if n == s:
        return
    helper(0, n)
    helper_forward(n + 1, s)


def print_triangle(length: int):
    helper_forward(0, length)  # the pyramid increment first
    helper_rev(0, length)   # then decrement
    

def main():
    print_triangle(5)


if __name__ == '__main__':
    main()
