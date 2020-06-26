# write your code here
def moment_checker(tuple_):
    possibilities = [tuple_[0:3], tuple_[3:6], tuple_[6:9], tuple_[0::3],
                     tuple_[1::3], tuple_[2::3], tuple_[0::4], tuple_[2:7:2]]
    match_x = tuple("XXX") in possibilities
    match_o = tuple("OOO") in possibilities
    return match_o, match_x


states = ["Game not finished", "Draw", "X wins", "O wins", "Impossible"]

cells = input("Enter cells:")
cells_tuple = tuple(cells)

print("""---------
| %s %s %s |
| %s %s %s |
| %s %s %s |
---------""" % cells_tuple)

x_count = cells_tuple.count("X")
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
    print(states[2])

