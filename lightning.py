class Lightning:
    def __init__(self):
        self.speed = 1100.00
        self.mile = 5280.00

    def time_mile(self, seconds):
        distance = float((self.speed * seconds) / self.mile)
        print ("You are %s miles away from the lightning strike" % distance)

lightning = Lightning()
lightning.time_mile(6.00)
