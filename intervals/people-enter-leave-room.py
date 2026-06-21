
'''
Given logs when people enter and leave return who was there at each interval

input:

name | start_time | end_time
Abby         10        100
Ben          50        70
Carla        60        90
Bob          110       120
output:

start_time | end_time | names
   10           50       Abby
   50           60       Abby, Ben, Carla
   60           70       Abby, Ben, Carla
   70           90       Abby, Carla
   90           100      Abby
   110          120      Bob

Clarifications:

Dont output empty intervals (no people)
Multiple people can enter or leave at same time

'''

# TC: O(n log n) for sorting the time points and O(n^2) for checking each interval against all people
# SC: O(n) for storing the unique time points and the result
def get_intervals(data):

    result = []

    # 1. Saare unique time points nikal kar sort karo
    time_points = sorted(list(set([row[1] for row in data] + [row[2] for row in data])))

    # 2. Har consecutive interval ko check karo
    for i in range(len(time_points) - 1):

        start = time_points[i]
        end = time_points[i + 1]

        # Check karo is interval mein kaun-kaun tha
        present_people = []

        for name, s_time, e_time in data:

            # Agar koi is pure interval ke dauran maujood tha
            if s_time <= start and end <= e_time:
                present_people.append(name)

        # Agar log thhe, to result mein add karo (Empty intervals skipped)
        if present_people:
            result.append((start, end, ", ".join(present_people)))

    return result


log_data = [
    ("Abby", 10, 100),
    ("Ben", 50, 70),
    ("Carla", 60, 90),
    ("Bob", 110, 120)
]

# Run and Print
for start, end, names in get_intervals(log_data):
    print(f"{start:<12}{end:<12}{names}")
