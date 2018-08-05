print "welcome to BillMaster v0.1"
# This application bills a 4 course meal for n number of people
 
coupon_amt = input("Enter Coupon Code Amount")
cust_no = input("Enter Number of Customers")
tax = input("enter tax percentage")
total_bill = []


def addtax(amt, perc):
    s = amt + (amt * (perc/100))
    return s

def adddisc(amt, disc):
    amt = amt - disc
    return amt
    
def bill(c):
    bill_amt_pt = 0
    
    for i in range(1, c+1):
        app_price = input("enter appertizer amount for customer " + str(i))
        start_price = input("enter starter amount for customer " + str(i))
        mc_price = input("enter main course amount for customer " + str(i))
        dessert_price = input("enter dessert amount for customer " + str(i))
        bill_amt = app_price + start_price + mc_price + dessert_price
        print "Total Bill for customer " + str(i) + " is " + str(bill_amt)
        total_bill.append(bill_amt)
        
    for j in total_bill:
        bill_amt_pt += j
    a = bill_amt_pt

    print "Bill Amount Pre-Tax is " + str(a)  

    b =  addtax(a, tax)
    
    print "Amount Post " + str(tax) + " percentage tax is " + str(b)
    final_bill = adddisc(b, coupon_amt)
    print "Amount Post-Discount is "  + str(final_bill)
    print "Your Bill Amount, Post tax and discount is === " + str(final_bill)


bill(cust_no)
    
        
    
