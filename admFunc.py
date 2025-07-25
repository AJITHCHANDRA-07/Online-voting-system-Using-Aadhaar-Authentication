import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)



def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    # Keep references to images to prevent garbage collection
    frame1.bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.BILINEAR))
    frame1.congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25,38),Image.BILINEAR))
    frame1.jspLogo = ImageTk.PhotoImage((Image.open("img/jsp.png")).resize((45,30),Image.BILINEAR))
    frame1.ycpLogo = ImageTk.PhotoImage((Image.open("img/ycp.png")).resize((40,35),Image.BILINEAR))
    frame1.notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.BILINEAR))

    Label(frame1, image=frame1.bjpLogo).grid(row = 2,column = 0)
    Label(frame1, image=frame1.congLogo).grid(row = 3,column = 0)
    Label(frame1, image=frame1.jspLogo).grid(row = 4,column = 0)
    Label(frame1, image=frame1.ycpLogo).grid(row = 5,column = 0)
    Label(frame1, image=frame1.notaLogo).grid(row = 6,column = 0)

    Label(frame1, text="BJP               :          ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" JSP              :           ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['jsp'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" YCP             :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ycp'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTA             :           ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()

# ...existing code...


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
