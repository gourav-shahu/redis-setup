import redis
import logging
import hashlib
import json
from typing import Optional, Any


class RedisUtility:
    def __init__(
        self,
        host: str,
        port: int,
        password: Optional[str] = None,
        db: int = 0,
        ssl: bool = False,
    ):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.ssl = ssl
        self.client = None
        self._initialize_client()

    def _initialize_client(self):
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
        Generate a hash-based cache key from a dictionary.
        :param data: Dictionary to hash.
        :return: MD5 hash as string.
        """
        return hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def set(self, key: str, value: Any, expiration: Optional[int] = None):
        try:
            self.client.set(key, value, ex=expiration)
        except Exception as e:
            logging.error(f"Error setting value in Redis: {e}")
            raise

    def get(self, key: str) -> Optional[str]:
        try:
            return self.client.get(key)
        except Exception as e:
            logging.error(f"Error getting value from Redis: {e}")
            return None

    def delete(self, key: str):
        try:
            self.client.delete(key)
        except Exception as e:
            logging.error(f"Error deleting key from Redis: {e}")
            raise

    def flush_all(self):
        try:
            self.client.flushall()
            logging.info("Flushed all keys from Redis!")
        except Exception as e:
            logging.error(f"Error flushing Redis keys: {e}")
            raise
