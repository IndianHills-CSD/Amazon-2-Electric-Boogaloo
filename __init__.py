"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Amazon2.views
import Amazon2.dbHelper
import Amazon2.dbModels
