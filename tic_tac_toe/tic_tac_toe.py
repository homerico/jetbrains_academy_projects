# write your code here
def moment_checker(tuple_):
    possibilities = [tuple_[0:3], tuple_[3:6], tuple_[6:9], tuple_[0::3],
                     tuple_[1::3], tuple_[2::3], tuple_[0::4], tuple_[2:7:2]]
    match_x = list("XXX") in possibilities
    match_o = list("OOO") in possibilities
    return match_o, match_x


def checker_caller():
    x_count = cells_list.count("X")
    o_count = cells_list.count("O")
    space_count = cells_list.count(" ")
    checker = moment_checker(cells_list)

    if abs(x_count - o_count) > 1 or checker == (True, True):
        return states[4]
    elif checker == (False, False) and space_count > 0:
        return states[0]
    elif checker == (False, False):
        return states[1]
    elif checker == (True, False):
        return states[3]
    else:
        return states[2]


def print_table():
    global cells_list
    print("""
    ---------
    | %s %s %s |
    | %s %s %s |
    | %s %s %s |
    ---------""" % tuple(cells_list))


states = ["Game not finished", "Draw", "X wins", "O wins", "Impossible"]

"""cells = "_________"
cells_list = list(cells)"""
standard_matrix = {}
cells_index = 0

for i in range(3):
    for j in range(3):
        standard_matrix[(j + 1, 3 - i)] = " " # cells_list[cells_index]
        cells_index += 1
cells_list = [standard_matrix[x] for x in standard_matrix]
print_table()

turn = 0
# Trocar por try ... except
while True:
    user = ["X", "O"][turn % 2]
    coordinates = input("Enter the coordinates:").split()
    if len(coordinates[0]) == 1 and len(coordinates[1]) == 1:
        coordinates = [int(coordinate) for coordinate in coordinates]
        num_limit_checker = [1 <= checker <= 3 for checker in coordinates]
        if num_limit_checker == [True, True]:
            if standard_matrix[tuple(coordinates)] == " ":
                standard_matrix[tuple(coordinates)] = user
                turn += 1
                cells_list = [standard_matrix[x] for x in standard_matrix]
                print_table()
                actual_state = checker_caller()
                if actual_state != "Game not finished":
                    print(actual_state)
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
