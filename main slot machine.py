from guizero import App, Picture, PushButton, Box, Text
import random

symbols = [
    'images/7.png',
    'images/cross.png',
    'images/bell.png',
    'images/cherry.png',
    'images/bar.png'
]

def spin():
    global balance
    if balance > 0:
        balance -= 5
        random1 = random.randint(0, 4)
        random2 = random.randint(0, 4)
        random3 = random.randint(0, 4)
        position1.image = symbols[random1]
        position2.image = symbols[random2]
        position3.image = symbols[random3]
        
        if symbols[random1] == symbols[random2] == symbols[random3]:
            balance += 20
            bottom_text.value = "Winner! +20"
            bottom_text.text_color = "green"
        else:
            bottom_text.value = "Loser :(   -5"
            bottom_text.text_color = "red"
        
        balance_output.value = f"Your balance is: {balance}"
    else:
        game_over()

def game_over():
    bottom_text.value = "Game Over"
    bottom_text.text_color = "red"
    spin_button.disable()

app = App(title="Slot Machine")

balance = 100
balance_output = Text(app, text=f"Your balance is: {balance}", align="top")

slot_box = Box(app, layout="grid", align="top")
position1 = Picture(slot_box, image=symbols[0], grid=[0, 0])
position2 = Picture(slot_box, image=symbols[1], grid=[1, 0])
position3 = Picture(slot_box, image=symbols[2], grid=[2, 0])

spin_button = PushButton(app, text="SPIN", command=spin, grid=[1, 1], width=10, align="top")

bottom_text = Text(app, text="", align="top", height=2)

app.display()
