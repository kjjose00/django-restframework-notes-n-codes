from rest_framework.throttling import UserRateThrottle

class JackThrottleRate(UserRateThrottle):
    scope='jack'