'''
Designing a Logging Framework

Requirements
- The logging framework should support different log levels, such as DEBUG, INFO, WARNING, ERROR, and FATAL.
- It should allow logging messages with a timestamp, log level, and message content.
- The framework should support multiple output destinations, such as console, file, and database.
- It should provide a configuration mechanism to set the log level and output destination.
- The logging framework should be thread-safe to handle concurrent logging from multiple threads.
- It should be extensible to accommodate new log levels and output destinations in the future.


#####################
Entities
#####################

--------------------------------------------------------------------------------
LogLevel (Enum)
- DEBUG
- INFO
- WARNING
- ERROR
- FATAL

--------------------------------------------------------------------------------
LogMessage
- timestamp: datetime
- level: LogLevel
- logger_name: str
- message: str
- thread_name: str

+ get_timestamp() -> datetime
+ get_level() -> LogLevel
+ get_logger_name() -> str
+ get_thread_name() -> str
+ get_message() -> str

--------------------------------------------------------------------------------
LogDestination (abstract)
+ log(message: LogMessage)

ConsoleDestination extends LogDestination
+ log(message: LogMessage)

FileDestination extends LogDestination
- file_path: str
+ log(message: LogMessage)

DatabaseDestination extends LogDestination
- connection_string: str
+ log(message: LogMessage)

--------------------------------------------------------------------------------

LogAppender (abstract)
+ append(log_message: LogMessage)
+ close()
+ get_formatter() -> LogFormatter
+ set_formatter(formatter: LogFormatter)

ConsoleAppender extends LogAppender
- formatter: LogFormatter

+ append(log_message)
+ close()

FileAppender extends LogAppender
- formatter: LogFormatter
- writer
- lock: threading.Lock

+ append(log_message)
+ close()

--------------------------------------------------------------------------------
AsyncLogProcessor
- executor: ThreadPoolExecutor
- shutdown_flag: bool

+ process(log_message: LogMessage, appenders: List[LogAppender])
+ stop()

--------------------------------------------------------------------------------
Logger
- name: str
- level: Optional[LogLevel]
- parent: Optional[Logger]
- appenders: List[LogAppender]
- additivity: bool

+ add_appender(appender: LogAppender)
+ get_appenders() -> List[LogAppender]
+ set_level(level: LogLevel)
+ set_additivity(flag: bool)

+ get_effective_level() -> LogLevel
+ log(level: LogLevel, message: str)

+ debug(message)
+ info(message)
+ warn(message)
+ error(message)
+ fatal(message)

---------------------------------------------------------------------------------
LogManager (Singleton)
- loggers: Dict[str, Logger]
- root_logger: Logger
- processor: AsyncLogProcessor

+ get_logger(name: str) -> Logger
+ get_root_logger() -> Logger
+ get_processor() -> AsyncLogProcessor
+ shutdown()

'''

import sys
import threading
from enum import Enum
from datetime import datetime, time
from abc import ABC, abstractmethod

from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5

    def is_greater_or_equal(self, other: 'LogLevel') -> bool:
        return self.value >= other.value


class LogMessage:
    def __init__(self, level: LogLevel, logger_name: str, message: str):
        self.timestamp = datetime.now()
        self.level = level
        self.logger_name = logger_name
        self.message = message
        self.thread_name = threading.current_thread().name

    def get_timestamp(self) -> datetime:
        return self.timestamp

    def get_level(self) -> LogLevel:
        return self.level

    def get_logger_name(self) -> str:
        return self.logger_name

    def get_thread_name(self) -> str:
        return self.thread_name

    def get_message(self) -> str:
        return self.message


class LogFormatter(ABC):
    @abstractmethod
    def format(self, log_message: LogMessage) -> str:
        pass

class SimpleTextFormatter(LogFormatter):
    def format(self, log_message: LogMessage) -> str:
        timestamp_str = log_message.get_timestamp().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return f"{timestamp_str} [{log_message.get_thread_name()}] {log_message.get_level().name} - {log_message.get_logger_name()}: {log_message.get_message()}\n"

class LogAppender(ABC):
    @abstractmethod
    def append(self, log_message: LogMessage):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def get_formatter(self) -> LogFormatter:
        pass

    @abstractmethod
    def set_formatter(self, formatter: LogFormatter):
        pass

class ConsoleAppender(LogAppender):
    def __init__(self):
        self.formatter = SimpleTextFormatter()

    def append(self, log_message: LogMessage):
        print(self.formatter.format(log_message), end='')

    def close(self):
        pass

    def set_formatter(self, formatter: LogFormatter):
        self.formatter = formatter

    def get_formatter(self) -> LogFormatter:
        return self.formatter


class FileAppender(LogAppender):
    def __init__(self, file_path: str):
        self.formatter = SimpleTextFormatter()
        self._lock = threading.Lock()
        try:
            self.writer = open(file_path, 'a')
        except Exception as e:
            print(f"Failed to create writer for file logs, exception: {e}")
            self.writer = None

    def append(self, log_message: LogMessage):
        with self._lock:
            if self.writer:
                try:
                    self.writer.write(self.formatter.format(log_message) + "\n")
                    self.writer.flush()
                except Exception as e:
                    print(f"Failed to write logs to file, exception: {e}")

    def close(self):
        if self.writer:
            try:
                self.writer.close()
            except Exception as e:
                print(f"Failed to close logs file, exception: {e}")

    def set_formatter(self, formatter: LogFormatter):
        self.formatter = formatter

    def get_formatter(self) -> LogFormatter:
        return self.formatter


class AsyncLogProcessor:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="AsyncLogProcessor")
        self.shutdown_flag = False

    def process(self, log_message: LogMessage, appenders: List[LogAppender]):
        if self.shutdown_flag:
            print("Logger is shut down. Cannot process log message.", file=sys.stderr)
            return

        def process_task():
            for appender in appenders:
                appender.append(log_message)

        self.executor.submit(process_task)

    def stop(self):
        self.shutdown_flag = True
        self.executor.shutdown(wait=True, timeout=2)
        if not self.executor._shutdown:
            print("Logger executor did not terminate in the specified time.", file=sys.stderr)


class LogManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if LogManager._instance is not None:
            raise Exception("This class is a singleton!")
        self.loggers: Dict[str, 'Logger'] = {}
        self.root_logger = Logger("root", None)
        self.loggers["root"] = self.root_logger
        self.processor = AsyncLogProcessor()

    @staticmethod
    def get_instance():
        if LogManager._instance is None:
            with LogManager._lock:
                if LogManager._instance is None:
                    LogManager._instance = LogManager()
        return LogManager._instance

    def get_logger(self, name: str) -> 'Logger':
        if name not in self.loggers:
            self.loggers[name] = self._create_logger(name)
        return self.loggers[name]

    def _create_logger(self, name: str) -> 'Logger':
        if name == "root":
            return self.root_logger
        
        last_dot = name.rfind('.')
        parent_name = "root" if last_dot == -1 else name[:last_dot]
        parent = self.get_logger(parent_name)
        return Logger(name, parent)

    def get_root_logger(self) -> 'Logger':
        return self.root_logger

    def get_processor(self) -> AsyncLogProcessor:
        return self.processor

    def shutdown(self):
        # Stop the processor first to ensure all logs are written
        self.processor.stop()

        # Then, close all appenders
        all_appenders = set()
        for logger in self.loggers.values():
            for appender in logger.get_appenders():
                all_appenders.add(appender)
        
        for appender in all_appenders:
            appender.close()
        
        print("Logging framework shut down gracefully.")


class Logger:
    def __init__(self, name: str, parent: Optional['Logger']):
        self.name = name
        self.level: Optional[LogLevel] = None
        self.parent = parent
        self.appenders: List[LogAppender] = []
        self.additivity = True

    def add_appender(self, appender: LogAppender):
        self.appenders.append(appender)

    def get_appenders(self) -> List[LogAppender]:
        return self.appenders

    def set_level(self, min_level: LogLevel):
        self.level = min_level

    def set_additivity(self, additivity: bool):
        self.additivity = additivity

    def get_effective_level(self) -> LogLevel:
        logger = self
        while logger is not None:
            current_level = logger.level
            if current_level is not None:
                return current_level
            logger = logger.parent
        return LogLevel.DEBUG  # Default root level

    def log(self, message_level: LogLevel, message: str):
        if message_level.is_greater_or_equal(self.get_effective_level()):
            log_message = LogMessage(message_level, self.name, message)
            self._call_appenders(log_message)

    def _call_appenders(self, log_message: LogMessage):
        if self.appenders:
            LogManager.get_instance().get_processor().process(log_message, self.appenders)
        
        if self.additivity and self.parent is not None:
            self.parent._call_appenders(log_message)

    def debug(self, message: str):
        self.log(LogLevel.DEBUG, message)

    def info(self, message: str):
        self.log(LogLevel.INFO, message)

    def warn(self, message: str):
        self.log(LogLevel.WARN, message)

    def error(self, message: str):
        self.log(LogLevel.ERROR, message)

    def fatal(self, message: str):
        self.log(LogLevel.FATAL, message)


class LoggingFrameworkDemo:
    @staticmethod
    def main():
        # --- 1. Initial Configuration ---
        log_manager = LogManager.get_instance()
        root_logger = log_manager.get_root_logger()
        root_logger.set_level(LogLevel.INFO)  # Set global minimum level to INFO

        # Add a console appender to the root logger
        root_logger.add_appender(ConsoleAppender())

        print("--- Initial Logging Demo ---")
        main_logger = log_manager.get_logger("com.example.Main")
        main_logger.info("Application starting up.")
        main_logger.debug("This is a debug message, it should NOT appear.")  # Below root level
        main_logger.warn("This is a warning message.")

        # --- 2. Hierarchy and Additivity Demo ---
        print("\n--- Logger Hierarchy Demo ---")
        db_logger = log_manager.get_logger("com.example.db")
        # db_logger inherits level and appenders from root
        db_logger.info("Database connection pool initializing.")

        # Let's create a more specific logger and override its level
        service_logger = log_manager.get_logger("com.example.service.UserService")
        service_logger.set_level(LogLevel.DEBUG)  # More verbose logging for this specific service
        service_logger.info("User service starting.")
        service_logger.debug("This debug message SHOULD now appear for the service logger.")

        # --- 3. Dynamic Configuration Change ---
        print("\n--- Dynamic Configuration Demo ---")
        print("Changing root log level to DEBUG...")
        root_logger.set_level(LogLevel.DEBUG)
        main_logger.debug("This debug message should now be visible.")

        try:
            time.sleep(0.5)
            log_manager.shutdown()
        except Exception as e:
            print("Caught exception:", e)

if __name__ == "__main__":
    LoggingFrameworkDemo.main()