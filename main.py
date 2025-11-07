import random
import math


ROAD    = '.'
WALL    = '#'
PLAYER  = 'O'


class Player:
    health: int = 3
    experience: int = 0
    coordinates = {
        "x": -1,
        "y": -1
    }

    def get_health(self):
        return self.health

    def gain_health(self, health):
        self.health += health

    def take_damage(self, dmg: int):
        self.health -= dmg
    
    def get_experience(self, exp: int):
        self.experience += exp


class Game:
    player: Player = Player()
    field: list = [[]]
    field_items: set = {}
    message: str = ""
    health_change: str = ""
    experience_change: str = ""
    step: int = 0
    """
    Field is NxM sized.
    Field has AT LEAST 2 roads.
    Every time the field will be different.
    
    The field will contain some rectangle roads that can intersect
    each other, e.g.:
    ____________________
    . . . X X X X . . . | . - no road to move
    . X X X . . X . . . | X - road for player
    . X . X . . X . . . |
    . X . X X X X . . . |
    . X X X . . . . . . |

    Of course, we make upper bound of roads amount and road cells.
    Let it be cells to move LESS than (n*m / 2) - all cells
    """
    def generate_field(self, field_width: int, field_height: int):
        self.field_items = [['' for x in range(field_width)] for y in range(field_height)]  
        gen_field: list = [[WALL for x in range(field_width)] for y in range(field_height)]        
        free_cells_amount: int = math.floor(field_height * field_width / 2)
        free_cells: list = []

        potions = math.floor(free_cells_amount / 15)
        monsters = math.floor(free_cells_amount / 10)

        while (free_cells_amount > 0):
            lt_corner_y = random.randint(0, field_height-3)
            lt_corner_x = random.randint(0, field_width-3)
            if (self.player.coordinates['x'] == -1):
                self.player.coordinates['x'] = lt_corner_x
                self.player.coordinates['y'] = lt_corner_y
            width = random.randint(3, field_width - lt_corner_x)
            height = random.randint(3, field_height - lt_corner_y)
            for i in range(lt_corner_y, lt_corner_y + height - 1):
                gen_field[i][lt_corner_x] = ROAD
                free_cells.append({
                    'x': lt_corner_x,
                    'y': i 
                })
                gen_field[i][lt_corner_x + width - 1] = ROAD
                free_cells.append({
                    'x': lt_corner_x + width - 1,
                    'y': i 
                })
            for j in range(lt_corner_x, lt_corner_x + width - 1):
                gen_field[lt_corner_y][j] = ROAD
                free_cells.append({
                    'x': j,
                    'y': lt_corner_y
                })
                gen_field[lt_corner_y + height - 1][j] = ROAD
                free_cells.append({
                    'x': j,
                    'y': lt_corner_y + height - 1
                })
            free_cells_amount -= width * height

        gen_field[self.player.coordinates['y']][self.player.coordinates['x']] = PLAYER
        self.field = gen_field

        win_cell = random.choice(free_cells)
        self.field_items[win_cell['y']][win_cell['x']] = 'Win'
        free_cells.remove(win_cell)
        while (potions > 0):
            cell = random.choice(free_cells)
            self.field_items[cell['y']][cell['x']] = 'Potion'
            free_cells.remove(cell)
            potions -= 1
        while (monsters > 0):
            cell = random.choice(free_cells)
            self.field_items[cell['y']][cell['x']] = 'Monster'
            free_cells.remove(cell)
            monsters -= 1

    def __init__(self):
        self.generate_field(30, 10)
        while (True):
            self.show_stage()
            move = input()
            self.step += 1
            coordinates = {
                'x': self.player.coordinates['x'],
                'y': self.player.coordinates['y']
            }

            if (move == 'a'): 
                coordinates['x'] -= 1
            if (move == 'd'):
                coordinates['x'] += 1
            if (move == 'w'):
                coordinates['y'] -= 1
            if (move == 's'):
                coordinates['y'] += 1

            if (0 <= coordinates['x'] < len(self.field[0]) and 
                0 <= coordinates['y'] < len(self.field) and 
                self.field[coordinates['y']][coordinates['x']] != WALL):
                self.place_player(coordinates)
                if (self.field_items[coordinates['y']][coordinates['x']] == "Monster"):
                    self.player.take_damage(1)
                    self.player.get_experience(100)
                    self.message = "THE MONSTER!!!"
                    self.health_change = "(-1)"
                    self.experience_change = "(+100)"
                if (self.field_items[coordinates['y']][coordinates['x']] == "Potion"):
                    self.player.gain_health(1)
                    self.message = "Potion."
                    self.health_change = "(+1)"
                if (self.field_items[coordinates['y']][coordinates['x']] == "Win"):
                    print("You won, bye!")
                    break
                self.field_items[coordinates['y']][coordinates['x']] = ''
            else:
                self.player.take_damage(1)
                self.message = "THE WALL!!!"
                self.health_change = "(-1)"

            if (self.player.get_health() <= 0):
                print("YOU DIED")
                break

            if (move == "EXIT"):
                break

    def place_player(self, coordinates: list):
        self.field[self.player.coordinates['y']][self.player.coordinates['x']] = ROAD
        self.field[coordinates['y']][coordinates['x']] = PLAYER
        self.player.coordinates = coordinates

    def show_stage(self):
        print('Print EXIT to end the game')
        print(WALL * (len(self.field[0]) + 2))
        for i in range(len(self.field)):
            info: str = ""
            if (i == 1):
                info = f"Experience: {self.player.experience} " + self.experience_change 
            if (i == 2):
                info = f"Health:     {self.player.health} " + self.health_change
            if (i == 3):
                info = f"Step:       {self.step}"
            if (i == len(self.field) - 5):
                info = 'a - Move Left'
            if (i == len(self.field) - 4):
                info = 'd - Move Right' 
            if (i == len(self.field) - 3):
                info = 'w - Move Top'
            if (i == len(self.field) - 2):
                info = 's - Move Bottom'
            if (i == len(self.field) - 1):
                info = self.message
            print(WALL + ''.join(self.field[i]) + WALL + ' ' * 5 + info)
        print(WALL * (len(self.field[0]) + 2) + '\n')
        self.message = ""
        self.health_change = ""
        self.experience_change = ""

game = Game()




    
