from string import ascii_uppercase
from random import choice


def make_grid(width, height, depth):
    return {
            (w, h, d): choice(ascii_uppercase)
                for w in range(width)
                    for h in range(height)
                        for d in range(depth)
            }


def potential_neighbours(position):
    col, row, dep = position

    neigbours = set([(c, r, d)
                    for c in range(col-1, col+2)
                        for r in range(row-1, row+2)
                            for d in range(dep-1, dep+2)])
    neigbours.remove(position)
    return neigbours


def path_to_word(path, grid):
    return "".join([grid[position] for position in path])



def load_word_list(filename):
    with open(filename) as f:
        text = f.read().upper().split("\n")
    return set(text)



def get_real_neighbours(grid):
    real_neighbours = {}

    for position in grid:
        pn = potential_neighbours(position)
        on_the_grid = [p for p in pn if p in grid]
        real_neighbours[position] = on_the_grid

    return real_neighbours



def get_real_neighbours_of_a_position(position, grid):
    pn = potential_neighbours(position)
    return [p for p in pn if p in grid]



def get_stems(word):
    return



def get_stems_for_word_list(wl):
    stems = []
    for word in wl:
        stems += [word[:i] for i in range(1, len(word))]
    return set(stems)



def search(grid, dictionary):
    neighbours = get_real_neighbours(grid)
    stems = get_stems_for_word_list(dictionary)
    words = []

    def do_search(path):
        word = path_to_word(path, grid)
        if word in dictionary:
            words.append(word)
        if word in stems:
            for next_pos in neighbours[path[-1]]:
                if next_pos not in path:
                    do_search(path + [next_pos])

    for position in grid:
        do_search([position])

    return set(words)



def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))



def main():
    grid = make_grid(4, 4, 4)
    word_list = load_word_list("words.txt")
    words = search(grid, word_list)
    display_words(words)



main()