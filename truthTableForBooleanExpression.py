t = "abc'+bc+a'+bcb'(b+c')' + a'b'c"
l = [i for i in t if i.isalpha()]
l.sort()
n = 0
i = 0
while i<len(l):
    if l.count(l[i])>1:
        l.pop(i)
    else:
        i += 1
n = len(l)
tt = []
for i in range(n):
    counter = 2**(n)/(2**(i+1))
    tt.append([])
    pol = -1
    for j in range(2**n):
        if counter == 0:
            counter = pol * 2**(n)/(2**(i+1))
            pol *= -1
        if counter>0:
            tt[i].append(0)
            counter -= 1
        else:
            tt[i].append(1)
            counter += 1


exp = ""
"""
k = True
for i in t:
    if i == "'":
        for j in range(len(exp)-2, -1, -1):
            if exp[j] == " " or exp[j] == "(":
                exp = exp[:j] + " not " + exp[j:]
                break
    elif i == "+":
        exp = exp + " or "
        k = False
    elif i == " ":
        continue
    elif exp and k:
        if i in l:
            exp = exp + " and " + "l1[" + str(l.index(i)) + "]"
        else:
            exp = exp + i
            k = False
    elif exp and not k:
        if i in l:
            exp = exp + "l1[" + str(l.index(i)) + "]"
        else:
            exp = exp + " and " + i
        k = True
    elif not exp:
        if i in l:
            exp += "l1[" + str(l.index(i)) + "]"
        else:
            k = False
            exp += i
    else:
        print(i)
l2 = []
for i in range(len(t)):
    if t[i] == "+":
        exp = exp + " or "
    elif t[i].isalpha():
        exp = exp + " l1[" + str(l.index(t[i])) + "] "
    elif t[i] == "(":
        exp = exp + " ( "
        l2.append(len(exp)-3)
    elif  t[i] == ")":
        exp = exp + ")"
    elif t[i] == "'":
        if exp[-6].isalpha():
            exp = exp[:-6] + "not " + exp[-6:]
        else:
            exp = exp[:l2[-1]] + " not " + exp[l2[-1]:]
    print(exp)
    
exp = exp.split()
i = 1
n = len(exp)
while i<n-1:
    if exp[i+1] == "or" or exp[i+1] == ")" or exp[i] == "or" or exp[i] == ")" or exp[i] == "not" or exp[i] == "or" or exp[i] == "(":
        pass
    else:
        exp.insert(i, "and")
        n = len(exp)
        i += 1
    i += 1
    print(exp)
exp = " ".join(exp)
"""

exp = ""
m = ""
for i in t:
    if i != " ":
        m += i

# abc'+bc+a(b+c)'+abc
buffer = {}
skip = False

def buffed(buffer, val):
    for i in buffer:
        buffer[i] += val

def unpack(buffer):
    for i in buffer:
        if buffer[i] == 0:
            del buffer[i]
            return 1

skip2 = False
for i in range(len(m)-1,-1,-1):
    if skip or skip2:
        if skip == True:
            skip = False
            print("1", i, exp)
            continue
        elif skip2 == True:
            skip2 = False
            print("2", i, exp)
            continue
    if m[i] == ")":
        if exp[0] != "+":
            exp = m[i] + "." + exp
        else:
            exp = m[i] + exp
        buffed(buffer, 1)
    elif m[i] == "(":
        exp = m[i] + exp
        buffed(buffer, -1)
        unpacked = unpack(buffer)
        if unpacked:
            exp = "'" + exp
            
    elif m[i] == "+":
        exp = m[i] + exp
    elif m[i] == "'":
        if m[i-1:i] == "":
            exp = "'" + exp
            skip = True
        elif m[i-1:i].isalpha():
            if exp[0] == "+":
                exp = "'" + m[i-1:i] + exp
                if m[i-2:i-1] == "+":
                    exp = "+" + exp
                    skip = True
                    skip2 = True
                else:
                    skip = True
            elif m[i-2:i-1] == "+":
                exp = "+" + "'" + m[i-1:i] + "." + exp
                skip = True
                skip2 = True
            else:
                exp = "'" + m[i-1:i] + "." + exp
                skip = True
        else:
            buffer[i] = 0
    else:
        if exp:
            if exp[0] == ")":
                exp = m[i] + exp
            elif exp[0] != "+":
                exp = m[i] + "." + exp
            else:
                exp = m[i] + exp
        else:
            exp = m[i]
    print(m[i], exp)


exp2 = exp
exp = []
for i in exp2:
    if i in l:
        exp.append("l1[" + str(l.index(i)) + "]")
    elif i == "+":
        exp.append("or")
    elif i == "'":
        exp.append("not")
    elif i == ".":
        exp.append("and")
    else:
        exp.append(i)

exp = " ".join(exp)
print(exp)
print(m)

for i in l:
    print(i.upper(), end=" ")
print()
for i in range(2**n):
    l1 = []
    for j in range(n):
        print(tt[j][i], end = " ")
        l1.append(int(tt[j][i]))
    print(int(eval(exp)))

"""
while True:
    t = input("Enter Variables : ").lower()
    if not t:
        break
    l = [i for i in t if i.isalpha()]
    l.sort()
    n = 0
    i = 0
    while i<len(l):
        if l.count(l[i])>1:
            l.pop(i)
        else:
            i += 1
    n = len(l)
    tt = []
    for i in range(n):
        counter = 2**(n)/(2**(i+1))
        tt.append([])
        pol = -1
        for j in range(2**n):
            if counter == 0:
                counter = pol * 2**(n)/(2**(i+1))
                pol *= -1
            if counter>0:
                tt[i].append(0)
                counter -= 1
            else:
                tt[i].append(1)
                counter += 1

    m = input("Enter Expression : ").lower()
    exp = []
    for i in m:
        if i == "+":
            exp.append("or")
        elif i == "'":
            exp.append("not")
        elif i == ".":
            exp.append("and")
        elif i.isalpha():
            exp.append("l1[" + str(l.index(i)) + "]")
        else:
            exp.append(i)
            
    exp = " ".join(exp)
    try:
        print(exp)
        for i in l:
            print(i.upper(), end=" ")
        print("Z")
        for i in range(2**n):
            l1 = []
            for j in range(n):
                print(tt[j][i], end = " ")
                l1.append(int(tt[j][i]))
            print(int(eval(exp)))
    except:
        print("\nInvalid!!", exp, sep="\n")
"""
