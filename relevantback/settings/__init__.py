import os
from .base import *
from dotenv import load_dotenv
load_dotenv(BASE_DIR / '.env')
if os.environ.get('relevant') == 'prod':
    from .prod import *
else:
    from .dev import *
