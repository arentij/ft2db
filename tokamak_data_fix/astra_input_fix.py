ti = []
up = []
ip = []
bt = []
ur = []
# Time  Up  Ip  Btor  Ur  Up  Ip  Btor  Ur
with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        l = [(i.replace(',', '.')) for i in line.split('  ')]
        if l[0] != 'Time':
            k = [float(i) for i in l]
            ti.append(k[0])
            up.append(k[1] - k[5])
            ip.append(k[2] - k[6])
            bt.append(k[3])
            ur.append(k[4] - k[8])

            # print(k)

tstart = 25
tend = 40
ustep = 20
ipstep = 20
bstep = 50
urstep = 20


for i in range(0, len(ti), ustep):
    if tstart <= ti[i] <= tend:
        tim = str(round(ti[i]/1000, 4))
        f = str(round(up[i], 2))
        string = 'UEXT    ' + tim + ' '.rjust(8-len(tim)) + f
        print(string)

print()

for i in range(0, len(ti), ipstep):
    if tstart <= ti[i] <= tend:
        tim = str(round(ti[i]/1000, 4))
        f = str(round(ip[i]/1000, 4))
        string = 'IPL     ' + tim + ' '.rjust(8-len(tim)) + f
        print(string)

print()

for i in range(0, len(ti), bstep):
    if tstart <= ti[i] <= tend:
        tim = str(round(ti[i]/1000, 4))
        f = str(round(bt[i]/10, 3))
        string = 'BTOR    ' + tim + ' '.rjust(8-len(tim)) + f
        print(string)

print()

for i in range(0, len(ti), urstep):
    if tstart <= ti[i] <= tend:
        tim = str(round(ti[i]/1000, 4))
        f = str(round(ur[i]/10, 3))
        string = 'ZDF47X  ' + tim + ' '.rjust(8-len(tim)) + f
        print(string)

print()




