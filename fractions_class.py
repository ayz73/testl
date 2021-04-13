class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + other_fraction.num*self.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    
    def __str__(self):
        return "%s/%s" %(self.num, self.den)

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den


f_1 = Fraction(1, 2)
f_2 = Fraction(3, 4)
f_3 = f_1 + f_2
print(f_3)