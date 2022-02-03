*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Register Command
    Input  new

Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
