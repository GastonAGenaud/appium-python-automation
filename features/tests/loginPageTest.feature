Feature: login for test APK

  Scenario:Login Successfully
    Given I open the application
    When I enter my user and password
    Then I should see the successful login