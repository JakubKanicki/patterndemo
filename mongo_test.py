import pymongo
from database.database_mongo import DatabaseMongo

def main():
    print(pymongo.get_version_string())

    db = DatabaseMongo('localhost', 27017)

    db.add_note('hangout')
    db.add_note('shower')
    db.add_note('eat')

    for nt in db.get_all_notes():
        print(nt)

    print(db.get_note('shower'))

    db.update_note('eat', 'drink')

    for nt in db.get_all_notes():
        print(nt)

    db.drop_database_lol()


main()