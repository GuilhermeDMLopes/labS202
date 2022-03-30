from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("exercicioCRUD", "livros")


def create(nome, autor, ano, preco):
    return db.collection.insert_one({"nome": nome, "autor": autor, "ano": ano, "preco": preco})

def read():
    books =  db.collection.find({})
    writeAJson(books, "allbooks")


def update(nome, preco):
    return db.collection.update_one(
        {"nome": nome},
        {
            "$set": {"preco": preco},
            "$currentDate": {"lastModified": True}
        }
    )

def delete(nome):
    return db.collection.delete_one({"nome": nome})



create("RabbitMQ", "Alura", 1996, 210.6)
create("JavaScript", "Udemy", 2000, 482.4)
create("Java", "CursosOnline", 1990, 568.8)
create("Python", "SENAI", 1999, 640.2)


update("RabbitMQ", 200.2)
update("Java", 520.6)

read()

delete("Python")

