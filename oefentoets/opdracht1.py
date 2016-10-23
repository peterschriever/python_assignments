# Convert a length and diameter given in centimeter to inches
import math

price_list = (0.1 , 0.25 , 0.5 , 0.8 , 1.05 , 1.5 , 2.0 , 2.5 , 3.1 , 3.7)

def cm_to_inch(input_cm):
    input_to_inch = math.ceil(input_cm/2.54)
    return input_to_inch

def calc_cost_pipe(inch_length , inch_diameter):
    return inch_length * price_list[inch_diameter-1]

def main():
    length = float(input("Enter pipe length in cm: "))
    diameter = float(input("Enter pipe diameter in cm (max. 25 cm): "))
    costs = calc_cost_pipe(cm_to_inch(length),cm_to_inch(diameter))
    print('The pipe with l=%dcm,d=%dcm will be converted to:  l=%d\",d=%d\"'
          % (length, diameter, cm_to_inch(length),cm_to_inch(diameter)))
    print('The costs of the pipe are: €',costs)

main()

assert cm_to_inch(254)==100 , 'Error : Faulty calculation'
assert calc_cost_pipe(100,cm_to_inch(25)), 'Error: D<25cm!!'
