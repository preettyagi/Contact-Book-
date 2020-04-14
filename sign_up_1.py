from tkinter import*
from tkinter.ttk import*
from sqlite3 import*
from tkinter import messagebox
import sign_up_2


class SignUp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title('Contact Book')
        self.geometry('500x400')

        self.style = Style()
        self.style.configure('Header.TFrame', background='Blue')

        self.header_frame = Frame(self, style='Header.TFrame')
        self.header_frame.pack(side=TOP, fill=X)

        self.style.configure('Header.TLabel', background='Blue', foreground='White', font=(NONE, 20))

        self.header_label = Label(self.header_frame, style='Header.TLabel', text='Sign Up')
        self.header_label.pack(pady=10)

        self.content_frame = Frame(self)
        self.content_frame.pack(side=TOP, fill=Y, pady=15)

        self.style.configure('Content.TLabel', foreground='Black', font=(NONE, 15))
        self.style.configure('Content.TEntry', foreground='Black', font=(NONE, 15))

        self.email_address_label = Label(self.content_frame, style='Content.TLabel', text='Email address:')
        self.email_address_label.grid(row=0, column=0, pady=8)

        self.email_address_entry = Entry(self.content_frame, style='Content.TEntry', width=30)
        self.email_address_entry.grid(row=0, column=1, padx=5, pady=8)

        self.username_label = Label(self.content_frame, style='Content.TLabel', text='Username:')
        self.username_label.grid(row=1, column=0, pady=8)

        self.username_entry = Entry(self.content_frame, style='Content.TEntry', width=30)
        self.username_entry.grid(row=1, column=1, padx=5, pady=8)

        self.password_label = Label(self.content_frame, style='Content.TLabel', text='Enter Password:')
        self.password_label.grid(row=2, column=0, pady=8)

        self.password_entry = Entry(self.content_frame, style='Content.TEntry', show='*', width=30)
        self.password_entry.grid(row=2, column=1, pady=8, padx=5)

        self.val = IntVar()

        self.show_password = Checkbutton(self.content_frame, text='Show Password', variable=self.val, onvalue=1,
                                         offvalue=0, command=self.show)

        self.show_password.grid(row=2, column=2, pady=8, padx=5)

        self.renter_password_label = Label(self.content_frame, style='Content.TLabel', text='Re-Enter Password:')
        self.renter_password_label.grid(row=3, column=0, pady=8)

        self.renter_password_entry = Entry(self.content_frame, style='Content.TEntry', show='*', width=30)
        self.renter_password_entry.grid(row=3, column=1, pady=8, padx=5)

        self.style.configure('SUW.TButton', foreground='Blue')

        self.submit_button = Button(self.content_frame, style='SUW.TButton', text='Submit', width=15,
                                    command=self.submit_click)
        self.submit_button.grid(row=4, column=1, pady=20)

    def submit_click(self):
        email_send = self.email_address_entry.get()
        if self.password_entry.get() == self.renter_password_entry.get():
            con = connect('AppDatabase.db')
            cur = con.cursor()
            cur.execute("""insert into LoginData (Username, Password, Email) values('{0}', '{1}', 
                           '{2}')""".format(self.username_entry.get(), self.password_entry.get(),
                                            self.email_address_entry.get()))
            messagebox.showinfo('Status', 'The Information has been inserted')
            con.commit()
            con.close()
            self.destroy()
            sign_up_2.SafetyQuestion(email_send)
        else:
            messagebox.showerror('Invalid', 'Password does not match')  # add some kind of exception for error

    def show(self):
        if self.val.get() == 1:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')


if __name__ == "__main__":

    sign_up_frame = SignUp()
    sign_up_frame.mainloop()
