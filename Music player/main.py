import tkinter as tk #for UI of the music player
import fnmatch
import os 
from PIL import Image, ImageTk 
from pygame import mixer 

# UI of app
canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("500x500") #size of the GUI application
canvas.config(bg = '#212121')

rootpath = "Songs"

#to get only mp3 files from folder create a pattern
pattern = "*.mp3"
mixer.init()


#images for the buttons

prev_img = Image.open("Images/backward.png")
prev_img = prev_img.resize((30,30))
prev_i = ImageTk.PhotoImage(prev_img)

stop_img = Image.open("Images/stop.png")
stop_img = stop_img.resize((30,30))
stop_i = ImageTk.PhotoImage(stop_img)

play_img = Image.open("Images/play.png")
play_img = play_img.resize((30,30))
play_i = ImageTk.PhotoImage(play_img)

pause_img = Image.open("Images/pause.png")
pause_img = pause_img.resize((30,30))
pause_i = ImageTk.PhotoImage(pause_img)

next_img = Image.open("Images/forward.png")
next_img = next_img.resize((30,30))
next_i = ImageTk.PhotoImage(next_img)

#function of each button
def select():
    label.config(text= listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor")) #to play the song by passing the rootpath
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    #to get index of the next song
    next_song = listBox.curselection()
    next_song = next_song[0]+1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)
    #to play next song
    mixer.music.load(rootpath + "\\" + next_song_name)  
    mixer.music.play()
    #to move the selection
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    #to get index of the previous song
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name)
    #to play previous song
    mixer.music.load(rootpath + "\\" + prev_song_name)  
    mixer.music.play()
    #to move the selection
    listBox.select_clear(0,'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)


def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else : 
        mixer.music.unpause()
        pauseButton["text"]="Pause"
    


#to show all the m3 files on ui use listbox present in tkinter
listBox = tk.Listbox(canvas, fg = "#00D7FF", bg= '#212121', width = 100,font=('poppins',14))
listBox.pack(padx=15,pady=15)

label = tk.Label(canvas, text='',bg='#212121',fg='#14FFEC',font=('poppins',18))#for selected one
label.pack(pady= 15)

#frame to hold all buttons
top = tk.Frame(canvas, bg ="#212121")
top.pack(padx=10,pady=5, anchor ='center')

#buttons
prevButton = tk.Button(canvas, text="Prev", image = prev_i, bg = '#212121', borderwidth = 0, command = play_prev, width=40,height=40,padx=10,font=("Ivy 10"))
prevButton.pack(pady=15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text="Stop", image = stop_i, bg = '#212121', borderwidth = 0, command =stop, width=40,height=40,padx=10,font=("Ivy 10"))
stopButton.pack(pady=15,in_ = top, side = 'left')

playButton = tk.Button(canvas, text="Play", image = play_i, bg = '#212121', borderwidth = 0, command = select, width=40,height=40,padx=10,font=("Ivy 10"))
playButton.pack(pady=15,in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text="Pause", image = pause_i, bg = '#212121', borderwidth = 0, command = pause_song, width=40,height=40,padx=10,font=("Ivy 10"))
pauseButton.pack(pady=15,in_ = top, side = 'left')

nextButton = tk.Button(canvas, text="Next", image = next_i, bg = '#212121', borderwidth = 0,command = play_next, width=40,height=40,padx=10,font=("Ivy 10"))
nextButton.pack(pady=15,in_ = top, side = 'left')

#adding items inside listbox
#1st parameter : index 2nd parameter : where you want to add
for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()