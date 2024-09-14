


def lemonadeChange(bills):

    bill_5 = 0
    bill_10 = 0
    bill_20 = 0


    for bill in bills:
        if bill == 5:
            bill_5 += 1

        elif bill == 10:
            if bill_5 == 0:
                return False
            bill_10 += 1
            bill_5 -= 1

        elif bill == 20:
            if (bill_10 > 0 and bill_5 > 0):
                bill_10 -= 1
                bill_5 -= 1
            elif bill_5 >= 3:
                bill_5 -= 3
            else:
                return False

    return True


bills = [5,5,5,10,20]

res = lemonadeChange(bills)

print(res)