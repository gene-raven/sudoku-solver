#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from sudoku import *


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    elif len(sys.argv) == 1:
        # Input filename as a number ex: 1 for 001.txt 
        while True:
            try:
                file_num = int(input('Sudoku # '))
                if file_num < 0 or file_num >= 1000:
                    raise ValueError
            except ValueError:
                print('Invalid input')
                continue
            break
            
        filename = os.path.join('data', f'{file_num:03}.txt')
        
    else:
        sys.exit('Too many command-line arguments')

    # Read sudoku from file
    try:
        with open(filename, 'r') as f:
            contents = f.read().splitlines()
    except FileNotFoundError:
        exit("File not found")
    
    # Check if file consists out of numbers and convert to int
    try:
        grid = [[int(n) for n in row] for row in contents]
    except ValueError:
        exit('Invalid sudoku file')

    try:
        sudoku = Sudoku(grid)
    except InvalidSudoku:
        exit('Invalid sudoku grid')
    sudoku.output()

    # Solve
    solver = SudokuSolver(sudoku)
    assignment = solver.solve()

    # Print result
    if not assignment:
        print('No solution')
        
    else:
        solver.print(assignment)


if __name__ == '__main__':
    main()