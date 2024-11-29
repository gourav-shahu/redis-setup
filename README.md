# Azure Redis Cache Setup

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

## Folder Structure
runner.py
The entry point of the Flask application. It initializes the app, extensions, and routes.

extensions.py
Contains the initialization code for third-party extensions, including the Redis utility. The init_extensions function sets up the Redis client using the utility.

utils/redis_utility.py
A reusable utility class for Redis integration. Provides methods to connect to a Redis server, set, get, delete cache, and compute cache keys. This file can be used across different projects.

controllers/controller.py
Demonstrates how to use the Redis utility in a Flask API controller. It includes caching logic to optimize API responses.
