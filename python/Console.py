import inspect
import os
from datetime import datetime

from colorama import Fore, Style, init


init(autoreset=True)


class Console:

    _colors = {
        "LOG": Fore.WHITE,
        "DEBUG": Fore.LIGHTCYAN_EX,
        "INFO": Fore.LIGHTGREEN_EX,
        "WARN": Fore.LIGHTYELLOW_EX,
        "ERROR": Fore.LIGHTRED_EX
    }

    @staticmethod
    def _log(tipo, mensagem):
        frame = inspect.currentframe().f_back.f_back

        arquivo = os.path.basename(frame.f_code.co_filename)
        linha = frame.f_lineno

        timestamp = datetime.now().strftime("%H:%M:%S")

        cor = Console._colors.get(tipo, Fore.WHITE)

        tipo_formatado = f"[{tipo}]".ljust(9)
        local_formatado = f"{arquivo}:{linha}".ljust(20)

        print(
            f"{Fore.LIGHTBLACK_EX}{timestamp} "
            f"{cor}{tipo_formatado}"
            f"{Fore.LIGHTBLUE_EX}{local_formatado}"
            f"{Style.RESET_ALL}{mensagem}"
        )

    @staticmethod
    def log(mensagem):
        Console._log("LOG", mensagem)

    @staticmethod
    def debug(mensagem):
        Console._log("DEBUG", mensagem)

    @staticmethod
    def info(mensagem):
        Console._log("INFO", mensagem)

    @staticmethod
    def warn(mensagem):
        Console._log("WARN", mensagem)

    @staticmethod
    def error(mensagem):
        Console._log("ERROR", mensagem)


console = Console()

console.log('olá!')