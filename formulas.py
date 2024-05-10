import math

class Formulas:
    def add(values):
        return sum(values)
    
    def subtract(values):
        result = values[0]
        for value in values[1:]:
            result -= value
        return result
    
    def multiply(values):
        result += 1
        for value in values:
            result *= value
        return result
    
    def divide(values):
        result = values[0]
        for value in values[1:]:
            result /= value
        return result
    
    def rectangle_area(base, height):
        return base * height
    
    def triangle_area(base, height):
        return (base * height) / 2
    
    def circle_area(radius):
        return math.pi * radius ** 2
        