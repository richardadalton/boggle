import argparse
from random import choice
from string import ascii_uppercase
from utils import (
    display_grid,
    load_word_list,
    display_words,
    search,
)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="words.txt",
                        help="Path to file containing list of valid words.")
    parser.add_argument("-c", "--columns", default=4, type=int,
                        help="Number of columns in the grid.")
    parser.add_argument("-r", "--rows", default=4, type=int,
                        help="Number of rows in the grid.")
    parser.add_argument("-g", "--grid", action="store_true",
                        help="Display the grid.")

    args = parser.parse_args()
    return args


def make_grid(columns, rows):
    return {(c, r): choice(ascii_uppercase)
            for r in range(rows)
            for c in range(columns)}


def potential_neighbours(position):
    col, row = position
    neighbours = set([(c, r)
                     for c in range(col - 1, col + 2)
                     for r in range(row - 1, row + 2)])
    neighbours.remove(position)
    return neighbours


def get_real_neighbours(grid):
    real_neighbours = {}

    for position in grid:
        pn = potential_neighbours(position)
        on_the_grid = [p for p in pn if p in grid]
        real_neighbours[position] = on_the_grid

    return real_neighbours


def main():
    args = get_arguments()
    grid = make_grid(args.columns, args.rows)

    if args.grid:
        display_grid(grid, args.columns, args.rows)

    word_list = load_word_list(args.file)
    neighbours = get_real_neighbours(grid)
    words = search(grid, neighbours, word_list)
    display_words(words)


main()
