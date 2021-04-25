def split(string, k):
    n = len(string)
    j = (n/k)
    i = 0
    while i < n:
        t = string[i:i+j]
        i += j
        if (t[0] == "\0"):
            break
        else:
            if(t[i] == t[i+1]):
                k = 0
                while (k < leg(ti)):
                    t[k] = t[k+1]
                    k += 1

        print(t)


split("ssmmkkttiill", 2)
