import random

def generatePass_word(len):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    passkey = "".join(random.choice(alphabet)
        for _ in range(len))
                   
    passkey = replace_Number(passkey)
    passkey = replace_Uppercase_Letter(passkey)       
    
    return passkey

def replace_Number(passkey):
    for _ in range(random.randint(1,3)):
        replace_index = random.randint(0, len(passkey)//2 - 1)
        passkey = passkey[:replace_index] + str(random.randint(0, 9)) + passkey[replace_index + 1:]
    return passkey

def replace_Uppercase_Letter(passkey):
    for _ in range(random.randint(1,3)):
        replace_index = random.randint(len(passkey)//2, len(passkey) -1)
        passkey =passkey[0:replace_index] +passkey[replace_index].upper() +passkey[replace_index + 1:]
    return passkey


def main():   
    num_Pass = int(input("How many password do you want to generate? : "))
    
    print("Generating " +str(num_Pass)+" passwords")
    print("Minimum length of password should be 8") 
    Passwords= [generatePass_word(max(int(input(f"Enter the length of Password # {i + 1}: ")), 3))

    for i in range(num_Pass)]
    for i, passkey in enumerate(Passwords,start=1):
         print(f"Password #{i} = {passkey}")




main()
