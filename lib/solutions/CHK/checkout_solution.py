prices = {
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 
    'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50,
    'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
    'Y': 20, 'Z': 21
}

specials = {
    '3R': ('Q', 3), '3U': ('U', 4), '2E': ('B', 2), '3N': ('M', 3), '2F': ('F', 3),
    '3Z': (45, 3), '3Y': (45, 3), '3S': (45, 3), '3T': (45, 3), '3X': (45, 3),
    '5A': (200, 5), '3A': (130, 3), '2B': (45, 2), '10H': (80, 10), '5H': (45, 5),
    '2K': (120, 2), '5P': (200, 5), '3Q': (80, 3), '3V': (130, 3), '2V': (90, 2),
}

group_discount_items = ['Z', 'Y', 'S', 'T', 'X']
group_discount_price = 45
group_discount_count = 3

def checkout(skus):
    if not isinstance(skus, str):
        return -1

    tally = dict.fromkeys(prices, 0)

    for char in skus:
        if char in tally:
            tally[char] += 1
        else:
            return -1

    total = 0

    # Handle free item offers (e.g., buy 2E get B free)
    for offer, value in specials.items():
        item = offer[-1]
        if isinstance(value[0], str):  # free item offer
            free_item, threshold = value
            free_qty = tally[item] // threshold
            tally[free_item] = max(0, tally[free_item] - free_qty)

    # Handle group discount (S, T, X, Y, Z - any 3 for 45)
    group_total = sum(tally[i] for i in group_discount_items)
    num_groups = group_total // group_discount_count
    total += num_groups * group_discount_price

    remaining = num_groups * group_discount_count
    for item in sorted(group_discount_items, key=lambda x: prices[x], reverse=True):
        if tally[item] >= remaining:
            tally[item] -= remaining
            break
        else:
            remaining -= tally[item]
            tally[item] = 0

    # Handle multi-buy discounts (fixed-price offers)
    for offer, value in specials.items():
        item = offer[-1]
        if isinstance(value[0], int):  # fixed-price deal
            price, quantity = value
            count = tally[item]
            offer_count = count // quantity
            total += offer_count * price
            tally[item] = count % quantity

    # Add remaining items at unit price
    for item, count in tally.items():
        total += prices[item] * count

    return total

# Example usage
print(checkout("ZZYCCXYABHDOWNCEOECEOCNE"))

    



