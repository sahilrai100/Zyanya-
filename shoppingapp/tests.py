from unittest import mock

from django.core import mail
from django.test import Client, TestCase, override_settings
from django_recaptcha.client import RecaptchaResponse

# Create your tests here.

RECAPTCHA_PATCH = mock.patch(
    "django_recaptcha.fields.client.submit",
    return_value=RecaptchaResponse(is_valid=True),
)


def register(client, username, email, phone):
    return client.post("/register/", {
        "username": username,
        "email": email,
        "password1": "S0meStrongPass!23",
        "password2": "S0meStrongPass!23",
        "phone": phone,
        "captcha": "dummy",
        "g-recaptcha-response": "dummy",
    })


def sent_otp(email):
    for m in mail.outbox:
        if email in m.to:
            return m.body.split("your otp is")[1].split(" this otp")[0].strip()
    raise AssertionError(f"no registration email found for {email}")


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class RegistrationOtpTests(TestCase):
    def test_each_registration_gets_its_own_otp(self):
        with RECAPTCHA_PATCH:
            register(Client(), "otp_user_one", "otp_one@example.com", "9999999999")
            register(Client(), "otp_user_two", "otp_two@example.com", "8888888888")

        otp_one = sent_otp("otp_one@example.com")
        otp_two = sent_otp("otp_two@example.com")
        self.assertNotEqual(otp_one, otp_two)

    def test_otp_is_scoped_to_the_registering_session(self):
        client_one = Client()
        client_two = Client()
        with RECAPTCHA_PATCH:
            register(client_one, "otp_user_three", "otp_three@example.com", "7777777777")
            register(client_two, "otp_user_four", "otp_four@example.com", "6666666666")

        otp_for_user_three = sent_otp("otp_three@example.com")

        # Submitting user three's OTP on user four's session must not verify.
        response = client_two.post("/validation/", {"otp": otp_for_user_three})
        self.assertContains(response, "otp is not verified")

        # But it does verify on the session that actually requested it.
        response = client_one.post("/validation/", {"otp": otp_for_user_three}, follow=True)
        self.assertEqual(response.redirect_chain[0][0], "/login/")
