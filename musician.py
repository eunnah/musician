class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boom", "Tap", "Crash"])
        
    def combust(self):
        print("Combusting. Spontaneously.")
        
    def counttofour(self):
        print("One. Two. Three. Four.")
        
class Band(object):
    members = []
    
    def hire(musician):
        members.append(musician)
        print(str(musician) + " is now hired.")
    
    def fire(musician):
        if musician in members:
            list.remove(musician)
            print(str(musician) + " is now fired.")
    
    def playsolos():
        if any(isinstance(x, Drummer) for x in list_of_stuff):
            x.counttofour()
        for member in members:
            member.solo(4)