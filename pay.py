#Takes the input of hours and rate/hour and figures out the pay
def main():
    hour = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    try:
        fh = float(hour)
        fr = float(rate)
    except:
        print('You must enter a number')
        quit()
    calc(fh, fr)

def calc(fh, fr):
    pay = fh * fr
    #Figures out the Bi-weekly or Bi-weekly with OT pay
    if fh <= 80 :
        print("Bi-weekly Pay:", pay)
        print("Monthly Pay:", float(pay) * 2)

    else:
        otp = (fh - 80.0) * (fr * 0.5)
        pay_ot = pay + otp
        print("Bi-weekly Pay with OT:", pay_ot)
        print("Monthly Pay with OT:", float(pay_ot) * 2)

if __name__ == '__main__' :
    main()

