import operator as op

def spam(func):
    func()

def ham():
    print("HAM HAM HAM")

class Eggs:
    def __init__(self):
        print("EGGS EGGS EGGS")
    def scramble(self):
        print("scrambling....")    
spam(ham)
spam(Eggs)
e = Eggs()
spam(e.scramble)
spam(lambda: print("I AM A LAMBDA"))
print(f"callable(ham): {callable(ham)}")
print(f"callable(Eggs): {callable(Eggs)}")

a = lambda x, y: x + y  # BAD PROGRAMMER! NO BISCUIT!!

def a(x, y):
    return x + y

print(f"a(10, 15): {a(10, 15)}")

p = 10
s = 9
result = p + s

result = op.add(p, s)   # p + s

words = ['wombat', 'wolverine', 'wallaby']
x = op.getitem(words, 2)     #  words[2]
print(f"x: {x}")

words_upper_iter = map(str.upper, words)
print(f"words_upper_iter: {words_upper_iter}")
for word in words_upper_iter:
    print(word)
print()

for length in map(len, words):
    print(length)
print()

total_length = sum(map(len, words))
print(f"total_length: {total_length}")











