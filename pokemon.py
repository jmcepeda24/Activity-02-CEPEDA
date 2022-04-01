#import the random module

import random

#modifiers value
modifiers = {
    "t": 1,
    "w": 1,
    "b": 1,
    "c": random.randint(1,2),
    "r": round(random.uniform(0.85 , 1.00),2),
    "s": 1,
    "type": round(random.uniform(0.25 , 0.50),2),
}

option= random.randint(0,1)

if option ==0:
    b=0.5
elif option ==1:
    b=1
other = 1

sumModifier = 1
for x in modifiers:
    sumModifier *= modifiers[x]

level = 90
power = 110
a = 205
d = 188

damage = ((((((2*level)/5)+2)*power*(a/5))/50)+2)* float(sumModifier)

print(damage)