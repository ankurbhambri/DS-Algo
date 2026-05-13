'''
LLD / Machine Coding

• Problem: Design an Asynchronous Task Management Library.

• Requirements:
    - Define tasks
    - Handle task dependencies
    - Global queue
    - Main task runner

This one tested design clarity + ability to translate it into working code. Focus on classes, queue management, and execution.
'''

import time

import threading

from enum import Enum
from queue import Queue
from typing import Callable, List

from concurrent.futures import ThreadPoolExecutor


class TaskStatus(Enum):
    CREATED = "CREATED"
    READY = "READY"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Task:
    def __init__(self, task_id: str, action: Callable):
        self.id = task_id
        self.action = action
        self.dependencies: List["Task"] = []
        self.dependents: List["Task"] = []
        self.in_degree = 0
        self.status = TaskStatus.CREATED

    def add_dependency(self, dependency: "Task"):
        self.dependencies.append(dependency)
        dependency.dependents.append(self)
        self.in_degree += 1

    def execute(self):
        self.status = TaskStatus.RUNNING
        try:
            self.action()
            self.status = TaskStatus.COMPLETED
        except Exception:
            self.status = TaskStatus.FAILED


class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, task: Task):
        self.queue.put(task)

    def dequeue(self) -> Task:
        return self.queue.get()


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.queue = TaskQueue()

    def register_task(self, task: Task):
        self.tasks[task.id] = task

    def build_queue(self):
        for task in self.tasks.values():
            if task.in_degree == 0:
                task.status = TaskStatus.READY
                self.queue.enqueue(task)

    def get_queue(self):
        return self.queue


class TaskRunner:
    def __init__(self, queue: TaskQueue, num_threads: int = 4):
        self.queue = queue
        self.executor = ThreadPoolExecutor(max_workers=num_threads)
        self.lock = threading.Lock()
        self.running = True

    def start(self):
        def worker():
            while self.running:
                task = self.queue.dequeue()

                def run_task(t=task):
                    t.execute()

                    for dependent in t.dependents:
                        with self.lock:
                            dependent.in_degree -= 1
                            if dependent.in_degree == 0:
                                dependent.status = TaskStatus.READY
                                self.queue.enqueue(dependent)

                self.executor.submit(run_task)

        # Start worker threads
        for _ in range(4):
            threading.Thread(target=worker, daemon=True).start()

    def shutdown(self):
        self.running = False
        self.executor.shutdown(wait=True)


manager = TaskManager()

A = Task("A", lambda: print("Task A done"))
B = Task("B", lambda: print("Task B done"))
C = Task("C", lambda: print("Task C done"))

# Dependencies
C.add_dependency(A)
C.add_dependency(B)

manager.register_task(A)
manager.register_task(B)
manager.register_task(C)

manager.build_queue()

runner = TaskRunner(manager.get_queue(), num_threads=2)
runner.start()

# Let tasks run
time.sleep(2)
runner.shutdown()