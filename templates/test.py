from uuid import uuid4


def f():
    d = uuid4()
    str = d.hex
    WORD = "C" + str[0:16]
    return WORD

default = f()
print(default)