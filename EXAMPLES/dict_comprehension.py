import re

animals = ['OWL  ', '  Badger', '   bushbaby  ', 'Tiger', '  Wombat', 'GORILLA   ', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.strip().lower(): len(a) for a in animals}  # Create a dictionary with key/value pairs derived from an iterable

print(d, '\n')

words = ['unicorn', 'stigmata', 'barley', 'bookkeeper', 'brandy']

d = {w:{c:w.count(c) for c in sorted(w)} for w in words if re.search('^b[aeiou]', w)} # Use a nested dictionary comprehension to create a dictionary mapping words to dictionaries which map letters to their counts (could be useful for anagrams)

for word, word_signature in d.items():
    print(word, word_signature)

#   VALUE for VAR ... in ITERABLE if CONDITION ....