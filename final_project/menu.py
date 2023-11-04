class Menu():
    exit = False
    MENU = {
    "Main": ["Hello", "Contacts", "Notes", "File Sorter", "Exit/Close/Good Bye"],
    "Contacts": ["Add", "Delete", "Add phone", "Del phone", "Find", "DTB", "SBS", "Show", "Next"],
    "Notes": ["Add", "Delete", "Add tag", "Del tag", "Find", "Show", "Next"],
    }

    def navigate(self, command: str):
        result = ""
        self.exit = command.lower() in "exit/close/good bye"
        for key in self.MENU:
            if command.lower() == key.lower():
                if self.MENU[key]:
                    result = "\n"
                    result = result.join(self.MENU[key]) + "\n------------------------"
                    result = f"-----------{key}--------\n" + result
                break
        return result