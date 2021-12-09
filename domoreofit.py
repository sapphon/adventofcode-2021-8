def setify(code):
    return frozenset([char for char in code])


def infer_digit_by_comparing_to_1_and_4(mystery_code, one_code, four_code):
    if len(mystery_code) == 5:
        if setify(mystery_code).issuperset(setify(one_code)):
            return 3
        elif len(setify(four_code) - setify(mystery_code)) == 2:
            return 2
        else:
            return 5
    else:
        if setify(mystery_code).issuperset(setify(four_code)):
            return 9
        elif setify(mystery_code).issuperset(setify(one_code)):
            return 0
        else:
            return 6


def get_number_codes(digit_codes):
    number_codes = [''] * 10
    digit_codes.sort(key=len)
    for (digit, index) in [(1, 0), (7, 1), (4, 2), (8, 9)]:
        number_codes[digit] = digit_codes[index]
    the_remaining_codes = [digit_codes[x] for x in range(3, 9)]
    for code in the_remaining_codes:
        number_codes[infer_digit_by_comparing_to_1_and_4(code, number_codes[1], number_codes[4])] = code
    return number_codes


def translate_output(output_codes, legend):
    codes_to_digits = {setify(val): idx for idx, val in enumerate(legend)}
    output_digits = ''
    for code in output_codes:
        output_digits += str(codes_to_digits[setify(code)])
    return output_digits


with open('input.txt') as incoming:
    sum_of_readouts = 0
    for line in incoming.readlines():
        (digit_string, output_string) = map(str.strip, line.split("|"))
        sum_of_readouts += int(translate_output(output_string.split(" "), get_number_codes(digit_string.split(" "))))
    print(sum_of_readouts)
