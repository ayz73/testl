# gives greatest common factor for two values
def gcf(x, y):
    if x == 0 or y == 0:
        return 0

    # use uclid's algorithm to find gcf
    r = x % y
    while r:
        x = y
        y = r
        r = x % y
    return y

class Fraction():

    def __init__(self, num, den):
        self.num = int(num / gcf(num, den))
        self.den = int(den / gcf(num, den))

    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + other_fraction.num*self.den
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __str__(self):
        return "%s/%s" %(self.num, self.den)

    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
