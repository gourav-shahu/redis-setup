from flask import Flask
from utils.redis_utility import RedisUtility
import os

redis_client = None


def init_extensions(app: Flask):
    global redis_client
    redis_client = RedisUtility(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        password=os.getenv("REDIS_PASSWORD"),
        ssl=True,
    )
    app.logger.info("Redis initialized successfully!")
