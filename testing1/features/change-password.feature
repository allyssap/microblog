Feature: As a registered user, I want to be able to change my password so that I can secure my account.

    Scenario: password not forgotten
        Given I am signed in and on my profile page
        When I click ‘edit my profile’
        Then click ‘change password’
        And enter my current password
        Then I will be prompted to set my new password