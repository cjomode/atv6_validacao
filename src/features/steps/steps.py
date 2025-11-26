from behave import given, when, then
import requests

API_URL = "http://localhost:5000"

@given('que o sistema está rodando')
def step_impl(context):
    pass

@when('eu envio os dados de cadastro para "/cadastrar"')
def step_impl(context):
    pessoa = context.table.rows[0].as_dict()
    response = requests.post(f"{API_URL}/cadastrar", data=pessoa)
    context.response = response
    

@then('o status code deve ser {code:d}')
def step_impl(context, code):
    assert context.response.status_code == code

@then('a resposta deve conter "{msg}"')
def step_impl(context, msg):
    assert msg in context.response.text


