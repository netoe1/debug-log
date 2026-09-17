
from pathlib import Path
class LogFile:

    # Stores log lines temporarily in memory.
    __lines = []

    # Enable save logs to file. For Default, is false.
    __enabled = False

    # Default output log file.
    __filename = "application.log"

    @classmethod
    def append(cls, text: str):
        """
        Add a new log entry to the internal buffer.
        """

        if(cls.__enabled == True):
            cls.__lines.append(text)

    @classmethod
    def set_filename(cls, filename: str):
        """
        Set the output log file name.
        """
        cls.__filename = filename

    @classmethod
    def clear(cls):
        """
        Remove all buffered log entries.
        """
        cls.__lines.clear()

    @classmethod
    def save(cls):
        """
        Persist all buffered log entries to disk.

        The file is created automatically if it does not exist.
        New entries are appended to the existing file.
        """
        if(cls.__enabled != False):
            path = Path(cls.__filename)

            with open(path, "a", encoding="utf-8") as file:
                for line in cls.__lines:
                    file.write(line + "\n")

            # Clear the buffer after saving.
            cls.__lines.clear()
            return
        from .Console import Console
        Console.warn('Cannot save if LogFile.__enabled == False!')


    @classmethod
    def enable(cls):
        """
        Enable the module to save logs.
        """
        cls.__enabled = True

    @classmethod
    def disable(cls):
        """
        Disable the module to save logs.
        """
        cls.__enabled = False
