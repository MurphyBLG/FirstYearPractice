import sys


def transliterate(chain):
    result = []

    i = 0
    while i < len(chain):
        if chain[i].isalpha():
            result.append([chain[i], "letter"])
        elif chain[i].isdigit():
            result.append([chain[i], "digit"])
        elif i + 1 < len(chain) and chain[i] + chain[i + 1] == ":=":
            result.append([":=", "assignment operator"])
            i += 1
        elif chain[i] in ['+', '-', '*']:
            result.append([chain[i], "sign"])
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
