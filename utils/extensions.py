from flask import Flask
from utils.redis_utility import RedisUtility
import os

redis_client = None


def init_extensions(app: Flask):
    """
    Initialize extensions for the Flask application, including the Redis client.

    This function sets up a Redis client using environment variables for the
    connection parameters. It creates a global `redis_client` instance that can
    be used across the application. Additionally, it logs the successful
    initialization of Redis.

    :param app: The Flask application instance.
    """
    global redis_client
    redis_client = RedisUtility(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        password=os.getenv("REDIS_PASSWORD"),
        ssl=True,
    )
    app.logger.info("Redis initialized successfully!")
