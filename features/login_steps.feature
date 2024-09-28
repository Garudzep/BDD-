Feature: User Login

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter "username" and "password"
    And I click the login button
    Then I should see the dashboard

  Scenario: Unsuccessful login with invalid credentials
    Given I am on the login page
    When I enter "invalid_username" and "invalid_password"
    And I click the login button
    Then I should see an error message

  Scenario: User clicks "Forgot Password"
    Given I am on the login page
    When I click the "Forgot Password" link
    Then I should be redirected to the password recovery page
