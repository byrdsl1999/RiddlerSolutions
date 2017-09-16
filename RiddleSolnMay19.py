'''
Solution for: http://fivethirtyeight.com/features/the-battle-for-riddler-nation-round-2/

Four co-workers carpool to work each day. A driver is selected randomly for the
 drive to work and again randomly for the drive home. Each of the drivers has a
lead foot, and each has a chance of being ticketed for speeding. Driver A has
a 10 percent chance of getting a ticket each time he drives, Driver B a 15
percent chance, Driver C a 20 percent chance, and Driver D a 25 percent chance. 
The state will immediately revoke the license of a driver after his or her third 
ticket, and a driver will stop driving in the carpool once his license is revoked.
 Since there is only one police officer on the carpool route, a maximum of one ticket
  will be issued per morning and a max of one per evening.

Assuming that all four drivers start with no tickets, how many days can we expect
 the carpool to last until all the drivers have lost their licenses?

'''

import numpy as np

class driver(object):
    def __init__(self, prob=.2):
        self.prob_of_tick = prob
        self.strikes = 0
    
    def add_strike(self):
        self.strikes+=1
    
    def drive(self):
        if np.random.uniform() < self.prob_of_tick:
            self.add_strike()


def check_for_legal_driver(carpool):
    for person in carpool:
        if person.strikes < 3:
            return True
    return False


def day(carpool):
    
    if check_for_legal_driver(carpool):
        morning_driver = np.random.choice(carpool)
        while morning_driver.strikes >= 3:
            morning_driver = np.random.choice(carpool)
        morning_driver.drive()
    else:
        return False
    
    if check_for_legal_driver(carpool):
        evening_driver = np.random.choice(carpool)
        while evening_driver.strikes >= 3:
            evening_driver = np.random.choice(carpool)
        evening_driver.drive()
    else:
        return False
    
    return True

def run_test(carpool):
    count = 0
    while day(carpool):
        count+=1
    return count

results=[]
for _ in range(5000):
    carpool_1=[driver(.1),driver(.15),driver(.2),driver(.25)]
    results.append(run_test(carpool_1))

print(np.mean(results))
