def roman_to_int(roman: str) -> int:

    if roman == "":
        raise ValueError("String cannot be empty")
    elif not roman.isupper():
        raise ValueError("String cannot be lower case")

    roman = list(roman)
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    current = []
    first = True
    for l in roman:
        if not first:
            if l == current[-1]:
                current.append(l)
                if l in ["I", "X", "C",] and len(current) > 3:
                    raise ValueError("Invalid repetition")
                elif l in ["V", "L", "D",] and len(current) > 1:
                    raise ValueError("Invalid repetition")
            else:
                current = [l]
        if l not in numerals:
            raise ValueError("Invalid character")
        if first:
            current.append(l)
        first = False


    total = 0
    subtract = False
    r = 0
    min_num = 1000
    while r < (len(roman)-1):
        if numerals[roman[r]] >= numerals[roman[r+1]]:
            total += numerals[roman[r]]
            subtract = False
            if int(numerals[roman[r]]) < min_num:
                min_num = int(numerals[roman[r]])
            r += 1
        else:
            subtracted_sum = numerals[roman[r+1]] - numerals[roman[r]]
            if subtracted_sum not in [4, 9, 40, 90, 400, 900]:
                raise ValueError("Invalid subtraction")
            else:
                total += subtracted_sum
            if numerals[roman[r+1]] > min_num:
                raise ValueError("Invalid ordering")
            subtract = True
            if int(numerals[roman[r]]) < min_num:
                min_num = int(numerals[roman[r]])
            r += 2
    if not subtract:
        total += numerals[roman[-1]]
    return total


