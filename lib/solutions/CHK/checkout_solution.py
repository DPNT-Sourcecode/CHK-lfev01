from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    tally = [0, 0, 0, 0]
    counter = Counter(skus)

    tally = [counter.get(chr(i), 0) for i in range(ord)]

    


