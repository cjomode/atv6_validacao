Feature: Cadastro de Pessoa

    Scenario: Usuário cadastra uma nova pessoa
        Given que o sistema está rodando
        When eu envio os dados de cadastro para "/cadastrar"
            | nome  | sobrenome | cpf       | data_nascimento |
            | Teste | silva     | 003465498 | 2000-01-01      |
        Then o status code deve ser 200
        And a resposta deve conter "Pessoa cadastrada"


    Scenario: Usuário tenta cadastrar pessoa com o nome vazio 
        Given que o sistema está rodando
        When eu envio os dados de cadastro para "/cadastrar"
            | nome | sobrenome | cpf        | data_nascimento |
            |      | silva     | 8945615458 | 2000-01-01      |
        Then o status code deve ser 400
        And a resposta deve conter "Nome é obrigatório"


    Scenario: Usuário tenta cadastrar pessoa com o sobrenome vazio
        Given que o sistema está rodando
        When eu envio os dados de cadastro para "/cadastrar"
            | nome  | sobrenome | cpf       | data_nascimento |
            | Teste |           | 895654858 | 2000-01-01      |
        Then o status code deve ser 400 
        And a resposta deve conter "Sobrenome é obrigatório"

    Scenario: Usuário tenta cadastrar pessoa com o cpf vazio
        Given que o sistema está rodando
        When eu envio os dados de cadastro para "/cadastrar"
            | nome  | sobrenome | cpf      | data_nascimento |
            | Teste | silva     |          | 2000-01-01      |
        Then o status code deve ser 400 
        And a resposta deve conter "CPF é obrigatório"

    Scenario: Usuário tenta cadastrar pessoa com campo de data de nascimento vazio
        Given que o sistema está rodando
        When eu envio os dados de cadastro para "/cadastrar"
            | nome  | sobrenome | cpf       | data_nascimento |
            | Teste | silva     | 897856465 |                 |
        Then o status code deve ser 400 
        And a resposta deve conter "Data de nascimento é obrigatória"
