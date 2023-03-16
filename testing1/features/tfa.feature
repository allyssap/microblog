Feature: two-factor authentication
  As a registered user, I want to be able to login to the Microblog by either PIN code in mobile phone or verification link in email, so that I can keep my account secure

    Scenario: Successfully login to the account by PIN code sent to the mobile phone
        Given I am a registered user for tfa
        When I try to login my account
        And I choose the PIN code option to login
        Then my mobile phone will receive a PIN code from Microblog
        And I enter this PIN code for verification
        And I login to my account

    Scenario: Successfully login to the account by verification link sent to the email address
        Given I am a registered user
        When I try to login my account
        And I choose the verification link option to login
        Then my email inbox will receive a verification link from Microblog
        And click this verification link
        And I login to my account by one time link