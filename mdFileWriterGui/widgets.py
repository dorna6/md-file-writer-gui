import tkinter as tk
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

class ElementListGui():
    def __init__(self,root,element_list):
        
        # Create a main frame
        main_frame = tk.Frame(root, bg=vu.COLOR_BACKGOUND)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.pack_propagate(False)

        # Create a frame to hold list area
        list_frame = tk.Frame(main_frame, width=vu.ELEMENT_LIST_WIDTH, bg=vu.COLOR_BACKGOUND)#, highlightbackground='red', highlightthickness=1)
        list_frame.pack(fill=tk.Y, side=tk.RIGHT)
        list_frame.pack_propagate(False)

        list_top_frame = tk.Frame(list_frame, bg=vu.COLOR_LIST)#, highlightbackground='blue', highlightthickness=2)
        list_top_frame.pack(fill=tk.BOTH, pady=5, side=tk.TOP, expand=True)
        list_top_frame.pack_propagate(False)

        list_down_frame = tk.Frame(list_frame, bg=vu.COLOR_LIST, height=40)#, highlightbackground='green', highlightthickness=2)
        list_down_frame.pack(fill=tk.X, side=tk.TOP)
        list_down_frame.pack_propagate(False)



        # Add a vertical scrollbar to the frame
        scrollbar = tk.Scrollbar(list_top_frame, orient="vertical")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a canvas widget inside the frame
        self.canvas = tk.Canvas(list_top_frame, bg = vu.COLOR_LIST, yscrollcommand=scrollbar.set, highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Configure the scrollbar to control the canvas
        scrollbar.config(command=self.canvas.yview)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Create a frame inside the canvas to hold the content
        content_frame = tk.Frame(self.canvas, bg = vu.COLOR_LIST)
        self.canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Add widgets to the content frame (for demonstration purposes)
        self.create_element_list(content_frame,element_list)
            
        # add buttons in the down area
        buttonDone = tk.Button(list_down_frame, text="Done", width=17)
        buttonDone.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=5)
        buttonAdd = tk.Button(list_down_frame, text="Add", width=7, command=lambda:  self.add_button(content_frame,element_list))
        buttonAdd.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=5)
        buttonDel = tk.Button(list_down_frame, text="Del", width=7, command=lambda:  self.del_button(content_frame,element_list))
        buttonDel.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=5)



    def on_canvas_configure(self,event):
         self.canvas.configure(scrollregion= self.canvas.bbox("all"))

    def create_element_list(self,frame, element_list):
        # Clear existing widgets from the content frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        for i in range(len(element_list)):
            iframe = tk.Frame(frame, width=vu.ELEMENT_IN_LIST_WIDTH, height=vu.ELEMENT_IN_LIST_HEIGHT, bg=vu.COLOR_ELEMENT_LIST)
            iframe.grid(sticky="w",padx=10, pady=5)
            iframe.pack_propagate(False)

            # Create labels within the frame
            label1 = tk.Label(iframe, text=element_list[i][0], height=0,
                                bg=vu.COLOR_BACKGOUND, fg=vu.TEXT_COLOR_2,
                                font=(vu.MAIN_FONT, 12))
            label1.place(x=10, y=4)

            label2 = tk.Label(iframe, text=element_list[i][1], height=0,
                                bg=vu.COLOR_BACKGOUND, fg=vu.TEXT_COLOR_1,
                                font=(vu.MAIN_FONT, 20))
            label2.place(x=10, y=30)
            
        self.on_canvas_configure(None)  

    def del_button(self,content_frame,element_list):
        if element_list:
            element_list.pop(-1)
        print("del")
        self.create_element_list(content_frame,element_list)
        
    def add_button(self,content_frame,element_list):
        element_list.append(["new","text text"])
        print("add")
        self.create_element_list(content_frame,element_list)