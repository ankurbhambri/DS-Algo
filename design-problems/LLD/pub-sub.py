'''
Designing a Pub-Sub System

Requirements
- The Pub-Sub system should allow publishers to publish messages to specific topics.
- Subscribers should be able to subscribe to topics of interest and receive messages published to those topics.
- The system should support multiple publishers and subscribers.
- Messages should be delivered to all subscribers of a topic in real-time.
- The system should handle concurrent access and ensure thread safety.
- The Pub-Sub system should be scalable and efficient in terms of message delivery.


####################
Entities
####################

--------------------------------------------------------------------------------
Message
- payload: str
- timestamp: datetime

+ get_payload() -> str
+ __str__() -> str

--------------------------------------------------------------------------------

Subscriber (abstract)
+ get_id() -> str
+ on_message(message: Message)

    AlertSubscriber extends Subscriber
    - id: str

    + get_id() -> str
    + on_message(message: Message)


    NewsSubscriber extends Subscriber
    - id: str

    + get_id() -> str
    + on_message(message: Message)


--------------------------------------------------------------------------------

Topic
- name: str
- subscribers: Set[Subscriber]
- delivery_executor: ThreadPoolExecutor

+ get_name() -> str
+ add_subscriber(subscriber: Subscriber)
+ remove_subscriber(subscriber: Subscriber)
+ broadcast(message: Message)
+ _deliver_message(subscriber: Subscriber, message: Message)


--------------------------------------------------------------------------------

PubSubService
- topic_registry: Dict[str, Topic]
- delivery_executor: ThreadPoolExecutor

+ create_topic(topic_name: str)
+ subscribe(topic_name: str, subscriber: Subscriber)
+ unsubscribe(topic_name: str, subscriber: Subscriber)
+ publish(topic_name: str, message: Message)
+ shutdown()
+ get_instance() -> PubSubService

'''


import threading
from typing import Set, Dict
from datetime import datetime, time
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor


class Message:
    def __init__(self, payload: str):
        self.payload = payload
        self.timestamp = datetime.now()

    def get_payload(self) -> str:
        return self.payload

    def __str__(self) -> str:
        return f"Message{{payload='{self.payload}'}}"


class Subscriber(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def on_message(self, message: Message):
        pass

class AlertSubscriber(Subscriber):
    def __init__(self, subscriber_id: str):
        self.id = subscriber_id

    def get_id(self) -> str:
        return self.id

    def on_message(self, message: Message):
        print(f"!!! [ALERT - {self.id}] : '{message.get_payload()}' !!!")

class NewsSubscriber(Subscriber):
    def __init__(self, subscriber_id: str):
        self.id = subscriber_id

    def get_id(self) -> str:
        return self.id

    def on_message(self, message: Message):
        print(f"[Subscriber {self.id}] received message '{message.get_payload()}'")


class Topic:
    def __init__(self, name: str, delivery_executor: ThreadPoolExecutor):
        self.name = name
        self.delivery_executor = delivery_executor
        self.subscribers: Set[Subscriber] = set()

    def get_name(self) -> str:
        return self.name

    def add_subscriber(self, subscriber: Subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self.subscribers.discard(subscriber)

    def broadcast(self, message: Message):
        for subscriber in self.subscribers:
            self.delivery_executor.submit(self._deliver_message, subscriber, message)

    def _deliver_message(self, subscriber: Subscriber, message: Message):
        try:
            subscriber.on_message(message)
        except Exception as e:
            print(f"Error delivering message to subscriber {subscriber.get_id()}: {str(e)}")


class PubSubService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self.topic_registry: Dict[str, Topic] = {}
        # A cached thread pool is suitable for handling many short-lived, bursty tasks (message deliveries).
        self.delivery_executor = ThreadPoolExecutor()
        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def create_topic(self, topic_name: str):
        if topic_name not in self.topic_registry:
            self.topic_registry[topic_name] = Topic(topic_name, self.delivery_executor)
        print(f"Topic {topic_name} created")

    def subscribe(self, topic_name: str, subscriber: Subscriber):
        topic = self.topic_registry.get(topic_name)
        if topic is None:
            raise ValueError(f"Topic not found: {topic_name}")
        topic.add_subscriber(subscriber)
        print(f"Subscriber '{subscriber.get_id()}' subscribed to topic: {topic_name}")

    def unsubscribe(self, topic_name: str, subscriber: Subscriber):
        topic = self.topic_registry.get(topic_name)
        if topic is not None:
            topic.remove_subscriber(subscriber)
        print(f"Subscriber '{subscriber.get_id()}' unsubscribed from topic: {topic_name}")

    def publish(self, topic_name: str, message: Message):
        print(f"Publishing message to topic: {topic_name}")
        topic = self.topic_registry.get(topic_name)
        if topic is None:
            raise ValueError(f"Topic not found: {topic_name}")
        topic.broadcast(message)

    def shutdown(self):
        print("PubSubService shutting down...")
        self.delivery_executor.shutdown(wait=True)
        print("PubSubService shutdown complete.")


class PubSubDemo:
    @staticmethod
    def main():
        pub_sub_service = PubSubService.get_instance()

        # --- Create Subscribers ---
        sports_fan1 = NewsSubscriber("SportsFan1")
        sports_fan2 = NewsSubscriber("SportsFan2")
        techie1 = NewsSubscriber("Techie1")
        all_news_reader = NewsSubscriber("AllNewsReader")
        system_admin = AlertSubscriber("SystemAdmin")

        # --- Create Topics and Subscriptions ---
        SPORTS_TOPIC = "SPORTS"
        TECH_TOPIC = "TECH"
        WEATHER_TOPIC = "WEATHER"

        pub_sub_service.create_topic(SPORTS_TOPIC)
        pub_sub_service.create_topic(TECH_TOPIC)
        pub_sub_service.create_topic(WEATHER_TOPIC)

        pub_sub_service.subscribe(SPORTS_TOPIC, sports_fan1)
        pub_sub_service.subscribe(SPORTS_TOPIC, sports_fan2)
        pub_sub_service.subscribe(SPORTS_TOPIC, all_news_reader)
        pub_sub_service.subscribe(SPORTS_TOPIC, system_admin)

        pub_sub_service.subscribe(TECH_TOPIC, techie1)
        pub_sub_service.subscribe(TECH_TOPIC, all_news_reader)

        print("\n--- Publishing Messages ---")

        # --- Publish to SPORTS topic ---
        pub_sub_service.publish(SPORTS_TOPIC, Message("Team A wins the championship!"))
        # Expected: SportsFan1, SportsFan2, AllNewsReader, SystemAdmin receive this.

        # --- Publish to TECH topic ---
        pub_sub_service.publish(TECH_TOPIC, Message("New AI model released."))
        # Expected: Techie1, AllNewsReader receive this.

        # --- Publish to WEATHER topic (no subscribers) ---
        pub_sub_service.publish(WEATHER_TOPIC, Message("Sunny with a high of 75°F."))
        # Expected: Message is dropped.

        # Allow some time for async messages to be processed
        time.sleep(0.5)

        print("\n--- Unsubscribing a user and re-publishing ---")

        # SportsFan2 gets tired of sports news
        pub_sub_service.unsubscribe(SPORTS_TOPIC, sports_fan2)

        # Publish another message to SPORTS
        pub_sub_service.publish(SPORTS_TOPIC, Message("Major player traded to Team B."))
        # Expected: SportsFan1, AllNewsReader, SystemAdmin receive this. SportsFan2 does NOT.

        # Give messages time to be delivered
        time.sleep(0.5)

        # --- Shutdown the service ---
        pub_sub_service.shutdown()

if __name__ == "__main__":
    PubSubDemo.main()