x = input()
xs = x.split()
xs2 = xs[0].split(":")
if xs[1] == "AM":
    if xs[0] == "00:00":
        print(xs[0])
    if int(xs2[0]) > 0:
        print("tes")
