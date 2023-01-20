def div42(div):
    try:
        return 42 / div
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42(2))
print(div42(12))
print(div42(0))
print(div42(1))