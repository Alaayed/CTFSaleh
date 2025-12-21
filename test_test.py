import random as r
value = 10
sum = 0
for i in range(100000):
    
    coin_toss = r.randint(0,1)
    if coin_toss == 0:
        sum += value * 0.5
    else:
        sum += value * 2
avg = sum / 100000
print(f'Precentage change: {avg/value * 100}%')    