import tkinter as tk
import config 


element_list = [['headline1','intro'],
                ['test','welcome to my app'],
                ['headline2','installing'],
                ['text','pip install my app'],]


# SECTION: functions
def cmd_barMenu_new():
    print("cmd_BarMenu_new")

def cmd_barMenu_open():
    print("cmd_BarMenu_open")

def on_list_canvas_configure(event):
        list_canvas.configure(scrollregion = list_canvas.bbox("all"))

def create_element_list(element_list):
    # clear existing widgets from the content frame
    for widget in list_cavnase_content_frame.winfo_children():
        widget.destroy()
    
    # create elements
    for i in range(len(element_list)):
        iframe = tk.Frame(list_cavnase_content_frame, width=config.ELEMENT_IN_LIST_WIDTH,
                          height=config.ELEMENT_IN_LIST_HEIGHT, bg=config.COLOR_ELEMENT_LIST)
        iframe.grid(sticky="w",padx=10, pady=5)
        iframe.pack_propagate(False)

        # Create labels within the frame
        label1 = tk.Label(iframe, text=element_list[i][0], height=0,
                            bg=config.COLOR_BACKGOUND, fg=config.TEXT_COLOR_2,
                            font=(config.MAIN_FONT, 12))
        label1.place(x=10, y=4)

        label2 = tk.Label(iframe, text=element_list[i][1], height=0,
                            bg=config.COLOR_BACKGOUND, fg=config.TEXT_COLOR_1,
                            font=(config.MAIN_FONT, 20))
        label2.place(x=10, y=30)
        
    on_list_canvas_configure(None)  

def list_del_button(element_list):
    if element_list:
        element_list.pop(-1)
    print("del")
    create_element_list(element_list)
    
def list_add_button(element_list):
    element_list.append(["new","text text"])
    print("add")
    create_element_list(element_list)



# SECTION: init tkinter
root = tk.Tk()

# set window size and label
root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
root.title(config.WINDOW_TITLE)
root.configure(bg=config.COLOR_BACKGOUND)



# SECTION: create a menu bar
menubar = tk.Menu(root)

# Create a file menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=cmd_barMenu_new)
file_menu.add_command(label="Open", command=cmd_barMenu_open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the file and edit menus to the menu bar
menubar.add_cascade(label="File", menu=file_menu)

# Configure the app to use the menu bar
root.config(menu=menubar)



# SECTION: create the list area
# Create a main frame
main_frame = tk.Frame(root, bg=config.COLOR_BACKGOUND)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False)

# Create a frame to hold list area
list_frame = tk.Frame(main_frame, width=config.ELEMENT_LIST_WIDTH, bg=config.COLOR_BACKGOUND,
                      highlightbackground='#ff0000', highlightthickness=config.SHOW_FRAME_STROKE)
list_frame.pack(fill=tk.Y, side=tk.RIGHT)
list_frame.pack_propagate(False)

list_top_frame = tk.Frame(list_frame, bg=config.COLOR_LIST,
                          highlightbackground='#ffc800', highlightthickness=config.SHOW_FRAME_STROKE)
list_top_frame.pack(fill=tk.BOTH, pady=5, side=tk.TOP, expand=True)
list_top_frame.pack_propagate(False)

list_down_frame = tk.Frame(list_frame, bg=config.COLOR_LIST, height=40,
                           highlightbackground='#3cc900', highlightthickness=config.SHOW_FRAME_STROKE)
list_down_frame.pack(fill=tk.X, side=tk.TOP)
list_down_frame.pack_propagate(False)



# Add a vertical scrollbar to the frame
scrollbar = tk.Scrollbar(list_top_frame, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a canvas widget inside the frame
list_canvas = tk.Canvas(list_top_frame, bg = config.COLOR_LIST, yscrollcommand=scrollbar.set,
                        highlightthickness=0)
list_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Configure the scrollbar to control the canvas
scrollbar.config(command=list_canvas.yview)
list_canvas.bind("<Configure>", on_list_canvas_configure)
# Create a frame inside the canvas to hold the content
list_cavnase_content_frame = tk.Frame(list_canvas, bg = config.COLOR_LIST)
list_canvas.create_window((0, 0), window=list_cavnase_content_frame, anchor="nw")

# Add widgets to the content frame (for demonstration purposes)
create_element_list(element_list)
    
    
    
# add buttons in the down area
buttonDone = tk.Button(list_down_frame, text="Done", width=17)
buttonDone.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=5)
buttonAdd = tk.Button(list_down_frame, text="Add", width=7,
                      command=lambda:  list_add_button(element_list))
buttonAdd.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=5)
buttonDel = tk.Button(list_down_frame, text="Del", width=7,
                      command=lambda:  list_del_button(element_list))
buttonDel.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=5)









# start loop
root.mainloop()


        