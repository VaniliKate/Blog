import unittest
from app.models import User, Category
class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(f_name = 'Grishon', l_name = 'Gikima', email = 'grishon.nganga01@gmail.com', password_hash = '123@Iiht')
        self.category = Category(name = 'sports')


    def test_user_init(self):
        self.assertTrue(self.new_user.f_name is not None)
        self.assertTrue(self.new_user.l_name is not None)
        self.assertTrue(self.new_user.email is not None)
        self.assertTrue(self.new_user.password_hash is not None)

        self.assertEqual(self.new_user.f_name, 'Grishon')
        self.assertEqual(self.new_user.l_name, 'Gikima')
        self.assertEqual(self.new_user.email, 'grishon.nganga01@gmail.com')
        self.assertEqual(self.new_user.password_hash, '123@Iiht')

    def test_categories(self):
        self.assertTrue(self.category.name is not None)
        
        self.assertEqual(self.category.name, 'sports')