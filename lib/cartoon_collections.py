def roll_call_dwarves(dwarf_names):
    i = 0
    for name in dwarf_names:
        i += 1
        print(f"{i}. {name}",end="\n")
        

def summon_captain_planet(planeteer_calls):
    new_planeteer_calls = list()
    for planeteer_call in planeteer_calls:
        new_planeteer_calls.append(planeteer_call.capitalize() + "!")
    return new_planeteer_calls

def long_planeteer_calls(list_of_calls):
    length_of_char = [len(call) for call in list_of_calls]
    true_or_false = list() 
    for length in length_of_char:
        if length <= 4:
            true_or_false.append(False)
        elif length > 4:
            true_or_false.append(True)
    
    if True in true_or_false:
        return True
    elif True not in true_or_false:
        return False

def find_the_cheese(list_of_strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    cheese_found = list()
    for i in list_of_strings:  
        if i in cheeses:
           cheese_found.append(i)
        
    if len(cheese_found) > 0:
        return cheese_found[0]
    elif len(cheese_found) == 0:
    	return None
            

