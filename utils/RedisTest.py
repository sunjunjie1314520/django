import redis


conn = redis.Redis(host='47.98.213.63', port=6379)

print(conn.keys())

# conn.set('15971345754', '415648', ex=300)

access_token = conn.get('access_token')
ticket = conn.get('ticket')

print(access_token)
print(ticket)

# 清除
# conn.flushall()