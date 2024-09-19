from rest_framework import test
from rest_framework import status


class CourseTestCase(test.APITestCase):
    """Тестирование Course"""

    def setUp(self) -> None:
        self.client.post(
            "/users/register/",
            data={
                "username": "testname",
                "password": "123",
                "email": "testemail@ya.ru",
            },
        )
        response = self.client.post(
            "/users/login/", data={"email": "testemail@ya.ru", "password": "123"}
        )
        self.headers = {}
        self.headers["access"] = response.json().get("access")
        self.headers["refresh"] = response.json().get("refresh")

    def test_unregistered_user_creates_course(self):
        """Тестирование создания Курса незарегистрированным пользователем"""
        data = {"name": "Test case without login", "description": "Test description"}
        response = self.client.post("/lms/courses/", data=data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_registered_user_creates_course(self):
        """Тестирование создания Курса зарегистрированным пользователем"""
        data = {"name": "Test case", "description": "Test description"}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.headers['access']}")
        response = self.client.post(path="/lms/courses/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "user": {
                    "id": 1,
                    "username": "testname",
                },
                "id": 1,
                "count_lessons": 0,
                "lessons": [],
                "name": "Test case",
                "description": "Test description",
                "preview": None,
            },
        )

    def test_course_name_contains_valid_url(self):
        """Тестирование содержания валидной ссылки в имени курса без содержания описания"""
        data = {"name": "Курс https://youtube.com/free_course/"}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.headers['access']}")
        response = self.client.post(path="/lms/courses/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_name_contains_invalid_url(self):
        data = {"name": "Курс https://some_example.com/free_course/"}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.headers['access']}")
        response = self.client.post(path="/lms/courses/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(), {"non_field_errors": ["Поле содержит запрещенные ссылки"]}
        )
