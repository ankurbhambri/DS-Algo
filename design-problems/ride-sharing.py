'''
Designing a Ride-Sharing Service Like Uber

Requirements:

- The ride-sharing service should allow passengers to request rides and drivers to accept and fulfill those ride requests.
- Passengers should be able to specify their pickup location, destination, and desired ride type (e.g., regular, premium).
- Drivers should be able to see available ride requests and choose to accept or decline them.
- The system should match ride requests with available drivers based on proximity and other factors.
- The system should calculate the fare for each ride based on distance, time, and ride type.
- The system should handle payments and process transactions between passengers and drivers.
- The system should provide real-time tracking of ongoing rides and notify passengers and drivers about ride status updates.
- The system should handle concurrent requests and ensure data consistency.

'''

from abc import ABC, abstractmethod


# ---------------------- Ride ----------------------

class IRide(ABC):
    @abstractmethod
    def request_ride(self, user, src, dst):
        pass


# Geospatial index, DB proximity, pull 5 min apart, QUEUE

def fare_price_calc(dist_data):
    pass

def fetch_lat_long(location):
    pass


class RideRequest(IRide):

    def request_ride(self, user, src, dst):
        # Euclidean distance, Manhattan distance
        price = fare_price_calc((fetch_lat_long(src), fetch_lat_long(dst)))
        return price


# ---------------------- Driver ----------------------

class IDriverProfiles(ABC):
    pass


class Driver(IDriverProfiles):

    def find_drivers(self, lat, long):
        # user_id, location
        # filter - select ... where
        # QUEUE - redis, 100k, 10k, last 2min -> 2k
        # cluster_id - Quad trees, maps - [c1 - [driver_id, ], c2 - [], c3 - []]
        pass


# ---------------------- Payments (SOLID) ----------------------

class IPayment(ABC):
    @abstractmethod
    def payment_type(self):
        pass


class IPaymentAuthenticate(ABC):
    @abstractmethod
    def auth_method(self):
        pass


class IOnlinePayments(IPayment):
    pass


class UPIPayments(IOnlinePayments):
    def payment_type(self):
        pass


class OnlineBankingPayments(IOnlinePayments, IPaymentAuthenticate):
    def payment_type(self):
        pass

    def auth_method(self):
        pass


class AmexCardPayments(IOnlinePayments, IPaymentAuthenticate):
    def payment_type(self):
        pass

    def auth_method(self):
        pass


class DebitCardPayments(IOnlinePayments, IPaymentAuthenticate):
    def payment_type(self):
        pass

    def auth_method(self):
        pass


class CashPayments(IPayment):
    def payment_type(self):
        pass


# ---------------------- Observer Pattern ----------------------

# Observer: User requested ride -> notify [[drivers]]
# Fetch [driver_ids] from redis cluster
# 10s TTL windows in redis (user_id, request_id, driver_id)

class Requests:
    # requests hashmap = {} -> [user_id, request_id]
    pass


class FindDriver:

    class Observer:
        def __init__(self):
            self.status = False

        def subscribe(self, driver_ids, user_id):
            requests = {}
            for driver_obj in driver_ids:
                requests[user_id] = tuple(driver_obj)
                # redis entry
                # yield return 10s delay

        def notify(self):
            # set status to True
            # driver location, time to reach, vehicle information, ratings
            self.status = True

        def readiness(self):
            if self.status is False:
                # return retry
                pass

    class Subscriber:
        def __init__(self, user_obj):
            self.user_obj = user_obj

        def ride_accept(self):
            self.user_obj.notify()

        def decline(self):
            # redis entry
            pass


# ---------------------- Kubernetes Pod Scheduling ----------------------

'''
Your task is to create a function that simulates a basic version of Kubernetes pod scheduling.
The function should assign pods based on their resource requirements and the available resources in a cluster.
You should return a list indicating whether each pod was successfully scheduled or not.

FOLLOW UP - How would you modify the scheduling logic to prioritize certain pods (e.g., critical pods) over others?
'''


class Pod:
    def __init__(self, name, cpu_request, memory_request):
        self.name = name
        self.cpu_request = cpu_request
        self.memory_request = memory_request


class Node:
    def __init__(self, name, cpu_capacity, memory_capacity, cpu_allocated, memory_allocated):
        self.name = name
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_allocated = cpu_allocated
        self.memory_allocated = memory_allocated


class Solution:

    def __init__(self, pods: list, nodes: list):
        self.pods = pods
        self.nodes = nodes

    def allocate(self):

        if not self.pods or not self.nodes:
            return []

        res = {pod.name: {"status": "Not Scheduled", "node_name": "NA"} for pod in self.pods}

        for pod in self.pods:

            for node in self.nodes:

                if pod.cpu_request <= node.cpu_capacity and pod.memory_request <= node.memory_capacity:

                    node.memory_capacity -= pod.memory_request
                    node.cpu_capacity -= pod.cpu_request

                    res[pod.name]["status"] = "Scheduled"
                    res[pod.name]["node_name"] = node.name
                    break

        return res


pods = [
    {"name": "pod1", "cpu_request": 1, "memory_request": 1024},
    {"name": "pod2", "cpu_request": 2, "memory_request": 5555},
    {"name": "pod3", "cpu_request": 3, "memory_request": 5555},
    {"name": "pod4", "cpu_request": 4, "memory_request": 256},
    {"name": "pod5", "cpu_request": 5, "memory_request": 768},
    {"name": "pod6", "cpu_request": 1, "memory_request": 256}
]

nodes = [
    {"name": "node1", "cpu_capacity": 4, "memory_capacity": 2048, "cpu_allocated": 0, "memory_allocated": 0},
    {"name": "node2", "cpu_capacity": 2, "memory_capacity": 1024, "cpu_allocated": 0, "memory_allocated": 0}
]

node_objs = [
    Node(n["name"], n["cpu_capacity"], n["memory_capacity"], n["cpu_allocated"], n["memory_allocated"])
    for n in nodes
]

pod_objs = [
    Pod(p["name"], p["cpu_request"], p["memory_request"])
    for p in pods
]

obj = Solution(pod_objs, node_objs)
print(obj.allocate())

'''
Expected output:
{'pod1': {'status': 'Scheduled', 'node_name': 'node1'}, 'pod2': {'status': 'Not Scheduled', 'node_name': 'NA'},
 'pod3': {'status': 'Not Scheduled', 'node_name': 'NA'}, 'pod4': {'status': 'Scheduled', 'node_name': 'node1'},
 'pod5': {'status': 'Not Scheduled', 'node_name': 'NA'}, 'pod6': {'status': 'Scheduled', 'node_name': 'node2'}}
'''
