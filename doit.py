with open('input.txt') as incoming:
    lines = incoming.readlines()
    countOf1478 = 0
    for line in lines:
        countOf1478 += len([x for x in line.split("|")[1].split(" ") if len(x.rstrip()) in [2, 3, 7, 4]])
    print(countOf1478)
