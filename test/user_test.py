import unittest 
from src.models.user import User

class UserTest(unittest.TestCase):

    def test_should_create_a_user(self):
        ID = 1
        NAME = "John Snow"

        user = User(ID, NAME)

        self.assertEqual(user.id, ID)
        self.assertEqual(user.name, NAME)

    
if __name__ == '__main__':
    unittest.main()