import random  
def game():
     
    n = random.randint(1,108)
    play = 0
    while play < 8:
        guess = int(input("Enter Guess: "))

        if(guess < n):
            print("LOW!")
        if(guess > n):
            print("HIGH!")
        if(guess == n):

            print(f"GOOD JOB,you choose correct guess {n}")
            break
        play += 1
        if play == 8:
            print(f"GAME OVER,{n}is correct answer")   
    
game()