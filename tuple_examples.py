
ips = ['192.168.123.3', '4.99.8.55']

guy = "Bill", "Gates", "Microsoft", "1955-10-28"


def spam(person):
    first_name, last_name, *product, dob = person   # iterable unpacking
    # print(f"person[0]: {person[0]}")
    # print(f"person[1]: {person[1]}")
    print(first_name, last_name)

spam(guy)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
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
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('Fred', 'Mertz', '1922-10-01'),
]

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
print('-' * 60)

for person in people:
    spam(person)
print('-' * 60)

a = 1, 2, 3   # 3-element tuple
b = 1, 2      # 2-element tuple
c = 1,        # 1-element tuple
d = 1         # integer
e = (1)       # also integer

cities = ['Durham', 'Austin', 'San Marino', 'Minneapolis']

def plot(x, y, alt):
    print(x, y, alt)

plot(1, 2, 3)
plot(50, 85, 10233)
print('=' * 60)
points = [(1, 2, 3), (50, 85, 10233), (18, 19, 343), ('a', 'b', 'c')]

for p in points:
    plot(p[0], p[1], p[2])
print()
print()

for x, y, alt in points:
    plot(x, y, alt)
print()

for point in points:
    plot(*point)
print()











