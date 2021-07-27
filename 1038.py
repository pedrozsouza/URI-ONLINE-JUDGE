cod1,qtde = input().split()

cod1 = int(cod1)
qtde = int(qtde)

if cod1 == 1:
    qtde = qtde * 4.00
    print("Total: R$ %0.2f" % qtde)
elif cod1 == 2:
    qtde = qtde * 4.50
    print("Total: R$ %0.2f" % qtde)
elif cod1 == 3:
    qtde = qtde * 5.00
    print("Total: R$ %0.2f" % qtde)
elif cod1 == 4:
    qtde = qtde * 2.00
    print("Total: R$ %0.2f" % qtde)
elif cod1 == 5:
    qtde == qtde * 1.50
    print("Total: R$ %0.2f" % qtde)




