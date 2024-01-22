def a(b, c):
    print("\nhello from foo function a")
    print("i see you sent", b, c)


def b(c, *d):
    print("\nhello from foo function b")
    print("i see you sent", c, d)

def c():
    return "\nhello from foo function c"