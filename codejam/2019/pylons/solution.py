"""
https://leetcode.com/problems/unique-paths-iii/submissions/

# Rows 1 to R
# Cols 1 to C
# never revisit (include start point)
#다음 방문지=상하좌우 + 대각선 까지 사용 불가
# cell 을 모두 다 방문가능하면 그 시나리오를 출력하면 됨.
# 불가능 하면 그냥 불가능하다고 하면됨.
"""


def solve(rows, cols):
    if rows < 4 and cols < 4:
        return False, []

    sinario = []

    if rows > cols:
        for row in range(rows):
            hopping_row = row + 2
            if hopping_row >= rows:
                hopping_row -= rows
            for col in range(cols):
                if col % 2 == 0:
                    sinario.append([row + 1, col + 1])
                else:
                    sinario.append([hopping_row + 1, col + 1])
    else:
        for col in range(cols):
            hopping_col = col + 2
            if hopping_col >= cols:
                hopping_col -= cols
            for row in range(rows):
                if row % 2 == 0:
                    sinario.append([row + 1, col + 1])
                else:
                    sinario.append([row + 1, hopping_col + 1])

    return True, sinario


if __name__ == "__main__":
    # start_millis = int(round(time.time() * 1000))

    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        r, c = [int(s) for s in input().split()]
        is_possible, possible_sinario = solve(r, c)
        if is_possible:
            print("Case #{}: POSSIBLE".format(i))
            for pair in possible_sinario:
                print("%s %s" % (pair[0], pair[1]))
        else:
            print("Case #{}: IMPOSSIBLE".format(i))

    # end_millis = int(round(time.time() * 1000))
    # print("Took {}ms".format(end_millis - start_millis))
