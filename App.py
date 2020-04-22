import tkinter as tk
from tkinter import messagebox
import OTP
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename

Encrypt = True
File = ''


def changeMode(Mode):
    global Encrypt
    if Mode is "Encryption":
        ptxtlb.configure(text='Plaintext')
        fnbtn.configure(text='Encrypt')
        atbtn.place(relx=0.72, rely=0.55, relwidth=0.15, relheight=0.05)
        ptxtEntry.configure(state='normal', bg='#eeeeee', fg='#222831')
        ptxtEntry.delete(0, "end")

        Encrypt = True
    else:
        ptxtlb.configure(text='Ciphertext')
        fnbtn.configure(text='Decrypt')
        atbtn.place_forget()
        ptxtEntry.configure(state='normal', bg='#eeeeee', fg='#222831')
        ptxtEntry.delete(0, "end")
        Encrypt = False


def ChooseFile():
    global File
    file = tk.filedialog.askopenfilename()
    if "txt" not in file:
        messagebox.showerror("Error", "The file selected must be text.")
        # Result.delete("1.0","end")
        # Result.insert(tk.END, "The file selected must be text. Please select a text file!!")
    else:
        print("Im in else")
        # f = str(file).split('/')[len(str(file).split('/'))-1]
        File = file
        if ReadFile() is '':
            messagebox.showerror("Error", "The file empty")
        else:
            ptxtEntry.delete(0, "end")
            ptxtEntry.insert('end', "Text uploaded")
            ptxtEntry.configure(bg='#222831')  # state='normal' to make it editable ,
            ptxtEntry.configure(state='disabled')

H = 420
W = 650
root = tk.Tk()
root.title("OTP")
canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()
v = tk.IntVar()
v.set(1)

InBackground = tk.Label(root, bg='#222831')
InBackground.place(relheight=1, relwidth=1)

Frame = tk.Frame(root, bg='#393e46')
Frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

Image = tk.PhotoImage(file='OTPSmall2.png')
Logo = tk.Label(Frame, image=Image, bg="#393e46")
Logo.place(relx=0.5, rely=0, relheight=0.34, relwidth=0.75, anchor='n')

RbtnEnc = tk.Radiobutton(Frame, text="Encryption", padx=20, variable=v, value=1, activebackground='#393e46',
                         bg='#393e46', fg="#00adb5", activeforeground="#00adb5", font="calibri 13 bold",
                         command=lambda: changeMode("Encryption"))
RbtnEnc.place(relx=0.3, rely=0.38, relwidth=0.2, relheight=0.05)
RbtnDec = tk.Radiobutton(Frame, text="Decryption", padx=20, variable=v, value=2, activebackground='#393e46',
                         bg='#393e46', fg="#00adb5", activeforeground="#00adb5", font="calibri 13 bold",
                         command=lambda: changeMode("Decryption"))
RbtnDec.place(relx=0.5, rely=0.38, relwidth=0.2, relheight=0.05)

ptxtlb = tk.Label(Frame, bg='#393e46', fg='#00adb5', text='Plaintext', font="ArialRoundedMT 15 bold")
ptxtlb.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.05)

ptxtEntry = tk.Entry(Frame, bg='#eeeeee', fg='#222831', font='7')
ptxtEntry.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.05)

# file = tk.filedialog.askopenfilename();
# print(file)


Chbtn = tk.Button(Frame, text="Choose", bg='#eeeeee', fg='#00adb5', font="calibri 12 bold",
                  command=lambda: ChooseFile())
Chbtn.place(relx=0.72, rely=0.45, relwidth=0.15, relheight=0.05)

ctxtlb = tk.Label(Frame, bg='#393e46', fg='#00adb5', text='KEY', font="ArialRoundedMT 15 bold")
ctxtlb.place(relx=0.1, rely=0.55, relwidth=0.2, relheight=0.05)

ktxtEntry = tk.Entry(Frame, bg='#eeeeee', fg='#222831', font='7')
ktxtEntry.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.05)

atbtn = tk.Button(Frame, text="Auto", bg='#eeeeee', fg='#00adb5', font="calibri 12 bold", command=lambda: Auto())
atbtn.place(relx=0.72, rely=0.55, relwidth=0.15, relheight=0.05)


def Auto():
    if str(ptxtEntry.get()) is not '':
        if str(ptxtEntry.get()) == "Text uploaded":
            ktxtEntry.delete(0, "end")
            ktxtEntry.insert('end', OTP.RandomKey(ReadFile()))
            print(ReadFile())
        else:
            ktxtEntry.delete(0, "end")
            ktxtEntry.insert('end', OTP.RandomKey(ptxtEntry.get()))
    else:
        messagebox.showerror("Error", "No plaintext entered.")


def ReadFile():
    global File
    f = open(File)
    str = ''
    Lines = f.readlines()
    i = len(Lines)
    for l in Lines:
        # str=str+repr(l.strip())[1:len(l.strip())+1]
        str = str + l.strip();
        i = i - 1
        if i is not 0:
            str = str + "\n"
    return str


fnbtn = tk.Button(Frame, text='Encrypt', bg='#eeeeee', fg='#00adb5', font="calibri 12 bold",
                  command=lambda: Translate())
fnbtn.place(relx=0.5, rely=0.63, relwidth=0.15, relheight=0.07, anchor='n')


def Translate():
    if ptxtEntry.get() is not '' and ktxtEntry.get() is not '':
        if str(ptxtEntry.get()) == "Text uploaded":
            if len(ReadFile()) == len(ktxtEntry.get()):
                Str = OTP.Translate(ReadFile(), ktxtEntry.get(), Encrypt)
                if Str is -1:
                    messagebox.showerror("Error", "This key already has been used")
                else:
                    Result.delete("1.0", "end")
                    Result.insert('end', Str)
            else:
                messagebox.showerror("Error", "The plaintext/ciphertext and the key must have the same length")
        else:
            if len(ptxtEntry.get()) == len(ktxtEntry.get()):
                Str = OTP.Translate(ptxtEntry.get(), ktxtEntry.get(), Encrypt)
                if Str is -1:
                    messagebox.showerror("Error", "This key already has been used")
                else:
                    Result.delete("1.0","end")
                    Result.insert('end',Str )
            else:
                ptext=ptxtEntry.get()
                ktext=ktxtEntry.get()
                while len(ptext) > len(ktext):
                    ktext=ktext+"z"
                while len(ptext) < len(ktext):
                    ptext=ptext+"z"
                Str = OTP.Translate(ptext, ktext, Encrypt)
                if Str is -1:
                    messagebox.showerror("Error", "This key already has been used")
                else:
                    Result.delete("1.0", "end")
                    Result.insert('end', Str)


    else:
        messagebox.showerror("Error", "The plaintext/ciphertext or the key is not entered.")


Border = tk.Frame(Frame, bg='#222831')
Border.place(relx=0.5, rely=0.72, relwidth=0.8, relheight=0.25, anchor='n')
Result = tk.Text(Border, bg='#eeeeee', fg='#222831', font='7', height=5)
Result.pack(fill="both", expand=True, padx=5, pady=5)


root.mainloop()
