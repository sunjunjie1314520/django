import redis


conn = redis.Redis(host='42.194.232.90', port=6379)

# conn.set('15971345754', '415648', ex=300)

# conn.flushall()

print(conn.keys())

access_token = conn.get('access_token')
ticket = conn.get('ticket')

print(access_token)
print(ticket)
