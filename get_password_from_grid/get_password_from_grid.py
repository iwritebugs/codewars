def _get_start_position(grid):
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter == 'x':
                return tuple((i, j))


def get_password(grid, directions):
    start_pos = _get_start_position(grid)
    if start_pos is None:
        return

    row, col = start_pos
    password = ''
    for direction in directions:
        if direction.startswith('left'):
            col -= 1
        elif direction.startswith('right'):
            col += 1
        elif direction.startswith('up'):
            row -= 1
        elif direction.startswith('down'):
            row += 1

        if direction.endswith('T'):
            password += grid[row][col]

    return password


def test_get_password():
    grid = [
        ["x", "l", "m"],
        ["o", "f", "c"],
        ["k", "i", "t"]
    ]
    directions = ["rightT", "down", "leftT", "right", "rightT", "down", "left",
                  "leftT"]

    assert get_password(grid, directions) == "lock"
