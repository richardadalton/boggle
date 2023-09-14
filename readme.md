# Boggle

![chartjs logo](boggle.jpeg)

## Overview

Boggle is a word game designed by Bill Cooke, invented by Allan Turoff and originally distributed by Parker Brothers. The game is played using a plastic grid of lettered dice, in which players attempt to find words in sequences of adjacent letters.

## Implementation

This version of boggle is written in Python. The program generates a random grid of letters and then finds all valid words in the grid based on a provided word list.

## Limitations

There are some limitations in the code as it currently stands.

* The letters in the grid are completely random. There are no guarantees of vowels, or the distribution of letters.

* Q and U are separate letters, there is no support for Qu

## Installation

Just clone this repository.

```bash
$ git clone https://github.com/richardadalton/boggle.git
```

## Running Boggle

Running the 2D version of Boggle (Grid)

```bash
$ python boggle.py [-h] [-f FILE] [-c COLUMNS] [-r ROWS] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file containing list of valid words.
  -c COLUMNS, --columns COLUMNS
                        Number of columns in the grid.
  -r ROWS, --rows ROWS  Number of rows in the grid.
  -g, --grid            Display the grid.
```

Running the 3D version of Boggle (Cube)

```bash
$ python boggle3d.py [-h] [-f FILE] [-c COLUMNS] [-r ROWS] [-d DEPTH] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file containing list of valid words.
  -c COLUMNS, --columns COLUMNS
                        Number of columns in the cube.
  -r ROWS, --rows ROWS  Number of rows in the cube.
  -d DEPTH, --depth DEPTH
                        Depth of the cube.
  -g, --grid            Display the grids that make up the cube.

```