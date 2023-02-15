#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def save_file(x):
    with open('my_file.txt', 'a') as f:
        my_file.write()
        return(str(x))


# In[ ]:


def menu():
    print('Welcome to your checkbook! \nMenu \n1. View current balance','\n2. Add a debit transaction','\n3. Add a credit transaction','\n4. Exit')
    selection = input('Please make a selection: ')
    if selection == '1':
        current_balance()
    elif selection == '2':
        debit_transaction()
    elif selection == '3':
        credit_transaction()
    elif selection == '4':
        exit()
    return selection


# In[20]:


menu()


# ### View current balance

# In[5]:


def current_balance():
    import os
    if os.path.exists('my_file.txt'):
        print('Congrats! Your checkbook exists!')
        with open('my_file.txt', 'r') as f:
            lines = f.readlines()
        print(lines)
    else:
        print('That checkbook does not exist, but no worries I made it for you!')
        with open('my_file.txt', 'w') as f:
            f.write('current balance: 0')
    
    menu()
current_balance()


# ### Add a debit (withdraw)

# In[8]:


def debit_transaction():
    transaction = {
        'date': input('date: '),
        'description': input('description: '),
        'dollar_amount': input('dollar amount: ')
    }
    save_file(transaction)
    menu()
    return(transaction)

debit_transaction()


# ### Add a credit (deposit)

# In[9]:


def credit_transaction():
    transaction = {
        'date': input('date: '),
        'description': input('description: '),
        'dollar_amount': input('dollar amount: ')
    }
    save_file(transaction)
    menu()
    return(transaction)

credit_transaction()


# In[ ]:





# In[ ]:




