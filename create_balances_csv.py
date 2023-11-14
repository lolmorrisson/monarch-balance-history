import pandas as pd

def generate_balances_csv(current_balance, file):
    
    # update the below to your usual working folder/filename preferences
    folder = 'C:\\Users\\lol\\SynologyDrive\\Documents\\mint_monarch\\'
    input_file = folder + file + '_monarch_transactions.csv'
    output_file = folder + file + '_monarch_balances.csv'
    
    transactions = pd.read_csv(input_file)

    balances = []
    previous_balance = current_balance
    
    for index, row in transactions.iterrows():
    
        current_balance -= row['Amount']
        account = row['Account']
        current_balance = round(current_balance, 2)
        balances.append({'Date': row['Date'], 'Balance': previous_balance, 'Account': account})
        previous_balance = current_balance

    balances_df = pd.DataFrame(balances)
    balances_df.drop_duplicates(subset='Date', keep='first', inplace=True)

    balances_df.to_csv(output_file, index=False)
    print(f"Left over amount: {previous_balance}")
    return output_file

current_balance = float(input("Enter the current balance:"))
file = input("Enter the file prefix:")

balances_csv_path = generate_balances_csv(current_balance, file)
print(f'Balances CSV file saved at: {balances_csv_path}')
