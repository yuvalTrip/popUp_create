import json


def start_game(num_people, angle_sun,recognize_points,decrease_points,totaltime):
    # Your game logic goes here
    print("Starting game with {} people and angle of sun {}.".format(num_people, angle_sun))
    print("For each person recognized you will recieve {} points".format(recognize_points))
    print("For each minute will pass in the game, you will loose {} points".format(decrease_points))
    print("The game will lasts {} seconds.".format(totaltime))

  # Convert values to a dictionary
    game_data = {
        "num_people": num_people,
        "angle_sun": angle_sun,
        "recognize_points": recognize_points,
        "decrease_points": decrease_points,
        "total_time": totaltime
    }
    #print(game_data)



 # Convert dictionary to JSON string
#     game_data_json = json.dumps(game_data)
# # Pass JSON string to the game class or function
#     game.start_game(game_data_json)
# Ensure that your game.start_game function accepts a JSON string as an argument.