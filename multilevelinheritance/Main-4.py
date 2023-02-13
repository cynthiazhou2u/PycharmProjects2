class Musician:

    def play(self):
        print("The musician plays music...")
        return self

    def gesture(self):
        print("The musician takes a bow in front of the audience...")
        return self

    def practice(self):
        print("The musician practices his music...")
        return self

    def teach(self):
        print("The musician teaches his music...")
        return self

    def buys_equitment(self):
        print("The musician buys new musical equipment...")
        return self


class Guitarist(Musician):

    def play(self):                           # method overriding
        print("The guitarist does a guitar solo...")
        return self                     # need to return self for method chaining

    def gesture(self):
        print("The guitarist dives into the crowd...")
        return self


class Bassist(Musician):

    def play(self):
        print("The bassist slaps his bass...")
        return self

    def gesture(self):
        print("The bassist is headbanging...")
        return self


class Drummer(Musician):

    def play(self):
        print("The drummer smashes his drums to the beat...")
        return self

    def gesture(self):
        print("The drummer spins his drum stick...")
        return self


musician_1 = Musician()
guitarist_1 = Guitarist()
bassist_1 = Bassist()
drummer_1 = Drummer()

musician_1.play()
musician_1.gesture()

guitarist_1.play()
guitarist_1.gesture()

bassist_1.play()
bassist_1.gesture()

drummer_1.play()
drummer_1.gesture()

print( '\nchaining musician  ===\n')
musician_1.play().gesture().teach().practice().buys_equitment()       #method chaining
print( '\nchaining guitarist ===\n')
guitarist_1.play().gesture().teach().practice().buys_equitment()
print( '\nchaining bassist ===\n')
bassist_1.play().gesture().teach().practice().buys_equitment()
print( '\nchaining dummer ===\n')
drummer_1.play().gesture().teach().practice().buys_equitment()

print( '\nchaining musician again ===\n')
musician_1.play()\                    #line continues by \
        .practice()\
        .teach()\
        .gesture()\
        .buys_equitment()