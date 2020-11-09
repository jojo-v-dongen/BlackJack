import pydealer
import random
deck = pydealer.Deck(rebuild=True, re_shuffle=True)
deck.shuffle(99)

def check_values(n):
    if n[0].value in ["King", "Queen", "Jack"]:
        n[0].value = 10
    elif n[0].value in ["Ace"]:
        n[0].value = 11

    try:
        if n[1].value in ["King", "Queen", "Jack"]:
            n[1].value = 10
        elif n[1].value in ["Ace"]:
            n[1].value = 11
    except IndexError:
        pass
    

def give_cards():
    global uc, bc, valuc, valbc
    uc = deck.deal(2)
    bc = deck.deal(2)
    print("\nYour cards:")
    print(uc)
    try:
        valuc = int(uc[0].value) + int(uc[1].value)
    except ValueError:
        check_values(uc)

    try:
        valuc = int(bc[0].value) + int(bc[1].value)
    except ValueError:
        check_values(bc)
    
    valuc = int(uc[0].value) + int(uc[1].value)
    valbc = int(bc[0].value) + int(bc[1].value)
    print("Total: " + str(valuc))
    game()


def add_values_uc(n):
    global valuc
    valuc = 0
    j = 0
    for i in n:
        valuc = valuc + int(n[j].value)
        j+=1

def add_values_bc(n):
    global valbc
    valbc = 0
    j = 0
    for i in n:
        valbc = valbc + int(n[j].value)
        j+=1
    
def game():
    global valucc
    if valuc == 21:
        print("\n\nYou won!")
        print("\n##################################################\n")
    elif valbc == 21:
        print("\n\nThe bank won, it had 21\n\ncards of the bank:\n"+ str(bc))
        print("\n##################################################\n")
    else:
        while True:
            extracard = input("Would you like another card? (y/n)\n-->").lower()
            if extracard == "y":
                ec = deck.deal()
                uc.add(ec)
                print("\nYour new cards\n" + str(uc))
                check_values(ec)
                add_values_uc(uc)
                if valuc > 21:
                    check_for_ace(uc)
                    add_values_uc(uc)
                print("Total: " + str(valuc))
                
                if valuc == 21:
                    print("\n\nYou got 21, you won!")
                    print("\n##################################################\n")
                    break
                if valuc > 21:
                    print("\n\nTotal is over 21, you lost")
                    print("\n##################################################\n")
                    break
                
            elif extracard == "n":
                valucc = valuc
                bank_plays()
                break
            
            else:
                print("invalid answer! Answer with 'y' or 'n'")
    

def check_value_limit_bc(value):
    global overlimit_bc
    overlimit_bc = False
    
    if value > 21:
        print("\n\nBank went over 21, you won")
        print("Bank's total: "+str(value))
        print("\n##################################################\n")
        overlimit_bc = True
        

def bank_plays():
    global valucc
    x = 0
    while True:
        if valbc < 16:
            ec = deck.deal()
            bc.add(ec)
            check_values(ec)
            add_values_bc(bc)
            check_value_limit_bc(valbc)
            if overlimit_bc == True:
                break

        elif valbc == 16 or valbc == 17:
            r = random.choice([True, False])
            
            if r == True and x == 0:
                x = 1
                ec = deck.deal()
                bc.add(ec)
                check_values(ec)
                add_values_bc(bc)
                check_value_limit_bc(valbc)
                if overlimit_bc == True:
                    break
                

            else:
                x = 1
                pass
        else:
            if valucc > valbc:
                won = 'You'
            else:
                won = 'The bank'
            print("\nYou have {} points\nBank has {} points".format(valuc, valbc))
            print(won, "won!")
            print("\n##################################################\n")
            break

def check_for_ace(cards):
    j = 0
    for i in cards:
        if i.value == "Ace":
            i.value = 1
        elif i.value == 11:
            i.value = 1
        j+=1
    

print('''
I assume you know what blackjack is with it's rules.
The rules in this code are the same as in blacjack however it is not possible to split (yet)
If you have an Ace it will automatically count as 11, unless you go over 21 it will count as an 1
All the other cards without number such as King, Queen and Jack are worth 10
Good luck and have fun!
''')


give_cards()
while True:
    ask = input('\nWant to continue playing? (y/n)\n-->').lower()
    if ask == "y":
        give_cards()
    elif ask == "n":
        break
    else:
        print("Invalid answer, answer 'y' or 'n'")
print("\nThanks for playing\nGoodbye")
