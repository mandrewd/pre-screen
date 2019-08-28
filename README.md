This a quick fix of that code from the junior developer.  We can `HSCAN` the hash, iterating over each user once.
 We check the hash value   

Really, we should store the `user_id` tokens in a redis `SET` for each day of the year, and then scan over each 
`user_id` in the set for the day we wish to process using the `SSCAN` operator.  That solution would work like this:
```python
r = redis.Redis(host='localhost', port=6379, db=0)
today = datetime.date.today()
month = today.month
day = today.day
collections.deque(map(sendBirthdayEmail,r.sscan_iter(f"{month}-{day}")))
```

Both `SSCAN` and `HSCAN` will run in `O(n)` time, where `n` is the number of items in the set or hash.