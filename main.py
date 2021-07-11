from transliterator import transliterate
from lexic import convert_to_lexemes
from syntax import syntactic_check


def main():
    inp = open("INPUT.txt", 'r')
    s = inp.read()
    inp.close()

    output = open("OUTPUT.txt", 'w')

    transliterated_chain = transliterate(s)
    if transliterated_chain == "REJECT":
        output.write("REJECT")
        return
    else:
        lexemes = convert_to_lexemes(transliterated_chain)

    if lexemes == "REJECT":
        output.write("REJECT")
        return
    else:
        output.write(syntactic_check(lexemes))


if __name__ == '__main__':
    main()
