import turtle
import pandas as pd

# Creating the screen
screen = turtle.Screen()
screen.title("Choose cities in the UAE")

# Adding the image as a possible shape
screen.addshape("emirats11.gif")

# Setting the shape of the turtle to the image
turtle.shape("emirats11.gif")

# This code can be used to get the coordinates on the image
cities = pd.DataFrame(columns=['city', 'x', 'y'])   # Create a dataframe to store the cities and their coordinates

def get_mouse_click_coor(x, y):
    city = screen.textinput(title="Which city is this?", prompt="What's the city's name?")
    print(city, x, y)

    if city is not None:
        new_row = {'city': city, 'x': x, 'y': y} # Create a new row to store the city and coordinates
        global cities   # update the dataframe outside the function
        new_index = len(cities)    # Get the index of the new row to be the current length of the dataframe
        cities.loc[new_index] = new_row # Insert the new row at that index location

turtle.onscreenclick(get_mouse_click_coor) # Upon clicking a location on the map, the function will be called

turtle.mainloop() # Keep the window open

# When the window is closed...
cities.to_csv("cities.csv", index=False) # Save the list to a csv file
