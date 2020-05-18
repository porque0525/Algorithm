# 추석 트래픽
from datetime import datetime, timedelta


def pre_process(lines, start, end):
    for idx, l in enumerate(lines):
        l = l.split()
        date = list(map(int, l[0].split('-')))
        time = list(map(str, l[1].split(':')))
        sec = list(map(int, time[-1].split('.')))
        
        proc_sec = list(map(int, l[2][:-1].split('.')))
        proc_sec_s = proc_sec[0]
        if len(proc_sec) > 1:
            proc_sec_ms = proc_sec[1]
        else:
            proc_sec_ms = 0
        endtime = datetime(date[0], date[1], date[2], int(time[0]), int(time[1]), sec[0], sec[1]*1000) 
        starttime = endtime - timedelta(seconds=proc_sec_s, milliseconds=proc_sec_ms) + timedelta(milliseconds=1)
        start.append(starttime)
        end.append(endtime)
        #print(starttime, " ~ ", endtime)
       
def solution(lines):
    maxV = 0
    length = len(lines)
    processing = 0
    
    start, end = [], []
    pre_process(lines, start, end)
   
    for idx in range(length):
        processing = 0
        for next_idx in range(length):
            if start[idx] <= start[next_idx] < start[idx] + timedelta(seconds=1) \
                    or start[next_idx] <= start[idx] < end[next_idx]:
                processing += 1         
                #print(start[next_idx])
        maxV = max(maxV, processing)
        #print("")

    #print("END") 
    for idx in range(length):
        processing = 0
        for next_idx in range(length):
            if end[idx] <= end[next_idx] < end[idx] + timedelta(seconds=1):
                processing += 1
                #print("1: ", end[next_idx])
            elif start[next_idx] <= end[idx] < end[next_idx]:
                processing += 1
                #print("2: ", end[next_idx])
            elif end[idx] <= start[next_idx] < end[idx] + timedelta(seconds=1):
                #print(end[idx], start[next_idx], end[idx] + timedelta(seconds=1))
                processing += 1
                #print("3: ", end[next_idx])
        maxV = max(maxV, processing)
        #print("")

    return maxV

l = ["2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
        ]

l2 = [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
        ]

l3 = [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
        ]
##print(solution(l))
##print(solution(l2))
#print(solution(l3))
