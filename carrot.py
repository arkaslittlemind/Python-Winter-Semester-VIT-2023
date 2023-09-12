import random

class Game:
    def __init__(self, width, height, num_carrots, num_holes):
        self.width = width
        self.height = height
        self.num_carrots = num_carrots
        self.num_holes = num_holes
        self.grid = [['-' for _ in range(width)] for _ in range(height)]
        self.rabbit_x, self.rabbit_y = self.place_element('R')
        self.carrots = []
        self.holes = []
        self.place_elements('C', num_carrots)
        self.place_elements('O', num_holes)
        self.carrot_held = None

    def place_element(self, element):
        while True:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.grid[y][x] == '-':
                self.grid[y][x] = element
                return x, y

    def place_elements(self, element, num_elements):
        for _ in range(num_elements):
            self.place_element(element)

    def display(self):
        for row in self.grid:
            print(" ".join(row))
    
    def move(self, direction):
        dx, dy = 0, 0
        if direction == 'a':
            dx = -1
        elif direction == 'd':
            dx = 1
        elif direction == 'w':
            dy = -1
        elif direction == 's':
            dy = 1
        new_x, new_y = self.rabbit_x + dx, self.rabbit_y + dy

        if self.is_valid_move(new_x, new_y):
            if self.grid[new_y][new_x] == 'C':
                self.carrot_held = (new_x, new_y)
            elif self.grid[new_y][new_x] == 'O':
                if self.carrot_held:
                    self.grid[new_y][new_x] = '-'
                    self.carrot_held = None
            self.grid[self.rabbit_y][self.rabbit_x] = '-'
            self.rabbit_x, self.rabbit_y = new_x, new_y
            self.grid[self.rabbit_y][self.rabbit_x] = 'R'
            return True
        return False

    def is_valid_move(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

def main():
    width = int(input("Enter the width of the map: "))
    height = int(input("Enter the height of the map: "))
    num_carrots = int(input("Enter the number of carrots: "))
    num_holes = int(input("Enter the number of rabbit holes: "))

    game = Game(width, height, num_carrots, num_holes)

    while True:
        game.display()
        move = input("Enter move (a/d/w/s/j/p/q): ")
        if move == 'q':
            break
        elif move == 'p':
            if game.carrot_held:
                x, y = game.carrot_held
                if game.grid[y][x] == 'O':
                    print("Carrot placed in the hole!")
                    break
            else:
                print("No carrot to place.")
        elif move in ('a', 'd', 'w', 's', 'j'):
            if game.move(move):
                continue
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
