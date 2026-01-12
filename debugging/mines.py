#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Make sure the number of mines does not exceed the number of cells.
        total_cells = width * height
        if mines >= total_cells:
            raise ValueError("Number of mines must be less than total cells.")
        self.mines = set(random.sample(range(total_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # If the cell is mined → loss
        if (y * self.width + x) in self.mines:
            return False
        #If it's already exposed, do nothing
        if self.revealed[y][x]:
            return True
        # Cell detection
        self.revealed[y][x] = True
        # If there are no nearby mines, the neighbors will automatically detect them.
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and 0 <= ny < self.height
                            and not self.revealed[ny][nx]):
                        self.reveal(nx, ny)
        return True

    def is_won(self):
        """ Check if all unmined cells have been detected"""
        revealed_count = sum(row.count(True) for row in self.revealed)
        total_safe = self.width * self.height - len(self.mines)
        return revealed_count == total_safe

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Check that the coordinates are within the limits
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Please try again.")
                    continue

                # Try to expose the cell
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Check the win after each successful detection
                if self.is_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except KeyboardInterrupt:
                print("\nGame exited by user.")
                break


if __name__ == "__main__":
    game = Minesweeper()
    game.play()