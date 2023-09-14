import argparse
from string import ascii_uppercase
from random import choice
from utils import (
    display_cube,
    load_word_list,
    display_words,
    search
)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="words.txt",
                        help="Path to file containing list of valid words.")
    parser.add_argument("-c", "--columns", default=4, type=int,
                        help="Number of columns in the cube.")
    parser.add_argument("-r", "--rows", default=4, type=int,
                        help="Number of rows in the cube.")
    parser.add_argument("-d", "--depth", default=4, type=int,
                        help="Depth of the cube.")
    parser.add_argument("-g", "--grid", action="store_true",
                        help="Display the grids that make up the cube.")

    args = parser.parse_args()
    return args


def make_grid(width, height, depth):
    return {
        (w, h, d): choice(ascii_uppercase)
        for w in range(width)
        for h in range(height)
        for d in range(depth)
    }


def potential_neighbours(position):
    col, row, dep = position

    neighbours = set([(c, r, d)
                      for c in range(col - 1, col + 2)
                      for r in range(row - 1, row + 2)
                      for d in range(dep - 1, dep + 2)])
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
    grid = make_grid(args.columns, args.rows, args.depth)

    if args.grid:
        display_cube(grid, args.columns, args.rows, args.depth)

    word_list = load_word_list(args.file)

    neighbours = get_real_neighbours(grid)
    words = search(grid, neighbours, word_list)

    display_words(words)


main()
