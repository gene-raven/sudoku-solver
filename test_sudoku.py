import sudoku
import pytest


def test_variable():
    '''
    Check if variable initialized correctly
    '''
    var0 = sudoku.Variable(1, 2, True)
    assert var0.box == 0

    var1 = sudoku.Variable(4, 4, True)
    var2 = sudoku.Variable(4, 4, True)
    assert var1.box == 4
    assert var1 == var2
    assert var0 != var1

    var = sudoku.Variable(8, 8, True)
    assert var.box == 8


def test_solve():
    '''
    Test sudoku.SudokuSolver.solve()
    
    Test if it corrrectly solves simple and hard sudoku.
    '''
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 6, 4, 0, 0, 0, 7, 1, 9],
        [0, 7, 0, 0, 6, 0, 0, 5, 0],
        [6, 0, 0, 4, 0, 5, 0, 0, 3],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [3, 0, 0, 1, 0, 2, 0, 0, 4],
        [0, 8, 0, 0, 3, 0, 0, 2, 0],
        [7, 2, 9, 0, 0, 0, 6, 3, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    ans = [
        [2, 9, 3, 7, 5, 1, 8, 4, 6],
        [5, 6, 4, 8, 2, 3, 7, 1, 9],
        [8, 7, 1, 9, 6, 4, 3, 5, 2],
        [6, 1, 7, 4, 9, 5, 2, 8, 3],
        [9, 4, 2, 3, 8, 6, 1, 7, 5],
        [3, 5, 8, 1, 7, 2, 9, 6, 4],
        [1, 8, 5, 6, 3, 9, 4, 2, 7],
        [7, 2, 9, 5, 4, 8, 6, 3, 1],
        [4, 3, 6, 2, 1, 7, 5, 9, 8]
    ]

    new_sudoku = sudoku.Sudoku(grid)
    solver = sudoku.SudokuSolver(new_sudoku)
    assert solver.grid(solver.solve()) == ans
    grid[8][0] = 5
    new_sudoku = sudoku.Sudoku(grid)
    solver = sudoku.SudokuSolver(new_sudoku)
    assert solver.solve() == None

    grid = [
        [0, 9, 2, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 9, 0, 0, 0, 2],
        [0, 0, 5, 0, 8, 7, 0, 0, 4],
        [8, 0, 0, 0, 2, 0, 0, 6, 0],
        [5, 0, 0, 0, 0, 8, 7, 0, 0],
        [6, 0, 0, 4, 1, 0, 0, 8, 5],
        [0, 0, 8, 1, 7, 0, 0, 5, 9],
        [0, 4, 1, 8, 5, 0, 0, 3, 0],
        [0, 5, 6, 9, 4, 3, 0, 2, 8]
    ]  

    ans = [
        [4, 9, 2, 5, 3, 1, 8, 7, 6],
        [3, 8, 7, 6, 9, 4, 5, 1, 2],
        [1, 6, 5, 2, 8, 7, 3, 9, 4],
        [8, 1, 4, 7, 2, 5, 9, 6, 3],
        [5, 2, 9, 3, 6, 8, 7, 4, 1],
        [6, 7, 3, 4, 1, 9, 2, 8, 5],
        [2, 3, 8, 1, 7, 6, 4, 5, 9],
        [9, 4, 1, 8, 5, 2, 6, 3, 7],
        [7, 5, 6, 9, 4, 3, 1, 2, 8]
    ]

    new_sudoku = sudoku.Sudoku(grid)
    solver = sudoku.SudokuSolver(new_sudoku)
    assert solver.grid(solver.solve()) == ans
    grid[6][0] = 3
    new_sudoku = sudoku.Sudoku(grid)
    solver = sudoku.SudokuSolver(new_sudoku)
    assert solver.solve() == None


def test_sudoku():
    '''
    Test sudoku.Sudoku

    Check if it raises InvalidSudoku exception for an invalid grid
    '''
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 6, 4, 0, 0, 0, 7, 1, 9],
        [0, 7, 0, 0, 6, 0, 0, 5, 0, 0],
        [6, 0, 0, 4, 0, 5, 0, 0, 3],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [3, 0, 0, 1, 0, 2, 0, 0, 4],
        [0, 8, 0, 0, 3, 0, 0, 2, 0],
        [7, 2, 9, 0, 0, 0, 6, 3, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    with pytest.raises(sudoku.InvalidSudoku):
        sudoku.Sudoku(grid)
