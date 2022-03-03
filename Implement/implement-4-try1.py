#문제를 잘보고 문제가 하라는데로하자
#뒤에가 바다면 멈춘다는 조건 무시하고 나혼자 new=past 포지션이 같으면 끝난다고 생각하고 프로그래밍함

n, m = map(int, input().split())
row, col, d = map(int, input().split())

flag = 0
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 1
new_position = (row, col)
past_position = (-1, -1)
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

start_d = d
while True:

    if (new_position[0] + direction[d - 1][0] < 0 or new_position[1] + direction[d - 1][1] < 0 or
            game_map[new_position[0] + direction[d - 1][0]][new_position[1] + direction[d - 1][1]] == 1):
        if d == 0:
            d = 3
        else:
            d -= 1

        if d== start_d:
            game_map[new_position[0]][new_position[1]]=1
            new_position=past_position
            
            past_position

    else:
        past_position = new_position
        new_position = (new_position[0] + direction[d - 1][0], new_position[1] + direction[d - 1][1])
        count += 1

        if d == 0:
            d = 3
        else:
            d -= 1

    if past_position == new_position:
        break

print(count)
