import sys

special_symbols = ["assignment operator",
                   "space",
                   "comma",
                   "opening square bracket",
                   "closing square bracket",
                   "opening bracket",
                   "closing bracket",
                   "arithmetic sign",
                   "semicolon"]


def append_identifier(lexeme, result, next_lex):
    result.append([lexeme, "identifier"])
    result.append(next_lex)


def convert_to_lexemes(transliterated_chain):
    state = "start"
    lexeme = ''
    result = []

    i = 0
    while i < len(transliterated_chain):
        if state == "start":
            if transliterated_chain[i][1] == "letter":
                lexeme += transliterated_chain[i][0]
                state = "identifier"
            elif transliterated_chain[i][1] == "space":
                continue
            else:
                sys.exit("Identifier must be started with letter")

        elif state == "identifier":
            if transliterated_chain[i][1] in ["letter", "digit"]:
                lexeme += transliterated_chain[i][0]
            elif lexeme:
                append_identifier(lexeme, result, transliterated_chain[i])
                state = transliterated_chain[i][1]
                lexeme = ''

        elif state in special_symbols:
            if transliterated_chain[i][1] in ["letter", "digit", "sign"]:
                lexeme += transliterated_chain[i][0]
                if transliterated_chain[i][1] == "digit":
                    state = "integer constant"
                elif transliterated_chain[i][1] == "sign":
                    state = "sign"
                else:
                    state = "identifier"
            else:
                result.append(transliterated_chain[i])
                state = transliterated_chain[i][1]

        elif state == "integer constant":
            if transliterated_chain[i][1] == "digit":
                lexeme += transliterated_chain[i][0]
            elif lexeme:
                if len(lexeme) == 1 and lexeme in ['-', '+']:
                    result.append([lexeme, "arithmetic sign"])
                else:
                    result.append([lexeme, "integer constant"])
                lexeme = ''
                result.append(transliterated_chain[i])
                state = transliterated_chain[i][1]

        elif state == "sign":
            if transliterated_chain[i][1] == "sign":
                sys.exit("There is no such token")
            elif transliterated_chain[i][1] == "digit":
                lexeme += transliterated_chain[i][0]
                state = "integer constant"
            else:
                result.append([lexeme, "arithmetic sign"])
                result.append(transliterated_chain[i])
                state = transliterated_chain[i][1]
                lexeme = ''

        else:
            result.append(transliterated_chain[i])

        i += 1

    if lexeme:
        result.append([lexeme, ("integer", "signed integer")[lexeme[0] in ['-', '+']]])

    return result
