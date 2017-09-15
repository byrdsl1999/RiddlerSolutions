import numpy as np

'''
    If you break a stick in two places at random, forming three pieces, what is the probability of being able to form a triangle with the pieces?
    If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form a triangle with them?
    If you break a stick in two places at random, what is the probability of being able to form an acute triangle — where each angle is less than 90 degrees — with the pieces?
    If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form an acute triangle with the sticks?
'''

def break_stick():
    #Returns an array of 3 positive numbers, of random size which sum to one.
    breaks = np.random.uniform(size=2)
    pieces=[]
    pieces.append(breaks.min()) #left piece 
    pieces.append(1-breaks.max()) #right piece
    pieces.append(1-breaks.min()-(1-breaks.max())) #middle piece
    return pieces

def pick_sticks():
    #Returns an array of three numbers, each uniformly random between 0 and 1.
    pieces = np.random.uniform(size=3)
    return pieces

def forms_triangle(sides):
    #Takes an array of three numbers then returns True if they can form a triangle, and False if not.
    if sides[0] + sides[1] < sides[2]:
        return False
    if sides[0] + sides[2] < sides[1]:
        return False
    if sides[1] + sides[2] < sides[0]:
        return False
    return True

def forms_acute_triangle(sides):
    #Takes an array of three numbers then returns True if they can form an accute triangle, and False if not.
    if not forms_triangle(sides):
        return False
    side_c=max(sides)
    side_a=min(sides)
    side_b=np.median(sides)
    right_side=(side_a**2+side_b**2)**.5
    if right_side > side_c:
        return True
    else:
        return False

def run_sims(stick_funct, triangle_funct, sim_count=1000000):
    successes=0
    for _ in range(sim_count):
        if triangle_funct(stick_funct()):
            successes += 1
    return (1.0* successes)/sim_count


def main():
    print 'Three broken sticks form a triangle with prob:'
    print run_sims(break_stick, forms_triangle)
    print 'Three random sticks form a triangle with prob:'
    print run_sims(pick_sticks, forms_triangle)
    print 'Three broken sticks form an accute triangle with prob:'
    print run_sims(break_stick, forms_acute_triangle)
    print 'Three random sticks form an accute triangle with prob:'
    print run_sims(pick_sticks, forms_acute_triangle)

if __name__ == '__main__':
    main()



