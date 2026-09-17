from enum import Enum
from colorama import Fore, Style, init    # Used to apply colors to console output.
from datetime import datetime             # Used to generate timestamps.
import inspect                            # Used to inspect the call stack.
from pathlib import Path                  # Used to manipulate file paths.
from LogFile import LogFile       # Used to store log messages into a file.


# Defines all available console message types.
class ConsoleType(Enum):
    LOG = "LOG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    SUCCESS = "SUCCESS"


# Initializes Colorama and automatically resets colors after each print.
init(autoreset=True)


class Console:

    # Controls whether debug messages should be displayed.
    __debug_is_active = True

    # Maps each log level to its respective console color.
    COLORS = {
        "LOG": Fore.WHITE,
        "INFO": Fore.CYAN,
        "WARN": Fore.YELLOW,
        "ERROR": Fore.RED,
        "SUCCESS": Fore.GREEN,
        "DEBUG": Fore.MAGENTA,
    }

    @classmethod
    def _caller_file(cls):
        """
        Returns the filename that initiated the current log call.
        """
        frame = inspect.stack()[3]
        return Path(frame.filename).name

    @classmethod
    def __write(cls, level: str, message: str):

        # Generates the current timestamp.
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Gets the filename of the calling script.
        filename = cls._caller_file()

        # Retrieves the color configured for the current log level.
        level_color = cls.COLORS[level]

        # Prints a formatted and colored message to the terminal.
        print(
            f"{Fore.LIGHTBLACK_EX}{timestamp}{Style.RESET_ALL} "
            f"{level_color}{level:<8}{Style.RESET_ALL} "
            f"{Fore.LIGHTBLACK_EX}[{filename}]{Style.RESET_ALL} "
            f"{message}"
        )

        # Creates a plain-text version of the log entry for file storage.
        raw_text = (
            f"{timestamp} "
            f"{level:<8} "
            f"[{filename}] "
            f"{message}"
        )

        # Adds the log entry to the log file buffer.
        LogFile.append(raw_text)

    @classmethod
    def log(cls, message):
        """
        Writes a generic log message.
        """
        cls.__write("LOG", message)

    @classmethod
    def info(cls, message):
        """
        Writes an informational message.
        """
        cls.__write("INFO", message)

    @classmethod
    def warn(cls, message):
        """
        Writes a warning message.
        """
        cls.__write("WARN", message)

    @classmethod
    def error(cls, message):
        """
        Writes an error message.
        """
        cls.__write("ERROR", message)

    @classmethod
    def success(cls, message):
        """
        Writes a success message.
        """
        cls.__write("SUCCESS", message)

    @classmethod
    def debug(cls, message):
        """
        Writes a debug message only when debug mode is enabled.
        """
        if(cls.__debug_is_active == True):
            cls.__write("DEBUG", message)

    @classmethod
    def set_debug_mode(cls, state: bool):
        """
        Enables or disables debug messages.
        """
        cls.__debug_is_active = state

    @classmethod
    def is_debug_mode_active(cls):
        return cls.__debug_is_active
