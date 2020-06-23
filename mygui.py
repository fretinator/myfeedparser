from tkinter import *
from unidecode import unidecode
from tkinterhtml import HtmlFrame

from myfeedparser import MyFeedParser

window = Tk()
window.geometry("800x600")
window.title("Welcome to My Feed Parser")

frame = HtmlFrame(window,horizontal_scrollbar="auto", vertical_scrollbar="auto")
f = MyFeedParser()
s = f.getLatestFeedsAsHtml(True)

# Convert non-ascii characters to their best ascii representation
#print(s)
ascii = unidecode(s)

frame.set_content(ascii)

frame.pack(expand=True, fill="both")
#window.pack_propagate()

window.mainloop()
