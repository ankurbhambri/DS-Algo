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



# Similar leetcode problem: https://leetcode.com/problems/design-log-storage-system/description/

'''
You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Implement the LogSystem class:

LogSystem() Initializes the LogSystem object.
void put(int id, string timestamp) Stores the given log (id, timestamp) in your storage system.
int[] retrieve(string start, string end, string granularity) Returns the IDs of the logs whose timestamps are within the range from start to end inclusive. 
Start and end all have the same format as timestamp, and granularity means how precise the range should be (i.e. to the exact Day, Minute, etc.). 

For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", and granularity = "Day" means that we need to find the logs within the inclusive range from Jan. 1st 2017 to Jan. 
2nd 2017, and the Hour, Minute, and Second for each log entry can be ignored.

Example 1:

Input
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]

Output
[null, null, null, null, [3, 2, 1], [2, 1]]

Explanation
LogSystem logSystem = new LogSystem();
logSystem.put(1, "2017:01:01:23:59:59");
logSystem.put(2, "2017:01:01:22:59:59");
logSystem.put(3, "2016:01:01:00:00:00");

// return [3,2,1], because you need to return all logs between 2016 and 2017.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");

// return [2,1], because you need to return all logs between Jan. 1, 2016 01:XX:XX and Jan. 1, 2017 23:XX:XX.
// Log 3 is not returned because Jan. 1, 2016 00:00:00 comes before the start of the range.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");
 

Constraints:

    1 <= id <= 500
    2000 <= Year <= 2017
    1 <= Month <= 12
    1 <= Day <= 31
    0 <= Hour <= 23
    0 <= Minute, Second <= 59
    granularity is one of the values ["Year", "Month", "Day", "Hour", "Minute", "Second"].
    At most 500 calls will be made to put and retrieve.

'''

class LogSystem:
    def __init__(self):
        self.d = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str):
        i = self.d[granularity]
        return [id for id, ts in self.logs if start[:i] <= ts[:i] <= end[:i]]


obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))   # returns [1, 2]
print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))   # returns [1, 2, 3]