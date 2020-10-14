"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Amazon2.views
