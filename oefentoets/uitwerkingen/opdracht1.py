# Convert a length and diameter given in centimeter to inches
import math

price_list = (0.1 , 0.25 , 0.5 , 0.8 , 1.05 , 1.5 , 2.0 , 2.5 , 3.1 , 3.7)

def cm_to_inch(input_cm):
    # 1" = 2.54cm cms/2.54 = inches
    return math.ceil(input_cm/2.54)

def inch_to_cm(input_inch):
    return math.ceil(input_inch*2.54)

def calc_cost_pipe(inch_length , inch_diameter):
    # get price bij diameter from price_list
    # price_list is per diameter inch (1", 2", 3", 4", etc)
    # price = price_list(inch_diameter) * inch_length
    if inch_diameter >= len(price_list):
        print("error: price can not be found in list")
        return None
    return price_list[round(inch_diameter, 0)] * inch_length

def main():
    pipe_length = int(input("Pipe length in cms:"))
    pipe_diameter = int(input("Pipe diameter in cms:[0-22]"))
    pipe_length = cm_to_inch(pipe_length)
    pipe_diameter = cm_to_inch(pipe_diameter)
    pipe_cost = calc_cost_pipe(pipe_length, pipe_diameter)
    print("Pipe length and diameter in inch:", pipe_length, ",", pipe_diameter)
    print("This pipe would cost you: ", pipe_cost)

main()
assert cm_to_inch(254) == 100
assert calc_cost_pipe(10, 2) == 5 # 10 * 0.5
