def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for idx, char in enumerate(game):  # enumerate()
        if char == '/':
            result += 10 - last
        else:
            result += get_value(char)
        if frame < 10 and get_value(char) == 10:
            if char == '/':
                result += get_value(game[idx+1])
            elif char.lower() == 'x':  # lower()
                result += get_value(game[idx+1])
                if game[idx+2] == '/':
                    result += 10 - get_value(game[idx+1])
                else:
                    result += get_value(game[idx+2])
        last = get_value(char)
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if char.lower() == 'x':  # lower()
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of numbers 1-9
    if char in nums:
        return int(char)
    elif char.lower() == 'x':  # lower()
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
