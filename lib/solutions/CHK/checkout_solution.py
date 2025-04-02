
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):


    skus = list(skus)

    total = 0 
    tally = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}

    for char in skus:
        if char in tally:
            tally[char] += 1
        else:
            return -1

    total += (tally['A'] // 5) * 200
    tally['A'] -= (tally['A'] // 5) * 5
    total += (tally['A'] % 3) * 50
    total += (tally['A'] // 3) * 130

    if tally['B'] > 0:
        if tally['B'] < tally['E'] // 2:
            tally['B'] = 0
        else:
            tally['B'] -= (tally['E'] // 2)

    total += (tally['B'] % 2) * 30
    total += (tally['B'] // 2) * 45
    total += tally['C'] * 20
    total += tally['D'] * 15
    total += tally['E'] * 40

    total += (tally['F'] // 3) * 20
    total += (tally['F'] * 3) * 10

    

    return total 


print(checkout("FFF"))

    



