def display_grid(grid, columns, rows):
    print("--- Grid ---")
    grid_rows = []
    for r in range(rows):
        row_cells = []
        for c in range(columns):
            row_cells.append(grid[c, r])
        grid_rows.append('|'.join(row_cells))

    for gr in grid_rows:
        print(gr)


def display_cube(cube, columns, rows, depth):
    print("--- Cube ---")
    for d in range(depth):
        grid = {(r, c): cube[(r, c, d)]
                for r in range(rows)
                for c in range(columns)
                }
        display_grid(grid, rows, columns)


def load_word_list(filename):
    with open(filename) as f:
        text = f.read().upper().split("\n")
    return set(text)


def display_words(words):
    print("--- Words ---")
    for word in words:
        print(word)
    print("Found %s words" % len(words))


def get_stems_for_word_list(wl):
    stems = []
    for word in wl:
        stems += [word[:i] for i in range(1, len(word))]
    return set(stems)


def path_to_word(path, grid):
    return "".join([grid[position] for position in path])


def search(grid, neighbours, dictionary):
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
