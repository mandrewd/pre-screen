import redis


# placeholder for the externally defined function
def sendBirthdayEmail():
    pass


def birthdayEmailer():
    # the redis config values should be obtained from config, not passed in
    r = redis.Redis(host='localhost', port=6379, db=0)
    today = datetime.date.today()
    for ut in r.hscan_iter('users'):
        keys = ut[::2]
        vals = ut[1::2]
        user = dict(zip(keys, vals))
        d = datetime.datetime.strptime(user['birthday'], "%Y-%m-%dT%H:%M:%S%z").date()
        if d.month == today.month and d.day == today.month:
            sendBirthdayEmail()


if __name__ == main:
    birthdayEmailer()
