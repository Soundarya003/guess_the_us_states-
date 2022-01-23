import turtle
import pandas

# making the screen set-up
screen = turtle.Screen()
# title of the screen
screen.title("Guess the U.S States")

# addding the map image to the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# using pandas read the data, convert the state column to a list
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()

# count will keep track of how many states we've guessed correctly
count = 0
# the list will contain names of all states we guessed correctly
guessed_states = []
# the list will contain names of all states we didn't guessed correctly
not_in_list = []

# we run the loop till the user guesses all 50 states rightly
while count < 50:
    user_answer = screen.textinput(title=f"Right states: {count}/50", prompt="Enter the state name").title()

    # if the user want to exit the game
    if user_answer == "Exit":
        for state in state_list:
            if state not in guessed_states:
                not_in_list.append(state)
        # this csv file will have the list of countries user didn't guess,will help them to learn
        s = pandas.DataFrame(not_in_list)
        s.to_csv("missing_states.csv")
        break

    # we're checking if user answer is right
    if user_answer in state_list:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            # we're moving the name of state to it's coordinates
            points = data[data["state"] == user_answer]
            t.goto(int(points.x), int(points.y))
            t.write(arg=user_answer, font=('Arial', 15, 'normal'))
            # increasing the number as user guesses correctly 
            count += 1
            guessed_states.append(user_answer)



