def duplicate_zeros(inventory):
    zeros = inventory.count(0)
    n = len(inventory)

    for i in range(n -1, -1, -1):
        if i + zeros < n:
            inventory[i + zeros] = inventory[i]

        if inventory[i] == 0:
            zeros -= 1
            if i + zeros < n:
               inventory[i + zeros] = 0 