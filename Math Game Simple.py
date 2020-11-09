import random
import time
import csv
import os

#the following code runs the leader board
#this function takes results from player game, adds it to previous results and sorts it
def leaderboard(n,csvpath):
    #checks if the file exists, if not, it creates one
    if not os.path.exists(csvpath):
        with open(csvpath, "w") as new_csv_writer:
            pass
    #opens csv file and reads all previous game results
    with open(csvpath, "r") as csv_file_reader:

        csv_reader = csv.DictReader(csv_file_reader)

        #this is a list which only contains the newest players results
        players = [n[0]]
        #adds old player data to list with new player data lines
        for line in csv_reader:
            line['time'] = float(line['time'])#data is stored as strings, this reverts it back to integers before adding to list
            line['solved'] = int(line['solved'])
            line['htime'] = int(line['htime'])
            players.append(line)
        #this sorts the data first by the amount of problems solved then by the amount of time taken
    leeder = sorted(players, key=lambda x: (-x['solved'], x['time']))
    fastleeder = sorted(players, key = lambda x: x['htime'])
    #this writes the sorted data including the newest player's results back to the csv, ready to read for next time
    with open(csvpath, "w") as new_csv_writer:
        fnames = ['name', 'solved', 'time', 'htime']

        csv_writer = csv.DictWriter(new_csv_writer, fieldnames=fnames)

        csv_writer.writeheader()
        for l in leeder:
            csv_writer.writerow(l)

    return leeder, fastleeder

print("Welcome to the Math Game")



#This asks the user to do addition with 2 single digit numbers
def add1dig(k):
    f = 2*(k+1)
    v = int(random.randrange(1,5)*f)
    j = int(random.randrange(1,5)*f)

    # this if statement helps format the question in a vertical way instead of horizontal
    dd = ''
    if j < 10 and v < 10:
        pp = ''
    elif j < 10 and v >= 10 and v < 100:
        pp = ' '
    elif j < 10 and v >= 100:
        pp = '  '
    elif j >= 10 and j < 100 and v >= 10 and v < 100:
        pp = ''
    elif j >= 10 and j < 100 and v >= 100:
        pp = ' '
    elif j >= 10 and j < 100 and v < 10:
        pp = ''
        dd = ' '
    elif j >= 100 and v < 10:
        dd = '  '
        pp = ''
    elif j >= 100 and v >= 10 and v < 100:
        dd = ' '
        pp = ''
    else:
        pp = ''
    #this formats the curser to start at the right length of digits for the answer
    ansr = v + j
    ansr1 = len(str(ansr))
    if ansr1 == len(pp + str(j)) + 1:
        ee = ''
    elif ansr1 == len(pp + str(j)):
        ee = ' '
    elif ansr1 == len(pp + str(j)) - 1:
        ee = '  '

    q = input("What is \n " + dd + str(v) + "\n+" + pp + str(j) +"?\n" + ee)
    if int(q) == (v+j):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print("Right answer was "+ str(v+j))
        return False, k

#This asks user to do subtraction
def sub(k):
    f = 4*(k+1)
    v = int(random.random()*f + 2*(k+1))
    j = int(random.random()*f)
    #this if statement helps format the question in a vertical way instead of horizontal
    gg = ''
    if j < 10 and v < 10:
        tt = ''
    elif j < 10 and v >= 10 and v < 100:
        tt = ' '
    elif j < 10 and v >= 100:
        tt = '  '
    elif j >= 10 and j < 100 and v >= 10 and v < 100:
        tt = ''
    elif j >= 10 and j < 100 and v >= 100:
        tt = ' '
    elif j >= 10 and j < 100 and v < 10:
        tt = ''
        gg= ' '
    elif j >= 100 and v < 10:
        gg = '  '
        tt = ''
    elif j >= 100 and v >= 10 and v < 100:
        gg = ' '
        tt = ''
    else:
        tt = ''

    #this formats the curser to start at the right length of digits for the answer
    ansr = v - j
    ansr1 = len(str(ansr))
    if ansr1 == len(tt + str(j)) + 1:
        ee = ''
    elif ansr1 == len(tt + str(j)):
        ee = ' '
    elif ansr1 == len(tt + str(j)) - 1:
        ee = '  '

    q = input("What is \n " + gg + str(v) + "\n-" + tt + str(j) +"?\n" + ee)
    if int(q) == (v-j):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print("Right answer was " + str(v-j))
        return False, k


#This asks the user to do multiplication with 2 single digit numbers
def mult1dig(k):
    f = 2*(k+1)
    f1 = (k+1)
    x = int(random.random()*f1)
    b = int(random.random()*f)

    #this if statement helps format the question in a vertical way instead of horizontal
    nn = ''
    if b < 10 and x < 10:
        zz = ''
    elif b < 10 and x >= 10 and x < 100:
        zz = ' '
    elif b < 10 and x >= 100:
        zz = '  '
    elif b >= 10 and b < 100 and x >= 10 and x < 100:
        zz = ''
    elif b >= 10 and b < 100 and x >= 100:
        zz = ' '
    elif b >= 10 and b < 100 and x < 10:
        zz = ''
        nn= ' '
    elif b >= 100 and x< 10:
        nn = '  '
        zz = ''
    elif b >= 100 and x >= 10 and x < 100:
        nn = ' '
        zz = ''
    else:
        zz = ''

    #this formats the curser to start at the right length of digits for the answer
    ansr = x*b
    ansr1 = len(str(ansr))
    if ansr1 == len(zz + str(b)) + 1:
        ee = ''
    elif ansr1 == len(zz + str(b)):
        ee = ' '
    elif ansr1 == len(zz + str(b)) - 1:
        ee = '  '

    q = input("What is \n " + nn + str(x) + "\nx" +  zz + str(b) +"?\n" + ee)
    if int(q) == (x*b):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print('Right answer was '+ str(x*b))
        return False, k

#'this asks player to do division'
def div(k):
    f = .25*(k+1)
    x = int(random.randrange(3,5)*f)
    b = int(random.randrange(3,5)*f + 1)
    d = x * b

    #this if statement helps format the question in a vertical way instead of horizontal
    yy = ''
    if b < 10 and d < 10:
        cc = ''
    elif b < 10 and d >= 10 and d < 100:
        cc = ' '
    elif b < 10 and d >= 100:
        cc = '  '
    elif b >= 10 and b < 100 and d >= 10 and d < 100:
        cc = ''
    elif b >= 10 and b < 100 and d >= 100:
        cc = ' '
    elif b >= 10 and b < 100 and d < 10:
        cc = ''
        yy= ' '
    elif b >= 100 and d< 10:
        yy = '  '
        cc = ''
    elif b >= 100 and d >= 10 and d < 100:
        yy = ' '
        cc = ''
    else:
        cc = ''

    #this formats the curser to start at the right length of digits for the answer
    ansr = x
    ansr1 = len(str(ansr))
    if ansr1 == len(cc + str(b)) + 1:
        ee = ''
    elif ansr1 == len(cc + str(b)):
        ee = ' '
    elif ansr1 == len(cc + str(b)) - 1:
        ee = '  '

    q = input("What is \n " + yy + str(d) + "\n/" + cc + str(b) +"?\n" + ee)
    if int(q) == (x):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print('Right answer was '+ str(x))
        return False, k

#this does exponents
def exp(k):
    f = .2*(k+1)
    x = int(random.random()*f)
    b = int(random.randrange(2,4))
    q = input("What is \n" + str(x) + "^" + str(b) +"?\n ")
    if int(q) == (x ** b):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print('Right answer was '+ str(x ** b))
        return False, k

#this does square root problems
def sqr(k):
    f = .1*(k+1)
    x = int(random.randrange(1,5)*f)
    d = x * x
    q = input("What is the sq root of " + str(d) +"?     ")
    if int(q) == (x):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print('Right answer was '+ str(x))
        return False, k

cc = 1
while cc == 1:
    nm = input("\nWhat is your name?    ")
    print("\nClock is running, calculate!\n")
    x = time.time()
    x2 = None
    funklist = [mult1dig,sub,add1dig,div]
    funk2list = [mult1dig,sub,add1dig,div,exp,sqr]
    i = True
    c = 0
    while i == True:
        if c < 20:
            i,c = random.choice(funklist)(c)
        elif c == 20:
            print("Hardcore Mode!!!!\n")
            x2 = time.time()
            i,c = random.choice(funk2list)(c)
        else:
            i,c = random.choice(funk2list)(c)
#stop timing
    x1 = time.time()
#print out the time difference
    z = int(x1-x)
    print('\n' +  nm +', you solved ' + str(c) + ' problems in ' + str(z) + ' seconds.\n')
    if x2:
        hrd = int(x2-x)
    else:
        hrd = 1000

    new_player = [{'name': nm, 'solved': c, 'time':z, 'htime':hrd}]
    d, y = leaderboard(new_player,r'C:\Users\Jason Keyser\Documents\mathgamethirdleaderboard.csv')
#this loops through the list of dicts and prints out the top ten scores
    print('Leaderboard\n Name Score Seconds')
    i2 = 1
    for l in d[0:10]:
        print(i2, l['name'],l['solved'],l['time'])
        i2 += 1
    #this asks player if they want to play again and loops game
    pa = input("\nPress p to play again\nPress a for advanced stats      ")
    if pa.lower() == 'p':
        cc = 1
    elif pa.lower() == 'a':
        if hrd < 1000:
            print('\n' + nm + ' unlocked hardcore mode in ' + str(hrd) + ' seconds.\n')
            #this loops through the time to unlock harcore mode and prints a leaderboard
            print('Fastest times to hardcore\n Name, Seconds to Hardcore')
            i3 = 1
            for l in y[0:10]:
                print(i3, l['name'], l['htime'])
                i3 += 1
            xll = input('\nType name to see career stats or p to play again               ')
            if not xll.lower() == 'p':
                xl = []
                #this for loop calculates player average problems solved
                for l in y:
                    if l['name'] == xll:
                        xl.append(l['solved'])
                avs = int(sum(xl) / len(xl))
                #this for loop calculates player average time to hardcore
                xl3 = []
                for l in y:
                    if l['name'] == xll:
                        if l['htime'] < 1000:
                            xl3.append(l['htime'])
                avh = int(sum(xl3)/len(xl3))
                print('\n'+ xll + "'s average problems solved is " + str(avs) + " and average time to hardcore mode is " + str(avh))

        else:
            print('\n' + nm + ' did not unlock hardcore mode this round.\n')

            print('Fastest times to hardcore\n Name, Seconds to Hardcore')
            i3 = 1
            for l in y[0:10]:
                print(i3, l['name'], l['htime'])
                i3 += 1
            xll = input('\nType name to see career stats or p to play again              ')
            if not xll.lower() == 'p':
                xl = []
                #this for loop calculates player average problems solved
                for l in y:
                    if l['name'] == xll:
                        xl.append(l['solved'])
                avs = int(sum(xl) / len(xl))
                #this for loop calculates player average time to hardcore
                xl3 = []
                for l in y:
                    if l['name'] == xll:
                        if l['htime'] < 1000:
                            xl3.append(l['htime'])
                avh = int(sum(xl3)/len(xl3))
                print('\n'+ xll + "'s average problems solved is " + str(avs) + " and average time to hardcore mode is " + str(avh))
    else:
        cc = 0
