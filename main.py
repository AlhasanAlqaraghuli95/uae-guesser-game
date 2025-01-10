import turtle
import pandas as pd

# Creating the screen
screen = turtle.Screen()
screen.title("UAE city guesser")
screen.setup(width=1000, height=800)

# Adding the image as a possible shape
screen.addshape("emirats11.gif")

# Setting the shape of the turtle to the image
turtle.shape("emirats11.gif")


# Read the csv file and set up the variables needed for the main logic
cities = pd.read_csv("cities.csv")
correct_guess = 0
cities_answered = []

while True:
    # Retrieve the guess and convert it to title case
    answer_city = screen.textinput(title=f"{correct_guess} / {len(cities)} guessed", prompt="What's another city's name?")
    answer_city = answer_city.lower().title()

    # check if the answer is in the list of citys & not already guessed
    if answer_city in cities['city'].values and answer_city not in cities_answered:
        city_data = cities[cities['city'] == answer_city]
        new_turtle = turtle.Turtle('turtle')
        new_turtle.penup()
        new_turtle.goto(int(city_data['x']), int(city_data['y'])) # Turtle go to position of the city on the map
        new_turtle.write(answer_city)
        new_turtle.hideturtle()

        # Store the answers in the list
        cities_answered.append(answer_city)
        correct_guess += 1

    # If the user types exit, break the loop
    if answer_city == "Exit":

        result_list = [city for city in cities['city'].values if city not in cities_answered] # Get the citys which were not guessed
        
        result = pd.DataFrame(result_list, columns=['city'])
        result.to_csv("citys_to_learn.csv") # Save the list to a csv file
        break

# This keeps the turtle screen open
turtle.mainloop()

