
def silly():
    for word in "wombat", "aardvark", "badger":
        yield word   # __next__()

s = silly()
print(f"type(s): {type(s)}\n")

for x in s:
    #  s.__next__()   # deep inside s
    print(x)
print()

def even_sillier():
    yield "Python"
    yield "is"
    yield "fun (and weird)"

es = even_sillier()
for phrase in es:
    print(phrase)

es = even_sillier()
a = next(es)
print(f"a: {a}")

with open('DATA/mary.txt') as mary_in:
    first_line = next(mary_in)  # mary_in.getline()
    print(f"first_line: {first_line}\n")
    print("other lines:")
    for raw_line in mary_in:
        print(raw_line.rstrip())



