import sys
case = int(input())

for _ in range(case):
    number = int(input())
    interviewers = list()
    count = 0
    for _ in range(number):
        man = list(map(int, sys.stdin.readline().split()))
        interviewers.append(man)
    interviewers.sort()
    for i in range(number):
        flag = True
        for j in range(i):
            if interviewers[j][1] < interviewers[i][1]:
                flag = False
                break
        if flag:
            count += 1
    print(count)
