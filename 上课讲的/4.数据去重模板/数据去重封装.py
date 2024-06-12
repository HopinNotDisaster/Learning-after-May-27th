import redis
import hashlib
import json


class DataFilter:
    # 默认的set_name为duplicate_data
    def __init__(self, set_name="duplicate_data"):
        self.redis_client = redis.Redis()
        self.set_name = set_name

    def is_duplicate(self, data: dict):
        hash_value = hashlib.md5(json.dumps(data).encode('utf-8')).hexdigest()

        if not self.redis_client.sismember(self.set_name, hash_value):
            self.redis_client.sadd(self.set_name, hash_value)
            print("新数据！", data)
            return False
        else:
            print("重复数据！", data)
            return True
    