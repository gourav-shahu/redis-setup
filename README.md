# Azure Redis Cache Setup

## Code Structure
backend/
├── app/
│   ├── controller.py  # Example API endpoint with Redis caching
├── utils/
│   ├── redis_utility.py           # Utility for Redis caching
│   ├── extensions.py              # Redis client setup
├── requirements.txt               # Python dependencies
├── .env                           # envrionment variables
└── runner.py                # flask App config 



## Step 1: Create a Redis Instance
Log in to Azure Portal.
Search for Redis Cache and select Create.
Fill in the required details:
Resource Group: Create or use an existing group.
DNS Name: Provide a unique name for your cache.
Pricing Tier: Select a tier (e.g., Basic C0).
Click Review + Create, then Create.

## Step 2: Access Connection Strings
Go to your Redis instance in Azure.
Navigate to Access Keys under Settings.
Copy the Primary Connection String and note the hostname and port.

## Installation Instructions
Clone the Repository
git clone https://github.com/gourav-shahu/redis-setup.git
cd redis-setup

Set up a .env file in the backend folder:
REDIS_HOST = "xxxxxxxx"
REDIS_PORT = 1234
REDIS_PASSWORD = "xxxxxxx"

Install Dependencies
pip install -r requirements.txt

Run the flask server
python runner.py
