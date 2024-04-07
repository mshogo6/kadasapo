import sys
sys.path.insert(0, '/app')
sys.path.insert(0, '/usr/local/lib/python3.11/site-packages')

import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

from app import app as application
