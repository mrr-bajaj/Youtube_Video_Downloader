from pytube import  *
from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from tkinter.messagebox import *
from threading import *
file_size = 0

#def progress(stream=None, chunk=None, file_handle=None, remaining=0):
 #   file_downloaded = (file_size - remaining)
  #  per = (file_downloaded / file_size)*100
  #  dbtn.config(text="{ } % downloaded".format(per))

def startdownload():
    global file_size
    try:
        url = urlfield.get()
        print(url)
        dbtn.config(text='Please Wait...')
        dbtn.config(state=DISABLED)
        path_to_save_video =  askdirectory() # it will ask directory to store video
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        obj = YouTube(url)  #, on_progress_callback = progress
        strm = obj.streams.first()  # download highest quality video
        file_size=strm.filesize
        vtitle.config(text=strm.title)
        vtitle.pack(side=TOP)
        print(file_size)
        strm.download(path_to_save_video)
        print("done..")
        dbtn.config(text='Start Download')
        dbtn.config(state=NORMAL)
        showinfo("Download Finished","Download Successfully")
        urlfield.delete(0,END)
        vtitle.pack_forget()
    except Exception as e:
        print(e)
        print("error")


def startdownloadthread():
    thread=Thread(target=startdownload())
    thread.start()



#started GUi building

main = Tk()

main.title("My Youtube Downloader")     #setting the title
main.iconbitmap('youtube.ico')          #setting icon
main.geometry("500x600")                  #setting height and width

#add image
file = ImageTk.PhotoImage(Image.open("youtube.jpg"))    #if image is in jpg
#file = PhotoImage(file='youtube.png')           #if image is in png
headingicon= Label(main,image=file)
headingicon.pack(side=TOP)

urlfield = Entry(main,font=("verdana",18),justify=CENTER)
urlfield.pack(side=TOP,fill=X,padx=10)

dbtn = Button(main,text="Start Download",font=("verdana",18),relief='ridge',command=startdownloadthread)
dbtn.pack(side=TOP,pady=10)

vtitle = Label(main,text="Video title")

main.mainloop()                         #it will run as long as window is not closed
