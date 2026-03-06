'''
Design a logging system

You are given a collection of log entries, where each entry consists of a unique id and a timestamp. 
The timestamp is a string in the format Year:Month:Day:Hour:Minute:Second (for example, 2018:07:14:09:21:00). All fields are zero-padded numbers.

Methods:

- void addLog(int logId, String time): Stores a log identified by logId and its time in the system.

- List<Integer> getLogs(String startTime, String endTime, String granularity):
    Returns the list of logIds sorted in ascending order whose timestamps are in the range from startTime to endTime (inclusive), 
    considering only up to the specified granularity ("Year", "Month", "Day", "Hour", "Minute", or "Second").

'''
class LogSystem:
    def __init__(self):
        self.logs = []
        # Define how many characters to keep for each granularity
        # Format: "Year:Month:Day:Hour:Minute:Second"
        # Indices: 4   7     10  13   16     19
        self.g_map = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def addLog(self, logId: int, time: str) -> None:
        self.logs.append((time, logId))

    def getLogs(self, startTime: str, endTime: str, granularity: str) -> list[int]:

        idx = self.g_map[granularity]

        # Truncate start and end bounds based on granularity
        start = startTime[:idx]
        end = endTime[:idx]

        result = []
        for log_time, log_id in self.logs:

            # Truncate current log time and compare lexicographically
            if start <= log_time[:idx] <= end:
                result.append(log_id)

        # Requirement: IDs must be sorted in ascending order
        result.sort()
        return result


obj = LogSystem()
obj.addLog(11, "2018:07:14:09:21:00")
obj.addLog(22, "2018:07:14:08:59:00")
obj.addLog(33, "2017:06:01:12:00:00")
print(obj.getLogs("2017:01:01:00:00:00", "2018:12:31:23:59:59", "Year"))   # returns [11, 22, 33]
print(obj.getLogs("2018:07:14:00:00:00", "2018:07:14:09:00:00", "Hour"))   # returns [11, 22]