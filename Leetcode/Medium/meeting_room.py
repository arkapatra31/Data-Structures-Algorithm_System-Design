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

# Time Complexity: O(n log n) where n is the number of intervals. This is due to sorting the intervals and the heap operations.
# Space Complexity: O(n) for the heap that stores the end times of the meetings.

# Strategy:
# 1. Sort the intervals based on start times.
# 2. Use a min-heap to keep track of the end times of meetings currently in progress.
# 3. If the current meeting starts after the earliest ending meeting, remove the earliest ending meeting from the heap.
# 4. Add the current meeting's end time to the heap.
# 5. The size of the heap at any time gives the number of rooms needed.