
#    Return a new table with the specified cards (makes a copy).
def add_to_table(table, card):
    new_table=table[:]
    new_table.append(card)
    return new_table

#    Return a new table without the specified cards (makes a copy).
def remove_from_table(table, cards):
    new_table=table[:]

    for x in cards:
        if x in new_table:
            new_table.remove(x)
        else:
            raise ValueError("card not in table")
    return new_table

