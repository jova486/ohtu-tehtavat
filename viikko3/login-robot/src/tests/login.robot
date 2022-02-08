*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  joppe  joppe123
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  kaapo  joppe123
    Output Should Contain  Invalid username or password




*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Create User  joppe  joppe234
    Input Login Command
