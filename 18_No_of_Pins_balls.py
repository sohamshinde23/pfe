#In bowling, the player starts with 10 pins at the far end of a lane. The object is to knock all the pins 
#down. For this exercise, the number of pins and balls will vary. Given the number of pins N and 
#then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), 
# determine which pins remain standing after all the balls have been rolled. The balls are numbered 
# from 1 to N (inclusive) for this situation. The subsequent number pairs, one for each K represent 
# the start to stop (inclusive) positions of the pins that were knocked down with each role. Print a 
# sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked 
# down.
#Input
#5
#3
#1 2
#3 4
#2 5
#Output
#.I..I

    #Explanation
    #The first line contains the number of pins N. The second line contains the number of balls
    #The third line contains the pins knocked down by the first ball. The fourth line contains th
    #pins knocked down by the second ball. The fifth line contains the pins knocked down by the
    #third ball. The sixth line contains the pins knocked down by the fourth ball. The seventh
    #line contains the pins knocked down by the fifth ball.
    #The output is a sequence of N characters, where "I" represents a pin left standing
    # and "." represents a pin knocked down.
    #Input
    #5
    #3
    #1 2
    #3 4
    #2 5
    #Output
    #.I..I 
n = int(input())
k = int(input())
pins = [True] * n
for i in range(k):
        a, b = map(int, input().split())
        for j in range(a - 1, b):
            pins[j] = False
            for i in range(n):
                if pins[i]:
                    print('I', end = "")
                else:
                    print('.', end = "")
                    print()
                    break
                #Explanation
                #The first line contains the number of pins N. The second line contains the number of balls
                #The third line contains the pins knocked down by the first ball. The fourth line contains th
                #pins knocked down by the second ball. The fifth line contains the pins knocked down by th
                #third ball. The sixth line contains the pins knocked down by the fourth ball. The seventh
                #line contains the pins knocked down by the fifth ball.
                #The output is a sequence of N characters, where "I" represents a pin left standing
                # and "." represents a pin knocked down.
                #Input
                #5
                #3
                #1 2
                #3 4
                #2 5
                #Output
                #.I..I
                #Explanation
                #The first line contains the number of pins N. The second line contains the number of balls
                #The third line contains the pins knocked down by the first ball. The fourth line contains th
                #pins knocked down by the second ball. The fifth line contains the pins knocked down by the
                #third ball. The sixth line contains the pins knocked down by the fourth ball. The seventh
                #line contains the pins knocked down by the fifth ball.
                #The output is a sequence of N characters, where "I" represents a pin left standing
                # and "." represents a pin knocked down.
                #Input
                #5
                #3
                #1 2
                
                    #3 4
                    #2 5
                    #Output
                    #.I..I
                    #Explanation
                    #The first line contains the number of pins N. The second line contains the number of balls
                    #The third line contains the pins knocked down by the first ball. The fourth line contains th
                    #pins knocked down by the second ball. The fifth line contains the pins knocked down by th
                    #third ball. The sixth line contains the pins knocked down by the fourth ball. The seventh
                    #line contains the pins knocked down by the fifth ball.
                    #The output is a sequence of N characters, where "I" represents a pin left standing
                    # and "." represents a pin knocked down.
                    #Input
                    #5
                    #3
                    #1 2
                    #3 4
                    #2 5
                    #Output
                    #.I..I
                    #Explanation
                    #The first line contains the number of pins N. The second line contains the number of balls
                    #The third line contains the pins knocked down by the first ball. The fourth line contains th
                    #pins knocked down by the second ball. The fifth line contains the pins knocked down by th
                    #third ball. The sixth line contains the pins knocked down by the fourth ball. The seventh
                    #line contains the pins knocked down by the fifth ball.
                    #Explanation
                    #The first line contains the number of pins N. The second line contains the number of balls
                    #The third line contains the pins knocked down by the first ball. The fourth line contains th
                    #pins knocked down by the second ball. The fifth line contains the pins knocked down by th
                    