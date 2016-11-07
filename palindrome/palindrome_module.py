def palindrome(str):
    transformed = ""

    for char in str:
        if char != " ":
            transformed += char.lower()

    checker = True
    j = len(transformed) - 1
    for i in range(0, len(transformed)):
        if transformed[i] != transformed[j]:
            checker = False
        j -= 1

    return checker


def main():
    bemenet = str(input("Please provide the text you want to check: "))

    check = palindrome(transformed)
    return


if __name__ == '__main__':
    main()
