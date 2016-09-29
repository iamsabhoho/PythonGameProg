size = 0
c = 0
ptime = 0
LS, LB, AS, AB, ES, EB = 0

if c == 1:
    ptime = 6
    if size == 1:
        p = LB
    else:
        p = LS

elif c == 2:
    ptime = 4
    if size == 1:
        p = AB
    else:
        p = AS

elif c == 3:
    ptime = 5
    if size == 1:
        p = EB
    else:
        p = ES
else:
    print('Please order again.')



if size == 1:
    if c == 1:
        p = LB
    elif c == 2:
        p = AB
    else:
        p = EB
elif size == 2:
    if c == 1:
        p = LS
    elif c == 2:
        p = AS
    else:
        p = ES
else:
    print('Please order again.')

if c == 1:
    ptime = 6
elif c == 2:
    ptime = 4
else:
    ptime = 5
