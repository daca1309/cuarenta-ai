
def add_to_table(table, card):
    new_table=table[:]
    new_table.append(card)
    return new_table


def remove_from_table(table, cards):
    """
    Return a new table without the specified cards.

    Parameters:
        table: List of cards currently on the table.
        cards: List of cards to remove.

    Returns:
        A new list containing the remaining cards.

    Requirements:
        - Remove exactly the specified cards.
        - Compare cards by both value and suit.
        - Preserve the order of remaining cards.
        - Do not modify the original table.
        - Raise ValueError if any requested card
          is not present in the table.
        - An empty list of cards must leave
          the table unchanged.
    """
    
    
    pass
    
