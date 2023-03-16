Feature: view other people’s posts
	As a registered user, I want to be able to view other people’s posts so that I can know how’s they going and not miss anything important

	Scenario: Successfully view other people’s existing posts
		Given I am a user who is signed in at index
		When I navigate to the explore tab
		Then other people’s posts should be displayed in the page
		And they are displayed as newest at the top
