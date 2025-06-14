from threading import Lock

class Singleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        # Double-checked locking for thread-safety
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Optional: Prevent re-initialization
        if not hasattr(self, "_initialized"):
            print("Initializing Singleton instance")
            self._initialized = True
