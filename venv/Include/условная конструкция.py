first =int(input("Введите число"))
if first % 3 == 0 and first % 2 == 0:
    print('FizzBuzz')
if first % 3 == 0:
    print('Fizz')
elif first % 2 == 0:
    print('Buzz')
