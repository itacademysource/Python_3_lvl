from unittest import TestCase, main, TestSuite, makeSuite

from ..database import Database


class InsertTest(TestCase):

    def setUp(self) -> None:
        self.db = Database('login_bot/tests/test.db')

    def test_insertion(self):
        """Тестирование вставки

        :return:
        """
        _input = self.db.add_user(123456)
        output = {'status': 'OK'}
        self.assertEqual(_input, output)

    def test_read_db(self):
        """Тестирование чтения из БД

        :return:
        """
        output = [(1, 123456, None, 0, 'setusername')]
        self.assertEqual(self.db.read_db(), output)

    def test_user_exists(self):
        """Тестирование существования пользователя в БД

        :return:
        """
        self.assertEqual(self.db.user_exists(123456), True)

    def test_set_username(self):
        """Тестирование отправки username-а

        :return:
        """
        self.assertEqual(self.db.set_username(123456, 'User'), True)

    def test_set_signup(self):
        """Тестирование отправки подтверждения регистрации

        :return:
        """
        self.assertEqual(self.db.set_signup(123456, 'done'), True)

    def tearDown(self):
        self.db.connection.close()


class GetTest(TestCase):
    def setUp(self) -> None:
        self.db = Database('login_bot/tests/test.db')

    def test_get_username(self):
        """Тестирование получения username-а

        :return:
        """
        self.assertEqual(self.db.get_username(123456), 'User')

    def test_get_signup(self):
        """Тестирование получения подтверждения регистрации

        :return:
        """
        self.assertEqual(self.db.get_signup(123456), 'done')

    def tearDown(self):
        self.db.connection.close()


class DeleteTest(TestCase):
    def setUp(self) -> None:
        self.db = Database('login_bot/tests/test.db')

    def test_delete_user(self):
        """
        Тестирование удаления пользователя
        :return:
        """
        self.assertEqual(self.db.delete_user(123456), True)

    def tearDown(self):
        self.db.connection.close()


if __name__ == '__main__':
    main()
