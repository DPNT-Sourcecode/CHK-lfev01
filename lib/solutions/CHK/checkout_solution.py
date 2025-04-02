
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):


    skus = list(skus)

    total = 0 
    tally = {'A': 0, 'B':0, 'C': 0, 'D': 0}

    for char in skus:
        if char in tally:
            tally[char] += 1
        else:
            return -1


    total += (tally['A'] % 3) * 50
    total += (tally['A'] // 3) * 130
    total += (tally['B'] % 2) * 30
    total += (tally['B'] // 2) * 45
    total += tally['C'] * 20
    total += tally['D'] * 15

    return total 


        

    





