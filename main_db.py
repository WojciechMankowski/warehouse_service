from Magazyn.Database import database
db = database()
# db.CreatingTabels()
db.dowlaod_all()
db.returnDICT("weight")
food = [
    ("Fasila biała", 10.00, 'kg', 3.0),
]
# db.add(food)
pr = {"Fasila biała": 3.50}
order = {"2233": pr}
db.updete(order)
