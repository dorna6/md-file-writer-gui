import tkinter as tk
import var_util as vu

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def update_gui():
    # Clear existing widgets from the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    for i in range(len(ele_list)):
        iframe = tk.Frame(content_frame, width=vu.ELEMENT_IN_LIST_WIDTH, height=vu.ELEMENT_IN_LIST_HEIGHT, bg=vu.COLOR_ELEMENT_LIST)
        iframe.pack(padx=10, pady=5)
        iframe.pack_propagate(False)

        # Create labels within the frame
        label1 = tk.Label(iframe, text="Headline 1", height=0,
                            bg=vu.COLOR_BACKGOUND, fg=vu.TEXT_COLOR_2,
                            font=(vu.MAIN_FONT, 12))
        label1.place(x=10, y=4)

        label2 = tk.Label(iframe, text="Intro", height=0,
                            bg=vu.COLOR_BACKGOUND, fg=vu.TEXT_COLOR_1,
                            font=(vu.MAIN_FONT, 20))
        label2.place(x=10, y=30)

def del_button():
    global ele_list 
    if ele_list:
        ele_list.pop(-1)
    print("del")
    update_gui()
    
def add_button():
    global ele_list
    ele_list.append(10)
    print("add")
    update_gui()

ele_list = [1,2,3,4,5,6,7,8,9,0]


root = tk.Tk()
root.geometry("1100x700")

# Create a main frame
main_frame = tk.Frame(root, bg=vu.COLOR_BACKGOUND)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False)

# Create a frame to hold list area
list_frame = tk.Frame(main_frame, width=280, bg=vu.COLOR_LIST)
list_frame.pack(fill=tk.Y, side=tk.RIGHT)  # Fill the height, placed on the left
list_frame.pack_propagate(False)

# Add a vertical scrollbar to the frame
scrollbar = tk.Scrollbar(list_frame, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a frame to hold list area
list_element_frame = tk.Frame(list_frame, bg=vu.COLOR_LIST)
list_element_frame.pack(fill=tk.BOTH, expand=True)
list_element_frame.pack_propagate(False)

# Create a canvas widget inside the frame
canvas = tk.Canvas(list_element_frame, bg = vu.COLOR_LIST, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Configure the scrollbar to control the canvas
scrollbar.config(command=canvas.yview)
canvas.bind("<Configure>", on_canvas_configure)

# Create a frame inside the canvas to hold the content
content_frame = tk.Frame(canvas, bg = vu.COLOR_LIST)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Add widgets to the content frame (for demonstration purposes)
update_gui()
    

list_buttons_frame = tk.Frame(list_frame, height=40, bg=vu.COLOR_LIST)
list_buttons_frame.pack(fill=tk.X, padx=10, pady=10)
list_buttons_frame.pack_propagate(False)
    
buttonDone = tk.Button(list_buttons_frame, text="Done", width=15)
buttonDone.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=0)
buttonAdd = tk.Button(list_buttons_frame, text="Add", width=7, command=add_button)
buttonAdd.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=0)
buttonDel = tk.Button(list_buttons_frame, text="Del", width=7, command=del_button)
buttonDel.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=0)


root.mainloop()
