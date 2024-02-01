Feature: login for test APK

  Scenario:Login Successfully
    Given I open the application
    When I enter my user
    Then I should see welcome text

  Scenario: Selecting Update States
    Given I open the application
    When I enter my user
    And select Update 1
    Then select Update 2