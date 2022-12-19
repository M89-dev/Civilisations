def resources(a : int, b : int, c : int):
    d = 100
    e = 80
    for i in range(4):
        print(a, "/", b, "/", c)
        a = int(round(a*(d+e)/d,0))
        b = int(round(b*(d+e)/d,0))
        c = int(round(c*(d+e)/d,0))
        d += 80
        e += 7.5
        
def health(a : int):
    b = 20
    print(a)
    for i in range(3):
        print(int(round(a*(100+b)/100)))
        b += 30

resources(50, 10, 25)
print("\n")
health(100)