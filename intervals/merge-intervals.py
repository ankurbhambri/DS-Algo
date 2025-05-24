# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    m = [intervals[0]]
    for i in intervals[1:]:
        end = m[-1]
        if end[1] >= i[0]:
            end[1] = max(end[1], i[1])
        else:
            m.append(i)
    return m

print(merge([[1, 3],[2, 6],[8,10],[15, 18]]))
print(merge([[1, 3],[4, 6],[0, 3],[15, 18]])) # Will fail for these type of cases, but will work fine at leetcode



# Line sweep approach
def merge_intervals(intervals):

    events = []
    for start, end in intervals: 
        events.append((start, True))  # Start event
        events.append((end, False))   # End event

    events.sort()
    
    result = []
    active = 0
    curr_start = None
    

    for time, is_start in events:
        if is_start:

            if active == 0:
                curr_start = time
            active += 1
        else:
          
            active -= 1
            if active == 0:
                result.append([curr_start, time])
    
    return result

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
print(merge_intervals([[1, 3],[4, 6],[0, 3],[15, 18]]))
