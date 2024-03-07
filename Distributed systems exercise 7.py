#!/usr/bin/env python
# coding: utf-8

# **User service**

# In[ ]:


# user_service.py
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Simple in-memory "database" for demonstration purposes
users_db = {}

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    if username in users_db:
        return jsonify({'message': 'User already exists'}), 400

    # In a real application, you'd also validate the password and perhaps store more user information
    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)


# **Wallet service**

# In[ ]:


# wallet_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory "database" for demonstration purposes
wallets_db = {}

@app.route('/balance/<username>', methods=['GET'])
def get_balance(username):
    balance = wallets_db.get(username, 0)
    return jsonify({'username': username, 'balance': balance})

@app.route('/transaction', methods=['POST'])
def process_transaction():
    data = request.get_json()
    sender = data['sender']
    receiver = data['receiver']
    amount = data['amount']
    
    if sender not in wallets_db or wallets_db[sender] < amount:
        return jsonify({'message': 'Insufficient funds'}), 400

    wallets_db[sender] -= amount
    wallets_db[receiver] = wallets_db.get(receiver, 0) + amount
    return jsonify({'message': 'Transaction successful'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)


# **Testing the service**

# You can test these services using tools like Postman or curl to make HTTP requests. Here are examples of how you might test the user registration and process a transaction:
# 
# Register a User: Send a POST request to http://localhost:5001/register with a JSON body like {"username": "john_doe", "password": "secure_password"}.
# Check Balance: Send a GET request to http://localhost:5002/balance/john_doe to see the balance.
# Process a Transaction: Send a POST request to http://localhost:5002/transaction with a JSON body like {"sender": "john_doe", "receiver": "jane_doe", "amount": 100}.

# In[ ]:




