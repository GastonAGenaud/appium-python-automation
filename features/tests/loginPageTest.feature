Feature: login for test APK

  Scenario:Login Successfully
    Given I open the application
    When I enter my user
    Then I should see welcome text

  Scenario: Select bottom options
    Given I open the application
    When I enter my user
    And I select Details option
    And I select Pedidos option
    Then I select Camera option