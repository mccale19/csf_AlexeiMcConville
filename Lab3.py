# Alexei McConville
# mccale19

x = 0
y = 1
z = 1
a = 10

i = a
add = 0
total = 0

series = 'sum'

if series == 'fibonacci':
    if a == 0: print 0
    elif a == 1: print 1
    else:
        for a in range (0, a - 1):
            z = x + y
            x = y
            y = z
        print z

elif series == 'sum':
    while (i > 0):
        add = (3 * i)
        i = i - 1
        total = total + add
    print total
    
else:
    print "Invalid String"
    
# Collaborator: Stephen Rancourt