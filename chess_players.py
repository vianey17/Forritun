RANK = 0
NAME = 1
COUNTRY = 2
POINTS = 3
BIRTH_YEAR = 4

def get_input(user_prompt):
    user_input = input(user_prompt)
    return user_input

def read_file(file_name):
    try:
        file_content = open(file_name, "r")
        return file_content
    except FileNotFoundError:
        return None

def create_dict_from_file_data(file_content):
    # Creates a dictionary with player information
    # Keys are player "firstname lastname" using create_key()
    # function. Values are player rank, country, points, 
    # and birth_year.
    # The function clean_data(data) is used to 
    # remove punctuation and ensure corrent data type
    # in each value

    chess_players_dict = {}
    for data in file_content:
        data = data.split(";")
        key = create_key(data[NAME])
        chess_players_dict[key] = clean_data(data)
    return chess_players_dict

def clean_data(data):
    rank = int(data[RANK].strip())
    country = data[COUNTRY].strip()
    points = int(data[POINTS].strip())
    birth_year = int(data[BIRTH_YEAR].strip())   
    return [rank, country, points, birth_year]

def create_key(data):
    lastname, firstname = data.split(",")
    lastname = lastname.strip()
    firstname = firstname.strip()
    return "{} {}".format(firstname,lastname)

def get_points_per_country(chess_player_dict):
    # Creates a dictionary that has each country
    # as a key, and the a list with the number of players and
    # the country's total points as a value

    my_dict = {}
    
    for chess_player_dict in chess_player_dict.items():
        country = chess_player_dict[1][1]
        if country in my_dict:
            my_dict[country][0] += 1
            my_dict[country][1] += chess_player_dict[1][2]
        else:
            data = [1,chess_player_dict[1][2]]
            my_dict[country] = data
    return my_dict

def print_header(header_string):
    # Prints decorative header for readability

    print(header_string)
    print("-" * len(header_string))

def print_results(chess_player_dict,countries_dict):
    # Takes in both dictionaries and first calculates
    # the country's respective average points,
    # then prints out player names by country with
    # their respective scores
    
    for country in sorted(countries_dict.keys()):
        number_of_players = countries_dict[country][0]
        total_points = countries_dict[country][1]
        average = total_points / number_of_players
        print("{} ({}) ({:.1f}):".format(country, number_of_players,average))
    
        for player in chess_player_dict.keys():
            if chess_player_dict[player][1] == country:
                print("{:>40}{:>10d}".format(player, chess_player_dict[player][2]))

def main():
    # get name of file from user
    file_name = get_input("Enter filename: ")
    # get data from csv file
    file_content = read_file(file_name)
    
    if file_content:
        chess_players_dict = create_dict_from_file_data(file_content)
        # Close file once data has been extracted, saves memory
        file_content.close() 
        # 4. Calculate avg for each country
        
        # 5. Calculate number of players for each country
        countries_dict = get_points_per_country(chess_players_dict)
        # 6. Print results
        print_header("Players by country:")
        print_results(chess_players_dict,countries_dict)
        

    # create dictionary from csv data, key = name

main()