
prices ={
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 
    'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50,
    'Q': 30, 'R': 50, 'S':20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
    'Y': 20, 'Z': 21
}

specials = {

    '3R': ('Q', 3),
    '3U': ('U', 4),
    '2E': ('B', 2),
    '3N': ('M', 3),
    '2F': ('F', 3),


    '3Z': (45, 3),
    '3Y': (45, 3),
    '3S': (45, 3),
    '3T': (45, 3),
    '3X': (45, 3),
    '5A': (200, 5),
    '3A': (130, 3),
    '2B': (45, 2),
    '10H': (80, 10),
    '5H': (45, 5),
    '2K': (120, 2),
    '5P': (200, 5),
    '3Q': (80, 3),
    '3V': (130, 3),
    '2V': (90, 2),

}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):


    skus = list(skus)

    total = 0 
    tally = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
    'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
    'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0
    }

    for char in skus:
        if char in tally:
            tally[char] += 1
        else:
            return -1



    for offer, value in specials.items():
        item = offer[-1:]


        if isinstance(value[0],int):
            offer_price, offer_count = value
            count = tally[item]

            if count >= offer_count:
                total += (count // offer_count) * offer_price
                tally[item] = count % offer_count
        else:
            free_item, offer_count = value
            count = tally[item]

            if count >= offer_count:
                num_free = count // offer_count

                if tally[free_item] < num_free :
                    tally[free_item] = 0
                else:
                    tally[free_item] -= num_free
            

    zystx = tally['S'] + tally['T'] + tally['X'] + tally['Y'] + tally['Z'] 

    num_deals = zystx // 3
    total += num_deals * 45 
    num_items = num_deals * 3

    print(tally)
    print(total)
    for char in list("ZYSTX"):  # in order of most expensive to cheapest to favour customer
        if tally[char] > num_items :
            tally[char] -= num_items
        else:
            num_items -= tally[char]
            tally[char] = 0 
        print(tally)
        print(total)


    
    for item, count in tally.items():
        if count > 0:
            total += prices[item] * count




    return total 

    


print(checkout("ZZYCCXY"))

# CXYZYZC
    





