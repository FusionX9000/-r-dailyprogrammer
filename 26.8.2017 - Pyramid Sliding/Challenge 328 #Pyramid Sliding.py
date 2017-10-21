# takes the input from file (input1.txt, input2.txt and input3.txt
def input_(n):
    with open('input'+n+'.txt','r') as target:
        target.readline()
        input = target.read()
    input = [[int(x) for x in i.split()] for i in input.split('\n')]
    return input

# Starts from bottom row of the pyramid, adding the minimum of the child nodes, approaching upwards in the pyraimid
def solve(input):
    x = len(input)-2  # start from second last row
    while(x>=0):
        for i in range(len(input[x])):
            input[x][i]+=min(input[x+1][i],input[x+1][i+1])  # adds minimum of the child node to the parent node
        x -= 1
    return input[0][0]

for i in range(1,4):
    print(solve(input_(str(i))))

"""
# irrelevant function to print input as a pyramid
def print_as_pyramid(list):
    length=len(list)
    for i in list:
        print('  '*(length-1),end="")
        for j in i:
            j = str(j)
            if(int(j)>99):
                print(j,end='')
            elif(int(j)>9):
                print(' '+j+'',end='')
            else:
                print(' '+j+' ',end='')
            print(' ',end='')
        print('')
        length=length-1
"""



