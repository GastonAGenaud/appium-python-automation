@selenium
Feature: Login

  @Test
  Scenario: User Login
    Given validate application open
    When complete username field
    And complete password field
    And tap Login button
    Then verify Login