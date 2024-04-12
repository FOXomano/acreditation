# python password_test.py -v
import unittest
from password import Password


#Тестовые примеры для тестирования методов расчета
#Вы всегда создаете дочерний класс, производный от unittest.TestCase
class TestPassword(unittest.TestCase):
  #Метод установки переопределяется из родительского класса TestCase
  def setUp(self):
    self.password = Password()

  #Каждый метод тестирования начинается с ключевого слова test_
  def test_validate_by_regexp(self):
    self.assertEqual(self.password.validate_by_regexp("qWer5ty"),
                     "Пароль имеет неправильный формат.")

  def test_validate_by_common_list(self):
    self.assertEqual(self.password.validate_by_common_list("qWer5%ty"),
                     "Не используйте такой распространенный пароль.")

  def test_validate_by_similarity(self):
    user_login = 'joda777jedi'
    email = 'jedimaster1@jediacademy.co'
    self.assertEqual(
        self.password.validate_by_similarity("jedimaster1", user_login, email),
        "Пароль слишком похож на пароль другого пользователя.")


if __name__ == "__main__":
  unittest.main()
