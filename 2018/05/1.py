import string
# can modify the list, modifications will be permanent 
def will_react(char1, char2):
    are_same_type = char1.casefold() == char2.casefold()
    are_different_parity = ((char1.islower() and char2.isupper()) or (char1.isupper() and char2.islower()))
    return are_same_type and are_different_parity

# refactor this: all reactions should happen in one function call
def reaction_cycle(polymer):
    for reaction in react_list:
        polymer = polymer.replace(reaction, '')
    return polymer

def generate_react_list():
    l = list(zip(string.ascii_lowercase, string.ascii_uppercase))
    l.extend(zip(string.ascii_uppercase, string.ascii_lowercase))
    r = []
    for t in l:
        r.append(''.join(t))
    return r

react_list = generate_react_list()
with open(r'input') as f:
    polymer = f.read()
while(True):
    prev = polymer
    polymer = reaction_cycle(polymer)
    if(len(prev) == len(polymer)):
        break
print(len(polymer))
