
from pylab import randn
from random import randint

age = [x for x in range(100)]

time_spent = []
for x in range(100):
    time_spent.append(randint(0,x))

print(time_spent)

plt.scatter(age, time_spent)
