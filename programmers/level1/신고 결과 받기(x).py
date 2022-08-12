# 다시풀기

def solution(id_list, report, k):
  size = len(id_list)
  
  reportCount = [0] * size
  for r in set(report):
    reporter, reported = r.split()
    i = id_list.index(reported)
    reportCount[i] += 1

  stoppedPeople = []
  for i in range(size):
    if reportCount[i] >= k :
      stoppedPeople.append(id_list[i])

  result = [0] * size
  for r in set(report):
    reporter, reported = r.split()
    reporterI = id_list.index(reporter)
    reportedI = id_list.index(reported)
    if reportCount[reportedI] >= k:
      result[reporterI] += 1
  return result

id_list = ["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

result = solution(id_list, report, k)

for i in result:
  print(i, end=" ")