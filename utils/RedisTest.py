import redis


conn = redis.Redis(host='42.194.232.90', port=6379)

conn.set('19871455054', '123456', ex=600)

# conn.flushall()

print(conn.keys())

access_token = conn.get('access_token')
ticket = conn.get('ticket')

if access_token:
    print(access_token.decode('utf8'))
    print(ticket.decode('utf8'))
