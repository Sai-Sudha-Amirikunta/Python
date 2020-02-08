
#Question

'''Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. 
After each, the program should tell them whether they got it right or wrong and what the correct answer is and finally it should display 
the total score out of 10 scored by user.'''


import random 

score = []
for i in range(1,11):
    n = random.randrange(1,21)
    a = random.randrange(1,21)
    m=n*a
    print(n,'*',a,'=')
    b = int(input('enter the answer:'))
    
    if b==m:
        print('Right!')
        score.append(b)
    else:
        print('Wrong. The answer is:',m)
    print()
    
    
print('Your Score is:',len(score),'out of 10')
