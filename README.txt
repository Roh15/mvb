Group members:
Rohin Nanavati - 201801108
Shvani Nandani - 201801076

Changes made:
- txGenerator.py 
    - added lock_time in generateTransaction() (default value 0)
- Transaction.py 
    - added the node_name to class definition
    - added lock_time to class definition
- driver.py 
    - now the node that verifies a transaction is accredicted the transaction fee and block reward (in processUnverifiedTx())
    - added lock_time condition to processUnverifiedTx() -> if lock_time is >= chain length, the Transaction is verified, else not
    - added malleabilityAttack() function that changes the public key of a randomly selected unverified transaction

Instructions:
- to alter the transactions modify the transactions in txGenerator.py
- create an input folder in the directory
- create an output folder in the directory
- run >>>python txGenerator.py
- run >>>python driver.py input/transactions.json