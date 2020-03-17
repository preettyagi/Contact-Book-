from tkinter import*
from tkinter.ttk import*
import Home_page
import sign_up_1
import Change_Password


class Login(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Contact Book")
        self.geometry("500x400")

        self.style = Style()
        self.style.configure("Header.TFrame", background="Blue")

        self.header_frame = Frame(self, style="Header.TFrame")
        self.header_frame.pack(side=TOP, fill=X)

        self.style.configure('Header.TLabel', background='Blue', foreground='White', font=(NONE, 28))

        self.Header_label = Label(self.header_frame, style='Header.TLabel', text='Login')
        self.Header_label.pack(pady=10)

        self.style.configure('Content.TFrame')

        self.style.configure('Content.TLabel', foreground='Black', font=(NONE, 15))

        self.content_frame = Frame(self, style='Content.TFrame')
        self.content_frame.pack(side=TOP, pady=15)

        self.username_label = Label(self.content_frame, style='Content.TLabel', text='Username:')
        self.username_label.grid(row=0, column=0)

        self.username_entry = Entry(self.content_frame, font=(NONE, 15), width=15)
        self.username_entry.grid(row=0, column=1)
        self.username_entry.focus()

        self.password_label = Label(self.content_frame, style='Content.TLabel', text='Password:')
        self.password_label.grid(row=1, column=0,  padx=5, pady=15)

        self.password_entry = Entry(self.content_frame, font=(NONE, 15), width=15, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=15)
        self.password_entry.focus()

        self.style.configure('LW.TButton', foreground='Blue', font=(NONE, 15))

        self.submit_button = Button(self.content_frame, style='LW.TButton', text='Submit', width=15,
                                    command=self.submit_button_click)
        self.submit_button.grid(row=2, column=1, padx=10)

        self.forgot_password_button = Button(self.content_frame, style='LW.TButton', text='Forgot Password', width=15,
                                             command=self.forgot_password_button_click)
        self.forgot_password_button.grid(row=2, column=2)

        self.sign_up_frame = Frame(self, style='Header.TFrame')
        self.sign_up_frame.pack(side=BOTTOM, fill=X)

        self.style.configure('SUB.TButton', background='Blue', foregroud='White', font=(NONE, 15))

        self.sign_up_button = Button(self.sign_up_frame, style='SUB.TButton', text='Sign Up', width=15,
                                     command=self.sign_up_button_click)
        self.sign_up_button.pack(side=RIGHT, pady=10)

    def submit_button_click(self):
        self.destroy()
        Home_page.HomePage()

    def sign_up_button_click(self):
        self.destroy()
        sign_up_1.SignUp()

    def forgot_password_button_click(self):
        self.destroy()
        Change_Password.ChangePassword()


if __name__ == "__main__":
    # we run mainloop so that our program wont immediately stop after execution
    login_window = Login()
    login_window.mainloop()
