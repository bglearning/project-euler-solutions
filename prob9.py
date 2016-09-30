#Problem 9
#Special Pythagorean Triplets
#a+b+c=1000 and a^2+b^2 = c^2. Find abc.

done = False
for c in range(333,501):
    if done: break
    for a in range(1,500):
        b = 1000 -c -a
        if a**2+b**2 == c**2:
            print('{},{},{}'.format(a,b,c))
            print(a*b*c)
            done = True
            break
