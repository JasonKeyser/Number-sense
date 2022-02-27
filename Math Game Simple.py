import random
import time
import csv
import os

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
            line['time'] = float(line['time']) #data is stored as strings, this reverts it back to integers before adding to list
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

def format_question(top_number, bottom_number, answer, symbol):
    '''
    formats question vertically like
    24
   +10
    34
    '''


    top_space = ''
    if bottom_number < 10 and top_number < 10:
        bottom_space = ''
    elif bottom_number < 10 and top_number >= 10 and top_number < 100:
        bottom_space = ' '
    elif bottom_number < 10 and top_number >= 100:
        bottom_space = '  '
    elif bottom_number >= 10 and bottom_number < 100 and top_number >= 10 and top_number < 100:
        bottom_space = ''
    elif bottom_number >= 10 and bottom_number < 100 and top_number >= 100:
        bottom_space = ' '
    elif bottom_number >= 10 and bottom_number < 100 and top_number < 10:
        bottom_space = ''
        top_space = ' '
    elif bottom_number >= 100 and top_number < 10:
        top_space = '  '
        bottom_space = ''
    elif bottom_number >= 100 and top_number >= 10 and top_number < 100:
        top_space = ' '
        bottom_space = ''
    else:
        bottom_space = ''

    # following formats the curser to start at the right length of digits for the answer
    ansr1 = len(str(answer))
    bottom_row = len(bottom_space + str(bottom_number)) + 1
    difference = bottom_row - ansr1
    answer_space = ""
    if difference > 0:
        for _ in range(difference):
            answer_space += " "

    question = input(f"What is \n {top_space}{str(top_number)}\n{symbol}{bottom_space}{str(bottom_number)}?\n{answer_space}")
    return question


def compare_answer(q, answer, k):
    if int(q) == answer:
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print("Right answer was "+ str(answer))
        return False, k

# bug, addition only has even numbers
def addition(k):
    f = (k+1)
    top_number = int(random.randrange(1,5)*f)
    bottom_number = int(random.randrange(1,5)*f)

    answer = top_number + bottom_number
    q = format_question(top_number, bottom_number, answer, "+")
    return compare_answer(q,answer,k)

#This asks user to do subtraction
def sub(k):
    f = 4*(k+1)
    top_number = int(random.random()*f + 2*(k+1))
    bottom_number = int(random.random()*f)

    answer = top_number - bottom_number
    q = format_question(top_number,bottom_number,answer,'-')
    return compare_answer(q,answer,k)


#This asks the user to do multiplication with 2 single digit numbers
def mult1dig(k):
    f = 2*(k+1)
    f1 = (k+1)
    top_number = int(random.random()*f1)
    bottom_number = int(random.random()*f)
    answer = top_number*bottom_number
    q = format_question(top_number,bottom_number,answer,'x')
    return compare_answer(q,answer,k)

#'this asks player to do division'
def div(k):
    f = .25*(k+1)
    answer = int(random.randrange(3,5)*f)
    bottom_number= int(random.randrange(3,5)*f + 1)
    top_number = answer * bottom_number

    q = format_question(top_number,bottom_number,answer,'/')
    return compare_answer(q,answer,k)

#this does exponents
def exp(k):
    f = .2*(k+1)
    x = int(random.random()*f +1)
    b = int(random.randrange(2,4))
    q = input("What is \n" + str(x) + "^" + str(b) +"?\n ")
    if int(q) == (x ** b):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print('Right answer was '+ str(x ** b))
        return False, k

# this does square root problems
def sqr(k):
    f = .1*(k+1)
    x = int(random.randrange(1,5)*f)
    d = x * x
    q = input("What is the sq root of " + str(d) +"?\n ")
    if int(q) == (x):
        print("Good Job\n")
        return True, k + 1
    else:
        print("Wrong")
        print('Right answer was '+ str(x))
        return False, k


classic_funcs = [mult1dig,sub,addition,div]
classic_funcs_2 = [mult1dig,sub,addition,div,exp,sqr]
multiplication_funcs = [mult1dig]
division_funcs = [div]
subtraction_funcs = [sub]
addition_funcs = [addition]

classic_leaderboard = r'C:\Users\Jason Keyser\Documents\mathgamethirdleaderboard.csv'
mult_leaderboard = r'C:\Users\Jason Keyser\Documents\mathgamethirdleaderboardmultiplication.csv'
div_leaderboard = r'C:\Users\Jason Keyser\Documents\mathgamethirdleaderboarddivision.csv'
add_leaderboard = r'C:\Users\Jason Keyser\Documents\mathgamethirdleaderboardaddition.csv'
sub_leaderboard = r'C:\Users\Jason Keyser\Documents\mathgamethirdleaderboardsubtraction.csv'

cc = 1
while cc == 1:
    game_type = input("\nWhat game mode? "
                      "\n Type 'c' for classic mode or 'multiplicaton' 'division' 'addition'  or 'subtraction' to practice specific operations. ")

    game_modes = {'m': [multiplication_funcs, multiplication_funcs, mult_leaderboard],
                  'd': [division_funcs,division_funcs,div_leaderboard],
                  's': [subtraction_funcs,subtraction_funcs, sub_leaderboard],
                  'a': [addition_funcs, addition_funcs, add_leaderboard],
                  'c':[classic_funcs, classic_funcs_2,classic_leaderboard]}

    choice = game_type[0].lower()
    funklist = game_modes[choice][0]
    funk2list = game_modes[choice][1]
    leaderboard_path = game_modes[choice][2]


    nm = input("\nType your name and press Enter    ")
    print("\nClock is running, calculate!\n")
    x = time.time()
    x2 = None
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
    d, y = leaderboard(new_player,leaderboard_path)
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
