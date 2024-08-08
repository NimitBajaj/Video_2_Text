import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog, messagebox
import os
import assemblyai as aai
from credentials import secret_api_key


def convert_to_text():
    video_path=entry.get()
    try:
        video = mp.VideoFileClip(video_path)
        audio = video.audio

    except Exception as e:
         messagebox.showerror("Error", f"An error occurred: {e}")

    


    
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)

root = Tk()
root.title("Video to Text Converter")


frame = Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = Label(frame, text="Select video file:")
label.grid(row=0, column=0, sticky=W)

entry = Entry(frame, width=50)
entry.grid(row=0, column=1, pady=5)

browse_button = Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5)

convert_button = Button(frame, text="Convert to Text", command=convert_to_text)
convert_button.grid(row=1, columnspan=3, pady=10)


root.mainloop()


