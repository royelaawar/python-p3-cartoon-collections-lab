def roll_call_dwarves(dwarf_list):
    
    i = 1
    for name in dwarf_list:
        print(f'{i}. {name}')
        i += 1

def summon_captain_planet(planeteer_calls):
    return[f'{call.title()}!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
    
CHEESE = ["cheddar", "gouda", "camembert"]

def find_the_cheese(foods):

    for food in foods:
        if food in CHEESE:
            return food
    return None
    
