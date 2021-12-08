def get_number_codes(line):
    number_codes = [''] * 10
    def infer_number_from_code(mystery_code):
        if len(mystery_code) == 5:
            if all(digit in [x for x in mystery_code] for digit in [x for x in number_codes[1]]):
                return 3
            elif len(set([x for x in number_codes[4]]) - set([x for x in mystery_code])) == 2:
                return 2
            else:
                return 5
        else:
            if all(digit in [x for x in mystery_code] for digit in [x for x in number_codes[4]]):
                return 9
            elif all(digit in [x for x in mystery_code] for digit in [x for x in number_codes[1]]):
                return 0
            else:
                return 6

    (digits, outputs) = line.split("|")
    digits = digits.split(" ")
    outputs = outputs.split(" ")
    number_codes[1] = next(x for x in digits if len(x) == 2)
    number_codes[7] = next(x for x in digits if len(x) == 3)
    number_codes[4] = next(x for x in digits if len(x) == 4)
    number_codes[8] = next(x for x in digits if len(x) == 7)
    the_remaining_codes = [x for x in digits if len(x) == 5 or len(x) == 6]
    for code in the_remaining_codes:
        number_codes[infer_number_from_code(code)] = code

    return number_codes


with open('input.txt') as incoming:
    lines = incoming.readlines()
    for line in lines:
        print(get_number_codes(line))
