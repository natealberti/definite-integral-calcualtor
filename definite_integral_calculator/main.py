import numpy as np
from Equation import Expression
from tqdm import tqdm

class Integrate:
    # constructor to represent the integral object
    def __init__(self, function):
        # instance variables
        self.function = function
        self.sign = 1

    # performs the integration algorithm
    # uses midpoint method
    def calculate(self, lower, upper, precision=10000):
        total_area = 0

        # if the limit of integration are backwards, they are...
        # swapped and the sign is changed
        if lower > upper:
            lower, upper = upper, lower
            self.sign *= -1

        # list of equally separated points bounded by upper and lower
        # used to create the rectangles
        num_of_points = int((upper - lower) * precision)
        point_list = np.linspace(lower, upper, num=num_of_points, endpoint=True)
        # width of every rectangle can be defined as the width...
        # between the first and second points in the list
        width = point_list[1] - point_list[0]

        # calculating the area of each rectangle width*height
        # adding that area to the accumulator total_area
        for index in tqdm(range(num_of_points - 1)):
            x1 = point_list[index]
            x2 = point_list[index+1]
            midpoint = (x1 + x2) / 2
            height = self.function(midpoint)
            current_area = width*height
            total_area += current_area

        return total_area

if __name__ == '__main__':
    # the equation for the integrand
    # x has to be the variable
    integrand_input = input('integrand: ')
    integrand = Expression(integrand_input, ['x'])

    # limits of integration
    lower = int(input('lower limit of integration: '))
    upper = int(input('upper limit of integration: '))

    # integral object
    integral = Integrate(integrand)
    # results
    result = integral.calculate(lower, upper)
    print('result: ' + str(result))