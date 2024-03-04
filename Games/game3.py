import random

class Minesweeper:
    def __init__(self, size=8, num_mines=10):
        self.size = size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.generate_mines()

    def generate_mines(self):
        while len(self.mines) < self.num_mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.mines.add((x, y))

    def display_board(self, reveal=False):
        print('   ' + ' '.join([str(i) for i in range(self.size)]))
        for i in range(self.size):
            row = [str(self.board[i][j]) if (i, j) in self.revealed or reveal else ' ' for j in range(self.size)]
            print(f'{i}: ' + ' '.join(row))

    def reveal(self, row, col):
        if (row, col) in self.mines:
            return False
        revealed = set()
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            if (r, c) in revealed:
                continue
            revealed.add((r, c))
            count = self.count_mines_around(r, c)
            if count:
                self.board[r][c] = count
            else:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size and (nr, nc) not in revealed:
                            stack.append((nr, nc))
        self.revealed |= revealed
        return True

    def count_mines_around(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.size and 0 <= nc < self.size and (nr, nc) in self.mines:
                    count += 1
        return count

    def play(self):
        self.revealed = set()
        while True:
            self.display_board()
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            if not (0 <= row < self.size and 0 <= col < self.size):
                print('Invalid row or column!')
                continue
            if not self.reveal(row, col):
                self.display_board(reveal=True)
                print('Game Over! You hit a mine!')
                break
            if len(self.revealed) == self.size * self.size - self.num_mines:
                self.display_board(reveal=True)
                print('Congratulations! You win!')
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
