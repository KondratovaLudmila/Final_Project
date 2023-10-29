from abc import abstractmethod, ABC
from menu import Menu

class InputInterface(ABC):
    @abstractmethod
    def data_input(self):
        """Returns user data or actions"""

class OutputInterface(ABC):
    @abstractmethod
    def data_output(self):
        """Shows proccessed data to user"""

class ConsoleInpute(InputInterface):
    def data_input(self):
        data = input()
        return data

class ConsoleOutput(OutputInterface):
    def data_output(self, data):
        print(data)


class BotInterface(ConsoleInpute,ConsoleOutput ):
    def __init__(self):
        self.menu = Menu()
        self.exit = False
        self.command = None

        