import collections


def hit(s, bricks):
    if len(bricks) == 3:
        if bricks[0] + bricks[1] <= S:
            bricks.popleft()
            bricks.popleft()
        else:
            if bricks[1] + bricks[2] <= S:
                bricks.pop()
                bricks.pop()
            else:
                if bricks[3] <= S:
                    bricks.pop()

    elif len(bricks) == 2:
        if bricks[0] + bricks[1] <= S:
            bricks.popleft()
            bricks.popleft()
        else:
            if bricks[1] <= S:
                bricks.pop()

    elif len(bricks) == 1:
        if bricks[0] <= S:
            bricks.pop()
        else:
            raise ValueError("Last brick too stronk")

    return bricks


T = int(input())

for i in range(T):
    S, W1, W2, W3 = [int(i) for i in input().split()]

    bricks = collections.deque([W1, W2, W3])
    count = 0

    while len(bricks) > 0:
        bricks = hit(S, bricks)
        count += 1

    print(count)
