import widgets as w
import var_util as vu

element_list = [['headline1','intro'],
                ['test','welcome to my app'],
                ['headline2','installing'],
                ['text','pip install my app'],]


# init tkinter
root = w.tk.Tk()

# set window size and label
root.geometry(f"{vu.WINDOW_WIDTH}x{vu.WINDOW_HEIGHT}")
root.title(vu.WINDOW_TITLE)
root.configure(bg=vu.COLOR_BACKGOUND)

# create menu bar
w.MenuBar(root)


# Create a frame
frame_list = w.tk.Frame(root, width=250, height=700, bg=vu.COLOR_LIST)
frame_list.place(x=850, y=0)
frame_list.pack_propagate(False)

for i in element_list:
    w.SingleElement(frame_list)


# start loop
root.mainloop()