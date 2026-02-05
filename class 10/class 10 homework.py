import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0, 0, 870, 80)
question_box = Rect(20, 100, 650, 150)
timer_box = Rect(700, 100, 150, 150)
answer_box1 = Rect(20, 270, 300, 150)
answer_box2 = Rect(370, 270, 300, 150)
answer_box3 = Rect(20, 450, 300, 150)
answer_box4 = Rect(370, 450, 300, 150)
skip_box = Rect(700, 270, 150, 330)

score = 0
time_left = 10
question_file_name = "homework_questions.txt"
marquee_message = ""
is_game_over = False

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "cyan")
    screen.draw.filled_rect(timer_box, "darkblue")
    screen.draw.filled_rect(skip_box, "lightblue")
    for ab in answer_boxes:
        screen.draw.filled_rect(ab, "teal")
    marquee_message = f"Welcome to Quiz Master...  Q: {question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color="white")
    screen.draw.textbox(str(time_left), timer_box, color="white", shadow=(1, 1), scolor="cyan")
    screen.draw.textbox("Skip", skip_box, color="white", angle=-90)
    if question:
        screen.draw.textbox(question[0].strip(), question_box, color="white")
        for i, ab in enumerate(answer_boxes, start=1):
            if i < len(question):
                screen.draw.textbox(question[i].strip(), ab, color="black")

def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH
"""
def read_question_file():
    global question_count, questions
    try:
        with open(question_file_name, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    questions.append(line)
                    question_count += 1
    except FileNotFoundError:
        print(f"⚠️ Could not find {question_file_name}")
"""
def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    global question
    if is_game_over:
        return
    for idx, box in enumerate(answer_boxes, start=1):
        if box.collidepoint(pos):
            try:
                correct = int(question[5])
            except (IndexError, ValueError):
                correct = -1
            if idx == correct:
                correct_answer()
            else:
                game_over()
            return
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left
    score += 1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def game_over():
    global question, time_left, is_game_over
    message = f"Game Over!\nYou got {score} questions correct!"
    question = [message, "-", "-", "-", "-", "5"]
    time_left = 0
    is_game_over = True

def skip_question():
    global question, time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left > 0:
        time_left -= 1
    else:
        game_over()

read_question_file()
if questions:
    question = read_next_question()
else:
    question = ["No questions found!", "-", "-", "-", "-", "5"]

clock.schedule_interval(update_time_left, 1)
pgzrun.go()
