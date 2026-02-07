Feature: User Login Functionality

  As a user
  I want to be able to login to the application
  So that I can access my account

  Background:
    Given I navigate to the login page

  Scenario: Successful login with valid credentials
    When I enter username "student" and password "Password123"
    And I click the Submit button
    Then I should see the success message "Congratulations student. You"
    And I should see the logout link
    And I should be on the logged-in page

  Scenario: Failed login with invalid username
    When I enter username "incorrectUser" and password "Password123"
    And I click the Submit button
    Then I should see an error message
    And I should see error text "Your username is invalid!"

  Scenario: Failed login with invalid password
    When I enter username "student" and password "incorrectPassword"
    And I click the Submit button
    Then I should see an error message
    And I should see error text "Your password is invalid!"