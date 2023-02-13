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

    def play(self):
        print("The guitarist does a guitar solo...")
        return self

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
        print("The drummer spins his guitar stick...")
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

musician_1.play().gesture().teach().practice().buys_equitment()
guitarist_1.play().gesture().teach().practice().buys_equitment()
bassist_1.play().gesture().teach().practice().buys_equitment()
drummer_1.play().gesture().teach().practice().buys_equitment()


musician_1.play()\
        .practice()\
        .teach()\
        .gesture()\
        .buys_equitment()