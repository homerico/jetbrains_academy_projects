# write your code here
"""def moment_checker(tuple_):
    possibilities = [tuple_[0:3], tuple_[3:6], tuple_[6:9], tuple_[0::3],
                     tuple_[1::3], tuple_[2::3], tuple_[0::4], tuple_[2:7:2]]
    match_x = tuple("XXX") in possibilities
    match_o = tuple("OOO") in possibilities
    return match_o, match_x"""

def print_table():
    global cells_tuple
    print("""---------
    | %s %s %s |
    | %s %s %s |
    | %s %s %s |
    ---------""" % tuple(cells_tuple))

states = ["Game not finished", "Draw", "X wins", "O wins", "Impossible"]

cells = input("Enter cells:")
cells_tuple = list(cells)
standard_matrix = {}
cells_index = 0

for i in range(3):
    for j in range(3):
      standard_matrix[(j + 1,3 - i)] = cells_tuple[cells_index]
      cells_index += 1

print_table()

# Trocar por try ... except
while True:
    coordinates = input("Enter the coordinates:").split()
    if len(coordinates[0]) == 1 and len(coordinates[1]) == 1:
        coordinates = [int(coordinate) for coordinate in coordinates]
        num_limit_checker = [1 <= checker <= 3 for checker in coordinates]
        if num_limit_checker == [True, True]:
            if standard_matrix[tuple(coordinates)] is "_":
                standard_matrix[tuple(coordinates)] = "X"
                break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

cells_tuple = [standard_matrix[x] for x in standard_matrix]
print_table()

"""x_count = cells_tuple.count("X")
o_count = cells_tuple.count("O")
space_count = cells_tuple.count("_")
checker = moment_checker(cells_tuple)

if abs(x_count - o_count) > 1 or checker == (True, True):
    print(states[4])
elif checker == (False, False) and space_count > 0:
    print(states[0])
elif checker == (False, False):
    print(states[1])
elif checker == (True, False):
    print(states[3])
else:
    print(states[2])"""

