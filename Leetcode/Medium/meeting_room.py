# 253. Meeting Rooms II
# Problem URL: https://leetcode.com/problems/meeting-rooms-ii/
# Problem Statement: Given an array of meeting time intervals consisting of start and end times
#  [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    heap = []  # stores end times
    
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    
    return len(heap)

print(minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
print(minMeetingRooms([[7,10],[2,4]]))            # 1
print(minMeetingRooms([[0,30],[5,25],[10,20]]))   # 3

