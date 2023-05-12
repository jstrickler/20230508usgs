
def spam(a, b):
    print(a, b)

spam(5, 10)
spam('a', 'b')

args = ["foo", "bar"]

spam(*args)  # unpack iterable into separate arguments

def ham(**kwargs):
    print(kwargs)

ham(filename="foo.txt", animal="koala")

my_args = {
    'filename': 'protoplasm.txt',
    'animal': 'gnu',
}

ham(**my_args)

#  positional, keyword
#  positional-only, positional, optional-positional, keyword-only, optional-keyword
def blech(*squid, **octopus):
    pass

def wacky(p1, /, p2, p3, *p4, kw1, kw2, **kw3):
    pass





