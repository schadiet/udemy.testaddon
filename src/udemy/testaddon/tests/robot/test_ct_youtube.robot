# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s udemy.testaddon -t test_youtube.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src udemy.testaddon.testing.UDEMY_TESTADDON_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/udemy/testaddon/tests/robot/test_youtube.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Youtube
  Given a logged-in site administrator
    and an add Youtube form
   When I type 'My Youtube' into the title field
    and I submit the form
   Then a Youtube with the title 'My Youtube' has been created

Scenario: As a site administrator I can view a Youtube
  Given a logged-in site administrator
    and a Youtube 'My Youtube'
   When I go to the Youtube view
   Then I can see the Youtube title 'My Youtube'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Youtube form
  Go To  ${PLONE_URL}/++add++Youtube

a Youtube 'My Youtube'
  Create content  type=Youtube  id=my-youtube  title=My Youtube

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Youtube view
  Go To  ${PLONE_URL}/my-youtube
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Youtube with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Youtube title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
