x = int(input())
while (x > 0):
    x -= 1
    y,z = input().split()
    y = int(y)
    z = int(z)
    if (y + z) == 0:
        music = "PROXYCITY"
    elif (y + z) == 1:
        music = "P.Y.N.G."
    elif (y + z) == 2:
        music = "DNSUEY!"
    elif (y + z) == 3:
        music = "SERVERS"
    elif (y + z) == 4:
        music = "HOST!"
    elif (y + z) == 5:
        music = "CRIPTONIZE"
    elif (y + z) == 6:
        music = "OFFLINE DAY"
    elif (y + z) == 7:
        music = "SALT"
    elif (y + z) == 8:
        music = "ANSWER!"
    elif (y + z) == 9:
        music = "RAR?"
    elif (y + z) == 10:
        music = "WIFI ANTENNAS"
    print(music)

