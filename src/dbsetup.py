from app import create_app
from db import *

db.create_all(app=create_app())
