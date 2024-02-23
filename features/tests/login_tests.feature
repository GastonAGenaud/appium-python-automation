Feature: Tests for MyWorkDoc application

Scenario: Successful Login
    Given The user input an name
    Then I am on main page


Scenario: title on the home page
    Given The user input an name
    Then Valid that the title of the home page is visible


Scenario: texts on the home page
    Given The user input an name
    Then Valid that the texts of the home page is visible

#fail
Scenario: buttons on the home page
    Given The user input an name
    When Select the Update State 1 button
    And Select the Update State 2 button
    And Select the Open Modal button
    And Select the Close Modal button
    And Select the Go to DetailScreen button
    Then I am on main page


Scenario: Pedidos Section
    Given The user input an name
    When Select the Pedidos section
    Then I am on main page


Scenario: Camera Section enabled
    Given The user input an name
    When Select the Camera section
    And Click on the option while using the app
    Then valid that the camera section is opened


Scenario: Camera Section disabled
    Given The user input an name
    When Select the Camera section
    And Click on the option Don't Allow
    Then Valid if the camera section is not open


Scenario: Details Section
    Given The user input an name
    When Select the details section
    Then  I validate the section titles
