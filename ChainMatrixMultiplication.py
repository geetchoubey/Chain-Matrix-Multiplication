p = []
i = 0
j = 0
temp = 0
k = 0
pas = 2
A = 0
def disp(l):
        for i in l:
                print i
        return 
A= int(raw_input("Enter no. of Matrices "))
for i in range(0, A+1):
	p.append(int(raw_input()))
mink = [ [] for _ in range(A)]
m = [ [] for _ in range(A)]
#Step 0:
for i in range(0, A):
        for j in range(i+1):
                m[i].append(0)
                mink[i].append(0)
print "m in step 0:\n", disp(m)
#Step 1:
for i in range(A-1):
        m[i].append(p[i]*p[i+1]*p[i+2])
print "m in step 1:\n", disp(m)
#Step 3:
for r in range(A-2, 0, -1):
        for i in range(0,r): 
                minn = 99999
                j = i+pas
                for z in range(j-i):
                        #when k = i
                        k = i+z                     
                        temp = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                        if temp < minn:
                                minn = temp
                                mik = k + 1
                m[i].append(minn)
                mink[i].append(mik)
        pas = pas + 1
disp(m)
disp(mink)


