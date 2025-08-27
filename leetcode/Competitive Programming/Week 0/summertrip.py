# new approach, keep track of all occurances of a character

def all_possible_pairs():
    found = 0
    events = input()
    indices = {}
    for i, char in enumerate(events):
        if char not in indices:
            indices[char] = [i]
        else:
            indices[char].append(i)
    print(indices)
    # have an instance and the next instance of a char
    # check each char, find if instance occurs between bounds
    # that is one valid pair

    return found

print(all_possible_pairs())
