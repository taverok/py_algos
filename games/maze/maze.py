import unittest

class Maze:
    WALL = 'W'
    EMPTY = '.'

    def __init__(self, arr):
        self.arr = arr
        self.max_raw = len(arr)-1
        self.max_col = len(arr[0])-1
        self.exit_loc = self.max_raw, self.max_col
        self.__visited = []
    
    def has_path_recursive(self, row, col):
        if self.exit_loc == (row, col):
            print('{} {} exit'.format(row, col))
            return True

        if Maze.WALL == self.arr[row][col]:
            print('{} {} wall'.format(row, col))
            self.__visited.append((row, col))
            return False
        
        for next_row in range(row-1, row+1):
            for next_col in range(col-1, col+1):
                if row <= self.max_raw \
                    and next_col <= self.max_col \
                    and (next_row, next_col) not in self.__visited :
                    print('{} {} visiting'.format(row, col))

                    return self.__visited.append((next_row, next_col))



class Test(unittest.TestCase):
    def test_mazes(self):
        maze = Maze([
            ['.','W','.'],
            ['.','W','.'],
            ['.','W','.'],
        ])
        self.assertFalse(maze.has_path_recursive(0,0))
        self.assertTrue(maze.has_path_recursive(0,0))

if __name__ == '__main__':
    unittest.main()