import redis

# Redis connection settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# Connect to Redis server
def connect_to_redis():
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

# Test connection
if __name__ == "__main__":
    redis_conn = connect_to_redis()
    try:
        redis_conn.ping()
        print("Connected to Redis!")
    except redis.ConnectionError:
        print("Failed to connect to Redis.")
