import allure
import pytest


@pytest.mark.skip
@pytest.mark.usefixtures("setup_authorization_window")
class TestAuthorizationPage:

    @pytest.mark.run(order=1)
    @allure.title("Verify that warning message is displayed provided that password field is mot populated")
    def test_verify_warning_message_displayed_for_missed_password_field(self, setup_authorization_window):
        setup_authorization_window.is_warning_message_displayed_for_not_populated_password()

    @pytest.mark.run(order=2)
    @allure.title("Verify that warning message is displayed provided that name field is mot populated")
    def test_verify_warning_message_displayed_for_missed_name_field(self, setup_authorization_window):
        setup_authorization_window.is_warning_message_displayed_for_not_populated_name_field()
