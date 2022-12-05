@selenium
Feature: Cases

  @Test
  Scenario: Validate Cases
    Given login
    When select cases
    And select a case
    Then verify chat section
    And verify follow ups section
    And verify tasks section