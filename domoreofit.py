def setify(code):
    return frozenset([char for char in code])


def get_digit_by_comparing_to_1_and_4(mystery_set, one_code, four_code):
    if len(mystery_set) == 5:
        return 3 if mystery_set.issuperset(setify(one_code)) else 2 if len(setify(four_code) - mystery_set) == 2 else 5
    else:
        return 9 if mystery_set.issuperset(setify(four_code)) else 0 if mystery_set.issuperset(setify(one_code)) else 6


def get_digit_codes(digit_codes):
    digits_to_codes = [''] * 10
    digit_codes.sort(key=len)
    for (digit, index) in [(1, 0), (7, 1), (4, 2), (8, 9)]:
        digits_to_codes[digit] = digit_codes[index]
    for code in [digit_codes[x] for x in range(3, 9)]:
        digits_to_codes[get_digit_by_comparing_to_1_and_4(setify(code), digits_to_codes[1], digits_to_codes[4])] = code
    return digits_to_codes


def translate_output(output_codes, digits_to_codes):
    codes_to_digits = {setify(val): idx for idx, val in enumerate(digits_to_codes)}
    output_digits = ''
    for code in output_codes:
        output_digits += str(codes_to_digits[setify(code)])
    return output_digits


with open('input.txt') as incoming:
    sum_of_readouts = 0
    for line in incoming.readlines():
        (digit_string, output_string) = map(str.strip, line.split("|"))
        sum_of_readouts += int(translate_output(output_string.split(" "), get_digit_codes(digit_string.split(" "))))
    print(sum_of_readouts)
