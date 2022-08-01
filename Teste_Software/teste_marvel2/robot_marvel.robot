*** Settings ***
Resource        marvel1.resource
Suite Setup     Criar Configuracao Inicial do Teste

*** Test Cases ***
Testar API Char da Marvel 
    Realizar requisicao GET
    Validar se status
    Validar se a chave "code" esta preenchida
    Validar se a chave "copyright" esta preenchida
