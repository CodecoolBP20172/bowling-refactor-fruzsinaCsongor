def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for idx, char in enumerate(game):
        if frame <= 10:
            if char.lower() == 'x':
                result += get_value(char)
                result += get_value(game[idx+1])
                if game[idx+2] == '/':
                    result += 10 - get_value(game[idx+1])
                else:
                    result += get_value(game[idx+2])
            elif char == '/':
                result += get_value(game[idx+1])
                result += 10 - last_tries_value
            else:
                result += get_value(char)
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if char.lower() == 'x':
            in_first_half = True
            frame += 1
        last_tries_value = get_value(char)
    return result


def get_value(char):
    if len(char) == 1 and char.isdigit():
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
