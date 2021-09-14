shares = []
buy = []
sell = []


def lossorprofit():
    val_buy = 0
    total_buy = 0
    val_sell = 0
    total_sell = 0
    strt = 0
    
    while True:
        if shares[strt] !='0':
            val_buy = shares[strt] * buy[strt]
            total_buy = total_buy + val_buy
            val_sell = shares[strt] * sell[strt]
            total_sell = total_sell + val_sell
            strt = strt +  1
    
    if total_buy > total_sell:
        difference = total_buy- total_sell 
        print ("loss of :" , difference)
    if total_sell > total_buy:
        difference = total_sell-total_buy
        print("profit of :" , difference)





def buying():
    global shares , buy , sell 
    quantity = input("Enter the number of shares: ") 
    shares.append(quantity)
    price = input("Input the price for share : ")
    buy.append(price) 
    
    
    


def selling(): 
    index=0
    while True:
        if shares[index] > 0 :
            price = input("Input selling price : ")
            sell.append(price)
            index = index + 1
        
        Lp_end = input("Do you want to sell more? : YES OR NO : ")
        if Lp_end == 'YES' or 'yes':
            break




choice = input("1: Selling  ,  2:Buying , 3:Captial gain or loss :    " )
while True:
    if choice == '1':
        selling()
        choice = 0
    if choice == '2':
        buying()
        choice = 0
    if choice == '3':
        lossorprofit()
        choice = 0






