*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  kalevi  eBA63mG3fPJ3nNow
  Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
  Input Credentials  horatius  Ut8LprXzH9uuzerj
  Output Should Contain   User with username horatius already exists

Register With Too Short Username And Valid Password
  Input Credentials   ez  k4l3v1us89zs
  Output Should Contain   Username ez is too short

Register With Valid Username And Too Short Password
  Input Credentials  kornelius  puu
  Output Should Contain   Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Credentials  teodore  pelkkiakirjaimia
  Output Should Contain   Password is not complex enough

*** Keywords ***
Create User And Input Register Command
  Create User   horatius  Hn3gCJHj7FCBrCNj
  Input Register Command
  