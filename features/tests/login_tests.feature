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


Scenario: Add a new post
    Given The user input an name
    When Select the details section
    And Click on the option Agregar un post
    And The user enters the title
    And The user enters the body
    And Click on the option Agregar
    Then Valid post was added

