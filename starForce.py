import random, time

prob_10 = [95.0, 90.0, 85.0, 85.0, 80.0, 75.0, 70.0, 65.0, 60.0, 55.0]
prob_15 = [[50.0, 0.0], [45.0, 0.0], [40.0, 0.6], [35.0, 1.3], [30.0, 1.4]]
prob_20 = [[30.0, 2.1], [30.0, 2.1], [30.0, 2.1], [30.0, 2.8], [30.0, 2.8]]
prob_22 = [[30.0, 7.0], [30.0, 7.0]]

is_chance = 0

def welcome():
    print("START STARFORCE SIMULATOR", end="")

    for _ in range (5):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print("")

def enchant(status, cur_lev):
    time.sleep(0.15)
    global is_chance
    if is_chance == 2:
        print("CHANCE TIME! ", cur_lev, ">", cur_lev+1)
        cur_lev += 1
        is_chance = 0
        return status, cur_lev
    prob = round(random.random() * 100, 1)
    if cur_lev < 10:
        if prob <= prob_10[cur_lev]:
            cur_lev += 1
            printResult(cur_lev)
        else:
            printResult(cur_lev*-1)
        return status, cur_lev
    elif cur_lev < 15:
        if prob <= prob_15[cur_lev-10][1] and prob > 0:
            printResult(cur_lev*100)
            status = False
        elif prob <= prob_15[cur_lev-10][0]+prob_15[cur_lev-10][1]:
            is_chance = 0
            cur_lev += 1
            printResult(cur_lev)
        else:
            if cur_lev == 10:
                printResult(cur_lev*-1)
            else:
                is_chance += 1
                printResult(cur_lev*-1)
                cur_lev -= 1
        return status, cur_lev
    elif cur_lev < 20:
        if prob <= prob_20[cur_lev-15][1] and prob > 0:
            printResult(cur_lev*100)
            status = False
        elif prob <= prob_20[cur_lev-15][0]+prob_20[cur_lev-15][1]:   
            is_chance = 0        
            cur_lev += 1             
            printResult(cur_lev)
        else:
            if cur_lev == 15:
                printResult(cur_lev*-1)
            else:
                is_chance += 1
                printResult(cur_lev*-1)
                cur_lev -= 1
        return status, cur_lev
    else:
        if cur_lev == 22:
            print("CONGRATULATIONS! YOU WIN!")
            status = False        
        elif prob <= prob_22[cur_lev-20][1] and prob > 0:
            printResult(cur_lev*100)
            status = False
        elif prob <= prob_22[cur_lev-20][0]+prob_22[cur_lev-20][1]:                    
            cur_lev += 1              
            printResult(cur_lev)
        else:
            if cur_lev == 20:
                printResult(cur_lev*-1)
            else:
                printResult(cur_lev*-1)
                cur_lev -= 1
        return status, cur_lev



def printResult(cur_lev):
    if cur_lev <= 0:
        if cur_lev > -10:
            print("ENCHANT FAILED!", cur_lev*-1, ">", cur_lev*-1) # when cur_lev is less than 10
        elif cur_lev % 5 == 0:
            print("ENCHANT FAILED!", cur_lev*-1, ">", cur_lev*-1) # when cur_lev is 10, 15, 20
        else:
            print("ENCHANT FAILED!", cur_lev*-1, ">", cur_lev*-1-1)
    elif cur_lev > 100:
        print("ITEM DESTROYED!", cur_lev//100, ">", "0")
    else:
        print("SUCCESSFULLY ENCHANTED!", cur_lev-1, ">", cur_lev)

def main():
    welcome()
    status = True
    cur_lev = 0
    while status != False:
        status, cur_lev = enchant(status, cur_lev)

main()