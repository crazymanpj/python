#encoding=utf-8
import redis

r = redis.Redis(host="10.20.224.33", port=6379, db=0)
r.set('name', 'zhangsan')
print(r.get('name'))