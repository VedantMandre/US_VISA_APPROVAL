import sys
import urllib
import os
import logging
import pymongo
import urllib.parse

# Define the USvisaException class
class USvisaException(Exception):
    def __init__(self, error_detail):
        self.error_detail = error_detail
        super().__init__(error_detail)

# Define constants
CONNECTION_URL = "mongodb+srv://vedantmandre29498:Vedant29@@cluster0.o6df7g2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"

class MongoDBClientException(Exception):
    pass

class MongoDBClient:
    client = None

    def __init__(self, connection_url=CONNECTION_URL, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                # Parse connection URL
                parsed_url = urllib.parse.urlparse(connection_url)

                # Extract username and password
                username = urllib.parse.quote_plus(parsed_url.username)
                password = urllib.parse.quote_plus(parsed_url.password)

                # Reconstruct netloc with escaped username and password
                netloc = f"{username}:{password}@{parsed_url.hostname}"
                if parsed_url.port:
                    netloc += f":{parsed_url.port}"

                # Reconstruct connection URL with escaped username and password
                escaped_url = urllib.parse.urlunparse(parsed_url._replace(netloc=netloc))

                # Connect to MongoDB
                MongoDBClient.client = pymongo.MongoClient(escaped_url)
                
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.collection = self.database[COLLECTION_NAME]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise MongoDBClientException(str(e))

# Usage example
try:
    mongo_client = MongoDBClient()
    # Use mongo_client.collection for further operations
except MongoDBClientException as e:
    logging.error(f"Failed to initialize MongoDB client: {e}")
    sys.exit(1)
