import pgzrun
import string
from random import  choice,randint

WIDTH = 800
HEIGHT = 500

colors = (145, 17, 10)

letter_velcity = 1
right_score = 0
wrong_score = 0

screen_letter = []



def draw():
    screen.fill(colors)
    for letter in screen_letter:
        screen.draw.text(letter['alphabet'],(letter['x'],letter['y'] ),fontsize = 50,color = "white")
    draw_score()
def update():
     global wrong_score
     for letter in screen_letter:
         letter['y'] += letter_velcity
         if letter['y'] > HEIGHT:
             wrong_score +=1
             remove_letter(letter)
             get_new_letter()

     while len(screen_letter) < 4:
         get_new_letter()

def on_key_down(unicode):
    global right_score ,wrong_score
    if unicode:
        for letter in screen_letter:
            if unicode == letter['alphabet']:
                right_score +=1
                remove_letter( letter )
                get_new_letter()
                break
            else:
                wrong_score += 1

def get_new_letter():
    letter = {}
    letter['alphabet'] = choice(string.ascii_lowercase)
    letter['x'] = randint(10 , WIDTH-10)
    letter['y'] = 10
    screen_letter.append(letter)

def draw_score():
    screen.draw.text("Right:"+str(right_score),(700,10),fontsize = 25,color = "white")
    screen.draw.text("wrong:"+str(wrong_score),(700,25),fontsize = 25,color = "white")


def remove_letter(letter):
    screen_letter.remove(letter)

pgzrun.go()
