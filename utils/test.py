import redis
import chardet

conn = redis.Redis(host='47.98.213.63', port=6379)

print(conn.keys())

# conn.set('15971345754', '415648', ex=300)

# conn.flushall()

result = conn.get('15971345754')

print(result)

