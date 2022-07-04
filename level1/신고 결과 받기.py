# defaultdict는 유사 딕셔너리로 인자로 주어진 객체(셋, 숫자, 리스트 등)의 기본값을 딕셔너리값의 초깃값으로 지정 가능
from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    # 중복 신고는 없애기
    s_report = list(set(report))
    # 유저가 신고한 사람
    user = defaultdict(set)
    # 신고당한 횟수
    cnt = defaultdict(int)

    for i in s_report:
        # 신고자, 신고받은자 나누기
        a, b = i.split()
        # add는 set에서만 사용가능한데 위에서 defaultdict(set)으로 초기화했기 때문에 활용 가능한 방식
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    return answer


id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k1 = 2

id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

print(solution(id_list1, report1, k1))
print(solution(id_list2, report2, k2))