# Sudoku Solver
## Description:

Solving sudoku given a file with unfinished grid.

### **Usage**
Sudoku file can be passed as command-line argument then usage is:
```bash
python3 main.py <path>
```
where *path* - path to file with sudoku grid

```bash
python3 main.py
```
then program prompts user for number of sudoku from directory data, for example if ures puts in number 1, it would take file ./data/001.txt

### **File format**
The passed file should be formatted as follows:
- One row per line
- Blanks are changed to zeros.
- No punctuation or letters or other symbols other than digits are allowed.

### Algorithm for solving Sudoku
1. Cross out impossible solutions for empty cells, i.e. all the numbers that are already present in the current row, column, or box, based on the already filled in cells in the grid.
2. Check if there is only one placement possible for some numbers. Cross out other numbers in such cells.
3. Repeat steps 1 and 2 while something changes. Continue when the previous steps have completed themselves.
4. Find all subsets of cells independent of their common neighbors (cells in the same row, column, or box). For example, if in 3 cells in one row, column or box only 3 numbers are possible, that means that these 3 numbers will be impossible in other cells in this row, column or box. That means that numbers possible in that subset can be crossed out from their common neighbors.
5. Repeat steps 1-3.
6. Generate current assignment.  *Assignment* - variable used for locking down an answer. It is a dictionary with Variable objects as keys and values of type int. Cell: assigned number
7. Backtracking search:
    1. Base case: if the assignment is complete, return it.
    2. Choose an analyzable variable.
    3. Iterate through the values of the selected variable.
        1. Add current value to the assignment.
        2. Check if the new assignment is complete, otherwise go to p. 6.
        3. Remember current state.
        4. Change domains of variable to single value
        5. Call solve (go to p. 1)
        6. Restore domains to their previous state before the p.4 change.
        7. Delete current value from the assignment   
    4. Return failure