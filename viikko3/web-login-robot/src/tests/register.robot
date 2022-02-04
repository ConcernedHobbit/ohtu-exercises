*** Settings ***
Resource    resource.robot
Resource    login_resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username        kaarle
    Set Password        kaarle123
    Set Confirmation    kaarle123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username        ez
    Set Password        peasy456
    Set Confirmation    peasy456
    Submit Registration
    Registration Should Fail With Message  Username should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username        kaarle
    Set Password        a1
    Set Confirmation    a1
    Submit Registration
    Registration Should Fail With Message  Password should be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username        kaarle
    Set Password        kaarle123
    Set Confirmation    kaarle456
    Submit Registration
    Registration Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username        karlos
    Set Password        karlos123
    Set Confirmation    karlos123
    Submit Registration
    Registration Should Succeed
    Go To Login Page
    Set Username        karlos
    Set Password        karlos123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username        fabian
    Set Password        fabian456
    Set Confirmation    karlos123
    Submit Registration
    Go To Login Page
    Set Username        fabian
    Set Password        fabian456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Confirmation
    [Arguments]  ${confirmation}
    Input Text  password_confirmation   ${confirmation}