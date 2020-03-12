import copy

MODULES_MARKET = 'mumarket'
MODULES_MALL = 'mumall'
MODULES_MUQY = 'muqy'
MODULES_APP = 'app'
MODULES_ARK = 'ark'
MODULES_MALLCRM = 'mall_crm'

ENV_LOCAL = 'local'
ENV_DEV = 'dev'
ENV_TEST = 'test'
ENV_PROD = 'prod'

DB_config = {
    ENV_LOCAL: {
        'host': '127.0.0.1',
        'username': 'root',
        'password': 'root',
        'port': 3306,
        'default_db': {
            MODULES_MARKET: 'test',
        }
    },
    ENV_DEV: {
        'host': '120.132.6.206',
        'username': 'root',
        'password': 'Matchu#2016',
        'port': 3306,
        'default_db': {
            MODULES_MARKET: 'mumarket',
            MODULES_MALL: 'mumall',
        }
    },
    ENV_TEST: {
        'host': '120.132.27.174',
        'username': 'root',
        'password': 'Matchu#2016',
        'port': 3306,
        'default_db': {
            MODULES_MARKET: 'mumarket',
            MODULES_MALL: 'mumall',
        }
    },
    ENV_PROD: {}
}

redis_config = {
    ENV_DEV: {
        'hostname': '120.132.6.206',
        'port': 6379,
        'password': 'matchu_2016'
    },
    ENV_TEST: {
        'hostname': '120.132.27.174',
        'port': 6379,
        'password': '9BqhaCbQ'
    },
    ENV_PROD: {},
}

host_config = {
    MODULES_MARKET: {
        ENV_DEV: 'http://cs-market.immatchu.com/',
        ENV_TEST: 'http://itest-market.immatchu.com/',
        ENV_PROD: 'https://market.immatchu.com/'
    },
    MODULES_MALL: {
        ENV_DEV: 'http://cs-muqy.immatchu.com/mugback/',
        ENV_TEST: 'http://itest-muqy.immatchu.com/mugback/',
        ENV_PROD: ''
    },
    MODULES_MUQY: {
        ENV_DEV: '',
        ENV_TEST: '',
        ENV_PROD: ''
    },
    MODULES_APP: {
        ENV_DEV: '',
        ENV_TEST: 'http://itest-mall-api.immatchu.com/',
        ENV_PROD: ''
    },
    MODULES_ARK: {
        ENV_DEV: 'http://cs-ark-api.immatchu.com/',
        # ENV_TEST: 'http://itest-ark-api.immatchu.com/',
        ENV_TEST: 'http://itest-ark-api.immatchu.com/',
    },
    MODULES_MALLCRM: {
        ENV_DEV: 'http://cs-mall-crm.immatchu.com/api/',
        ENV_TEST: 'http://itest-mall-crm.immatchu.com/api/',
    }
}


def get_db_config(modules=MODULES_MARKET, env=ENV_DEV):
    result = copy.deepcopy(DB_config[env])
    result['default_db'] = result['default_db'][modules]
    return result


def get_redis_config(env=ENV_DEV):
    return redis_config[env]


def get_host(modules, env=ENV_DEV):
    return host_config[modules][env] if host_config[modules][env] is not None else ''


def get_full_url(api, modules=MODULES_MARKET, env=ENV_DEV):
    return get_host(modules=modules, env=env) + api
