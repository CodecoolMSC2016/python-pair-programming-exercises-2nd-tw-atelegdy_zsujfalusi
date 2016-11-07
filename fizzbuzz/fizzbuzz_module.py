def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"

    print(number)
    return number


def main():
    numbers = []

    for i in range(0, 100):
        numbers.append(i + 1)
        fizzbuzz(numbers[i])
    return

if __name__ == '__main__':
    main()
