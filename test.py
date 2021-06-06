import unittest
from order import Order
from user import User 

class TestUser(unittest.TestCase):
    def setUp(self):
        u=User(12345, 'P@ssword1', 'cpestana','Pestana', 'Christine', 'cpestana@yahoo.com')
    def test_Id(self):
        self.assertEqual(self.u.getuserID, 12345)
    def test_userpassword(self):
        self.assertEqual(self.u.getUserPassword(), 'P@ssword1')
    def test_username(self):
        self.assertEqual(self.u.getUserName(), 'cpestana')
    def test_userlastname(self):
        self.assertEqual(self.u.getLastName(), 'Pestana')
    def test_userfirstname(self):
        self.assertEqual(self.u.getFirstName(), 'Christine')
    def test_useremail(self):
        self.assertEqual(self.u.getEmail(), 'cpestana@yahoo.com')
    def test_ToString(self):
        self.assertEqual(str(self.u), 'P@ssword1 cpestana Pestana Christine cpestana@yahoo.com')

class TestOrder(unittest.TestCase):
    def setUp(self):
        o=Order(1234, '06/06/2021', 'awaiting', '25')
    def test_Id(self):
        self.assertEqual(self.o.getOrderID, 1234)
    def test_orderdate(self):
        self.assertEqual(self.o.getOrderDate(), '06/16/2021')
    def test_orderstatus(self):
        self.assertEqual(self.o.getOrderStatus(), 'awaiting')  
    def test_totalamount(self):
        self.assertEqual(self.o.getTotalAmount(), '25')
    def test_ToString(self):
        self.assertEqual(str(self.o), 'awaiting')