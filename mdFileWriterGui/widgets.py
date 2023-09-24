import tkinter as tk
import tkinter as ttk
import var_util as vu

class MenuBar():
    def __init__(self,root):
        # Create a menu bar
        menubar = tk.Menu(root)

        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self._file_new)
        file_menu.add_command(label="Open", command=self._file_open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Add the file and edit menus to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)

        # Configure the app to use the menu bar
        root.config(menu=menubar)

    def _file_new(self):
        print("file new fun")

    def _file_open(self):
        print("file open fun")
        

class SingleElement():
    def __init__(self,root):
        # Create a frame
        frame = tk.Frame(root, width=vu.ELEMENT_IN_LIST_WIDTH, height=vu.ELEMENT_IN_LIST_HEIGHT, bg=vu.COLOR_ELEMENT_LIST)
        frame.pack(padx=0, pady=5)
        frame.pack_propagate(False)

        # Create labels within the frame
        label1 = tk.Label(frame, text="Headline 1", height=0,
                            bg=vu.COLOR_BACKGOUND, fg=vu.TEXT_COLOR_2,
                            font=(vu.MAIN_FONT, 12))
        label1.place(x=10, y=4)

        label2 = tk.Label(frame, text="Intro", height=0,
                            bg=vu.COLOR_BACKGOUND, fg=vu.TEXT_COLOR_1,
                            font=(vu.MAIN_FONT, 20))
        label2.place(x=10, y=30)


class ElementViewerFrame():
    def __init__(self,root):
        left_frame = tk.Frame(root, width=400, height=600, bg="red")
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # Create a large text input in the left frame
        text_input = tk.Text(left_frame, wrap=tk.WORD)
        text_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)