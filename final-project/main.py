from handler import CommandCreator, Command
from interfaces import BotInterface

def main():
    ui = BotInterface()
    handler = CommandCreator()
    ui.data_output(ui.menu.navigate("Main"))

    while not ui.menu.exit:
        output_data = ""
        user_data = ui.data_input()

        if ui.command is None:
            output_data = ui.menu.navigate(user_data)
            ui.command = handler.create(user_data)
        else:
            ui.command.set_args(user_data)
        
        if ui.command is not None:
            result = ui.command.execute()
            if ui.command.success:
                ui.command = None
        if not output_data:
            output_data = result

        ui.data_output(output_data)

        
if __name__ == "__main__":
    
    main()