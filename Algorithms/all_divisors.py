a = int(input('Input a number: '))

def divisorGen(num):
    for i in range(1, int(num/2+1)):
        if num%i == 0:
            yield i
    yield num

for i in divisorGen(a):
    print(i)