def setify(code):
    return set([char for char in code])


def infer_number_by_comparing_to_1_and_4(mystery_code, one_code, four_code):
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
    for digit_and_length in [(1, 2), (7, 3), (4, 4), (8, 7)]:
        number_codes[digit_and_length[0]] = next(x for x in digit_codes if len(x) == digit_and_length[1])
    the_remaining_codes = [x for x in digit_codes if len(x) == 5 or len(x) == 6]
    for code in the_remaining_codes:
        number_codes[infer_number_by_comparing_to_1_and_4(code, number_codes[1], number_codes[4])] = code
    return number_codes


def translate_output(output_codes, legend):
    output_digits = ''
    for code in output_codes:
        for i in range(10):
            if setify(legend[i]) == setify(code.rstrip()):
                output_digits += str(i)
    return output_digits


with open('input.txt') as incoming:
    lines_of_input = incoming.readlines()
    sum_of_readouts = 0
    for line in lines_of_input:
        (digit_string, output_string) = line.split("|")
        sum_of_readouts += int(translate_output(output_string.split(" "), get_number_codes(digit_string.split(" "))))
    print(sum_of_readouts)
