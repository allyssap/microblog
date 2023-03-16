Feature: As a registered user, I want to be able to delete my account so that I can close my account.
    
    Scenario: Account deleted
        Given I am signed into my account
        When I click on the ‘edit my profile’
        Then click the ‘delete account’
        And click ‘yes’ on the ‘Are you sure?’ prompt
        Then my account will be deleted