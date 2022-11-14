#import modules (Local testing is found at the end of this script)
if __name__ != "__main__":
    from Data_Access.db_query import *
import datetime
import requests
import json

#Connect to SQL
if __name__ != "__main__":
    conn = create_connection()

#SQL for sender
def sqlsender(checkidsender):
    query = """\
            select customer_id, savingaccount, customer_name
            from dbo.customer_info
            where customer_id = '{}'
            """.format(checkidsender)

    checksender = execute_read_query(conn, query)

    for checkidS in checksender:
        if (checkidsender in checkidS[0]):
            print("Welcome " + str(checkidS[2]))
            return (True)


#SQL for receiver
def sqlreceiver(checkidreceiver):
    query = """\
            select customer_id, savingaccount, customer_name
            from dbo.customer_info
            where customer_id = '{}'
            """.format(checkidreceiver)
    checkreceiver = execute_read_query(conn, query)

    for checkidR in checkreceiver:
        if (checkidreceiver in checkidR[0]):
            print("Transfering to: " + str(checkidR[2]))
            return (True)


#SQL to check if transfer is eligible(whether the sender have enough money in his savings account)
def sqltransfer(checkeligible):
    query = """\
            select savingaccount
            from dbo.customer_info
            where customer_id = '{}'
            """.format(checkeligible)
    checktransfer = execute_read_query(conn, query)
    return(checktransfer[0][0])


#Put transaction records into SQL
def transaction_records(checkid,checkotherid,transaction_date,transfer,currency,amount):
    query = """\
        Insert into dbo.transaction_info values
        ('{}','{}','{}','{}','{}','{}')
        """ .format(checkid, checkotherid, transaction_date, transfer, currency.upper(), amount)
    execute_query_commit(conn, query)


#Update saving account of sender
def update_records_of_sender(checkid,transfer):
    query = """\
        select savingaccount
        from dbo.customer_info
        where customer_id = '{}'
        """.format(checkid)
    checksaving = execute_read_query(conn, query)
    checkinteger = checksaving[0][0]

    updatedatabase = """\
        UPDATE dbo.customer_info
        SET savingaccount = '{}'
        where customer_id = '{}'
        """.format(float(checkinteger) - float(transfer),checkid)
    execute_update_query_commit(conn, updatedatabase)


#Call API
def data(response_list,inputted_list):
    url = "https://coingecko.p.rapidapi.com/exchange_rates"

    headers = {
        'x-rapidapi-host': "coingecko.p.rapidapi.com",
        'x-rapidapi-key': "a57fa5904dmsh9afc0d45af51316p191bd4jsn172333859512"
        }

    response = requests.request("GET", url, headers=headers)
    response = response.json()


#Get accepted currencies in their full name(eg. Singapore Dollars) from json
    for money in response['rates']:
        acceptedcurrencies = response['rates'][money]['name'] + '(' + money + ')'
        response_list.append(acceptedcurrencies)
    for x in response_list:
            print(x)


#Clear list of accepted currencies   
    response_list.clear()


#Get currency rates from json
    for countryrates in response['rates']:
        response_list.append(countryrates)
        value = response['rates'][countryrates]['value']
        inputted_list.append(value)


#Local Testing
# Before running locally, at the Terminal,
#cd (change directory) to the business folder
if __name__ == "__main__":
    response_list = []
    inputted_list = []

    #Accepted API currencies
    print("Accepted currencies and their units -->")
    data(response_list,inputted_list)
    print("")

    #Hard coded SGD for local testing
    print("SGD rate for 1 bitcoin -->")
    print(inputted_list[response_list.index('sgd')])