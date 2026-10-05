

"""
def sjakkbrett(n):

    for y in range(1, n + 1, 1):
        linje = ""
        for x in range(1, n + 1, 1):
            if (y + x) % 2 == 0:
                linje += "|"
            else:
                linje += "-"

        print(linje)


sjakkbrett(10)

"""

"""
def loop(a):
    count = 0

    i = 0

    while i < a:
        i += 2
        count += 1
        print(f'before if setning: i = {i}, count = {count}')

        if i % 2 == 0:
            i -= 1
            print(f'inside: i = {i}, count = {count}')

    return count

loop(89)
"""

"""
def collatz(n):
    i = 0

    while n > 1: 
        if (n % 2) == 0:
            n = int(n / 2)
        else:
            n = n*3 + 1

        i += 1
        print(f'runde {i}, tall: {n}')
    return n

collatz(10)
"""

"""
def palindrom(s):
    omvendt = ""
    for tegn in s:
        omvendt = tegn + omvendt 
        print(omvendt)
    print(s)
    return s == omvendt

print(palindrom("bobby"))

"""

"""
def palindrome(s):
    for i in range(len(s)):
        if s[i] == s[len(s) - 1 - i]:
            return False
    return True

print(palindrome("koky"))
"""

