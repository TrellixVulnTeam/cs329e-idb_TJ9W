
import os
import unittest
from models import Base, Book, Author, Publisher, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Book(id='1', title = 'TESTONE')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '1').one()
        self.assertEqual(str(r.id), '1')

        session.query(Book).filter_by(id = '1').delete()
        session.commit()

if __name__ == '__main__':
	unittest.main()