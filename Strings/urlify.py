def urlify(s, i):
    s = list(s)
    p1, p2 = len(s) - 1, i - 1
    while p1 >= 0 and p2 >= 0:
        if s[p2] != " ":
            s[p1] = s[p2]
            p1 -= 1
            p2 -= 1
        else:
            for i in reversed("%20"):
                s[p1] = i
                p1 -= 1
            p2 -= 1
    return "".join(s)

print(urlify('Mr John Smith    ',13)) 
