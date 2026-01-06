def add_digits(a, b, carry):

    total = a + b + carry

    digit = total % 10
    new_carry = total // 10

    print(digit, new_carry)


add_digits(8, 7, 0)
add_digits(3, 4, 1)
