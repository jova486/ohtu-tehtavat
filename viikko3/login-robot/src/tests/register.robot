*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User



*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  joppe  joppe123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kaapo  kaapo123
    Output Should Contain  User with username kaapo already exists

Register With Too Short Username And Valid Password
    Input Credentials  jo  kaapo123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  joppe  k
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  joppe  joppelainen
    Output Should Contain  Password must have numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kaapo  kaapo123
