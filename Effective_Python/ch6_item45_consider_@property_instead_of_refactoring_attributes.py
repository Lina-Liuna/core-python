# Advanced but common use of @property is: transitioning what was once a simple numerical attribute
# into an on-the-fly calculation.

# this is extremely helpful because it lets you migrate all existing usage of a class to have new behviors
# without requiring any of the call sites to be rewritten.

# @property provides an important stopgap for improving interfaces over time.

# Example: Implement a leaky bucket quota.
# the bucket class represents how much quota remains and the duration for which the quota will be available.
import datetime

class Bucket:
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return(f'Bucket(max_quota={self.max_quota}'
               f'quota_consumed={self.quota_consumed})')

    # To match the previos interface of the original bucket class, I use @property method to compute the current
    # level of quota on-the-fly using these new attributes
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # Quota being reset for a new period
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # Quota being filled for the new period
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # Quota being consumed during the period
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


def fill(bucket, amount):
    now = datetime.datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False  # Bucket hasn't been filled this period
    if bucket.quota - amount < 0:
        return False  # Bucket was filled, but not enough
    bucket.quota -= amount
    return True  # Bucket had enough, quota consumed

bucket = Bucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)
if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')

# why we like using @property?
# @property lets you make incremental progress toward a better data model over time.

# Things-to-Remember:
# 1. Use @property to give existing instance attributes new functionality.
# 2. Make incremental progress towards better data models by using @property.
# 3. consider refactoring a class and all call sites when you find yourself using @property too heavily.
