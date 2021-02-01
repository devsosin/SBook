import re

def solution(files):
    answer = []
    p = re.compile('([a-z\-\s]+)([0-9]+)(.*)')
    s_list = []
    for i in files:
        num = re.search('[0-9]+', i).group()
        head = i[:i.index(num)].lower()
        s_list.append((head, num, i))
    
    # 파일명이 아예 같을수도 있기 때문에, 인덱스가 또 들어갈 소지가 있음. 따라서 정렬후에 for문으로 확인
    temp = sorted(s_list, key=lambda i : (i[0], int(i[1])))
    
    for t in temp:
        answer.append(t[2])
        
    return answer


print(solution(["imgJOISDJ100.p2ng", "img202.png123"]))
