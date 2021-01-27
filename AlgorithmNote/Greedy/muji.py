import heapq

def solution(food_times, K):
    if sum(food_times) <= K:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    previous = 0
    length = len(q)
    while K >= (q[0][0] - previous) * length:
        now, idx = heapq.heappop(q)
        K -= (now-previous)*length
        previous = now
        length -= 1

    q = sorted(q, key=lambda i : i[1])
    return q[K%length][1]

food_times = [4, 2, 3, 6, 7, 1, 5, 8]
K = 27

solution(food_times, K)