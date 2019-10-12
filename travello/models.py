from django.db import models


class Destination:

    id:int
    name:str
    desc:str
    img:str
    price:int
    offer:bool

    def __init__(self, id, name, desc, img, price, offer):
        self.id = id
        self.name = name
        self.desc = desc
        self.img = img
        self.price = price
        self.offer = offer