from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import random
root = Tk()
root.wm_geometry('230x300')
root.title('THE GAME OF HANGMAN')
words = ['abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'pneumonoultramicroscopicsilicovolcanoconiosis',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie'
]
global secret_word
secret_word = random.choice(words)
#get the dashes for the secret word
dash = []
guesdinc = []
guesCOR = []
def dashes():
    for i in range(len(secret_word)):
        dash.append('-')
dashes()
#IMAGES FOR THE GAME BEING IMPORTED HERE FOR USE
my_img0 = ImageTk.PhotoImage(Image.open("hangman_Image0.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("hangman_Image1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("hangman_Image2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("hangman_Image3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("hangman_Image4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("hangman_Image5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("hangman_Image6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("hangman_Image7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("hangman_Image8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("hangman_Image9.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("hangman_Image10.jpg"))
imglst = [my_img0, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img1]
def switchIMG():
    global y
    global v
    myimage0.grid_forget()
    y = len(guesdinc)
    v = y - 1
    if y == 1:
        newIMG = Label(image=my_img0).grid(row=1, column=0, columnspan=3)
    elif y == 2:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 3:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 4:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 5:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 6:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 7:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 8:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 9:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 10:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    elif y == 11:
        newIMG = Label(image=imglst[v]).grid(row=1, column=0, columnspan=3)
    else:
        newIMG = Label(image=my_img0).grid(row=1, column=0, columnspan=3)
def getletterwrong():
    x = e.get()
    guesdinc.append(x)
    switchIMG()
    #print the new list on the screen
    label4 = Label(root, text=(str(''.join(guesdinc)))).grid(row=5, column=0, columnspan=3)
    e.delete(0, 'end')
    if len(guesdinc) >= 10:
        answer = messagebox.askyesno((str(secret_word)), 'You killed a man, his blood is on your hands...would you like to try again? ')
        if answer == True:
            resetallLose()
        else:
            root.quit()
def getletterright():
    x = e.get()
    guesCOR.append(x)
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
def resetallwin():
    global y
    global v
    global secret_word
    y = 0
    v = 0
    secret_word = ()
    dash.clear()
    guesdinc.clear()
    guesCOR.clear()
    secret_word = random.choice(words)
    dashes()
    label1 = Label(root, text='                           ').grid(row=2, column=0, columnspan=3)
    label1 = Label(root, text='Your secret word is ' + (str(len(secret_word))) + ' letters long').grid(row=2, column=0, columnspan=3)
    label3 = Label(root, text='                           ').grid(row=3, column=0, columnspan=3)
    label3 = Label(root, text=(''.join(dash))).grid(row=3, column=0, columnspan=3)
    label4 = Label(root, text='                           ').grid(row=5, column=0, columnspan=3)
    label4 = Label(root, text=(str(''.join(guesdinc)))).grid(row=5, column=0, columnspan=3)
    myimage0 = Label(image=my_img0).grid(row=1, column=0, columnspan=3)
def resetallLose():
    global y
    global v
    global secret_word
    y = 0
    v = 0
    secret_word = ()
    dash.clear()
    guesdinc.clear()
    guesCOR.clear()
    secret_word = random.choice(words)
    dashes()
    label1 = Label(root, text='                           ').grid(row=2, column=0, columnspan=3)
    label1 = Label(root, text='Your secret word is ' + (str(len(secret_word))) + ' letters long').grid(row=2, column= 0, columnspan=3)
    label3 = Label(root, text='                           ').grid(row=3, column=0, columnspan=3)
    label3 = Label(root, text=(''.join(dash))).grid(row=3, column=0, columnspan=3)
    label4 = Label(root, text='                           ').grid(row=5, column=0, columnspan=3)
    label4 = Label(root, text=(str(''.join(guesdinc)))).grid(row=5, column=0, columnspan=3)
    myimage0 = Label(image=my_img1).grid(row=1, column=0, columnspan=3)
#function that lets the user press the enter key to submit letters to the program
#letter is just used to show that your are passing information from e through decideletter()
def onEnter(letter):
    decideletter()
def decideletter():
    x = e.get()
    if len(x) > 1:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You must enter only one letter at a time.')
    elif x in guesdinc:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You have already guessed that letter incorrectly.')
    elif x in guesCOR:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You have already guessed that letter correctly.')
    elif x.isupper() == True:
        e.delete(0, END)
        messagebox.showinfo('BIG OOF', 'You must only enter lowercase letters')
    elif x in secret_word:
        getletterright()
    elif x not in secret_word:
        getletterwrong()
    label3 = Label(root, text=(''.join(dash))).grid(row=3, column= 0, columnspan=3)
#all the things on the screen in order of the screen
label0 = Label(root, text='Welcome to Hangman').grid(row=0, column=0, columnspan=3)
#first hangman image that the user can see
my_img0 = ImageTk.PhotoImage(Image.open("hangman_Image0.jpg"))
myimage0 = Label(image=my_img0)
myimage0.grid(row=1, column=0, columnspan=3)
label1 = Label(root, text='Your secret word is ' + (str(len(secret_word))) + ' letters long')
label1.grid(row=2, column= 0, columnspan=3)
#the text of the word
label3 = Label(root, text=(str(''.join(dash)))).grid(row=3, column=0, columnspan=3)
label4 = Label(root, text=(str(''.join(guesdinc)))).grid(row=5, column=0, columnspan=3)
#what the user has entered
guesdlabel = Label(root, text='So far you\'ve entered...').grid(row=4, column=0, columnspan=3)
#where the letters are entered
e = Entry(root)
e.bind('<Return>', onEnter)
e.grid(row=6, column=0, columnspan=3)
e.insert(0, '???')
btn = Button(root, text='enter', command=decideletter)
btn.grid(row=7, column=0, columnspan=3)
root.mainloop()