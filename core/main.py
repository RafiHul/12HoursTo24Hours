x = input()
xrep = x.replace(":"," ")
xs = xrep.split(" ")
if xs[2] == "AM":
    if xs[0] == "00" and int(xs[0]) <= 11 and 0 <= int(xs[1]) <= 59:
        print(f"00:{xs[1]}")
    elif 00 <= int(xs[1]) <= 59 and int(xs[0]) <= 11:
        print(f"{xs[0]}:{xs[1]}")
if xs[2] == "PM":
    if xs[0] == "12":
        print(f"12:{xs[1]}")
    elif 1 <= int(xs[0]) <= 11:
        total = int(xs[0]) + 12
        print(f"{total}:{xs[1]}")