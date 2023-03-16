Feature: view followed posts
	As a registered user, I want to see the posts of people that I follow on the Home page, so that I will not miss the posts they posted

	Scenario: Successfully see the followed posts on Home page
		Given I am a registered user who is logged in
		When I navigate to the “Home” tab
		Then posts that are posted by the people I follow will be displayed on the Home page
