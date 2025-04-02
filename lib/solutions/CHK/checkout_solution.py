
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0 
    tally = {'A': 0, 'B':0, 'C': 0, 'D': 0}

    for char in skus:
        if char in tally:
            tally[char] += 1



    tally += (tally['A'] % 3) * 50
    tally += (tally['A'] // 3) * 130
    tally += (tally['A'] % 3) * 50
    tally += (tally['A'] // 3) * 130
    total += tally['C'] * 20
    total += tally['D'] * 15



    
        

    




