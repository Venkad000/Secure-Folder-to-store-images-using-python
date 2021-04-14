from tkinter import *
from PIL import ImageTk,Image
import account
import authenticate

def pressBackButton():
    for widget in root.winfo_children():
            widget.destroy()

    save_image_button = Button(root,text = "Save Image",font = ("Arial",22),command = lambda: save_button())
    save_image_button.place(x = 200,y = 200)

    deleteImage_button = Button(root,text = "Delete Image",font = ("Arial",22),command = lambda: delete_button())
    deleteImage_button.place(x = 200,y = 300)

    displayImage_button = Button(root,text = "Display Image",font = ("Arial",22),command = lambda: display_button())
    displayImage_button.place(x = 200,y = 400)

    renameImage_button = Button(root,text = "Rename Image",font = ("Arial",22),command = lambda: rename_button())
    renameImage_button.place(x = 800,y = 200)

    filterImage_button = Button(root,text = "Filters",font = ("Arial",22),command = lambda: filter_button())
    filterImage_button.place(x = 800,y = 300)

    changeAccount_Button = Button(root,text = "Exit",font = ("Arial",22),command = root.quit)
    changeAccount_Button.place(x = 800,y = 400)


def save_button():
    a = account.Account(accountname)

    for widget in root.winfo_children():
        widget.destroy()

    Image_path_label = Label(root,text = "Image Path",font = ("Arial",22))
    Image_path_label.place(x = 200, y = 150)

    image_path = Entry(root,font=("Arial", 14),width = 25)
    image_path.place(x = 200,y = 200)

    Image_name_Label = Label(root,text = "Image Name",font = ("Arial",22))
    Image_name_Label.place(x = 200, y = 250)
                
    image_name = Entry(root,font = ("Arial",14),width = 25)
    image_name.place(x = 200,y = 300)

    EncryptionKey_Label = Label(root,text = "Encryption Key",font = ("Arial",22))
    EncryptionKey_Label.place(x = 200, y = 350)

    encryptionKey = Entry(root,font = ("Arial",14),width = 25)
    encryptionKey.place(x = 200,y = 400)

    SubmitButton = Button(root,text = "Submit",font = ("Arial",14),command = lambda: pressSaveImage())
    SubmitButton.place(x = 200,y = 500)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: pressBackButton())
    Back_Button.place(x = 200,y = 600)

    def pressSaveImage():
        a.saveImage(image_path.get(),image_name.get(),int(encryptionKey.get()))
        PreviewImage = ImageTk.PhotoImage(Image.open(image_path.get()))
        PreviewImage_Label = Label(image = PreviewImage)
        PreviewImage_Label.place(x = 600,y = 200)
        image_path.delete(0,END)
        image_name.delete(0,END)
        encryptionKey.delete(0,END)

def delete_button():
    a = account.Account(accountname)

    for widget in root.winfo_children():
        widget.destroy()

    Image_name_Label = Label(root,text = "Image Name",font = ("Arial",22))
    Image_name_Label.place(x = 200, y = 150)
                
    image_name = Entry(root,font = ("Arial",14),width = 25)
    image_name.place(x = 200,y = 200)

    SubmitButton = Button(root,text = "Submit",font = ("Arial",14),command = lambda: pressDeleteImage())
    SubmitButton.place(x = 200,y = 500)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: pressBackButton())
    Back_Button.place(x = 200,y = 600)

    def pressDeleteImage():
        a.deleteImage(image_name.get())
        image_name.delete(0,END)

def display_button():
    a = account.Account(accountname)

    for widget in root.winfo_children():
        widget.destroy()

    Image_name_Label = Label(root,text = "Image Name",font = ("Arial",22))
    Image_name_Label.place(x = 200, y = 150)
                
    image_name = Entry(root,font = ("Arial",14),width = 25)
    image_name.place(x = 200,y = 200)

    DEncryptionKey_Label = Label(root,text = "Encryption Key",font = ("Arial",22))
    DEncryptionKey_Label.place(x = 200, y = 250)

    DencryptionKey = Entry(root,font = ("Arial",14),width = 25)
    DencryptionKey.place(x = 200,y = 300)

    SubmitButton = Button(root,text = "Submit",font = ("Arial",14),command = lambda: pressDisplayImage())
    SubmitButton.place(x = 200,y = 500)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: pressBackButton())
    Back_Button.place(x = 200,y = 600)

    def pressDisplayImage():
        a.displayImage(image_name.get(),int(DencryptionKey.get()))
        image_name.delete(0,END)
        DencryptionKey.delete(0,END)

def rename_button():
    a = account.Account(accountname)

    for widget in root.winfo_children():
        widget.destroy()

    OldName_label = Label(root,text = "Old Image Name",font = ("Arial",22))
    OldName_label.place(x = 200, y = 150)

    OldName = Entry(root,font=("Arial", 14),width = 25)
    OldName.place(x = 200,y = 200)

    NewName_Label = Label(root,text = "Image Name",font = ("Arial",22))
    NewName_Label.place(x = 200, y = 250)
                
    NewName = Entry(root,font = ("Arial",14),width = 25)
    NewName.place(x = 200,y = 300)

    SubmitButton = Button(root,text = "Submit",font = ("Arial",14),command = lambda: pressRenameImage())
    SubmitButton.place(x = 200,y = 500)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: pressBackButton())
    Back_Button.place(x = 200,y = 600)

    def pressRenameImage():
        a.renameImage(OldName.get(),NewName.get())
        OldName.delete(0,END)
        NewName.delete(0,END)

def filter_button():
    a = account.Account(accountname)

    for widget in root.winfo_children():
        widget.destroy()

    Image_name_Label = Label(root,text = "Image Name",font = ("Arial",22))
    Image_name_Label.place(x = 200, y = 150)
                
    image_name = Entry(root,font = ("Arial",14),width = 25)
    image_name.place(x = 200,y = 200)

    DEncryptionKey_Label = Label(root,text = "Encryption Key",font = ("Arial",22))
    DEncryptionKey_Label.place(x = 200, y = 250)

    DencryptionKey = Entry(root,font = ("Arial",14),width = 25)
    DencryptionKey.place(x = 200,y = 300)

    GrayScale_button = Button(root,text = "Gray Scale",font = ("Arial",14),command = lambda: press_grayScale_button())
    GrayScale_button.place(x = 800,y = 200)

    Lab_button = Button(root,text = "Lab Scale",font = ("Arial",14),command = lambda: press_labScale_button())
    Lab_button.place(x = 800,y = 300)

    Hsv_button = Button(root,text = "Hsv Scale",font = ("Arial",14),command = lambda: press_hsv_button())
    Hsv_button.place(x = 800,y = 400)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: pressBackButton())
    Back_Button.place(x = 200,y = 600)
    
    def press_grayScale_button():
        a.grayScale(image_name.get(),int(DencryptionKey.get()))
    def press_labScale_button():
        a.labscale(image_name.get(),int(DencryptionKey.get()))
    def press_hsv_button():
        a.hsvScale(image_name.get(),int(DencryptionKey.get()))

def pressAuth():
    a = authenticate.Authenticate(usernameEntry.get(),passEntry.get())
    global accountname
    accountname = usernameEntry.get()
    try:
        if (a.auth()):
            usernameEntry.delete(0,END)
            passEntry.delete(0,END)
            # Label(root,text = "                  ",font = ("Arial",22)).place(x = 540,y = 650)
            # Label(root,text = "Verified!",font = ("Arial",22)).place(x = 540,y = 650)
            for widget in root.winfo_children():
                widget.destroy()

            save_image_button = Button(root,text = "Save Image",font = ("Arial",22),command = lambda: save_button())
            save_image_button.place(x = 200,y = 200)

            deleteImage_button = Button(root,text = "Delete Image",font = ("Arial",22),command = lambda: delete_button())
            deleteImage_button.place(x = 200,y = 300)

            displayImage_button = Button(root,text = "Display Image",font = ("Arial",22),command = lambda: display_button())
            displayImage_button.place(x = 200,y = 400)

            renameImage_button = Button(root,text = "Rename Image",font = ("Arial",22),command = lambda: rename_button())
            renameImage_button.place(x = 800,y = 200)

            filterImage_button = Button(root,text = "Filters",font = ("Arial",22),command = lambda: filter_button())
            filterImage_button.place(x = 800,y = 300)

            changeAccount_Button = Button(root,text = "Exit",font = ("Arial",22),command = root.quit)
            changeAccount_Button.place(x = 800,y = 400)


        else:
            usernameEntry.delete(0,END)
            passEntry.delete(0,END)
            Label(root,text = "Please Try Again!",font = ("Arial",22)).place(x = 540,y = 650)
    except:
        usernameEntry.delete(0,END)
        passEntry.delete(0,END)
        Label(root,text = "Please Try Again!",font = ("Arial",22)).place(x = 540,y = 650)
        


def createUserButton():
    def createUser():
        try:
            a = authenticate.Authenticate(usernameEntry.get(),passEntry.get())
            a.createUser()
            Label(root,text = "Successfully created a new user!",font = ("Arial",22)).place(x = 440,y = 650)
            usernameEntry.delete(0,END)
            passEntry.delete(0,END)
        except:
            usernameEntry.delete(0,END)
            passEntry.delete(0,END)
            Label(root,text = "Please Try Again!",font = ("Arial",22)).place(x = 540,y = 650)
    
    for widget in root.winfo_children():
            widget.destroy()
    welcome = Label(root,text = "FALCON",font=("Arial", 35))
    welcome.place(x = 540,y = 150)

    usernameLabel = Label(root,text = "New Username",font=("Arial", 20))
    usernameLabel.place(x = 500,y = 250)

    usernameEntry = Entry(root,font=("Arial", 14),width = 25)
    usernameEntry.place(x = 500,y = 300)

    passLabel = Label(root,text = "New Password",font=("Arial", 20))
    passLabel.place(x = 500, y = 370)

    passEntry = Entry(root,show = "*",width = 19,font=("Arial", 20))
    passEntry.place(x = 500, y = 420)

    submit_button = Button(root,text = "Submit",font=("Arial", 15),command = lambda: createUser())
    submit_button.place(x = 700,y = 500)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: backToHomeButton())
    Back_Button.place(x = 200,y = 600)

def deleteUserButton():
    def deleteUser():
        try:
            a = authenticate.Authenticate(usernameEntry.get(),passEntry.get())
            a.deleteUser()
            Label(root,text = "Successfully deleted a user!",font = ("Arial",22)).place(x = 440,y = 650)
            usernameEntry.delete(0,END)
            passEntry.delete(0,END)
        except:
            usernameEntry.delete(0,END)
            passEntry.delete(0,END)
            Label(root,text = "Please Try Again!",font = ("Arial",22)).place(x = 540,y = 650)
    
    for widget in root.winfo_children():
            widget.destroy()
    welcome = Label(root,text = "FALCON",font=("Arial", 35))
    welcome.place(x = 540,y = 150)

    usernameLabel = Label(root,text = "User to be deleted",font=("Arial", 20))
    usernameLabel.place(x = 500,y = 250)

    usernameEntry = Entry(root,font=("Arial", 14),width = 25)
    usernameEntry.place(x = 500,y = 300)

    passLabel = Label(root,text = "Password",font=("Arial", 20))
    passLabel.place(x = 500, y = 370)

    passEntry = Entry(root,show = "*",width = 19,font=("Arial", 20))
    passEntry.place(x = 500, y = 420)

    submit_button = Button(root,text = "Submit",font=("Arial", 15),command = lambda: deleteUser())
    submit_button.place(x = 700,y = 500)

    Back_Button = Button(root, text = "Back",font = ("Arial",14),command = lambda: backToHomeButton())
    Back_Button.place(x = 200,y = 600)

def backToHomeButton():
    
    for widget in root.winfo_children():
            widget.destroy()

    welcome = Label(root,text = "FALCON",font=("Arial", 35))
    welcome.place(x = 540,y = 150)

    usernameLabel = Label(root,text = "Username",font=("Arial", 20))
    usernameLabel.place(x = 500,y = 250)
    global usernameEntry
    usernameEntry = Entry(root,font=("Arial", 14),width = 25)
    usernameEntry.place(x = 500,y = 300)

    passLabel = Label(root,text = "Password",font=("Arial", 20))
    passLabel.place(x = 500, y = 370)

    global passEntry 
    passEntry = Entry(root,show = "*",width = 19,font=("Arial", 20))
    passEntry.place(x = 500, y = 420)

    auth_button = Button(root,text = "Next",font=("Arial", 15),command = lambda: pressAuth())
    auth_button.place(x = 700,y = 500)

    new_user_button = Button(root,text = "Create User",font=("Arial", 15),command = lambda: createUserButton())
    new_user_button.place(x = 700,y = 550)

    delete_user_button = Button(root,text = "Delete a user",font = ("Arial",15),command = lambda: deleteUserButton())
    delete_user_button.place(x = 700,y = 600)


if __name__ == "__main__":

    root = Tk()
    root.title("Falcon")
    root.geometry("1280x720")

    backToHomeButton()

    root.mainloop()
    