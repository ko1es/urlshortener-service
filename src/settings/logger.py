LOGGER_CONFIG = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'detailed': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s.%(msecs)03d [%(levelname)s] [%(processName)s] in %(pathname)s:%(lineno)d %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'detailed',
            }
        },
        'loggers': {
            'foo': {
                'handlers': ['console']
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
}
