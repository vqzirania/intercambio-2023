### IMPORTANT ###
# THIS FILE CREATES THE PAIRINGS FOR SECRET SANTA!

import copy
import random
import json

# PARTICIPANTS
# Same as original
fams = [
        ["IRANIA", "JHOVANNA", "DOMINGO", "GUADALUPE"],
        ["MARIA", "CHRISTIAN"],
        ["OSCAR", "JASMIN", "AXEL", "ANTHONY"],
        ["MARICELA", "PATO", "LENNY","VANESSA","ISABELLA"],
        ["ALEJANDRA VAZQUEZ","JUAN","JOHANNA","YARE", "JAYLIN"],
        ["PEPE", "JESSICA", "MATEO","JIROSHI","MAX"],
        ["OLIVIA","FREDDY","FRIDA","KENDRA"],
        ["ALEJANDRA MENDEZ","TITO","DAVID"],
        ["MAMA CHUCHA","PAPA GERARDO"],
        ["TONIO"]
        
        ]
names = sum(fams, []) # makes one list from lists of lists

# CREATING PAIRINGS DEFINITION
def secret_santa(names):
    my_list = fams
    choose = copy.copy(names) 
    
    # my_list = names
    # choose = copy.copy(my_list) # copy.deepcopy() for classes
    
    result = {}
    for fam in my_list:
        # print("this is fam", fam)
        names = copy.copy(my_list)
        
        # print('this is the original names:', names)
        names.pop(names.index(fam)) # Removes a person from choosing themself # With Fam, removes the whole fam from being selected by one another
        names = sum(names,[]) # Removing lists from lists
        # print('names after pop:', names)
        for person in fam:
            # print(person)
            chosen = random.choice(list(set(choose)&set(names)))
            # print(list(set(choose)&set(names)))
            result[person] = chosen
            choose.pop(choose.index(chosen))
    return result

# GETTING THE PAIRS
for i in range(10):  # try 10 times
    try:
        # getting the secret santa names
        ss_result = secret_santa(names)
        # print('results:', ss_result)
        break # as soon as it works, break out of the loop
    
    # Handling our index error, where we run out of ppl from a different fam
    # Note: when plugging in fam names:
    # Place larger families first!
    except IndexError:
        continue # means try again

with open("pairs.json", "w") as pairings:
    json.dump(ss_result, pairings)

# Making a Backup file
with open("backuppairs.json", "w") as pairings:
    json.dump(ss_result, pairings)
