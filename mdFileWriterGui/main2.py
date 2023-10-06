import tkinter as tk
from tkinter import ttk
import config 


element_list = [['headline1','intro'],
                ['test','welcome to my app'],
                ['headline2','installing'],
                ['text','pip install my app'],]



# SECTION: main app
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # main app config
        self.title(config.WINDOW_TITLE)
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.configure(bg=config.COLOR_BACKGOUND)
        
        # create a menu bar
        menubar = tk.Menu(self)
        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.cmd_barMenu_new)
        file_menu.add_command(label="Open", command=self.cmd_barMenu_open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        # Add the file and edit menus to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)
        # Configure the app to use the menu bar
        self.config(menu=menubar)
        
        # create main frame
        self.main_frame = MainFrame(self)
        
        
    def cmd_barMenu_new(self):
        print('cmd_barMenu_new')

    def cmd_barMenu_open(self):
        print('cmd_barMenu_open')

             
        
# SECTION: main frame
class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                        highlightbackground='#ff0000', highlightthickness=config.SHOW_FRAME_STROKE)

        # frame config
        self.pack(fill=tk.BOTH, expand=True)
        self.pack_propagate(False)

        # create list frame
        self.list_frame = ListFrame(self)
        self.list_frame.pack(padx=(10,0),pady=10,fill=tk.Y, side=tk.LEFT)
        
        # create element frame
        self.element_frame = ElementFrame(self)
        self.element_frame.pack(padx=10,pady=10,fill=tk.BOTH, side=tk.RIGHT, expand=True)       

        

# SECTION: list frame
class ListFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=config.ELEMENT_LIST_WIDTH, bg=config.COLOR_1,
                            highlightbackground='#3cc900', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        # add headline
        self.label = tk.Label(self, text="Element list",
                              bg=config.COLOR_1, fg=config.TEXT_COLOR_1,
                              font=("Arial", 14), anchor="w")
        self.label.pack(fill=tk.BOTH, padx=10, pady=(10,5))
    
        # add explain text after headline
        self.label = tk.Label(self, text="Create and modify your element list.",
                              bg=config.COLOR_1, fg=config.TEXT_COLOR_2,
                              font=("Arial", 10), anchor="w")
        self.label.pack(fill=tk.BOTH, padx=10, pady=(0,10))
        

        # add element tree
        tree = ttk.Treeview(self, style="Custom.Treeview", columns=("Index", "Type", "Text"), show="headings")
        tree.pack(fill=tk.BOTH, padx=10,pady=(0,10),expand=True)

        # Define column properties
        tree.column("Index", width=50, anchor="center")
        tree.column("Type", width=70, anchor="center")
        tree.column("Text", anchor="w")

        # Create headings
        tree.heading("Index", text="Index")
        tree.heading("Type", text="Type")
        tree.heading("Text", text="Text")
  

        # Add sample elements
        for i in range(5):
            tree.insert("", "end", text=f"Item {i}", values=(i, "Type", f"Content {i}"))

        
        




# SECTION: element frame
class ElementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        self.label = tk.Label(self, text="Right Frame")
        self.button = tk.Button(self, text="Right Button", command=self.on_button_click)
        
        self.label.pack(pady=10)
        self.button.pack(pady=10)
        
    def on_button_click(self):
        # Handle button click in right frame
        pass




# SECTION: run app
app = MainApp()
app.mainloop()
