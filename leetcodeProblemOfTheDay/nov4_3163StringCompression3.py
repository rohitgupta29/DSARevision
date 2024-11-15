


def compressedString(word):

    if len(word) == 0:
        return ""

    comp = ""
    index = 0

    length = len(word)

    while index < length:
        current_char = word[index]
        count = 0

        # count consecutive characters
        while index < length and count < 9 and word[index] == current_char:
            count += 1
            index += 1

        # if count > 9:
        #     comp += "9" + current_char
        #     count -= 9
        #
        #     while count > 0:
        #         comp += "9" + current_char
        #         count -=9

        if count > 0:
            comp += str(count) + current_char

    return comp


res = compressedString("aaaaaaaaaaaaaaaaaaaaaaaaaaabcde")

print(res)
