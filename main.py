#finding the value of pi upto nth digit
p = int(input("Insert the number of digits you want to see of Pi : \n"))
i = 0
a = 2
b = 3
c = 4
pi = 4/(a*b*c)
pi_str = []
while i<10000:
    a = -1*c
    if a < 0:
        b = a-1
        c = a-2
    else:
        b = a+1
        c = a+2
    x = 4/(a*b*c)
    pi = x+pi
    i+=1
z = str(pi)
for u in range(2, (p+2)):
    int(u)
    pi_str.append(z[u])
print("\n \n The digit is : \n 3.", end="")
print("".join(map(str, pi_str)))
print("\n \n Note : This is calculated by Nilakantha Series upto 1000 so it can be a little inaccurate ")
input()