*** Settings ***
Resource    resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username        kalle
    Set Password        kalle123
    Set Confirmation    kalle123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username        ez
    Set Password        peasy456
    Set Confirmation    peasy456
    Submit Registration
    Registration Should Fail With Message  Username should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username        kalle
    Set Password        a1
    Set Confirmation    a1
    Submit Registration
    Registration Should Fail With Message  Password should be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username        kalle
    Set Password        kalle123
    Set Confirmation    kalle456
    Submit Registration
    Registration Should Fail With Message  Passwords don't match

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Text  password_confirmation   ${confirmation}

Submit Registration
    Click Button    Register