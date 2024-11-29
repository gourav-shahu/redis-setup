import redis
import logging
import hashlib
import json
from typing import Optional, Any


class RedisUtility:
    """
    RedisCache utility for managing Redis operations.

    Provides methods to connect to Redis, store, retrieve, and delete cached data,
    and decorate functions for caching their responses.

    Attributes:
        client (redis.StrictRedis): Redis client instance for performing operations.
    """
    def __init__(
        self,
        host: str,
        port: int,
        password: Optional[str] = None,
        db: int = 0,
        ssl: bool = False,
    ):
        """
        Initialize the RedisCache object.

        :param host: Redis server hostname or IP.
        :param port: Redis server port.
        :param password: Redis password, if applicable.
        """
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.ssl = ssl
        self.client = None
        self._initialize_client()

    def _initialize_client(self):
        """
        Establish connection to the Redis server.
        """
        try:
            self.client = redis.StrictRedis(
                host=self.host,
                port=self.port,
                password=self.password,
                db=self.db,
                ssl=self.ssl,
                decode_responses=True,  # Ensures string responses
            )
            # Check connection
            self.client.ping()
            logging.info("Connected to Redis successfully!")
        except redis.ConnectionError as e:
            logging.error(f"Failed to connect to Redis: {e}")
            raise

    def compute_cache_key(self, data: dict) -> str:
        """
        Generate a unique hash-based cache key.

        :param key_data: The data used to generate the cache key.
        :return: A hashed string key.
        """
       
        return hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def set(self, key: str, value: Any, expiration: Optional[int] = None):
        """
        Set a value in Redis.

        :param key: Cache key.
        :param value: Value to cache.
        :param ttl: Time-to-live in seconds (optional).
        """
        try:
            self.client.set(key, value, ex=expiration)
        except Exception as e:
            logging.error(f"Error setting value in Redis: {e}")
            raise

    def get(self, key: str) -> Optional[str]:
        """
        Retrieve a value from Redis.

        :param key: Cache key.
        :return: Cached value if exists, otherwise None.
        """
        try:
            return self.client.get(key)
        except Exception as e:
            logging.error(f"Error getting value from Redis: {e}")
            return None

    def delete(self, key: str):
        """
        Delete a key from Redis.

        :param key: Cache key to delete.
        """
        try:
            self.client.delete(key)
        except Exception as e:
            logging.error(f"Error deleting key from Redis: {e}")
            raise

    def flush_all(self):
        """
        Delete All key data from Redis.
        """
        try:
            self.client.flushall()
            logging.info("Flushed all keys from Redis!")
        except Exception as e:
            logging.error(f"Error flushing Redis keys: {e}")
            raise
