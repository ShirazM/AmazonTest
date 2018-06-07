*** Settings ***
Documentation    Suite description
Test Teardown     Close Browser
Library           Selenium2Library
Library           String

*** Test Cases ***
Navigate to Amazon and Login
    [Tags]  test1
    Open Browser    https://www.amazon.ca/   googlechrome
    Set Browser Implicit Wait    10 seconds
    Maximize Browser Window
    Click Link    nav-link-yourAccount
    wait until page contains  Sign in
    Input Text    ap_email    rajagiriyakotte1234@gmail.com
    Click Element    continue
    wait until page contains  Password
    Input Password    ap_password    W0rkopolis
    Click Button    signInSubmit
    wait until page contains  Hello, Sim
    Page Should Contain    Hello, Sim
    Page Should Contain  Amazon



