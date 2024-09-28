Feature: Fb Login Page
  Scenario Outline: Login pages
    Given Launch chrome browsers
    When open Fb homepage
    Then Enter User name And Password
    And close browsers

   Examples:
    |  username  |  password  |
    |  1235674   |  adfdfsddd |
    |  9623873895|Garudzep@10 |