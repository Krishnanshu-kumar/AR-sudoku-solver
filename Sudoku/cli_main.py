from time import time
import numpy as np

# import Sudoku class to solve the puzzle using Algorithm X
from Sudoku.sudoku import Sudoku


def main():
    """Driver method"""

    # note start time
    start = time()
    # input the puzzle
    matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 3, 0, 8, 5],
                       [0, 0, 1, 0, 2, 0, 0, 0, 0],
                       [0, 0, 0, 5, 0, 7, 0, 0, 0],
                       [0, 0, 4, 0, 0, 0, 1, 0, 0],
                       [0, 9, 0, 0, 0, 0, 0, 0, 0],
                       [5, 0, 0, 0, 0, 0, 0, 7, 3],
                       [0, 0, 2, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 4, 0, 0, 0, 9]], dtype=int)
    # num of rows in sub grid
    num_rows_sub_grid = 3
    # num of cols in sub grid
    num_cols_sub_grid = 3

    try:
        # get solution_list from the class
        solution_list = Sudoku(matrix.copy(),
                               box_row=num_rows_sub_grid,
                               box_col=num_cols_sub_grid).get_solution()
        # get shape of the matrix
        rows, cols = matrix.shape
        # iterate through all the solutions
        for sol_num, solution in enumerate(solution_list):
            print("Solution Number {} -\n".format(sol_num + 1))
            # iterate through rows
            for i in range(rows):
                # if sub grid rows are over
                if i % num_rows_sub_grid is 0 and i != 0:
                    print('-' * (2 * (cols + num_rows_sub_grid - 1)))
                # iterate through columns
                for j in range(cols):
                    # if sub grid columns are over
                    if j % num_cols_sub_grid == 0 and j != 0:
                        print(end=' | ')
                    else:
                        print(end=' ')
                    # print solution element
                    print(solution[i, j], end='')
                # end row
                print()
            print("\n")
        # time taken to solve
        print("\nSolved in {} s".format(round(time() - start, 4)))
    # Key Value Error raised if solution not possible
    except Exception:
        print("Solution does not exist, try with a different puzzle")


if __name__ == '__main__':
    main()
