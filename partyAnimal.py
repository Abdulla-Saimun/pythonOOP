class partiAnimal:
    x=0

    def party(self):
        self.x=self.x+1
        print('so farr ', self.x )


an=partiAnimal()
an.party()
an.party()
an.party()
partiAnimal.party(an)