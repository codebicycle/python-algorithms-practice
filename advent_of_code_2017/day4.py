"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?

"""

def count_passphrases(puzzle_input, validator):
    count = 0
    for row in puzzle_input:
        if validator(row):
            count += 1
    return count

def no_duplicates(row):
    return len(row) == len(set(row))

def no_anagrams(row):
    sorted_letters = [str.join('', sorted(word)) for word in row]
    return no_duplicates(sorted_letters)


def read_input(filename):
    with open(filename) as f:
        puzzle_input = [[word for word in line.split()] 
                        for line in f]
    return puzzle_input

def main():
    puzzle_input = read_input('input4.txt')

    result = count_passphrases(puzzle_input, validator=no_duplicates)
    print(f'Part 1 solution: {result}')

    result = count_passphrases(puzzle_input, validator=no_anagrams)
    print(f'Part 1 solution: {result}')


if __name__ == '__main__':
    main()
