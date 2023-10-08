import tkinter as tk
from tkinter import ttk
import config 


element_list = [['headline1','intro'],
                ['text','welcome to my app'],
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
        self.list_frame.pack(padx=(0,0),pady=0,fill=tk.Y, side=tk.LEFT)
        
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
        self.tree = ttk.Treeview(self, style="Custom.Treeview", columns=("Index", "Type", "Text"), show="headings")
        self.tree.pack(fill=tk.BOTH, padx=10,pady=(0,10),expand=True)

        # Define column properties
        self.tree.column("Index", width=50, anchor="center")
        self.tree.column("Type", width=75, anchor="w")
        self.tree.column("Text", anchor="w")

        # Create headings
        self.tree.heading("Index", text="Index")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Text", text="Text")
  
        self.update_list()
            
        
        # button frame
        self.buttons_frame = tk.Frame(self, height=30, bg=config.COLOR_1,
                                highlightbackground='#3cc900', highlightthickness=config.SHOW_FRAME_STROKE)
        self.buttons_frame.pack_propagate(False)
        self.buttons_frame.pack(fill=tk.X, padx=10, pady=(0,10))
        
        self.del_button = tk.Button(self.buttons_frame, width=8, text="delete", command=lambda: self.cmd_del_button())
        self.add_button = tk.Button(self.buttons_frame, width=8, text="add", command=lambda: self.cmd_add_button())
        self.done_button = tk.Button(self.buttons_frame, text="done", command=lambda: self.cmd_done_button())
        self.del_button.pack(fill=tk.Y, side=tk.LEFT, padx=(0,5))
        self.add_button.pack(fill=tk.Y, side=tk.LEFT, padx=5)
        self.done_button.pack(fill=tk.BOTH, side=tk.LEFT, padx=(5,0), expand=True)
        
           
    def cmd_del_button(self):
        if element_list:
            element_list.pop(-1)
        self.update_list()
        print("list - del button")
            
    def cmd_add_button(self):
        element_list.append(['text','empty'])
        self.update_list()
        print("list - add button")       

    def cmd_done_button(self):
        self.update_list()
        print("list - done button")
        
    def update_list(self):
        # Clear existing items
        self.tree.delete(*self.tree.get_children())

        # Add sample elements
        for i in range(len(element_list)):
            self.tree.insert("", "end", text=f"Item {i}", values=(i, element_list[i][0], element_list[i][1]))

# SECTION: element frame
class ElementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        # add headline
        self.label = tk.Label(self, text="Element configuration",
                              bg=config.COLOR_BACKGOUND, fg=config.TEXT_COLOR_1,
                              font=("Arial", 14), anchor="w")
        self.label.pack(fill=tk.BOTH, padx=10, pady=(10,5))
    
        # add explain text after headline
        self.label = tk.Label(self, text="Select the element type and modify its parameters.",
                              bg=config.COLOR_BACKGOUND, fg=config.TEXT_COLOR_2,
                              font=("Arial", 10), anchor="w")
        self.label.pack(fill=tk.BOTH, padx=10, pady=(0,10))

        # add drop down type
        self.drop_down_frame = tk.Frame(self, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE,
                            height=30)
        self.drop_down_frame.pack_propagate(False)        
        self.drop_down_frame.pack(fill=tk.BOTH, padx=10, pady=(0,10))

        # add label near the drop down
        self.label = tk.Label(self.drop_down_frame, text="Type: ",
                              bg=config.COLOR_BACKGOUND, fg=config.TEXT_COLOR_1,
                              font=("Arial", 10), anchor="w")
        self.label.pack(side=tk.LEFT, fill=tk.Y, padx=(0,5))
        
        # Create a dropdown
        options = ["Headline", "Text"]
        self.dropdown = ttk.Combobox(self.drop_down_frame, values=options, state='readonly', width=30,
                                font=("Arial", 12))
        self.dropdown.set(options[0])
        self.dropdown.pack(side=tk.LEFT)


        # Create a container for frames
        self.frames_container = tk.Frame(self, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE)
        self.frames_container.pack(fill=tk.BOTH, padx=10, pady=(0,10), expand=True)
        self.frames_container.pack_propagate(False)
        
        # create element input frames
        self.elenet_input_text = ElementInput_Text(self.frames_container)
        self.elenet_input_headline = ElementInput_Headline(self.frames_container)
        self.show_frame(self.elenet_input_text)

        # add lower button frame
        self.lower_button_frame = tk.Frame(self, bg=config.COLOR_BACKGOUND,
                                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE,
                                            height=35)
        self.lower_button_frame.pack_propagate(False)        
        self.lower_button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(0,10))
        
        
        # Create a button to add frames
        saveElement_button = tk.Button(self.lower_button_frame, width=8,
                                       text="Save", command=lambda: self.cmd_saveElement_button())
        saveElement_button.pack(fill=tk.Y, side=tk.RIGHT, padx=(10, 0))

        clearElement_button = tk.Button(self.lower_button_frame, width=8, 
                                       text="Clear", command=lambda: self.cmd_clearElement_button())
        clearElement_button.pack(fill=tk.Y, side=tk.RIGHT, padx=(10, 0))
        
        
    def cmd_saveElement_button(self):
        self.forgot_element_input_frame()
        self.show_frame(self.elenet_input_text)
        print("cmd_saveElement_button")

    def cmd_clearElement_button(self):
        self.forgot_element_input_frame()
        self.show_frame(self.elenet_input_headline)
        print("cmd_clearElement_button")
        
    def show_frame(self,frame):
        frame.pack(fill=tk.BOTH, expand=True)
        frame.tkraise()
        
    def forgot_element_input_frame(self):
        self.elenet_input_headline.pack_forget()
        self.elenet_input_text.pack_forget()

# SECTION: element input frame
class ElementInput_Text(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        # add headline
        self.label = tk.Label(self, text="text aaaa")
        self.label.pack(fill=tk.BOTH, padx=10, pady=(10,5))

# SECTION: element input frame
class ElementInput_Headline(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=config.COLOR_BACKGOUND,
                            highlightbackground='#4600c9', highlightthickness=config.SHOW_FRAME_STROKE)
        
        # frame config
        self.pack_propagate(False)
        
        # add headline
        self.label = tk.Label(self, text="headline aaaa")
        self.label.pack(fill=tk.BOTH, padx=10, pady=(10,5))

# SECTION: run app
app = MainApp()
app.mainloop()
