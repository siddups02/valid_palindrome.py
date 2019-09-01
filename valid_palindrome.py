import re
def check(s):
    s = s.lower()
    str = re.findall("[a-zA-Z0-9]", s)
    rstr = str[::-1]


    print(str)
    print(rstr)
    if str == rstr:
        return True
    else:
        return False

print (check("ab2a"))
