inputstr = input()


def gencipher(s):
    ret = ""
    for i in range(len(s)):
        if 97 <= ord(s[i]) and ord(s[i]) <= 122:
            ret += chr(219 - ord(s[i]))
        else:
            ret += s[i]
    return ret


print(gencipher(inputstr))
