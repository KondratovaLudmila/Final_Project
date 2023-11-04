from abc import abstractmethod, ABC
import difflib
from final_project.menu import Menu

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
        
class BotInterface(ConsoleInpute, ConsoleOutput):
    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.exit = False
        self.command = None

    def find_closest_match(self, user_input, commands):
        closest_match = difflib.get_close_matches(
            user_input, commands, n=1, cutoff=0.6)
        if closest_match:
            return closest_match[0]
        else:
            return user_input

        