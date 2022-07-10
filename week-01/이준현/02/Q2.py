N, M = map(int, input().split())
matrix = list()
MAX = 0
card = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(len(matrix)):
    if MAX <= min(matrix[i]):
        card = min(matrix[i])

print(card)

