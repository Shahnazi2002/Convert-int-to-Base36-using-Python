def decToBase36(number):
    base = 36
    result = ""
    while True:
        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if number < base:
            result = symbols[number] + result
            break
        else:
            div, mod = divmod(number, base)
            result = symbols[mod] + result
            number = div
    return result

print(decToBase36(1381))
