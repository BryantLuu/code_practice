def check_valid_word(word, board, current):
    if not word:
        return True
    x = current[0]
    y = current[1]
    # check off board east or west
    if x < 0 or x >= len(board[0]):
        return False
    # check off board north or south
    if y < 0 or y >= len(board):
        return False
    # check if letter correct
    if board[y][x] != word[0]:
        return False

    temp = board[y][x]
    board[y][x] = ''

    north = [current[0], current[1]-1]
    south = [current[0], current[1]+1]
    east = [current[0]-1, current[1]]
    west = [current[0]+1, current[1]]
    
    rest_of_word = word[1:]
    
    result = check_valid_word(rest_of_word, board, north) \
        or check_valid_word(rest_of_word, board, south) \
        or check_valid_word(rest_of_word, board, east) \
        or check_valid_word(rest_of_word, board, west)
    
    if not result:
        board[y][x] = temp

    return result

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        y_length = len(board)
        x_length = len(board[0])
        letter = word[0]
        for y in range(y_length):
            for x in range(x_length):
                letter == board[y][x]
                if check_valid_word(word, board, [x,y]):
                    return True
        return False
        
        