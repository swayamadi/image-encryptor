'''
IMAGE ENCRYPTION
AV 
'''
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import *
import tkinter.messagebox
from PIL import Image,ImageTk
import hashlib
import enc_script

def pass_alert():
   tkinter.messagebox.showinfo("Password Alert","Please enter a password.")

def encrypt():

    global file_path_e
    enc_pass = passg.get()
    if enc_pass == "":
        pass_alert()
    else:
        #LOAD THE IMAGE
        filename = tkinter.filedialog.askopenfilename()
        file_path_e = os.path.dirname(filename)

        #GENERATE KEY & INITIALIZATION VECTOR
        hash=hashlib.sha256(enc_pass.encode()) 
        p = hash.digest()
        key = p
        iv = p.ljust(16)[:16]
        print("Encoding key is: ",key)

        input_file = open(filename,'rb')
        input_data = input_file.read()
        input_file.close()
        enc_script.enc_image(input_data,key,iv,file_path_e)
        tkinter.messagebox.showinfo("Encryption Alert","Encryption ended successfully. File stored as: encrypted.enc")

def decrypt():

    global file_path_e
    enc_pass = passg.get()
    if enc_pass == "":
        pass_alert()
    else:
        filename = tkinter.filedialog.askopenfilename()
        file_path_e = os.path.dirname(filename)

        hash=hashlib.sha256(enc_pass.encode()) 
        p = hash.digest()
        key = p
        iv = p.ljust(16)[:16]
        input_file = open(filename,'rb')
        input_data = input_file.read()
        input_file.close()
        enc_script.dec_image(input_data,key,iv,file_path_e)
        tkinter.messagebox.showinfo("Decryption Alert","Decryption ended successfully File Stored as: output.png")


# GUI STUFF
top=tk.Tk()
top.geometry("500x150")
top.resizable(0,0)
top.title("ImageEncryption")

title="Image Encryption Using AES"
msgtitle=Message(top,text=title)
msgtitle.config(font=('helvetica',17,'bold'),width=300)
msgtitle.pack()

sp="---------------------------------------------------------------------"
sp_title=Message(top,text=sp)
sp_title.config(font=('arial',12),width=650)
sp_title.pack()


passlabel = Label(top, text="Enter Encryption/Decryption Key:")
passlabel.pack()
passg = Entry(top, show="*", width=20)
passg.config(highlightthickness=1,highlightbackground="blue")
passg.pack()

encrypt=Button(top,text="Encrypt",width=28,height=3,command=encrypt)
encrypt.pack(side=LEFT)
decrypt=Button(top,text="Decrypt",width=28,height=3,command=decrypt)
decrypt.pack(side=RIGHT)

top.mainloop()
