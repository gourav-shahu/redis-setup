# This is an example of realtime code usage in APIs

from flask import current_app, jsonify, request
from utils.extensions import redis_client
import json


class MyController:
    def post(self):
        # Generate cache key using RedisUtility
        request_data = request.get_json()
        cache_key = redis_client.compute_cache_key(request_data)

        # Check if response exists in cache
        cached_response = redis_client.get(cache_key)
        if cached_response:
            current_app.logger.info("Returning cached response")
            return jsonify(json.loads(cached_response)), 200

        # Perform expensive operation
        response_data = {"message": "Processed data"}  # Replace with actual processing
        redis_client.set(
            cache_key, json.dumps(response_data), expiration=3600
        )  # Cache for 1 hour

        return jsonify(response_data), 200
