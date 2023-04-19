Feature: As a registered user, I want to be able to set a security question so I may change my password in case I forget it
    
    Scenario: Set question
        Given I am signed in and at my profile page
        When I clicking ‘edit my profile’
        Then click ‘set security question’
        And enter my question into a text box
        And enter my answer into another text box
        And click ‘save security question’
        Then my security question will be saved