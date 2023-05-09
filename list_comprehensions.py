fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.title() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 6]
print(f"f3: {f3}\n")

f4 = [f for f in fruits if f.startswith('a')]
print(f"f4: {f4}\n")

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()

cards = [(r, s) for s in suits for r in ranks]
print(f"cards: {cards}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print(f"dobs: {dobs}\n")

dob_gen = (p[-1] for p in people)
print(f"dob_gen: {dob_gen}\n")
for dob in dob_gen:
    print(dob)
print('-' * 60)

def spam(blah):
    for x in blah:
        print(x)

spam(p[1] for p in people if p[0].startswith('L'))

del fruits # remove fruits from memory

#  



