#small private key to the power of the private key mod the big number range
#there are two modes one is for testing and i would recommend acutally using it that is option 1
#the more than two people function has not been made yet
def encrypt(user_p, LP):
    # user_p is the users private key that they have
    # SP is the small prime number that notebook
    # BR Big.Number.Range.Private.Key
    BNRPK = LP[0]
    SP = LP[1]
    return (int((SP**user_p) % BNRPK))


def encrypt_2ppl():
    user1_p = int(input("Your private key"))
    g = int(input("Public key"))
    n = int(input("Second public small key"))
    # public domain numbers
    PDN = [g, n]
    us1_pu = (encrypt(user1_p, PDN))
    ls = [user1_p, g, n]
    if check_num(ls) == False:
        print("numeric incorrect")
        exit()
    print("-----------------Your exchange key-------------------")
    print(us1_pu)
    print("----------------------------------------------------")
    us2_pu = int(input("the other encrypted input"))
    print("-----------------agreed number-------------------")
    print(us2_pu ** us1_pu)
    print("-------------------------------------------------")
    return (us2_pu ** us1_pu)


def check_num(ls):
    if (ls[1]) - (ls[0]) < 0:
        print("error")
        return (False)
    elif ((ls[1]) - (ls[2]) < 0):
        print("error")
        return (False)


mode = int(input("1)Personal 2)communication"))
if mode == 1:
    user1_p = int(input("user1"))
    user2_p = int(input("user2"))
    g = int(input("big number g"))
    n = int(input("a prime small number"))
    # public domain numbers
    PDN = [g, n]
    print(PDN)
    print("-----------------public domain-------------------")
    us1_pu = (encrypt(user1_p, PDN))
    us2_pu = (encrypt(user2_p, PDN))
    print("user1" + str(us1_pu))
    print("user2" + str(us2_pu))
    print("-----------------private answer-------------------")
    print(us2_pu ^ (us1_pu))
    print(us1_pu ^ (us2_pu))
    exit()
if mode == 2:
    mode_2 = (input("more than 2 people Y/N"))
    if mode_2 == "Y":
        mode_3 = int(input("how many?"))

    elif mode_2 == "N":
        encrypt_2ppl()
else:
    print("error:incorrect input")
