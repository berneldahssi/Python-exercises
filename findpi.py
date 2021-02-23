import random

def estimate_pi(n):
    nb_pts_circle = 0
    nb_pts_total = 0
    for i in n:
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            nb_pts_circle += 1
        nb_pts_total += 1

    return 4 * nb_pts_circle/nb_pts_total

n = 1
while(n != 0):
    n = input()
    print ("estimate_pi(", n, ")  -->  ", estimate_pi(n))    