from tkinter import *
from .GUI_baseUI import UI
import traceback


class LoadScan_UI(UI):

    """
        The UI for load scan into classifier
    """

    def __init__(self, master, img):
        super().__init__(master, img)


        # ------------------MID FRAME ----------------------------------
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(2, weight=1)

        self.mid_frame.grid_rowconfigure(0, weight=0)
        self.mid_frame.grid_rowconfigure(1, weight=1)

        self.header_label = Label(self.mid_frame, text='Load Scan', font=("TkDefaultFont", 12))
        self.header_label.grid(row=0, column=1, pady=10)

        self.CS_frame = Frame(self.mid_frame)
        self.CS_frame.grid(row=1, column=1)

        self.Load_frame = Frame(self.CS_frame)
        self.Load_frame.grid(row=0, column=0)
        self.Load_frame.grid_columnconfigure(1, weight=1)

        self.File_label = Label(self.Load_frame, text='File: ')
        self.File_label.grid(row=0, column=0, padx=2, pady=5)

        self.log_File_Path = StringVar()
        self.File_path = Label(self.Load_frame, textvariable=self.log_File_Path, width=40, anchor=W)
        self.File_path.grid(row=0, column=1, pady=5)

        self.Open_but = Button(self.Load_frame, text='Open', width=5)
        self.Open_but.grid(row=0, column=2, padx=10, pady=5)

        self.Data_frame = Frame(self.CS_frame)
        self.Data_frame.grid(row=1, column=0, sticky='nswe')
        self.Data_frame.grid_rowconfigure(1, weight=1)
        self.Data_frame.grid_columnconfigure(1, weight=1)


        self.Data_label = Label(self.Data_frame, text='File Data:', justify='left')
        self.Data_label.grid(row=0, column=0, padx=2, pady=5)

        self.Data_listbox = Listbox(self.Data_frame, selectmode=BROWSE)
        self.Data_listbox.grid(row=1, column=0, columnspan=2, sticky='nswe')
        self.Data_listbox_scrollbar = Scrollbar(self.Data_frame, orient='vertical')
        self.Data_listbox.config(yscrollcommand=self.Data_listbox_scrollbar.set)
        self.Data_listbox_scrollbar.config(command=self.Data_listbox.yview)
        self.Data_listbox_scrollbar.grid(row=1, column=3, sticky='ns')

        # -------------Bottom FRAME ---------------------------------------------
        self.botbut_frame.grid_rowconfigure(0, weight=1)
        self.botbut_frame.grid_rowconfigure(2, weight=1)

        self.botbut_frame.grid_columnconfigure(0, weight=1)
        self.botbut_frame.grid_columnconfigure(1, weight=1)
        self.botbut_frame.grid_columnconfigure(2, weight=1)
        self.botbut_frame.grid_columnconfigure(3, weight=1)
        self.botbut_frame.grid_columnconfigure(4, weight=1)


        self.can_but = Button(self.botbut_frame, text='Back', width=10)
        self.can_but.grid(row=1, column=0, pady=15)

        self.show_but = Button(self.botbut_frame, state=DISABLED, text='Show Model', width=10)
        self.show_but.grid(row=1, column=1, pady=15)

        self.hist_but = Button(self.botbut_frame, state=DISABLED, text='Show Histogram', width=13)
        self.hist_but.grid(row=1, column=2, pady=15)

        self.classify_but = Button(self.botbut_frame, text='Classify', width=8)
        self.classify_but.grid(row=1, column=3, pady=15)

        self.more_but = Button(self.botbut_frame,  text="Add to Reference Library", command=self.run_bad_math, width=10)
        self.more_but.grid(row=1, column=4, pady=15)


    def run_bad_math(self):
        print('in run bad math')
        try:
            1 / 0
        except Exception as error:
            title = "Traceback Error"
            message = "An error has occurred: '{}'.".format(error)
            detail = traceback.format_exc()
            topErrorWindow(title, message, detail)


class topErrorWindow(Toplevel):
    def __init__(self, title, message, detail):
        Toplevel.__init__(self)
        self.details_expanded = False
        self.title(title)
        self.geometry("350x75")
        self.minsize(350, 75)
        self.maxsize(425, 250)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        button_frame = Frame(self)
        button_frame.grid(row=0, column=0, sticky="nsew")
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        text_frame = Frame(self)
        text_frame.grid(row=1, column=0, padx=(7, 7), pady=(7, 7), sticky="nsew")
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        Label(button_frame, text=message).grid(row=0, column=0, columnspan=2, pady=(7, 7))
        Button(button_frame, text="OK", command=self.destroy).grid(row=1, column=0, sticky="e")
        Button(button_frame, text="Details", command=self.toggle_details).grid(row=1, column=1, sticky="w")

        self.textbox = Text(text_frame, height=6)
        self.textbox.insert("1.0", detail)
        self.textbox.config(state="disabled")
        self.scrollb = Scrollbar(text_frame, command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.scrollb.set)

    def toggle_details(self):
        if self.details_expanded == False:
            self.textbox.grid(row=0, column=0, sticky='nsew')
            self.scrollb.grid(row=0, column=1, sticky='nsew')
            self.geometry("350x160")
            self.details_expanded = True

        else:
            self.textbox.grid_forget()
            self.scrollb.grid_forget()
            self.geometry("350x75")
            self.details_expanded = False


if __name__ == "__main__":
    root = Tk()
    img = ""
    LoadScan_UI(root, img)
    mainloop()
