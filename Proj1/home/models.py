from cgi import print_exception
from django.db import models

# Create your models here.
class Destination:
    name : str
    price : int
    img : str
    id : int
    desc : str
    offer : bool