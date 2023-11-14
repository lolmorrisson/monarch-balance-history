# monarch-balance-history

This is a super simple script that can take a transaction export CSV from monarch money and generate a balances.csv for upload. Use it when you have exported transactions from mint into Monarch.

## Basic Process ##

  1. Ensure you set the usual working path at the top of the script.
  2. Export transactions from Mint.
  3. Upload Mint exported CSV to Monarch. (This uploads the transactions but does not provide a balance history - so no pretty graph.
  4. Download the transactions from Monarch. (This just puts the input CSV into the right format).
       Could I have written this to accept the Mint CSV directly? Yes, but I started out with transactions from another source that were already in Monarch.
  5. Save the file as <prefix>_monarch_transactions.csv (The script will be expecting this. You can adjust if you like, but this helped me stay organized when converting a bunch of accounts).
  6. Execute this script. It will ask you two things;
      a. The current balance of this account - it uses this to work backwards through your transactions to calculate daily balances.
      b. The "prefix" or account name. This is what you used above when you saved the transaction file. The output will have the same format.
  7. If it goes well your balances CSV file will get saved into your defined working folder.
  8. Upload the balances file to Monarch. (Do so at your own risk - this may or may not work for you.
