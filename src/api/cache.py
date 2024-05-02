from cachetools import TTLCache

cache = TTLCache(maxsize=2000, ttl=float("inf"))
