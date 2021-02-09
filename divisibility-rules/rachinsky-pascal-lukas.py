def cut_it(num, s, mode):
    if s == 0 or len(str(num)) == 1:
        return(num)
    else:
        line = str(num)
        beg = int(line[0:-s])
        en = int(line[-s:])
        if(mode == 0):
            return(beg)
        else:
            return(en)

def divisibility1_Rachinsky(n, p, s):
    print("")
    print("1-й признак Рачинского:")
    a = cut_it(p, s, 0)
    b = cut_it(p, s, 1)
    print("Дано p = ", p, ". Тогда при s = ", s, ": a = ", a, ", b = ", b, ".", sep="")
    print("n = ", n)
    cur_n = n
    prev_n = n + 1
    i = 0
    while cur_n > p and cur_n < prev_n:
        m = cut_it(cur_n, s, 0)
        k = cut_it(cur_n, s, 1)
        prev_n = cur_n
        cur_n = m*b - k*a
        i += 1
        print(i, ") ", "s = ", s, ", m = ", m, ", k = ", k, ".", sep="")
        print("mb - ka =", m, "*", b, "-", k, "*", a, "=", cur_n)
        if cur_n < 0:
            print("|", cur_n, "| = ", -cur_n, sep="")
            cur_n = -cur_n
    

    ans = "Ответ: "
    if cur_n == 0 or cur_n == n:
        ans += str(n) + " делится на " + str(p)
    elif cur_n > prev_n and cur_n > p:
        ans += str(n) + "/" + str(p) + " <=> " + str(cur_n) + "/" + str(p)
    elif cur_n < p:
        ans += str(n) + " не делится на " + str(p)
    print(ans)

def divisibility2_Rachinsky(n, p, s):
    # Setting default s to 1
    s = 1
    print("")
    print("2-й признак Рачинского:")
    a = cut_it(p, s, 0)
    b = cut_it(p, s, 1)
    b_ = b
    if b_ == 1 or b_ == 9:
        b_ = 10 - b_
    q = int('%g'%((p * b_ + 1) / 10))
    print("Дано p = ", p, ". Тогда при s = ", s, ": a = ", a, ", b = ", b,
            ", q = (pb* + 1)/10 = (", p, " * ", b_, " + 1) / 10 = ", q, sep="")
    print("n = ", n)

    cur_n = n
    prev_n = n + 1
    i = 0
    while cur_n > p and cur_n < prev_n:
        m = cut_it(cur_n, s, 0)
        k = cut_it(cur_n, s, 1)
        prev_n = cur_n
        cur_n = m + k*q
        i += 1
        print(i, ") m = ", m, ", k = ", k, ".", sep="")
        print("m + kq =", m, "+", k, "*", q, "=", cur_n)
        if cur_n < 0:
            print("|", cur_n, "| = ", -cur_n, sep="")
            cur_n = -cur_n
    
    ans = "Ответ: "
    if cur_n == 0 or cur_n == n:
        ans += str(n) + " делится на " + str(p)
    elif cur_n > prev_n and cur_n > p:
        ans += str(n) + "/" + str(p) + " <=> " + str(cur_n) + "/" + str(p)
    elif cur_n < p:
        ans += str(n) + " не делится на " + str(p)
    print(ans)

def divisibility3_Rachinsky(n, p, s):
    # Setting default s to 1
    s = 1
    print("")
    print("3-й признак Рачинского:")
    a = cut_it(p, s, 0)
    b = cut_it(p, s, 1)
    b_ = b
    if b_ == 1 or b_ == 9:
        b_ = 10 - b_
    q = int('%g'%((p * b_ + 1) / 10))
    q_ = abs(p - q)
    print("Дано p = ", p, ". Тогда при s = ", s, ": a = ", a, ", b = ", b,
            ", q = ", q, " q* = |p - q| = |", p, " - ", q, "| = ", q_, sep="")
    print("n = ", n)

    cur_n = n
    prev_n = n + 1
    i = 0
    while cur_n > p and cur_n < prev_n:
        m = cut_it(cur_n, s, 0)
        k = cut_it(cur_n, s, 1)
        prev_n = cur_n
        cur_n = m - k*q_
        i += 1
        print(i, ") m = ", m, ", k = ", k, ".", sep="")
        print("m - kq* =", m, "-", k, "*", q_, "=", cur_n)
        if cur_n < 0:
            print("|", cur_n, "| = ", -cur_n, sep="")
            cur_n = -cur_n
    
    ans = "Ответ: "
    if cur_n == 0 or cur_n == n:
        ans += str(n) + " делится на " + str(p)
    elif cur_n > prev_n and cur_n > p:
        ans += str(n) + "/" + str(p) + " <=> " + str(cur_n) + "/" + str(p)
    elif cur_n < p:
        ans += str(n) + " не делится на " + str(p)
    print(ans)

def divisibility_Pascal(n, p):
    print("")
    print("Признак Паскаля:")
    cur_n = n
    prev_n = n + 1
    l = len(str(cur_n))
    ri = []
    cur_r = 1
    out = ""
    for i in range(l):
        ded = cur_r % p
        ri.append(ded)
        out += "r" + str(i) + " = "
        if (ded != cur_r):
            out += str(cur_r) + " mod " + str(p) + " = "
        out += str(ded) + ", "
        cur_r *= 10
    print(out)

    cur_r = cut_it(cur_r, 1, 0)
    print("n =", n)
    j = 1
    while cur_n > p and len(str(cur_n)) > len(str(p)) and cur_n < prev_n:
        out = str(j) + ") r = "
        sum = 0
        new_n = 0
        l = len(str(cur_n))
        pw = pow(10, l - 1)
        for i in range(l):
            num = cut_it(cut_it(cur_n, l - 1 - i, 0), 1, 1)
            new_n += num * ri[l - 1 - i]
            if ri[l - i - 1] == pw:
                sum += num * pw
            else:
                out += str(num) + " * " + str(ri[l - i - 1]) + " + "
            pw = cut_it(pw, 1, 0)
        out += str(sum) + " = " + str(new_n)
        print(out)

        
        j += 1
        prev_n = cur_n
        cur_n = new_n

    ans = "Ответ: "
    if cur_n == 0 or cur_n == p:
        ans += str(n) + " делится на " + str(p)
    elif len(str(cur_n)) == len(str(p)) and cur_n > p:
        ans += str(n) + "/" + str(p) + " <=> " + str(cur_n) + "/" + str(p)
    elif cur_n < p:
        ans += str(n) + " не делится на " + str(p)
    print(ans)

def divisibility_Lucas(n, p):
    #Todo
    return(0)


print("Enter n, p, s")
n, p, s = map(int, input().split())

divisibility1_Rachinsky(n, p, s)
divisibility2_Rachinsky(n, p, s)
divisibility3_Rachinsky(n, p, s)
divisibility_Pascal(n, p)
divisibility_Lucas(n, p)