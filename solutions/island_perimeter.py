from typing import List


class Solution:

    @staticmethod
    def island_perimeter(grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            line = grid[i]
            for j in range(len(line)):
                v = line[j]
                if v == 0:
                    continue
                if j == 0:  # left edge
                    result += 1
                if j == len(line) - 1:  # right edge
                    result += 1
                if i == 0:  # top edge
                    result += 1
                if i == len(grid) - 1:  # bottom edge
                    result += 1
                if left_is_zero(j, line):
                    result += 1
                if right_is_zero(j, line):
                    result += 1
                if up_is_zero(i, j, grid):
                    result += 1
                if down_is_zero(i, j, grid):
                    result += 1
        print(result)


def left_is_zero(j, line):
    if j == 0:
        return False
    left = line[j - 1]
    if left == 0:
        return True
    else:
        return False


def right_is_zero(j, line):
    if j == len(line) - 1:
        return False
    right = line[j + 1]
    if right == 0:
        return True
    else:
        return False


def up_is_zero(i, j, grid):
    if i == 0:
        return False
    v = grid[i - 1][j]
    if v == 0:
        return True
    else:
        return False


def down_is_zero(i, j, grid):
    if i == len(grid) - 1:
        return False
    v = grid[i + 1][j]
    if v == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    Solution.island_perimeter([[0, 1, 0, 0],
                               [1, 1, 1, 0],
                               [0, 1, 0, 0],
                               [1, 1, 0, 0]])
    Solution.island_perimeter([[1]])
