from django.test import TestCase


class TestAccounts(TestCase):
    def test_get_register(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h2>Register</h2>", html=True)
        self.assertContains(response, "Username")
        self.assertContains(response, "Email")
        self.assertContains(response, "First name")
        self.assertContains(response, "Last name")
        self.assertContains(response, "Password")
        self.assertContains(response, "Password confirmation")
        self.assertContains(response, "Register")

    def test_post_register_valid_user(self):
        user = {
            "username": "john",
            "email": "john@doe.com",
            "password1": "notsecure1234",
            "password2": "notsecure1234",
            "first_name": "john",
            "last_name": "doe",
        }
        response = self.client.post("/accounts/register/", user, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Goto home")

    def test_post_register_invalid_user(self):
        user = {
            "username": "john",
            "password1": "notsecure1234",
            "password2": "notsecure1234",
            "first_name": "john",
            "last_name": "doe",
        }
        response = self.client.post("/accounts/register/", user, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h2>Register</h2>", html=True)
