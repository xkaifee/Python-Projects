"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 12.1 - Battleship
Date: 12/8/2023

Description:
   This program is a game of battleship. The user will be able to play the game where each player 
   will take turns guessing the location of the enemy's ships. The game will end when all of the 
   enemy's ships have been destroyed. The user will be able to view the hall of fame and 
   instructions. The user will also be able to quit the game at any time.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random


"""Write new functions below this line (starting with unit 4)."""

EMPTY_CELL = '~'
SHIP_SYMBOLS = {
    'M': 'Mothership',
    'D': 'Destroyer',
    'B': 'Battleship',
    'S': 'Stealth Ship',
    'P': 'Patrol Ship'
}

def make_grid():
    grid = [['~' for _ in range(12)] for _ in range(10)]

    ship_shapes = {
        'M': [[1,0,1], [0,1,0], [1,0,1]],  # Mothership shape
        'D': [[1, 0, 1], [0, 1, 0]],  # Destroyer shape
        'B': [[1,1],[1,1]],  # Battleship shape
        'S': [[1,1,1]],  # Stealth ship shape
        'P': [[1] * 2]  # Patrol ship shape
    }

    for ship_type, shape in ship_shapes.items():
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 11)
            shape_height = len(shape)
            shape_width = len(shape[0])
            if col + shape_width <= 12 and row + shape_height <= 10:
                valid = True
                for i in range(shape_height):
                    for j in range(shape_width):
                        if shape[i][j] == 1:
                            if grid[row + i][col + j] != EMPTY_CELL:
                                valid = False
                                break
                    if not valid:
                        break
                if valid:
                    for i in range(shape_height):
                        for j in range(shape_width):
                            if shape[i][j] == 1:
                                grid[row + i][col + j] = ship_type
                    break

    return grid

def check_hit(row, col, ship_locations):
    """Check if a cell is a hit or miss."""
    hit_symbol = None
    for ship_type, locations in ship_locations.items():
        if (row, col) in locations:
            hit_symbol = ship_type
            break
    return hit_symbol  # Return the symbol of the ship hit or None for empty cell hit




def display_example_grid():
    """Display an example grid with ship symbols."""
    example_grid = make_grid()  # Create a new example grid
    display_grid(example_grid, hide_ships=False)  # Display the example grid with ship symbols


def display_grid(grid, hide_ships=True, ship_locations=None):
    """Display the grid without showing the ship symbols."""
    print('   A  B  C  D  E  F  G  H  I  J  K  L')
    for i in range(len(grid)):
        print(f'{i}  ', end='')
        for j in range(len(grid[0])):
            cell = grid[i][j]
            if cell in SHIP_SYMBOLS and hide_ships:
                cell = EMPTY_CELL
            print(cell, end='  ' if j < len(grid[0]) - 1 else '')  # Remove the extra space for the last column
        print()


# Function to update the game grid based on the target location
def update_grid(grid, target, ship_locations=None):
    """Update the grid based on the target location."""
    row = int(target[0])
    col = ord(target[1].upper()) - ord('A')
    
    if grid[row][col] == EMPTY_CELL or grid[row][col] == 'o':
        grid[row][col] = 'o'  # Mark as a miss
    else:
        grid[row][col] = 'x' # Mark as a hit
        hit_symbol = grid[row][col]
          
        if ship_locations is not None:
            for locations in ship_locations.values():
                if (row, col) in locations:
                    locations.remove((row, col))  # Remove the location from ship_locations
                    break

        return hit_symbol  # Return the symbol of the ship hit or None for empty cell hit

def update_ship_locations(user_input, ship_locations):
    for ship_type, locations in ship_locations.items():
        if user_input in locations:
            locations.remove(user_input)
            if not locations:  # If locations for a ship are empty after removal
                return ship_type  # Return the ship type indicating it's destroyed
    return None  # No ship destroyed


# Function to check if a ship is destroyed
def check_ship_destroyed(ship_locations, grid):
    destroyed_ships = []
    for ship, locations in ship_locations.items():
        destroyed = all(grid[row][col] == 'x' for row, col in locations)
        if destroyed:
            destroyed_ships.append(ship)
    return destroyed_ships

# Function to update the Hall of Fame
def update_hall_of_fame(player_name, misses):
    """Update the hall of fame with the player's name and number of misses."""
    try:
        records = []
        with open('battleship_hof.txt', 'r') as file:
            header = file.readline()
            for line in file:
                record = line.strip().split(',')
                records.append((int(record[0]), record[1]))
        records.append((misses, player_name))
        records.sort(key=lambda x: x[0])
        records = records[:10]
        with open('battleship_hof.txt', 'w') as file:
            file.write(header)
            for miss, name in records:
                file.write(f'{miss},{name}\n')
    except FileNotFoundError:
        print('Hall of fame file not found.')

# Function to display the Hall of Fame
def display_hall_of_fame():
    """Display the hall of fame."""
    print('Hall of Fame:')
    print('+------+-------------+----------+')
    print('| Rank | Player Name | Accuracy |')
    print('+------+-------------+----------+')
    try:
        with open('battleship_hof.txt', 'r') as file:
            next(file)  # Skip the header
            content = file.readlines()
            for index, line in enumerate(content, start=1):
                split_values = line.strip().split(',')
                if len(split_values) >= 2:
                    misses, name = split_values[:2]  # Taking the first two values if available
                    accuracy = (17 / (int(misses) + 17)) * 100
                    print(f'| {index:>3}  |   {"".join(name):^7}   |{accuracy:>8.2f}% |')
                else:
                    print(f"Invalid entry found at line {index}: {line.strip()}")
    except FileNotFoundError:
        print('Hall of fame file not found.')
    print('+------+-------------+----------+')
    
    
    
def calculate_accuracy(hits, total_shots):
    """Calculate the accuracy."""
    return hits / total_shots * 100

# Main function to run the game
def main():
    print()
    print("                   ~ Welcome to Battleship! ~                   ")
    print()
    print("ChatGPT has gone rogue and commandeered a space strike fleet.")
    print("It's on a mission to take over the world.  We've located the")
    print("stolen ships, but we need your superior intelligence to help")
    print("destroy them before it's too late.")
    while True:
        print()
        print('Menu:')
        print('  1 : Instructions')
        print('  2 : View Example Map')
        print('  3 : New Game')
        print('  4 : Hall of Fame')
        print('  5 : Quit')
        choice = input('What would you like to do? ')
        
        if choice == '1':
            print()
            print('\nInstructions:')
            print('Ships are positioned at fixed locations in a 10-by-12 grid. The')
            print('rows of the grid are labeled 0 through 9, and the columns are')
            print('labeled A through L. Use menu option "2" to see an example.')
            print('Target the ships by entering the row and column of the location')
            print('you wish to shoot. A ship is destroyed when all of the spaces')
            print('it fills have been hit. Try to destroy the fleet with as few')
            print('shots as possible. The fleet consists of the following 5 ships:')
            print('\nSize : Type')
            print('   5 : Mothership')
            print('   4 : Battleship')
            print('   3 : Destroyer')
            print('   3 : Stealth Ship')
            print('   2 : Patrol Ship') 
            
        elif choice == '2':
            print()
            display_example_grid() 
            
        elif choice == '3':
            print()
            new_grid = make_grid()
            
            
            ship_locations = {symbol: [] for symbol in SHIP_SYMBOLS}  # Initialize ship_locations with empty lists
            
            for i, row in enumerate(new_grid):
                for j, cell in enumerate(row):
                    if cell in SHIP_SYMBOLS.keys():  # Check if the cell is a ship symbol
                        ship_locations[cell].append((i, j))
                        
              
            display_grid(new_grid, hide_ships=True, ship_locations=None)

            hits = 0
            total_shots = 0

            while True:
                print()
                target = input('Where should we target next (q to quit)? ').strip()
                
                if target.lower() == 'q':
                    break
                elif len(target) != 2:
                    print('Please enter exactly two characters.')
                elif not (target[0].isdigit() and target[1].isalpha()):
                    print('Please enter a location in the form "6G".')
                elif target[0].isdigit() and target[1].isdigit():
                    print('Please enter a location in the form "6G".')
                elif target[0].isalpha() and target[1].isalpha():
                    print('Please enter a location in the form "6G".')
                else:
                    total_shots += 1
                    hit_symbol = update_grid(new_grid, target, ship_locations) # Update the grid and get the hit symbol
                    
            
                    if hit_symbol == 'x':
                        print("\nIT'S A HIT!")
                        hits += 1
                        destroyed_ships = check_ship_destroyed(ship_locations, new_grid)
                        if destroyed_ships:
                            for destroyed_ship in destroyed_ships:
                                print(f"The enemy's {SHIP_SYMBOLS[destroyed_ship]} has been destroyed.")
                                ship_locations.pop(destroyed_ship, None)  # Remove the destroyed ship from ship_locations
                              

                        if not any(ship_locations.values()):
                            accuracy = calculate_accuracy(hits, total_shots)
                            print()
                            print("You've destroyed the enemy fleet!")
                            print("Humanity has been saved from the threat of AI.")
                            print()
                            print("For now ...")
                            print()
                            print(f'Congratulations, you have achieved a targeting accuracy of') 
                            print(f'{accuracy:.2f}% and earned a spot in the Hall of Fame.')
                            player_name = input('Enter your name: ')
                            print()
                            
                            misses = total_shots - hits
                            
                            update_hall_of_fame(player_name, misses)
                            display_hall_of_fame()
                            break
                    else:
                        print()
                        print('miss')
                      
                        
                    print()    
                    display_grid(new_grid, hide_ships=True)    
        elif choice == '4':
            print()
            display_hall_of_fame()
            
        elif choice == '5':
            print('\nGoodbye')
            return
            
        else:
            print('\nInvalid selection.  Please choose a number from the menu.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
