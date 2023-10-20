
def board_horizon():
    return ' --- ' * board_size


def board_vertical():
    return'|    ' * (board_size+1)


if __name__ == '__main__':
    board_size = int(input('what size do you want your board? '))
    for i in range(board_size):
        print(board_horizon())
        print(board_vertical())
    print(board_horizon())
