''' We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Input: n = 10, pick = 6
Output: 6

 '''

def guess(num,key):
    if(num>key):
        print("Too large")
    elif(num<key):
        print("too small")
    else:
        print("correct guess")

key=90
#num=input("guess the number ")
num=0
while(num!=key):
    num=int(input('guess the number'))
    guess(num,key)