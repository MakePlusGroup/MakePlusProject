# Features:
# Email Parser - gathers .ply scans from an email
# Model Classifier - loads .ply file and returns the shape of the object

from tkinter import Tk, mainloop
from controller.GUI_main_controller import main_controller

def main():
    root = Tk()
    main_controller(root)
    mainloop()

if __name__ == "__main__":
    main()
