def convert(s):
    s1 = "\N{Slightly Smiling Face}"
    s2 = "\N{Slightly Frowning Face}"
    s = s.replace(':)', s1)
    s = s.replace(':(', s2)
    return s

def main():
    s = input()
    s = convert(s)
    print(s)

main ()