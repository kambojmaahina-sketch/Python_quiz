import pygame
import sys
import random

pygame.init()

# Screen
WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (40, 100, 255)
GREEN = (0, 180, 0)
RED = (220, 0, 0)
GRAY = (220, 220, 220)

# Fonts
title_font = pygame.font.SysFont("Arial", 45)
font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()


# Questions

questions = [

{
"q":"Who developed Python programming language?",
"options":["Dennis Ritchie","Guido van Rossum","James Gosling","Bjarne Stroustrup"],
"answer":"Guido van Rossum"
},

{
"q":"Which keyword is used to create a function in Python?",
"options":["function","define","def","fun"],
"answer":"def"
},

{
"q":"Which function is used to display output?",
"options":["output()","print()","show()","display()"],
"answer":"print()"
},

{
"q":"Which data type stores multiple values?",
"options":["Integer","List","Float","Boolean"],
"answer":"List"
},

{
"q":"Which symbol is used for comments in Python?",
"options":["//","#","/* */","--"],
"answer":"#"
},

{
"q":"Which operator is used for exponentiation?",
"options":["^","%","**","//"],
"answer":"**"
},

{
"q":"Which loop is used to iterate over a sequence?",
"options":["if","for","switch","case"],
"answer":"for"
},

{
"q":"What is the extension of Python file?",
"options":[".java",".cpp",".py",".html"],
"answer":".py"
},

{
"q":"Which keyword stops a loop?",
"options":["stop","break","exit","end"],
"answer":"break"
},

{
"q":"Which data type stores True or False?",
"options":["String","Integer","Boolean","List"],
"answer":"Boolean"
},

{
    "q":"Which keyword is used to create a class in Python?",
    "options":["class","Class","define","object"],
    "answer":"class"
},

{
    "q":"Which function returns the length of a list?",
    "options":["count()","len()","size()","length()"],
    "answer":"len()"
},

{
    "q":"Which data type is immutable?",
    "options":["List","Dictionary","Tuple","Set"],
    "answer":"Tuple"
},

{
    "q":"Which operator is used for floor division?",
    "options":["/","//","%","**"],
    "answer":"//"
},

{
    "q":"Which keyword is used for conditional statements?",
    "options":["if","switch","case","when"],
    "answer":"if"
},

{
    "q":"Which keyword is used to import a module?",
    "options":["include","using","import","require"],
    "answer":"import"
},

{
    "q":"Which function converts a string into an integer?",
    "options":["float()","str()","int()","bool()"],
    "answer":"int()"
},

{
    "q":"Which data type stores key-value pairs?",
    "options":["List","Tuple","Dictionary","Set"],
    "answer":"Dictionary"
},

{
    "q":"Which keyword is used to handle exceptions?",
    "options":["catch","except","error","finally"],
    "answer":"except"
},

{
    "q":"Which keyword is used to create an anonymous function?",
    "options":["lambda","def","func","anonymous"],
    "answer":"lambda"
}

,
{
    "q":"Which function is used to take user input in Python?",
    "options":["scan()","input()","read()","accept()"],
    "answer":"input()"
},

{
    "q":"Which Boolean value represents false in Python?",
    "options":["false","False","FALSE","0"],
    "answer":"False"
},

{
    "q":"Which keyword is used to repeat a block of code while a condition is True?",
    "options":["for","repeat","while","loop"],
    "answer":"while"
},

{
    "q":"Which function is used to find the maximum value?",
    "options":["largest()","high()","max()","maximum()"],
    "answer":"max()"
},

{
    "q":"Which function is used to find the minimum value?",
    "options":["smallest()","min()","low()","minimum()"],
    "answer":"min()"
}
]

random.shuffle(questions)

# Variables

state = "menu"
question_no = 0
score = 0
selected_option = None
answered = False

def draw_text(text, x, y, color=BLACK, size="normal"):

    if size == "title":
        img = title_font.render(text, True, color)
    else:
        img = font.render(text, True, color)

    screen.blit(img, (x,y))


def button(text, x, y, w, h, color):

    rect = pygame.Rect(x, y, w, h)

    # Mouse hover
    mouse = pygame.mouse.get_pos()

    draw_color = color

    if rect.collidepoint(mouse) and color == GRAY:
        draw_color = (190, 190, 190)

    # Rounded Button
    pygame.draw.rect(
        screen,
        draw_color,
        rect,
        border_radius=12
    )

    # Border
    pygame.draw.rect(
        screen,
        BLACK,
        rect,
        2,
        border_radius=12
    )

    # Center Text
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return rect



running = True


while running:

    screen.fill(WHITE)


    # ---------------- MENU ----------------

    if state == "menu":

        draw_text(
            "PYTHON QUIZ GAME",
            230,
            100,
            BLUE,
            "title"
        )

        start_btn = button(
            "START QUIZ",
            330,
            250,
            250,
            60,
            GRAY
        )


        quit_btn = button(
            "QUIT",
            380,
            350,
            150,
            60,
            GRAY
        )


    # ---------------- QUIZ ----------------

    elif state == "quiz":


        q = questions[question_no]


        draw_text(
            f"Question {question_no+1}/{len(questions)}",
            50,
            40,
            BLUE,
            "title"
        )


        draw_text(
            q["q"],
            50,
            120
        )


        option_buttons = []

        y = 190


        for option in q["options"]:
            color = GRAY
            if answered:
                if option == q["answer"]:
                    color=GREEN
                elif option == selected_option:
                    color=RED
            btn = button(
                option,
                80,
                y,
                600,
                45,
                color
            )

            option_buttons.append((btn, option))
            y += 60

        if answered:
            next_btn = button(
                "NEXT QUESTION",
                300,
                500,
                300,
                55,
                BLUE
            )



    # ---------------- RESULT ----------------


    elif state == "result":


        draw_text(
            "QUIZ COMPLETED",
            250,
            100,
            BLUE,
            "title"
        )


        draw_text(
            f"Your Score: {score}/{len(questions)}",
            330,
            220
        )

        percentage = (score / len(questions)) * 100
        draw_text(
            f"Percentage: {percentage:.1f}%",
            330,
            270,
            BLUE
            )


        restart_btn = button(
            "PLAY AGAIN",
            330,
            330,
            250,
            60,
            GRAY
        )


        exit_btn = button(
            "EXIT",
            380,
            430,
            150,
            50,
            GRAY
        )



    pygame.display.update()



    # Events

    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()



        if event.type == pygame.MOUSEBUTTONDOWN:


            mouse = event.pos


            # Menu buttons

            if state == "menu":

                if start_btn.collidepoint(mouse):

                    state = "quiz"
                    question_no = 0
                    score = 0


                if quit_btn.collidepoint(mouse):

                    pygame.quit()
                    sys.exit()



            # Quiz options

            elif state == "quiz":
                if not answered:
                    for btn, option in option_buttons:
                        if btn.collidepoint(mouse):
                            selected_option = option
                            answered = True
                            if option == questions[question_no]["answer"]:
                                score += 1
                else:
                    if next_btn.collidepoint(mouse):
                        question_no += 1
                        selected_option = None
                        answered = False
                        if question_no >= len(questions):
                            state = "result"



            # Result screen

            elif state == "result":


                if restart_btn.collidepoint(mouse):

                    state = "quiz"
                    question_no = 0
                    score = 0
                    random.shuffle(questions)
                    selected_option = None
                    answered = False


                if exit_btn.collidepoint(mouse):

                    pygame.quit()
                    sys.exit()



    clock.tick(60)