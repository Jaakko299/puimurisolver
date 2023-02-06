while (1):
    print("1. Laske Jännite")
    print("2. Laske Resistanssi")
    print("3. Laske Virta")
    print("4. Lopeta")
    ask = input("> ")
    if (ask == "1"):
        print("-- Lasketaan jännitettä --")
        i = float(input("Virta: "))
        r = float(input("Resistanssi: "))
        v = i * r
        print("Jännite = ", format(v, ".2f"))

    elif(ask == "2"):
        print("-- Lasketaan resistanssi --")
        v = float(input("Jännite: "))
        i = float(input("Virta: "))
        r = v / i
        print("Resistanssi = ", format(r, ".2f"))

    elif(ask == "3"):
        print("-- Lasketaan Virta --")
        v = float(input("Jännite: "))
        r = float(input("Resistanssi: "))
        i = v / r
        print("Current = ", format(i, ".2f"))

    elif(ask == "4"):
        break
    else:
        print("Error")