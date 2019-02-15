from tkinter import *

from controller.GUI_controllers import LoadGet_controller
from view import main_frame


class main_controller:

    """
        Where the start of the GUI runs.
        gives controller a "main" frame based on the master
        all UI will use the main frame
    """

    def __init__(self, master):
        self.master = master
        self.main = main_frame(self.master)
        self.main.current_ctr = LoadGet_controller(self.main.UI_frame)


if __name__ == "__main__":

    root = Tk()
    main_controller(root)
    mainloop()