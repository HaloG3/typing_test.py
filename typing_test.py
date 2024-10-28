import curses
from curses import wrapper
import time

def start_screen (stdscr):
    stdscr.clear()
    stdscr.addstr('welcome to the sppeed typinggggg')
    stdscr.addstr('\n press any key to move on...')
    stdscr.refresh()
   
    stdscr.getkey()

def display_text(stdscr, target, current,wpm=0): # these are parameter and we pass the value when we run it 
    stdscr.addstr(target)
    stdscr.addstr(1,0 , f'WPM : {wpm}') # and so on
# it overlay the words and show if we type wrong word
    for i, char in enumerate (current): #enum give us the elemnt as well as index in the list 
        correct_char = target[i] # break just after we hit the limeit
    
        color= curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char,color ) # decide which color pair we use

def wpm_test (stdscr):
    target_text = ('hi world i am mohit Rao and this is my typing test ')
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round ((len(current_text)/ (time_elapsed/60))/5) # rond off the decimal number and we assume a world =5 letter

        stdscr.clear() # clear the screen everytime
        display_text(stdscr, target_text, current_text, wpm )
        stdscr.refresh() # refresh evey time
        if ''.join (current_text)== target_text: # remove all whitespace and help to convert the string to list
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()# our program crash if we dont type super super fast so we need this

        except:
            continue

        if ord(key) == 27: # when we hit esc it exit the terminal 27 is ascii code for esc
               break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'): # representation of backspace key 
            if len(current_text)> 0:
                current_text.pop()  # we choose a list in here and we pop out the last word when user hit the backspace key
        elif len(current_text)< len(target_text): # it not allow us to type more than the limit   
            current_text.append(key)


     

def main(stdscr): # std screen = give us a screen where we type the words
    curses.init_pair(1,curses.COLOR_MAGENTA, curses.COLOR_BLACK) #(code, foreground, bg color)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK )
    curses.init_pair(3,curses.COLOR_CYAN, curses.COLOR_BLACK)
    
   


    
   # stdscr.addstr( 2,0,'HEllo World!')  1 line down and 0th index

    #stdscr.getkey() # the output is wait to press any key to exit
    #print(key)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "you complete the test ! press any key to exit")

        key = stdscr.getkey()
        if ord(key) == 27:
            break # if user don't press esc key it will continue agai and again
wrapper(main)
 # we need to run this code in terminal to shw its real screen