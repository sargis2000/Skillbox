from typing import IO


class File:
    """
    Модернизированная версия контекст-менеджера File — теперь при попытке
    открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи.
    """

    def __init__(self, filename: str, mode: str = 'w') -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> IO:
        self.file = open(self.filename, self.mode)  # Add self.mode
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()


with File('example.txt') as file:
    file.write('Hello Wouytjtyrld!!')