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
    def __init__(self):
        self.members = []
    
    def hire(self, musician):
        self.members.append(musician)
        print(str(musician) + " is now hired.")
    
    def fire(self, musician):
        if musician in self.members:
            self.members.remove(musician)
            print(str(musician) + " is now fired.")
    
    def playsolos(self):
        for member in self.members:
            #STUDY isinstance function
            if isinstance(member, Drummer):
                member.counttofour()
        for member in self.members:
            member.solo(4)
            
if __name__ == '__main__':
    band = Band()
    bob = Drummer()
    band.hire(bob)
    jack = Bassist()
    joe = Guitarist()
    band.hire(jack)
    band.hire(joe)
    band.playsolos()
    band.fire(bob)
    