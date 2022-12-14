def values(a : int, b : int, c : int):
    d = 100
    e = 80
    for i in range(4):
        print(a, "/", b, "/", c)
        a = int(round(a*(d+e)/d,0))
        b = int(round(b*(d+e)/d,0))
        c = int(round(c*(d+e)/d,0))
        d += 80
        e += 7.5
        
