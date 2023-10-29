from abc import abstractmethod, ABC
from menu import Menu

class UserInterface(ABC):
    @abstractmethod
    def data_input(self):
        """Returns user data or actions"""
    
    @abstractmethod
    def data_output(self, data):
        """Shows proccessed data to user"""


class ConsoleUserInterface(UserInterface):
    def __init__(self):
        self.menu = Menu()

    def data_input(self):
        user_input = input()
        
        return user_input
    
    def data_output(self, data):
        print(data)

        