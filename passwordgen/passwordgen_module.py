import random


def passwordgen():
    lowerLetters = ("abcdefghijlkmnopqrstuvwxyz")
    upperLetters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = ("0123456789")
    symbols = ("!@#$%^&*()?")
    words = ['pass1234', 'jelszo12', 'password', 'kutya678', 'cicacica']
    password = ""
    pwlength = random.randint(8, 16)

    while len(password) <= pwlength:
        pwtype = random.randint(1, 4)
        if pwtype == 1:
            pwchar = lowerLetters[random.randint(0, len(lowerLetters) - 1)]
            password += pwchar
        elif pwtype == 2:
            pwchar = upperLetters[random.randint(0, len(upperLetters) - 1)]
            password += pwchar
        elif pwtype == 3:
            pwchar = numbers[random.randint(0, len(numbers) - 1)]
            password += pwchar
        elif pwtype == 4:
            pwchar = symbols[random.randint(0, len(symbols) - 1)]
            password += pwchar

    return password


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
