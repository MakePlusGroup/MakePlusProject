from tkinter import *

class main_frame:

    """
        This is the blank page the is populated by the other UIs
        it has a current frame that shows the UI intended (passed into by the controller)
        current controller is the controller that is active on the screen at that time.
        current controller will be replaced when moving on to a new page
    """

    def __init__(self, UI_frame):
        self.master = UI_frame
        self.screenW = str(int(self.master.winfo_screenwidth()/3))
        self.screenH = str(int(self.master.winfo_screenheight()/2))
        self.master.title('PyScan')
        self.master.geometry(self.screenW + "x" + self.screenH)
        self.master.resizable(0, 0)

        self.UI_frame = Frame(self.master)
        self.UI_frame.pack(fill=BOTH, expand=YES)

        self.current_frame = None
        self.current_ctr = None

if __name__ == "__main__":
    root = Tk()
    main_frame(root)
    mainloop()
