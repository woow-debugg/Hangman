"""
PROGRAM INFORMATION

29 September 2021
Programmer: Tristin Hinojosa

filename: Hangman_App.py

SUMMARY:
This program lets the user play the game of hangman using the tkinter GUI

"""
from tkinter import messagebox, Tk, Label, END, Entry, Button
from PIL import ImageTk, Image
from hangman_words import words
import random
root = Tk()
root.wm_geometry('230x300')
root.title('HANGMAN')


global secret_word
secret_word = random.choice(words)

dash = []
guessed_incorrect = []
guessed_correct = []


#IMAGES FOR THE GAME BEING IMPORTED HERE FOR THE GAME
my_img0  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image0.jpg"))
my_img1  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image1.jpg"))
my_img2  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image2.jpg"))
my_img3  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image3.jpg"))
my_img4  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image4.jpg"))
my_img5  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image5.jpg"))
my_img6  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image6.jpg"))
my_img7  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image7.jpg"))
my_img8  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image8.jpg"))
my_img9  = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image9.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image10.jpg"))
imglst = [my_img0, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img1]

#This function converts the "secret_word" into dashes,
# in order for the user to see the placement of their correct guesses in the secret word.
def dashes():
    for letter in range(len(secret_word)):
        dash.append('-')

dashes()


#This function is used to switch the images depending on the status of the game
def switchIMG():
    global y
    global v
    myimage0.grid_forget()
    y = len(guessed_incorrect)
    v = y - 1
    if y == 1:
        newIMG = Label(image=my_img0).grid(row=1, column=0, columnspan=3)
    else:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)


#This function is used when a letter is guessed incorrectly
#If the user has incorrectly guessed 10 or more times they lose the game. 
def getletterwrong():
    x = e.get()
    guessed_incorrect.append(x)
    switchIMG()
    #print the new list on the screen
    label4 = Label(root, text=(str(''.join(guessed_incorrect)))).grid(row=5, column=0, columnspan=3)
    e.delete(0, 'end')
    if len(guessed_incorrect) >= 10:
        answer = messagebox.askyesno("REST IN PEACE", f'''You killed a man, his blood is on your hands
                                    ...would you like to try again? The secret word was {str(secret_word)}''')
        if answer == True:
            resetallLose()
        else:
            root.quit()


#This function is used when a letter is guessed correctly
#If the user has correctly guessed the enough letters to match the "secret_word" they win the game. 
def getletterright():
    x = e.get()
    guessed_correct.append(x)
    label3 = Label(root, text=(''.join(dash))).grid(row=3, column= 0, columnspan=3)
    for i in range(len(secret_word)):
        if secret_word[i] == x:
            dash[i] = x
    if (''.join(dash)) == secret_word:
        answer = messagebox.askyesno('Nice Job', 'Congratulations you have found the secret word, would you like to try your skills again? ')
        if answer == False:
            root.quit()
        else:
            resetallwin()
    else:
        label3 = Label(root, text=(''.join(dash))).grid(row=3, column=0, columnspan=3)
        e.delete(0, 'end')
    e.delete(0, END)



#This function will display the basic layout of the screen after the user has restarted the game, win or lose.
def BasicScreenLayout():
    label1 = Label(root, text='                           ').grid(row=2, column=0, columnspan=3)
    label1 = Label(root, text='Your secret word is ' + (str(len(secret_word))) + ' letters long').grid(row=2, column= 0, columnspan=3)
    label3 = Label(root, text='                           ').grid(row=3, column=0, columnspan=3)
    label3 = Label(root, text=(''.join(dash))).grid(row=3, column=0, columnspan=3)
    label4 = Label(root, text='                           ').grid(row=5, column=0, columnspan=3)
    label4 = Label(root, text=(str(''.join(guessed_incorrect)))).grid(row=5, column=0, columnspan=3)


# This function resets the game if the user wins, it resets y and v.
# By resetting y and v it allows all the mistakes and progress of the last game to be places at 0.
def resetallwin():
    global y
    global v
    global secret_word
    y = 0
    v = 0
    secret_word = ()
    dash.clear()
    guessed_incorrect.clear()
    guessed_correct.clear()
    secret_word = random.choice(words)
    dashes()
    BasicScreenLayout()

    myimage0 = Label(image=my_img0).grid(row=1, column=0, columnspan=3)

# This function resets the game if the user loses, it resets y and v.
# By resetting y and v it allows all the mistakes and progress of the last game to be places at 0.
def resetallLose():
    global y
    global v
    global secret_word
    y = 0
    v = 0
    secret_word = ()
    dash.clear()
    guessed_incorrect.clear()
    guessed_correct.clear()
    secret_word = random.choice(words)
    dashes()
    BasicScreenLayout()
    myimage0 = Label(image=my_img1).grid(row=1, column=0, columnspan=3)


#function that lets the user press the enter key to submit letters to the program
#letter is just used to show that your are passing information from e through decideletter()
def onEnter(letter):
    decideletter()



#This function decides if the input is a lowercase letter, all other input will result in an error message.
def decideletter():
    x = e.get()
    if len(x) > 1:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You must enter only one letter at a time.')
    elif x in guessed_incorrect:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You have already guessed that letter incorrectly.')
    elif x in guessed_correct:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You have already guessed that letter correctly.')
    elif x.isupper() == True:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You must only enter lowercase letters!')
    elif x.isdigit() == True:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You must only enter letters, digits are not allowed!')
    elif x in secret_word:
        getletterright()
    elif x not in secret_word:
        getletterwrong()
    label3 = Label(root, text=(''.join(dash))).grid(row=3, column= 0, columnspan=3)

    
#THIS STARTS THE ORGANIZATION OF THE SCREEN AS SHOWN TO THE USER
label0 = Label(root, text='Welcome to Hangman').grid(row=0, column=0, columnspan=3)


#First hangman image that the user will see, the cover photo.
first_image = ImageTk.PhotoImage(Image.open("Pictures\hangman_Image0.jpg"))
myimage0 = Label(image=first_image)
myimage0.grid(row=1, column=0, columnspan=3)
label1 = Label(root, text='Your secret word is ' + (str(len(secret_word))) + ' letters long')
label1.grid(row=2, column= 0, columnspan=3)


#Displays the word to be guessed and the incorrect guesses of the user.
label3 = Label(root, text=(str(''.join(dash)))).grid(row=3, column=0, columnspan=3)
label4 = Label(root, text=(str(''.join(guessed_incorrect)))).grid(row=5, column=0, columnspan=3)


#Displays what the user has entered.
guesdlabel = Label(root, text='So far you\'ve entered...').grid(row=4, column=0, columnspan=3)


#This sets up the input box so the user can enter characters.
e = Entry(root)
e.bind('<Return>', onEnter)
e.grid(row=6, column=0, columnspan=3)
e.insert(0, '???')
btn = Button(root, text='enter', command=decideletter)
btn.grid(row=7, column=0, columnspan=3)
print(f'{"_" * 35}The Game of Hangman is currently running{"_" * 35}')
root.mainloop()
