def startswith_capital_counter(names):

    capital_lettes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    count = 0

    for name in names:
        for letter in capital_lettes:
            if name[0] == letter:
                count += 1
                break
    return count
