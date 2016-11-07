def listoverlap(a, b):
    c = []
    actual = 0
    for i in a:
        if i in b and actual != i:
            c.append(i)
            actual = i

        '''for j in b:
            if a[i] != actual:
                if a[i] == b[j]:
                    c.append(a[i])
                    actual = a[i]
                    '''

    return c


def main():
    c = []
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = listoverlap(a, b)
    print(c)

    return


if __name__ == '__main__':
    main()
