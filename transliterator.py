import sys


def transliterate(chain):
    result = []

    i = 0
    while i < len(chain):
        if chain[i].isalpha():
            result.append([chain[i], "letter"])
        elif chain[i].isdigit():
            result.append([chain[i], "digit"])
        elif chain[i] == ':':
            result.append([':', "colon"])
        elif chain[i] == '=':
            result.append(['=', "equals"])
        elif chain[i] == '+' or chain[i] == '-':
            result.append([chain[i], "sign"])
        elif chain[i] == '*':
            result.append([chain[i], "arithmetic sign"])
        elif chain[i] == ' ':
            result.append([chain[i], "space"])
        elif chain[i] == '[':
            result.append([chain[i], "opening square bracket"])
        elif chain[i] == ']':
            result.append([chain[i], "closing square bracket"])
        elif chain[i] == '(':
            result.append([chain[i], "opening bracket"])
        elif chain[i] == ')':
            result.append([chain[i], "closing bracket"])
        elif chain[i] == ',':
            result.append([chain[i], "comma"])
        elif chain[i] == ';':
            result.append([chain[i], "semicolon"])
        else:
            sys.exit("Unexpected symbol: " + chain[i])

        i += 1

    return result
