import random 

MYroll = random.randint(1, 6)
CPUroll = random.randint(1, 6)

print("You rolled a", MYroll)
print("The compuer rolled a", CPUroll)

if MYroll == CPUroll:
    print("You tied!")
    
if MYroll >= CPUroll:
    print("You win!")

if MYroll <= CPUroll:
    print("Computer wins!")


