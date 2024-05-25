import heapq

class Output:
    def __init__(self, arr):
        self.arr = arr


    def preProcess(self):
        # Serializing the data in format
        """
        {
            '1': {'timestamps': [1, 3, 2], 'actions': ['u1', 'u3', 'u2']},
            '2': {'timestamps': [4, 9, 7], 'actions': ['u1', 'u4', 'u7']},
            '3': {'timestamps': [3, 7], 'actions': ['u2', 'u5']},
            '4': {'timestamps': [5], 'actions': ['u4']}
        }
        """
        preProcess = {item["id"]: {"actions": [], "timestamps": []} for item in values}
        for item in values:
            obj = preProcess[item["id"]]
            obj["actions"].append(item["action"])
            obj["timestamps"].append(item["timeStamp"])

        return preProcess


    # Heap data structure TC O(nlogn)
    def method2(self):
        data = self.preProcess()
        res = dict()
        for item in data:
            data_tuples = list(zip(data[item]["actions"], data[item]["timestamps"]))
            heapMap = heapq.heapify(data_tuples)
            res[item] = list(i for i, j in data_tuples)
        return res 


    # Python sorted function TC O(n^2)
    def method1(self):
        data = self.preProcess()
        res = dict() # dictionary
        for item in data:
            # zip two arrays
            obj = zip(data[item]["actions"], data[item]["timestamps"]) # O(1) approach
            # sorted function and lambda anonymous function
            res[item] = list(i for i, j in list(sorted(obj, key = lambda x: x[1]))) # sorting is O(n)
        return res


    # Brute force TC O(n^3)
    def method3(self):
        data = self.preProcess()
        res = {}
        for item in data: # O(n)
            # taking actions out of data
            actions = data[item]["actions"] 
            # taking timestamps out of data
            time = data[item]["timestamps"]
            mapData = {}
            # mapping both activities            
            for i in range(len(actions)):
                mapData[actions[i]] = time[i]

            # sorting time
            time.sort()
            # matching time and appending an action.
            # fifo approach if two action time is same.
            temp = []
            for t in time: # O(n)
                for k, v in mapData.items(): # O(n)
                    if v == t:
                        temp.append(k)
            res[item] = temp
        return res



values = [{
  "id": "1", "action": "u1", "timeStamp": 1
},{
  "id": "1", "action": "u3", "timeStamp": 3
},{
  "id": "1", "action": "u2", "timeStamp": 2
},{
  "id": "2", "action": "u1", "timeStamp": 4
},{
  "id": "2", "action": "u4", "timeStamp": 9
},{
  "id": "2", "action": "u7", "timeStamp": 7
},{
  "id": "3", "action": "u2", "timeStamp": 3
},{
  "id": "4", "action": "u4", "timeStamp": 5
},{
  "id": "3", "action": "u5", "timeStamp": 7
}]


obj = Output(values)
print(obj.method1())
print(obj.method2())
print(obj.method3())
