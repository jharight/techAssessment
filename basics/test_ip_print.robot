*** Settings ***
Library    OperatingSystem

*** Keywords ***
Custom Run Process
    [Arguments]    ${command}    ${file}    ${json_file}
    ${output}=    OperatingSystem.Run    ${command} ${file} ${json_file}
    [Return]    ${output}

*** Test Cases ***
Test with input1.json
    ${output}=    Custom Run Process    python    ip_print.py    input1.json
    Should Contain     ${output}    192.168.101.101
    Should Contain     ${output}    192.168.101.70
    Should Contain     ${output}    192.168.101.153

Test with input2.json
    ${output}=    Custom Run Process    python    ip_print.py    input2.json
    Should Contain     ${output}    192.168.102.33
    Should Contain     ${output}    192.168.103.74
    Should Contain     ${output}    192.168.102.155
    Should Contain     ${output}    10.0.0.77
    Should Contain     ${output}    10.0.0.87
    Should Contain     ${output}    10.0.0.99