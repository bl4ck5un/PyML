import sys
f = sys.argv[1]

fout = open(f+'.out', 'w')

with open(f, 'r') as inf:
    l = 'haha'
    while True:
        l = inf.readline().strip()
        if l == '':
            break
        y = int(l.split()[0])
        if y == -1:
            y = 0

        fout.write('%d, ' %y)
        x = l.split()[1:]
        record = {}
        for i, xx in enumerate(x):
            idx = int(xx.split(':')[0])
            val = xx.split(':')[1]
            record[idx] = val

        for i in range(1, 8+1):
            if record.has_key(i):
                val = record[i]
            else:
                print 'missing value %d' %i
                print l
                val = ', '

            if i == 8:
                fout.write(val)
            else:
                fout.write('%s, ' % val)

        fout.write('\n')
