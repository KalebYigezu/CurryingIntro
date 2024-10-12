# add(1,2,3). -> add(1)(2)(3)

def add(a, b, c):
    return a+b+c

print(add(10,100,1000))

#---------------------------------------------------------

from functools import partial

add_10 = partial(add, 10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))

#---------------------------------------------------------

from inspect import signature

def curry(fnc):
    def inner(arg):
        if len(signature(fnc).parameters) == 1:
            return fnc(arg)
        return curry(partial(fnc, arg))
    return inner

@curry
def add(a, b, c):
    return a+b+c

add_10 = add(10)
add_10_100 = add_10(100)
print(add_10_100(1000))
# Or
print(add(10)(100)(1000))

----------------  Currying In Its Best Version --------------


def addt(t):
    def addf(f):
        def adds(s):
            return t + f + s
        return adds
    return addf

two = addt(2)
four = two(4)
six = four(6)
# Or
print(addt(2)(4)(6))

print(six)

