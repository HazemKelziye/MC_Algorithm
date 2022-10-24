import math


def lvl(a):
    """ This method acts as a half-ceiling for the floating points
        so that we can easily derive multiples of halves """
    if 0 < a < 0.5:
        return 0.5
    elif 0.500 < a <= 1.000:
        return 1.0
    elif 1.000 < a <= 1.500:
        return 1.5
    elif 1.500 < a <= 2.000:
        return 2.0
    elif 2.000 < a <= 2.500:
        return 2.5
    elif 2.500 < a <= 3.000:
        return 3.0
    elif 3.000 < a <= 3.500:
        return 3.5
    elif 3.500 < a <= 4.000:
        return 4.0
    elif 4.000 < a <= 4.500:
        return 4.5
    elif 4.500 < a <= 5.000:
        return 5.0
    elif 5.000 < a <= 5.500:
        return 5.5
    elif 5.500 < a <= 6.000:
        return 6.0
    elif 6.000 < a <= 6.500:
        return 6.5
    elif 7.000 < a <= 7.500:
        return 7.5
    elif 7.500 < a <= 8.000:
        return 8.0
    elif 8.000 < a <= 8.500:
        return 8.5
    elif 8.500 < a <= 9.000:
        return 9.0
    elif 9.000 < a <= 9.500:
        return 9.5
    elif 9.500 < a <= 10.000:
        return 10.0
    elif 10.000 < a <= 10.500:
        return 10.5
    elif 10.500 < a <= 11.000:
        return 11.0
    elif 11.000 < a <= 11.500:
        return 11.5
    elif 11.500 < a <= 12.000:
        return 12.0
    elif 12.000 < a <= 12.500:
        return 12.5
    elif 12.500 < a <= 13.000:
        return 13.0
    elif 13.000 < a <= 13.500:
        return 13.5
    elif 13.500 < a <= 14.000:
        return 14.0
    elif 14.000 < a <= 14.500:
        return 14.5
    elif 14.500 < a <= 15.000:
        return 15.0
    elif 15.000 < a <= 15.500:
        return 15.500
    elif 15.500 < a <= 16.000:
        return 16.0
    elif 16.000 < a <= 16.500:
        return 16.5
    elif 16.500 < a <= 17.000:
        return 17.0
    elif 17.000 < a <= 17.500:
        return 17.5
    elif 17.500 < a <= 18.000:
        return 18.0
    elif 18.000 < a <= 18.500:
        return 18.5
    elif 18.500 < a <= 19.000:
        return 19.0
    else:
        return None


def factors(number):
    """Getting the factors of a number, by dividing it by all the numbers till
    it gets to its value"""
    arr = list()
    for i in range(2, number):
        if number % i == 0:
            arr.append(i)
    return arr


class MarkerCombination:
    """MC class is used to generate marker combination based on the given size distribution"""

    def __init__(self, dic, percentage, fabric, cut):
        """"Property of a given article's cutting number"""

        self.dic = dic
        self.fabric = fabric.lower()
        self.cut = cut.lower()
        self.percentage = percentage
        self.commonM = list()
        self.ply_number = None
        self.marker_number = None
        self.sigma = dict()
        self.lamda = dict()
        self.sigmaKeys = None
        self.sigmaValues = None
        self.lamdaKeys = None
        self.lamdaValues = None
        self.d = dict()
        self.dKeys = list()
        self.dValues = list()
        self.gamma = dict()
        self.gammaKeys = list()
        self.gammaValues = list()
        delete = list()

        # Error handling a non-natural number in the Size Distribution
        for value in dic.values():
            if value < 0:
                raise ValueError('Cutting numbers must be a Natural Number ')

        # Deleting the vacant numbers in the distribution (i.e. lambda == 0)
        for key, value in dic.items():
            if value == 0:
                delete.append(key)
        for i in delete:
            del dic[i]
        # end

        self.cutting_sum = sum(self.dic.values())
        # specifying the ply limit according to the fabric type & cutting method
        if self.cut == "cutter":
            if self.fabric == "alpha fleece brushed":
                self.ply_limit = 36
            elif self.fabric == "alpha fleece not brushed":
                self.ply_limit = 50
            elif self.fabric == "strauss fleece brushed":
                self.ply_limit = 36
            elif self.fabric == "single cotton":
                self.ply_limit = 105
            elif self.fabric == "single lycra":
                self.ply_limit = 80
            elif self.fabric == "versace fleece brushed":
                self.ply_limit = 40
            elif self.fabric == "versace fleece not brushed":
                self.ply_limit = 55
            elif self.fabric == "love moschino fleece not brushed":
                self.ply_limit = 60
            elif self.fabric == "fleece carbon brush":
                self.ply_limit = 40
            elif self.fabric == "pique cotton":
                self.ply_limit = 40
            else:
                raise ValueError("No such a fabric type")
        elif self.cut == "manual":
            if self.fabric == "alpha fleece brushed":
                self.ply_limit = 70
            elif self.fabric == "alpha fleece not brushed":
                self.ply_limit = 85
            elif self.fabric == "strauss fleece brushed":
                self.ply_limit = 90
            elif self.fabric == "single cotton":
                self.ply_limit = 200
            elif self.fabric == "single lycra":
                self.ply_limit = 175
            elif self.fabric == "versace fleece brushed":
                self.ply_limit = 60
            elif self.fabric == "versace fleece not brushed":
                self.ply_limit = 75
            elif self.fabric == "love moschino fleece not brushed":
                self.ply_limit = 80
            elif self.fabric == "fleece carbon brush":
                self.ply_limit = 60
            elif self.fabric == "pique cotton":
                self.ply_limit = 100
            else:
                raise ValueError("No such a fabric type")
        else:
            raise ValueError("There is no such a cutting method")

    def calc_ply(self):
        #  from here on this calculates the possible ply according to the given parameters
        temp1 = list()
        temp2 = list()
        y_add = math.ceil(self.cutting_sum * (1 + self.percentage / 100))
        for j in range((y_add - self.cutting_sum) + 1):
            temp1.append(factors(self.cutting_sum + j))
        for q in temp1:  # for putting them all in one list
            temp2 += q

        fltr = temp2[:]

        for b in temp2:
            if b > self.ply_limit:
                fltr.remove(b)

        res = [*set(fltr)]
        self.commonM = sorted(res)
        # end

        self.ply_number = self.commonM[-1]

    def upgraded_cutting_sum(self):
        self.marker_number = self.cutting_sum/self.ply_number
        cutting2 = lvl(self.cutting_sum / self.ply_number)
        self.cutting_sum = (cutting2 * self.ply_number)

    def mc_algorithm(self):
        self.sigma = self.dic.copy()
        self.lamda = self.dic.copy()
        for key, value in self.sigma.items():
            self.sigma[key] = value/sum(self.dic.values())
            self.lamda[key] = self.marker_number * self.sigma[key]
        self.sigmaKeys = list(self.sigma)
        self.sigmaValues = list(self.sigma.values())
        self.lamdaKeys = list(self.lamda)
        self.lamdaValues = list(self.lamda.values())

        self.dValues.append(lvl(self.lamdaValues[-1]))
        self.gammaValues.append((self.dValues[0] - self.lamdaValues[-1]))

        for i in reversed(range(len(self.sigmaKeys) - 1)):
            if self.gammaValues[-1] > self.lamdaValues[i]:
                self.dValues.append(lvl(float(self.gammaValues[-1])))
            else:
                self.dValues.append(lvl(round(float(self.lamdaValues[i]), 5) - round(float(self.gammaValues[-1]), 5)))
            self.gammaValues.append(self.gammaValues[-1] + self.dValues[-1] - self.lamdaValues[i])

        self.dValues = list(reversed(self.dValues))





dist = {'XXS': 0, 'XS': 0, 'S': 74, 'M': 156, 'L': 154, 'XL': 116, 'XXL': 61, '3XL': 11, '4XL': 0, '5XL': 0}
trial = MarkerCombination(dist, 0.5, "alpha fleece brushed", "manual")
trial.calc_ply()
trial.upgraded_cutting_sum()
trial.mc_algorithm()
print(trial)
print(trial.dic)
print(trial.sigma)
print("lamdaValues", trial.lamdaValues)
print("dValues", trial.dValues)
print("sum of dValues", sum(trial.dValues))
print("Marker number", trial.marker_number)
print("gammaValues", trial.gammaValues)
print("length", len(trial.sigmaKeys))
