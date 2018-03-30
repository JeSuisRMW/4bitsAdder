i=0
count = 0


print("Type number A (4 bits): ")
x=input()
x = [int(w) for w in str(x)]

print("Type number B (4 bits): ")
y=input()
y = [int(w) for w in str(y)]


x=x[::-1]
y=y[::-1]

c=0
s=[0,0,0,0,0]


def pnand(x, y):
        global count
        count = count+ 1
        return (int(not(x * y)))

def por(x, y):
        global count
        count +=1
        return(x or y)

def pand(x, y):
        global count
        count +=1
        return(int(not pnand(x, y)))


def pxor(x, y):
        global count
        count += 1
        return(int((x and not y) or (y and not x)))



while i<5:
        if(i==4):
                s[i]=c
                i = i+1
        else:
                s[i]= pxor(pxor(x[i], y[i]), c)
                c= por(pand(x[i],y[i]), pand(pxor(x[i], y[i]), c))
                i+=1

s=s[::-1]


string_s= "".join(str(u)for u in s)

string_s=string_s[0].strip('0') + string_s[1:]


print("\n\n\tThe Sum of the two numbers is: ", string_s, "\n")
print("\tRemainder ", c, "\n")
print("\tThis took" , count, "logical gates to count.")
input()
