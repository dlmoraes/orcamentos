from django.template.defaultfilters import slugify
from orcamentos.crm.models import Employee, Occupation
from orcamentos.utils.lists import OCCUPATION_LIST

'''
Definindo a senha padrão para todos os usuarios,
como o django aceita apenas hash, criei uma senha padrão [password=1] e copiei
o hash dela ou seja, para acessar cada uma das contas use como senha 1.
'''

hashpass = 'pbkdf2_sha256$12000$Pe4addAsDo1D$xEtHWLnSIVkEppr4pbK69SBhuLwWsSHdXyhkCZBNktA='

# Primeiro verifica se existe os cargos, caso contrário os grava.
if not Occupation.objects.all().count():
    obj = [Occupation(occupation=val) for val in OCCUPATION_LIST]
    Occupation.objects.bulk_create(obj)


def get_occupation(occupation_name):
    occupation = Occupation.objects.get(occupation=occupation_name)
    return occupation


employees = {
    'amanda': {
        'username': 'amanda',
        'first_name': 'Amanda',
        'last_name': 'Santos',
        'occupation': 'Diretor',
        'gender': 'F',
        'treatment': 'aa',
        'company': 'Tivit',
        'department': u'Arquitetura',
        'cpf': '11122233396',
        'rg': '40373800',
        'address': u'Avenida Paulista, 1320',
        'complement': 'Apto 303',
        'district': u'Cerqueira César',
        'city': u'São Paulo',
        'uf': 'SP',
        'cep': '01020000'},
    'caio': {
        'username': 'caio',
        'first_name': 'Caio',
        'last_name': 'Silva Oliveira',
        'occupation': 'Engenheiro',
        'gender': 'M',
        'treatment': 'e',
        'company': 'Tivit',
        'department': 'Engenharia',
        'cpf': '73842008714',
        'rg': '506793799',
        'address': 'Rua Marília de Dirceu, 1525',
        'complement': 'Apto 16',
        'district': 'Aclimação',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01100000'},
    'rebeca': {
        'username': 'rebeca',
        'first_name': 'Rebeca',
        'last_name': 'Araujo Costa',
        'occupation': 'Orçamentista',
        'gender': 'F',
        'treatment': '',
        'company': 'Titanium',
        'department': 'Orçamentos',
        'cpf': '24644675769',
        'rg': '592288359',
        'address': 'Rua Monte Belo, 704',
        'complement': 'cj. 3',
        'district': 'Vergueiro',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01289098'},
    'douglas': {
        'username': 'douglas',
        'first_name': 'Douglas',
        'last_name': 'Cardoso Rodrigues',
        'occupation': 'Gerente',
        'gender': 'M',
        'treatment': '',
        'company': 'Titanium',
        'department': 'Suprimentos',
        'cpf': '96699840361',
        'rg': '224651880',
        'address': 'Rua Dráusio Camargo, 440',
        'complement': '',
        'district': 'Paraíso',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '02812750'},
    'jose': {
        'username': 'jose',
        'first_name': 'José',
        'last_name': 'Carlos Frederico',
        'occupation': 'Vendedor',
        'gender': 'M',
        'treatment': 'sr',
        'company': 'Bot',
        'department': 'Vendas',
        'cpf': '88922876699',
        'rg': '967728378',
        'address': 'Estrada Macacu, 1530',
        'complement': '',
        'district': 'Centro',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01627400'},
    'alice': {
        'username': 'alice',
        'first_name': 'Alice',
        'last_name': 'Cunha Santos',
        'occupation': 'Orçamentista',
        'gender': 'F',
        'treatment': 'srta',
        'company': 'Plan',
        'department': 'Gerência',
        'cpf': '52168942960',
        'rg': '742367358',
        'address': 'Rua Georgina Sá Leite Orcessi, 1851',
        'complement': '',
        'district': 'Santo Amaro',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '02616720'},
    'carla': {
        'username': 'carla',
        'first_name': 'Carla',
        'last_name': 'Azevedo Santos',
        'occupation': 'Arquiteto',
        'gender': 'F',
        'treatment': 'srta',
        'company': 'Plan',
        'department': 'Arquitetura',
        'cpf': '27663116303',
        'rg': '188830743',
        'address': 'Rua Vinte e Oito, 1491',
        'complement': '',
        'district': 'Filipinas',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01327465'},
    'regis': {
        'username': 'regis',
        'first_name': 'Regis',
        'last_name': 'da Silva Santos',
        'occupation': 'Vendedor',
        'gender': 'M',
        'treatment': '',
        'company': 'RG Solutions',
        'department': 'TI',
        'cpf': '15895419181',
        'rg': '305467840',
        'address': 'Praça Otaviano de Paulo, 89',
        'complement': 'Apto 44',
        'district': 'Pompéia',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '01727389'},
    'fernando': {
        'username': 'fernando',
        'first_name': 'Fernando',
        'last_name': 'Souza',
        'occupation': 'Orçamentista',
        'gender': 'F',
        'treatment': '',
        'company': 'RG Solutions',
        'department': 'TI',
        'cpf': '20095419180',
        'rg': '400467851',
        'address': 'Rua Gomes de Carvalho, 100',
        'complement': '10º andar',
        'district': 'Vila Olímpia',
        'city': 'São Paulo',
        'uf': 'SP',
        'cep': '04547001'},
    'adailton': {
        'username': 'adailton',
        'first_name': 'Adailton',
        'last_name': 'do Nascimento',
        'occupation': 'Vendedor',
        'gender': 'M',
        'treatment': '',
        'company': 'RG Solutions',
        'department': 'TI',
        'cpf': '41895976210',
        'rg': '535121673',
        'address': 'Rua Jaqueira, 460',
        'complement': '',
        'district': 'Santo Antonio',
        'city': 'Aparecida de Goiânia',
        'uf': 'GO',
        'cep': '10282900'}
}


for k in employees:
    slug = slugify('{} {}'.format(
        employees[k]['first_name'], employees[k]['last_name']))
    Employee.objects.create(
        username=employees[k]['username'],
        first_name=employees[k]['first_name'],
        last_name=employees[k]['last_name'],
        slug=slug,
        email=employees[k]['username'] + '@example.com',
        is_staff=True,
        password=hashpass,
        occupation=get_occupation(employees[k]['occupation']),
        gender=employees[k]['gender'],
        treatment=employees[k]['treatment'],
        company=employees[k]['company'],
        department=employees[k]['department'],
        cpf=employees[k]['cpf'],
        rg=employees[k]['rg'],
        address=employees[k]['address'],
        complement=employees[k]['complement'],
        district=employees[k]['district'],
        city=employees[k]['city'],
        uf=employees[k]['uf'],
        cep=employees[k]['cep'],
    )


# done
