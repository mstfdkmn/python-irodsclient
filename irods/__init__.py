from .version import __version__

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Magic Numbers
MAX_PASSWORD_LENGTH = 50
MAX_SQL_ATTR = 50
MAX_PATH_ALLOWED = 1024
MAX_NAME_LEN = MAX_PATH_ALLOWED + 64
RESPONSE_LEN = 16
CHALLENGE_LEN = 64
MAX_SQL_ROWS = 256
DEFAULT_CONNECTION_TIMEOUT = 120

AUTH_SCHEME_KEY = 'a_scheme'
AUTH_USER_KEY = 'a_user'
AUTH_PWD_KEY = 'a_pw'
AUTH_TTL_KEY = 'a_ttl'

NATIVE_AUTH_SCHEME = 'native'

GSI_AUTH_PLUGIN = 'GSI'
GSI_AUTH_SCHEME = GSI_AUTH_PLUGIN.lower()
GSI_OID = "1.3.6.1.4.1.3536.1.1"  # taken from http://j.mp/2hDeczm

PAM_AUTH_PLUGIN = 'PAM'
PAM_AUTH_SCHEME = PAM_AUTH_PLUGIN.lower()
