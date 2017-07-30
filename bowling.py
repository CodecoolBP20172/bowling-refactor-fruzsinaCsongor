def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for idx, char in enumerate(game):  # enumerate()
        if frame <= 10:  # removed value equaling with 10, less then or equal to
            if char.lower() == 'x':  # lower()
                result += get_value(char)  # moved here from another if statement
                result += get_value(game[idx+1])
                if game[idx+2] == '/':
                    result += 10 - get_value(game[idx+1])
                else:
                    result += get_value(game[idx+2])
            elif char == '/':
                result += get_value(game[idx+1])
                result += 10 - last_tries_value  # moved here from another if statement
            else:
                result += get_value(char)  # moved here from another if statement

        if in_first_half is True:
            in_first_half = False
        else:
            frame += 1  # moved excess 'if' statement here
            in_first_half = True

        if char.lower() == 'x':  # lower()
            in_first_half = True
            frame += 1
        last_tries_value = get_value(char)
    return result


def get_value(char):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # list of numbers 1-9
    if char in nums:
        return int(char)
    elif char.lower() == 'x' or char == '/':  # lower(), one line for 10
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
