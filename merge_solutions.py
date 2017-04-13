N_WORKERS = 5

s = open('solution.csv','w')
for i in range(N_WORKERS):
    f = open('solution_'+str(i)+'.csv','r')
    while True:
        line = f.readline()
        s.write(line+'\n')
        if not line: break
    f.close()
s.close()