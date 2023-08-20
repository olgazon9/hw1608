
import json
from user_input import *



if __name__ == '__main__':
   
    clear_screen()   
    jsondata = {}  # Create an empty dictionary to hold user data
    
    name = get_name()
    jsondata['name'] = name  # Add name to dictionary
    
    family_name = get_family_name()
    jsondata['family_name'] = family_name  # Add family name to dictionary
    
    # Save JSON data to a file
    with open('jsondata.json', 'w') as json_file:
        json.dump(jsondata, json_file, indent=4)
    
    print(GREEN +"JSON data saved to jsondata.json" + RESET_COLOR)
    print(GREEN +name + " " + family_name + " hello")

      # Read JSON data from the file
    with open('jsondata.json', 'r') as json_file:
        loaded_data = json.load(json_file)

    # Print the loaded JSON data
    print("Loaded JSON data:")
    print(json.dumps(loaded_data, indent=4))