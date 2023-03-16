Feature: view my existing posts
	As a registered user, I want to be able to view my existing posts so that I can check my existing posts’ popularity or mistakes

	Scenario: Successfully view my existing posts
		Given I am a user who is signed in
		When I go to the profile page
		Then all my existing posts should be displayed in the page
		And they are displayed as newest at the top
