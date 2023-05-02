from tkinter import * 
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('Text Editor')
root.geometry("1200x680")

global opened_file_name
opened_file_name = False

global selected_text
selected_text = False

def new_file():
    text.delete("1.0",END)
    root.title('New File - Text Editor')
    status_bar.config(text="New File        ")
    
    global opened_file_name
    opened_file_name = False

def open_file():
    #Delete previous text
    text.delete("1.0",END)
    #grab filename
    text_file = filedialog.askopenfilename(initialdir="C:/downloads/", title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    #to check if there is a file name
    if text_file:
        global opened_file_name
        opened_file_name = text_file
    
    #update status bars
    name = text_file
    
    status_bar.config(text=f'{name}        ')
    name = name.replace("C:/Users/DELL/Downloads/","")
    root.title(f'{name} - Text Editor')
    #open files
    text_file=open(text_file,'r')
    stuff= text_file.read()
    text.insert(END,stuff)
    #close the opened file
    text_file.close() 

def saveas_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/downloads/", title="Save File", filetypes=(("Text File","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    if text_file:
        name = text_file
        #Update status bar
        status_bar.config(text=f'Saved : {name}        ')
        name = name.replace("C:/Users/DELL/Downloads/","")
        root.title(f'{name} - Text Editor')

        #saving the file
        text_file = open(text_file,'w')
        text_file.write(text.get(1.0,END))  
        text_file.close()

def save_file():
    global opened_file_name
    if opened_file_name:
        #saving the file
        text_file = open(opened_file_name,'w')
        text_file.write(text.get(1.0,END))
        text_file.close()
        status_bar.config(text=f'Saved : {opened_file_name}        ')
    else:
        saveas_file()
    
def cut_text(e):
    global selected_text
    #check to see if we used the keyboard shortcut
    if e:
        selected_text = root.clipboard_get() 
    else:
        if text.selection_get():
        #grabbing selected text from text box
            selected_text = text.selection_get()
        #delete selected text from text box
            text.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected_text)



def copy_text(e):
    global selected_text
    #check to see if we used the keyboard shortcut
    if e:
        selected_text = root.clipboard_get()
    if text.selection_get():
        #grabbing selected text from text box
        selected_text = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected_text)
         
        



def paste_text(e):
    global selected_text
    #check to see if we used the keyboard shortcut
    if e:
        selected_text = root.clipboard_get()
    else:
        if selected_text:
            position = text.index(INSERT)
            text.insert(position, selected_text)

def bold_it():
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")
    #configure a tag
    text.tag_configure("bold",font=bold_font)

    current_tags = text.tag_names("sel.first")
    #if statement to see if tag has been set
    if "bold" in current_tags:
        text.tag_remove("bold","sel.first","sel.last")
    else:
        text.tag_add("bold","sel.first","sel.last")




def italic_it():
    italic_font = font.Font(text, text.cget("font"))
    italic_font.configure(slant="italic")
    #configure a tag
    text.tag_configure("italic",font=italic_font)

    current_tags = text.tag_names("sel.first")
    #if statement to see if tag has been set
    if "italic" in current_tags:
        text.tag_remove("italic","sel.first","sel.last")
    else:
        text.tag_add("italic","sel.first","sel.last")

def text_color():
    #picking color
    my_color =colorchooser.askcolor()[1]
    # status_bar.config(text=my_color)
    if my_color:
        color_font = font.Font(text, text.cget("font"))
    #configure a tag
        text.tag_configure("colored",font=color_font,foreground=my_color)

        current_tags = text.tag_names("sel.first")
    #if statement to see if tag has been set
        if "colored" in current_tags:
            text.tag_remove("colored","sel.first","sel.last")
        else:
            text.tag_add("colored","sel.first","sel.last")

def bg_color():
    my_color =colorchooser.askcolor()[1]
    if my_color:
        text.config(bg=my_color)

    
def all_text_color():
    my_color =colorchooser.askcolor()[1]
    if my_color:
        text.config(fg=my_color)

def select_all():
    #adding tag
    text.tag_add("sel",'1.0','end')

def clear_all():
    text.delete(1.0,END)

#create a toolbar frame      
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)




#create Main frame of the text editor
frame = Frame(root)
frame.pack(pady=5)

#create vertical scrollbar for text box
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)
#create horizontal scroll bar
hor_scroll = Scrollbar(frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)


#Create text box
text = Text(frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
text.pack()

#configure the scroll bar
text_scroll.config(command=text.yview)
hor_scroll.config(command=text.xview)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)


#adding file menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As",command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Adding edit menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda: cut_text(False),accelerator="Ctrl+x")
edit_menu.add_command(label="Copy",command=lambda: copy_text(False),accelerator="Ctrl+c")
edit_menu.add_command(label="Paste        ",command=lambda: paste_text(False),accelerator="Ctrl+v")
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=text.edit_undo,accelerator="Ctrl+z")
edit_menu.add_command(label="Redo",command=text.edit_redo,accelerator="Ctrl+y")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=lambda: select_all(True),accelerator="Ctrl+a")
edit_menu.add_command(label="Clear",command=clear_all)

#adding color menu
color_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label="Change selected text",command=text_color)
color_menu.add_command(label="All text",command=all_text_color)
color_menu.add_command(label="Background",command=bg_color)




#Adding status bar at bottom
status_bar = Label(root, text='Ready        ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=15)


#edit bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)
root.bind('<Control-A>',select_all)
root.bind('<Control-a>',select_all)

#create Button
bold_button = Button(toolbar_frame,text="Bold",command=bold_it)
bold_button.grid(row=0,column=0,sticky=W,padx=5)

italics_button = Button(toolbar_frame,text="Italics",command=italic_it)
italics_button.grid(row=0,column=1,padx=5)

undo_button = Button(toolbar_frame,text="Undo",command=text.edit_undo)
undo_button.grid(row=0,column=2,padx=5)

redo_button = Button(toolbar_frame,text="Redo",command=text.edit_redo)
redo_button.grid(row=0,column=3,padx=5)

#text color
text_color_button = Button(toolbar_frame,text="Text Color",command=text_color)
text_color_button.grid(row=0,column=4,padx=5)

root.mainloop()