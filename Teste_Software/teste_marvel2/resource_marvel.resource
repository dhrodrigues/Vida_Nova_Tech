*** Settings ***
Library     RequestsLibrary
Variables       marvel.py

*** Keywords ***
Criar Configuracao Inicial do Teste
    Create Session  request_marvel_char  ${BASE_URL_MARVEL}  verify=true  headers=${HEADERS}

Realizar requisicao GET
    ${response_char}=  Get On Session  request_marvel_char  /v1/public/creators  params=apikey=${API_KEY}
    Set Test Variable  ${response_char}

Validar se status
    Request Should Be Successful  ${response_char}

Validar se a chave "code" esta preenchida
    ${StatusCodeInt}=   Convert To Integer  200
    Should Be Equal  ${response_char.json()}[code]  ${StatusCodeInt}

Validar se a chave "copyright" esta preenchida
    Should Be Equal  ${response_char.json()}[copyright]  © 2022 MARVEL
