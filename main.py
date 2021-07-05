from transliterator import transliterate
from lexic import convert_to_lexemes


def main():
    s = input()
    temp = transliterate(s)
    ans = convert_to_lexemes(temp)

    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
