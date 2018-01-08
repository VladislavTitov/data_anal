import random, time, string
from collections import namedtuple

Item = namedtuple('Item', 'user query time')

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def get_random_item():
    return Item(random.randint(0, 99), generate_random_string(random.randint(5, 20)), time.time())

def generator(x, d):
    tuples = []
    for i in range(x):
        item = get_random_item()
        tuples.append(item)
    for j in range(d):
        item = get_random_item() 
        tuples.append(item)
        tuples.append(item)
    random.shuffle(tuples)
    return tuples

def filter(tuples):
    storage = []
    for i in range(len(tuples)):
        item = tuples.pop()
        if item.user % 10 == 0:
            storage.append(item)
    return storage

def algorith(items):
    length = len(items)
    no_doubles = dict()
    d = 0
    for i in range(length):
        item = items.pop()
        query = item.query
        if query in no_doubles:
            del no_doubles[query]
            d += 1
        else:
            no_doubles[query] = item
    x = len(no_doubles)
    return x, d

x, d = 10000, 735
x1, d1 = algorith(filter(generator(x, d)))

proportion = x / (x + d)
proportion1 = x1 / (x1 + d1)
print(proportion, "=", proportion1)