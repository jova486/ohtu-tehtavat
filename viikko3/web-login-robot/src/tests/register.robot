*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start




*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Already Taken Username And Valid Password
    Set Username  joppe
    Set Password  kalle123
    Set password Confirmation  kalle123
    Submit Credentials
    Register Should Not Succeed


Register With Too Short Username And Valid Password
    Set Username  jo
    Set Password  kalle123
    Set password Confirmation  kalle123
    Submit Credentials
    Register Should Not Succeed


Register With Valid Username And Too Short Password
    Set Username  koira
    Set Password  koira2
    Set password Confirmation  koira2
    Submit Credentials
    Register Should Not Succeed

Register With Valid Username And Long Enough Password Containing Only Letters
    Set Username  koira
    Set Password  koirakissa
    Set password Confirmation  koirakissa
    Submit Credentials
    Register Should Not Succeed

Login After Successful Registration
    Set Username  koira
    Set Password  koirakissa1
    Set password Confirmation  koirakissa1
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  koira
    Set Password  koirakissa1
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  koira
    Set Password  koi
    Set password Confirmation  koi
    Submit Credentials
    Register Should Not Succeed
    Go To Login Page
    Set Username  koira
    Set Password  koirakissa1
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Register Should Not Succeed
    Title Should Be  Register

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Start
    Create User  joppe  joppe123
    Go To Register Page
    Register Page Should Be Open
