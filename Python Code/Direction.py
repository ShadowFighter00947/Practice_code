x = 0
y = 0

while True:
    move = input()
    if (move == 'STOP'):
        break
    elif(move == 'START'):
        continue
    elif(move == 'UP'):
        y += 1
    elif(move == 'DOWN'):
        y -= 1
    elif(move == 'LEFT'):
        x -= 1
    elif(move == 'RIGHT'):
        x += 1
print(abs(x) + abs(y))