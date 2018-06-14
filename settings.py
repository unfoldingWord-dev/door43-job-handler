print("settings.py got loaded")
# NOTE: These variable names are defined by the rq package

# TODO: Read the redis URL from an environment variable
REDIS_URL = 'redis://127.0.0.1:6379'
# You can also specify the Redis DB to use
# REDIS_HOST = 'redis.example.com'
# REDIS_PORT = 6380
# REDIS_DB = 3
# REDIS_PASSWORD = 'very secret'

# Queues to listen on
#QUEUES = ['high', 'normal', 'low']
QUEUES = ['Door43','dev-Door43'] # NOTE: The first queue in the list is processed first

# If you're using Sentry to collect your runtime exceptions, you can use this
# to configure RQ for it in a single step
# The 'sync+' prefix is required for raven: https://github.com/nvie/rq/issues/350#issuecomment-43592410
#SENTRY_DSN = 'sync+http://public:secret@example.com/1'
