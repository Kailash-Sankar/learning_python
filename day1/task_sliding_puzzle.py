#sliding puzzle board game
board = [8,5,7,6,3,4,2,0,1]

while True:
    print(board[:3])
    print(board[3:6])
    print(board[6:])

    move = int(input('Enter your move:'))
    mp = board.index(move)
    zp = board.index(0)

    valid_moves = [zp-1,zp+1,zp-3,zp+3]

    for x in valid_moves:
        if x < 0 or x > 8:
            valid_moves.remove(x)

    if zp % 3 == 0:
        valid_moves.remove(zp-1)

    if zp % 3 == 2:
        valid_moves.remove(zp+1)

    print('valid moves',valid_moves)

    if mp in valid_moves:
        board[mp],board[zp] = 0,move
    else:
        print("Please enter a valid move")



'''
x-1,x+1,x+3,x-3
'''
