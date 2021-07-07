import sys


def convert_to_lexemes(transliterated_chain):
    state = "start"
    lexeme = ''
    result = []
    acceptable = False

    for sym in transliterated_chain:
        if state == "start":
            if sym[1] == "letter":
                lexeme += sym[0]
                state = "var_name"
            elif sym[1] == "space":
                continue
            else:
                sys.exit("REJECT")

        elif state == "var_name":
            if sym[1] in ["letter", "digit"]:
                lexeme += sym[0]
            elif sym[1] == "space":
                result.append([lexeme, "variable name"])
                lexeme = ''
                state = "var_space"
            elif sym[1] == "assignment operator":
                result.append([lexeme, "variable name"])
                lexeme = ''
                state = "as_op"
                result.append([":=", "assignment operator"])
            else:
                sys.exit("REJECT")

        elif state == "var_space":
            if sym[1] == "space":
                continue
            elif sym[1] == "assignment operator":
                state = "as_op"
                result.append([":=", "assignment operator"])
            else:
                sys.exit("REJECT")

        elif state == "as_op":
            if sym[1] == "letter":
                lexeme += sym[0]
                state = "arr_name"
            elif sym[1] == "space":
                continue
            else:
                sys.exit("REJECT")

        elif state == "arr_name":
            if sym[1] in ["letter", "digit"]:
                lexeme += sym[0]
            elif sym[1] == "opening square bracket":
                result.append([lexeme, "array name"])
                result.append(sym)
                lexeme = ''
                state = "const_chain"
            else:
                sys.exit("REJECT")

        elif state == "const_chain":
            if sym[1] == "digit":
                lexeme += sym[0]
                state = "const"
            elif sym[1] == "sign":
                lexeme += sym[0]
                state = "check_on_sign"
            elif sym[1] == "space":
                continue
            else:
                sys.exit("REJECT")

        elif state == "const":
            if sym[1] == "digit":
                lexeme += sym[0]
            elif sym[1] == "closing square bracket":
                result.append([lexeme, "integer constant chain"])
                lexeme = ''
                result.append(sym)
                state = "chain_space"
            elif sym[1] == "comma":
                lexeme += sym[0]
                state = "const_chain"
            else:
                sys.exit("REJECT const")

        elif state == "check_on_sign":
            if sym[1] == "digit":
                lexeme += sym[0]
                state = "const"
            else:
                sys.exit("REJECT")

        elif state == "chain_space":
            if sym[1] == "letter":
                lexeme += sym[0]
                state = "sign_name"
            elif sym[1] == "sign":
                result.append([sym[0], "arithmetic sign"])
                state = "ar_sign"
            elif sym[1] == "space":
                continue
            else:
                sys.exit("REJECT")

        elif state == "sign_name":
            if sym[1] == "letter":
                lexeme += sym[0]
            elif sym[1] == "space":
                result.append([lexeme, "sign_identifier"])
                lexeme = ''
                state = "ar_sign"
            else:
                sys.exit("REJECT sign name")

        elif state == "ar_sign":
            if sym[1] == "letter":
                lexeme += sym[0]
                state = "f_name"
            elif sym[1] == "space":
                continue
            else:
                sys.exit("REJECT")

        elif state == "f_name":
            if sym[1] in ["letter", "digit"]:
                lexeme += sym[0]
            elif sym[1] == "opening bracket":
                result.append([lexeme, "function name"])
                result.append(sym)
                lexeme = ''
                state = "id_chain"
            else:
                sys.exit("REJECT")

        elif state == "id_chain":
            if sym[1] == "letter":
                lexeme += sym[0]
                state = "par_name"
            elif sym[1] == "space":
                continue
            else:
                sys.exit("REJECT")

        elif state == "par_name":
            if sym[1] in ["letter", "digit"]:
                lexeme += sym[0]
            elif sym[1] == "closing bracket":
                result.append([lexeme, "identifier chain"])
                lexeme = ''
                result.append(sym)
                state = "final"
            elif sym[1] == "comma":
                lexeme += sym[0]
                state = "id_chain"
            else:
                sys.exit("REJECT")

        elif state == "final":
            if sym[1] == "semicolon":
                result.append(sym)
                acceptable = True
            else:
                sys.exit("REJECT")

        else:
            sys.exit("REJECT")

    if not acceptable:
        sys.exit("REJECT")

    return result
