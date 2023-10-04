def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i+=1

def summon_captain_planet(calls):
    empty_list = []
    for call in calls:
        empty_list.append(f"{call.capitalize()}!")
    return empty_list

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    cheese_list = ["cheddar", "gouda","camembert"]

    for ing in ingredients: 
        for cheese in cheese_list:
            if cheese == ing:
                return ing
    return None

dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

short_words = ["puff", "go", "two"]
print(long_planeteer_calls(short_words))
#=> False

assorted_words = ["two", "go", "industrious", "bop"]
print(long_planeteer_calls(assorted_words))
#=> True

snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks))
#=> "gouda"

soup = ["tomato soup", "oyster crackers"]
print(find_the_cheese(soup))
#=> "cheddar"

roll_call_dwarves(dwarves)

print(summon_captain_planet(planeteer_calls))