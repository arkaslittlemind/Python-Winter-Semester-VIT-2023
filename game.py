import random

# Game elements
RABBIT = "r"
CARROT = "c"
RABBIT_HOLE = "O"
PATHWAY_STONE = "-"

# Function to generate a random map
def generate_map(width, height, num_carrots, num_rabbit_holes):
  map = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(PATHWAY_STONE)
    map.append(row)

  # Place the rabbit
  map[random.randint(0, height - 1)][random.randint(0, width - 1)] = RABBIT

  # Place the carrots
  for i in range(num_carrots):
    map[random.randint(0, height - 1)][random.randint(0, width - 1)] = CARROT

  # Place the rabbit holes
  for i in range(num_rabbit_holes):
    map[random.randint(0, height - 1)][random.randint(0, width - 1)] = RABBIT_HOLE

  return map

# Function to move the rabbit
def move_rabbit(map, position, direction):
  row, col = position

  if direction == "a":
    col -= 1
  elif direction == "d":
    col += 1
  elif direction == "w":
    row -= 1
  elif direction == "s":
    row += 1
  elif direction == "wa":
    row -= 1
    col -= 1
  elif direction == "wd":
    row -= 1
    col += 1
  elif direction == "sa":
    row += 1
    col -= 1
  elif direction == "sd":
    row += 1
    col += 1
  else:
    raise ValueError("Invalid direction")

  new_position = (row, col)

  if map[row][col] == PATHWAY_STONE:
    return new_position
  elif map[row][col] == CARROT:
    return (row, col), True
  elif map[row][col] == RABBIT_HOLE:
    return (row, col), False
  else:
    return None, False

# Function to solve the game
def solve_game(map):
  start_position = (0, 0)
  carrots_collected = 0

  while carrots_collected < len(map[0]):
    current_position = start_position
    direction = ""

    while True:
      possible_moves = ["a", "d", "w", "s", "wa", "wd", "sa", "sd"]
      for move in possible_moves:
        new_position, carrot_collected = move_rabbit(map, current_position, move)
        if new_position is not None:
          current_position = new_position
          direction = move
          break
      else:
        break

    if carrot_collected > 0:
      start_position = current_position

  return carrots_collected, direction

# Main function
def main():
  width = int(input("Enter the width of the map: "))
  height = int(input("Enter the height of the map: "))
  num_carrots = int(input("Enter the number of carrots: "))
  num_rabbit_holes = int(input("Enter the number of rabbit holes: "))

  map = generate_map(width, height, num_carrots, num_rabbit_holes)

  print("The map is:")
  for row in map:
    print("".join(row))

  carrots_collected, direction = solve_game(map)

  print("The rabbit has collected {} carrots.".format(carrots_collected))
  print("The solution is to move the rabbit {}.".format(direction))

if __name__ == "__main__":
  main()
