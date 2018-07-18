import unittest

class Maze:
    WALL = 'W'
    EMPTY = '.'

    def __init__(self, arr):
        self.arr = arr
        self.max_row = len(arr)-1
        self.max_col = len(arr[0])-1
        self.exit_loc = self.max_row, self.max_col
        self.visited = []
    
    def should_visit(self, row, col):
        return (row, col) not in self.visited and 0<=row<=self.max_row and 0<=col<=self.max_col

    def has_path_recursive(self, row, col):
        self.visited.append((row, col))

        if self.exit_loc == (row, col):
            print('{} {} exit'.format(row, col))
            return True

        if Maze.WALL == self.arr[row][col]:
            print('{} {} wall'.format(row, col))
            return False
        
        if (self.should_visit(row-1, col) and self.has_path_recursive(row-1, col))\
            or (self.should_visit(row+1, col) and self.has_path_recursive(row+1, col))\
            or (self.should_visit(row, col-1) and self.has_path_recursive(row, col-1))\
            or (self.should_visit(row, col+1) and self.has_path_recursive(row, col+1)):
            return True
        
        return False



class Test(unittest.TestCase):
    def test_mazes(self):
        maze = Maze([
            ['.','W','.'],
            ['.','W','.'],
            ['.','.','.'],
        ])
        self.assertTrue(maze.has_path_recursive(0,0))
        maze = Maze([
            ['.','W','.','.','.','.',],
            ['.','W','.','.','.','.',],
            ['.','W','.','.','.','.',],
            ['.','W','W','.','.','.',],
            ['.','.','.','W','.','.',],
            ['.','.','.','.','W','.',],
        ])
        self.assertFalse(maze.has_path_recursive(0,0))
        maze = Maze([
            ['.','W','.','.','.','.',],
            ['.','W','.','.','.','.',],
            ['.','W','.','.','.','.',],
            ['.','W','.','.','.','.',],
            ['.','.','.','W','.','.',],
            ['.','.','.','.','W','.',],
        ])
        self.assertTrue(maze.has_path_recursive(0,0))

if __name__ == '__main__':
    unittest.main()