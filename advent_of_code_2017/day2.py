"""
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

"""

def checksum(puzzle_input):
    sum = 0
    for row in puzzle_input:
        sum += max(row) - min(row)
    return sum


def read_input(filename):
    with open(filename) as f:
        puzzle_input = [[int(s) for s in line.split()] 
                        for line in f]
    return puzzle_input

def main():
    puzzle_input = read_input('input2.txt')

    result = checksum(puzzle_input)
    print(f'Part 1 solution: {result}')

    result = checksum(puzzle_input)
    print(f'Part 2 solution: {result}')


if __name__ == '__main__':
    main()