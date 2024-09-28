Feature: OrangeHRM Login
  Scenario: Login page
    Given Launch chrome browser
    When open orange hrm homepage
    Then Login Page
    And close browser

  Scenario Outline: Login to oranageHRM with multiple parameters
    Given Launch chrome browser
    When open orange hrm homepage
    Then Login Page
    And close browser

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
