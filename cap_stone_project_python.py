import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random 
import smtplib

root =tk.Tk()
root.title("Otp verification System")
root.geometry('500x250')

# Generating OTP

def otp_gen():
    otp = ''
    for i in range(1,7):
          num = random.randint(1,9)
          otp += str(num)
    return int(otp)

# Entering user Email_ID

def mail_id():
    lbl = Label(root,text='Enter your E-mail')
    lbl.grid(row=0,column=1,padx=20,pady=30)
    user = Entry(root,width=30)
    user.grid(column=2,row=0,padx=10,pady=30)
    user_btn = Button(root,text='click to get OTP',command=lambda:pro(user.get()))
    user_btn.grid(column=3,row=0,padx=50,pady=30)


# Testing Email by passing user's mail through user_mail function

def pro(mail):
        valid_email_address = user_email(mail)
        if valid_email_address:
           send_otp(valid_email_address)


# Validating Email

def user_email(email_add):
        dom = ["gmail","hotmail","yahoo","outlook"]
        ext = ["com","in","org","edu","co.in"]
        s = email_add.split("@")
        if len(s) != 2:
                messagebox.showerror("Error", "Invalid Email. Please enter again.")
                return None
        else:
            test = s[1].split(".",1)
            if (' ' not in email_add) and ("@" in email_add) and (test[0] in dom) and (test[1] in ext):
                    return email_add
            else:
                    messagebox.showerror("Error", "Invalid Email. Make sure you don't have spaces while entering.")
                    return None


#  sending OTP to the users mail.

try:
    def send_otp(valid_email_address):
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login("vits20731A3152@gmail.com",'rfab irjo uise kcbr')
        subject = "OTP verification"
        send = otpnum
        body = "your otp is :" + str(send)
        message = f'subject:{subject}\n\n{body}'
        user_input = valid_email_address
        s.sendmail('vits20731A3152@gmail.com',user_input,message)
        messagebox.showinfo(title='success',message='OTP sent Successfully')
        s.quit()
except Exception as e:
        messagebox.showerror('Error Occured','Unable to send OTP. Please check you Mail Address.')
        mail_id()


# OTP Verification.

count = 4
def otp_val(user):
    global count
    try:
        user_otp = int(user)
    except Exception as e:
        messagebox.showerror('Value Error','number must be integer')
        otp_entry.delete(0,tk.END)
        return
    if user_otp == otpnum:
        messagebox.showinfo('Success','Access Granted')
        root.quit()
    else:
                count -= 1
                if count>0:
                    messagebox.showwarning("warning",f'Invalid number.enter number Again.Last {count} chances')
                    otp_entry.delete(0,tk.END)
                else:
                        messagebox.showerror("Error","Invalid number,your chances are over.")
                        user1=messagebox.askquestion('question','do you want to enter again.')
                        if user1 == 'yes':
                            count=4
                            mail_id()
                            otp_entry.delete(0,tk.END)
                        else :
                             root.quit()

# User Enter OTP

lbl = Label(root,text='Enter OTP')
lbl.grid(row=1, column=1, padx=20, pady=30)
otp_entry = Entry(root,width=10)
otp_entry.grid(row=1, column=2, padx=10, pady=30)
otp_btn = Button(root,text='Verify OTP',command=lambda:otp_val(otp_entry.get()))
otp_btn.grid(row=1, column=3, padx=50, pady=30)


otpnum = otp_gen()

mail_id()

root.mainloop()