import datetime


def years(age):
    today = datetime.date.today()
    hundredyears = int(today.year) + (100 - age)
    return hundredyears


def main():
    name = str(input("Please tell me your name: "))
    age = int(input("Please tell me your age: "))
    multiplier = int(input("How many times would you like to see the answer? "))

    hundredyears = years(age)
    for i in range(0, multiplier):
        print("Kedves {0}, Te {1}-ban/ben leszel 100 éves!".format(name, hundredyears))

    return


if __name__ == '__main__':
    main()
