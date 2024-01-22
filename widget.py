def a(b, c):
    print("\nhello from widget function a")
    print("i see you sent", b, c)


def b(c, *d):
    print("\nhello from widget function b")
    print("i see you sent", c, d)

def c():
    return "\nhello from widget function c"