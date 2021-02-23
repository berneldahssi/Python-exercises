import random

code = list()
code_tried = list()
nb_attempts = 0

for i in range(4):
    x = random.randint(1,8)
    while x in code:
        x = random.randint(1,8)
    code.append(x)

while (code_tried != code):
    code_tried = list()
    correspondance = list()
    misplaced_digits = list()
    for i in range(4):
        y = int(input("Enter the #{} code's digit : ".format(i+1)))
        while y in code_tried:
            y = int(input("Enter the #{} code's digit : ".format(i+1)))
        code_tried.append(y)
        if code_tried[i] == code[i]:
            correspondance.append(code[i])
        else:
            correspondance.append("X")
            if code_tried[i] in code:
                misplaced_digits.append(code_tried[i])
    print(correspondance)
    print("Misplaced Digits : {}\n".format(misplaced_digits))
    nb_attempts += 1
print("You win after {} attempts".format(nb_attempts))