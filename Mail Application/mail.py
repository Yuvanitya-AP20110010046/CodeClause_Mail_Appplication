from tkinter import * 
import smtplib
from email.message import EmailMessage
import ssl 

#Main Screen
root = Tk()
root.title("Mail Application")
root.geometry("300x350")
 
#Functions
def send():
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username==" " or password=="" or to=="" or subject=="" or body=="":
            return
        else:
            em = EmailMessage()  #object used to write email
            em['From'] = username
            em['To'] = to
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            #sending email
            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                smtp.login(username, password)
                smtp.sendmail(username, to, em.as_string())
        

def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')

#GUI 
titleLabel = Label(root,text="Mail App",font=('Helvetica',15))
titleLabel.grid(row=0,sticky=N)
Label(root,text="Use the form below to send an email",font=('Helvetica',11)).place(x=40,y=60)
Label(root,text="Email",font=('Helvetica',11)).place(x=40,y=100)
Label(root, text="Password",font=('Helvetica',11)).place(x=40,y=140)
Label(root,text="To",font=('Helvetica',11)).place(x=40,y=180)
Label(root,text="Subject",font=('Helvetica',11)).place(x=40,y=220)
Label(root,text="Body",font=('Helvetica',11)).place(x=40,y=260)


#Collecting information from the user
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#entries
usernameEntry = Entry(root,textvariable=temp_username )
usernameEntry.place(x=120,y=100)

passwordEntry = Entry(root,textvariable=temp_password )
passwordEntry.place(x=120,y=140)

receiverEntry = Entry(root,textvariable=temp_receiver )
receiverEntry.place(x=120,y=180)

subjectEntry = Entry(root,textvariable=temp_subject )
subjectEntry.place(x=120,y=220)

bodyEntry = Entry(root,textvariable=temp_body )
bodyEntry.place(x=120,y=260)

#Buttons
Button(root,text="Send",command=send).place(x=40,y=300)
Button(root,text="Reset",command=reset).place(x=80,y=300)

root.mainloop()