import pygame as pg
import sys
import time
import random
from random import choice


background = pg.image.load('board_finish.png')
screen = pg.display.set_mode((1270,688))
sprite = pg.image.load('B2.png')
currency = 500
Spend = 50
Invest = 0
Save = 500
Donate = 5
gold =(255,153,0)
screen.blit(background,[0,0])
white = (225,255,255)
black = (0,0,0)
answer = pg.image.load('pop_up_box.png').convert()
answer.set_alpha(208)


def player(x,y):
    screen.blit(sprite,(x,y))

# invest options    
def Invests():
    font = pg.font.SysFont(None,40)
    text = font.render('                     Invest     ',True,white)
    text0 = font.render('Would you like to Invest in a lemonade',True,white)
    text1 = font.render('stand for $100? ',True,white)
    text2 = font.render('A.) Yes', True,white)
    text3 = font.render('B.) No', True,white)
    screen.blit(text,(310,320))
    screen.blit(text0,(310,370))
    screen.blit(text1,(310,400))
    screen.blit(text2,(310,450))
    screen.blit(text3,(310,490))
    
def Spends():
    font = pg.font.SysFont(None,40)
    text = font.render('                     Spend     ',True,white)
    text0 = font.render('Your lemonade stand is out of lemons.',True,white)
    text1 = font.render('A.) Buy 2 lemons for $10 ',True,white)
    text2 = font.render('B.) Buy 4 lemons for $30',True,white)
    text3 = font.render('C.) Buy 7 lemons for $20',True,white)
    text4 = font.render('D.) Buy 10 lemons for $50',True,white)
    screen.blit(text,(310,320))
    screen.blit(text0,(310,370))
    screen.blit(text1,(310,420))
    screen.blit(text2,(310,450))
    screen.blit(text3,(310,490))
    screen.blit(text4,(310,520))



def Saves():
    font = pg.font.SysFont(None,40)
    text = font.render('                     Save     ',True,white)
    text0 = font.render('At the end of the month you',True,white)
    text1 = font.render('will have $1000. What should you',True,white)
    text2 = font.render('do with it?',True,white)
    text3 = font.render('A.) Buy 3 pounds of candy for $300',True,white)
    text4 = font.render('B.) Save $500',True,white)
    screen.blit(text,(310,320))
    screen.blit(text0,(310,370))
    screen.blit(text1,(310,400))
    screen.blit(text2,(310,430))
    screen.blit(text3,(310,490))
    screen.blit(text4,(310,525))



def Donates():
    font = pg.font.SysFont(None,40)
    text = font.render('                     Donate     ',True,white)
    text0 = font.render('Would you like to Donate $5',True,white)
    text1 = font.render('to local homeless shelter? ',True,white)
    text2 = font.render('A.) Yes',True,white)
    text3 = font.render('B.) No',True,white)
    screen.blit(text,(310,320))
    screen.blit(text0,(310,370))
    screen.blit(text1,(310,400))
    screen.blit(text2,(310,450))
    screen.blit(text3,(310,490))

    

#number generator
def number():
    #initialization of font module and creating a font to draw with
    screen.blit(answer,(295,290))
    fontdir = pg.font.match_font('TimesNewRoman', False, False)
    myfont = pg.font.Font(fontdir,40)
    font = pg.font.SysFont(None,40)
    text6 = font.render('YOU ARE CORRECT',True,white)
    text7 = font.render('MOVE',True,white)
    text8 = font.render('SPACES!',True,white)
    screen.blit(text6,(400,320))
    screen.blit(text7,(400,370))
    screen.blit(text8,(540,370))
    #creating the random list and their corresponding surfaces
    random_list = [random.randrange(1,3) for x in range(1)]
    text_list = [myfont.render(str(x),True,white) for x in random_list]
    pos = (500,360)
    for text in text_list:
        screen.blit(text,pos)
        pos = (pos[0],pos[1]+50)

#pops up after the stand is purchased        
def correctI():
    global currency
    global Save
    global Invest 
    global Donate
    global Spend
    font = pg.font.SysFont(None,40)
    text = font.render('$'+str(currency), True, gold)
    new = font.render('$'+ str(Invest), True, gold)
    screen.blit(text,(1080,520))#currency
    screen.blit(new, (1030,600))#Invest
    
def correctS():
    #pressed = pg.key.get_pressed()
    global currency
    global Save
    global Invest 
    global Donate
    global Spend
    font = pg.font.SysFont(None,40)
    text = font.render('$'+str(currency), True, gold)
    text1 = font.render('$'+str(Save), True, gold)
    screen.blit(text,(1080,520))#currency
    screen.blit(text1,(1120,555))#save
    
def correctSp():
    #pressed = pg.key.get_pressed()
    global currency
    global Save
    global Invest 
    global Donate
    global Spend
    font = pg.font.SysFont(None,40)
    text = font.render('$'+str(currency), True, gold)
    new1 = font.render('$'+ str(Spend), True, gold)
    screen.blit(text,(1080,520))#currency
    screen.blit(new1, (1028,555))#spend
    
def correctd():
    #pressed = pg.key.get_pressed()
    global currency
    global Save
    global Invest 
    global Donate
    global Spend
    font = pg.font.SysFont(None,40)
    text = font.render('$'+str(currency), True, gold)
    text2 = font.render('$'+str(Donate), True, gold)
    screen.blit(text,(1080,520))#currency
    screen.blit(text2, (1140,600))#donate

# rotator
def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pg.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


    
    
    
def main():
    clock = pg.time.Clock()
    image = pg.image.load("small1.png")
    # Keep a reference to the original to preserve the image quality.
    orig_image = image
    rect = image.get_rect(center=(1030,230))
    angle = 0
    options= [(270,300,600,300),(0,0,3,4)]
    global currency
    global Spend
    global Invest
    global Donate
    global Save
    x = 100
    y = 150
    width = 40
    height = 70
    vel = 50 
    select_rect = pg.Rect(x,y,600,300)
    done = False
    font = pg.font.SysFont(None, 40)
    while not done: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            pressed = pg.key.get_pressed()
            if pressed[pg.K_UP]:# and y > vel:
                y -= 50
                screen.blit(background,[0,0])
                text = font.render('$'+str(currency), True, gold)
                #new = font.render('$'+ str(Invest), True, gold)
                screen.blit(text,(1080,520))
                #screen.blit(new, (1030,600))
            if pressed[pg.K_DOWN]:#  and y < 800 - height - vel:
                y += 50
                screen.blit(background,[0,0])
                text = font.render('$'+str(currency), True, gold)
                #new = font.render('$'+ str(Invest), True, gold)
                screen.blit(text,(1080,520))
                #screen.blit(new, (1030,600)) 
            if pressed[pg.K_LEFT]: #and x > vel:
                x -= 140
                screen.blit(background,[0,0])
                text = font.render('$'+str(currency), True, gold)
                #new = font.render('$'+ str(Invest), True, gold)
                screen.blit(text,(1080,520))
                #screen.blit(new, (1030,600)) 
            if pressed[pg.K_RIGHT]:# and x < 795 - width - vel:
                x += 140
                screen.blit(background,[0,0])
                text = font.render('$'+str(currency), True, gold)
                #new = font.render('$'+ str(Invest), True, gold)
                screen.blit(text,(1080,520))
                #screen.blit(new, (1030,600)) 
            if pressed[pg.K_SPACE]:
                screen.blit(background,[0,0])
                screen.blit(answer,(295,290))
                text = font.render('$'+str(currency), True, gold)
                new = font.render('$'+str(Invest), True, gold)
                screen.blit(text,(1080,520))
                screen.blit(new, (1030,600)) 
                time.sleep(2)
                for rects in options:
                    if select_rect.colliderect(rects):
                        random.choice([Invests,Spends,Saves,Donates])
                        random.choice([Invests,Spends,Saves,Donates])()
                        
                    
                                 
            if pressed[pg.K_a]:
                screen.blit(background,[0,0])#invest
                Invest += 100
                currency -= Invest
                correctI()
                number()
            if pressed[pg.K_w]:
                screen.blit(background,[0,0])#save
                Save += 500
                currency-= Save
                correctS()
                number()
            if pressed[pg.K_e]:
                screen.blit(background,[0,0])#donate
                currency-=Donate
                correctd()
                number()
            if pressed[pg.K_d]:
                screen.blit(background,[0,0])#spend
                currency-=Spend
                correctSp()
                number()
            if pressed[pg.K_b]:
                screen.blit(background,[0,0])
                screen.blit(answer,(295,290))
                font = pg.font.SysFont(None,40)
                text8 = font.render('YOU ARE INCORRECT',True,white)
                text9 = font.render('SORRY CANT MOVE ON THIS TURN!',True,white)
                screen.blit(text8,(300,320))
                screen.blit(text9,(300,370))
                
               

            
        
        angle += 2
        image, rect = rotate(orig_image, rect, angle)
        
        player(x,y)
        screen.blit(image, rect).center
        text = font.render('$'+str(currency), True, gold)
        screen.blit(text,(1080,520))
        pg.display.flip()
        clock.tick(70)
        

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
