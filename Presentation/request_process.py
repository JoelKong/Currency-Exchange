from Business.transaction_process import *

def inputoutput():
    #Create list for json data
    response_list = []
    inputted_list = []
    #Define the transaction date and time as later need to call it
    transaction_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #Introduction
    print("Welcome to Definite Pte Ltd bitcoin money transfer system.")
    checksender = str(input("Please enter your Customer ID: "))
    #Get SQL data to check whether customer id is correct
    if sqlsender(checksender):
        checkreceiver = str(input("Please enter the Customer ID of the person you want to transfer to: "))
        if checksender != checkreceiver and sqlreceiver(checkreceiver):
            print("These are the current currency rates we have. \n")
            #Print out json data of accepted currencies
            data(response_list,inputted_list)
            print('')
            currency = str(input("What is the currency(not BTC) you want to convert to bitcoin and transfer in units?(Example:sgd) ").lower())
            if (currency not in response_list) or (currency == "btc" or currency == "BTC"):
                print("This is not a accepted currency. Please try again")
            else:
                print("These are your current rates as of " + str(transaction_date))
                #Print how much of their selected currency is worth 1 btc, using the json data
                print("1 BTC is equals to " + str(inputted_list[response_list.index(currency.lower())]) + ' ' + currency.upper())


                #Money transfer process
                transfer = float(input("How much " + currency.upper() + " would you like to convert to bitcoin and transfer? "))
                if transfer <= float(sqltransfer(checksender)):
                    confirmation = str(input("Confirm?(y/n) "))
                    if confirmation.lower() == 'y':
                        amount = (1 / float(inputted_list[response_list.index(currency.lower())])) * float(transfer)
                        print('Transaction completed! You have just transferred ' + str(amount) + ' btc.')

                        #Update records in both SQL tables
                        update_records_of_sender(checksender,transfer)
                        transaction_records(checksender,checkreceiver,transaction_date,transfer,currency,amount)
                        
                        
                else:
                    print("You do not have sufficient funds. Please try again.")


        else:
            print("You entered a wrong ID or tried to transfer to yourself. Please try again")
    else:
        print("You entered a wrong ID. Please try again")
