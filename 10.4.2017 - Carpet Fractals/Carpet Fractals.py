#https://www.reddit.com/r/dailyprogrammer/comments/748ba7/20171004_challenge_334_intermediate_carpet/

# Creates a list from the string where each new line is a new element
def input_(string):
    string=string.split('\n')
    string=[x.split() for x in string]
    return string

# Reads the input
with open(r'C:\Users\FusionX\Desktop\DailyProgrammer\10.4.2017\input1.txt','r') as target:
    raw_input=target.read()

# Initializing the values
info=input_(raw_input)
pbm=[[0]]
ncolors=int(info[0][0])
niterations=int(info[0][1])
all_instructions=info[1:]
size = 3**niterations
maxvalue = max([int(x) for x in raw_input.split()[2:]])

# Assigning each color code to its respective instruction and saving as dictionary
instance={}
for x in all_instructions:
    instance[all_instructions.index(x)]= x

# Interpreting instance
def interpret(instruction):
    chunk=[[0 for x in range(0,3)] for y in range(0,3)]
    a=0
    b=0
    for x in instruction:
        if(b<=3):
            if(a==3):
                a=0
                b+=1
            (chunk[b])[a]= x
            a+=1
    return chunk

# Stitches each 3x3 chunk horizontally to the horizontal chunk of height 3
def stitch_horizontal(image,chunk):
    final = [None,None,None]
    if(len(image)==0):
        return chunk
    else:
        for x in range(0,3):
            final[x] = image[x]+chunk[x]
        return final

# Creating the image
def image():
    global pbm
    global niterations
    global instance
    horizontal_chunk=[]
    vertical_chunk=[]
    for x in range(niterations):
        for a in pbm:
            for b in a:
                chunk=interpret(instance[int(b)])
                horizontal_chunk=stitch_horizontal(horizontal_chunk,chunk)
            vertical_chunk=vertical_chunk+horizontal_chunk # stitches vertically
            horizontal_chunk=[]
        pbm=vertical_chunk # Image finished for current iteration, all the chunks are hence reset
        vertical_chunk=[]
    return pbm

# Writing to file
image = image()

if (ncolors > 2):
    with open("output1.pgm","w") as target:
        target.write('P2')
        target.write('\n')
        target.write(str(size) + ' ' + str(size))
        target.write('\n')
        target.write(str(maxvalue))
        target.write('\n')
        for x in image:
            target.write(' '.join(x))
            target.write('\n')
else:
    if (ncolors == 2):
        with open("output.pbm","w") as target:
            target.write('P2')
            target.write('\n')
            target.write(str(size) + ' ' + str(size))
            target.write('\n')
            for x in image:
                target.write(' '.join(x))
                target.write('\n')