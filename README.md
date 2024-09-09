# Restaurante SI

## Descrição
Este é um projeto para a matéria de Fundamentos de Sistemas da Informação desenvolvido com o framework Django. Nele, você encontrará um sistema de gestão de restaurante, com módulos de *Gerenciamento de Clientes, **Gerenciamento de Reservas, **Gerenciamento de Pedidos, **Gerenciamento de Menu, **Gerenciamento de Funcionário* e *Feedback de Clientes*.

## Autores
- [Gustavo Nery](https://github.com/gustavonerywe/)
- [Kayllane Sanches](https://github.com/KayllaneSCardoso)
- [Laura Torres](https://github.com/lauratorresss)
- [Paulo Affonso](https://github.com/affonsopaulo/)

## Demonstração
Acesse o seguinte site para verificar o funcionamento do sistema: http://18.228.13.180:8000/

## Pré-requisitos

Antes de começar, certifique-se de que o seguinte software esteja instalado:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) 3.x
- [pip](https://pip.pypa.io/en/stable/installation/)

## Instalação

### Clonando o repositório

bash
git clone https://github.com/seu-usuario/seu-projeto-django.git
cd seu-projeto-django


### Criação e ativação do ambiente virtual

É recomendável utilizar um ambiente virtual para isolar as dependências do projeto.

bash
python -m venv venv
source venv/bin/activate #No Windows: venv\Scripts\activate


### Instalação das dependências
Instale as dependências do projeto listadas no arquivo *requirements.txt*:

bash
pip install -r requirements.txt


### Rodando o projeto
Para rodar o servidor de desenvolvimento na porta 8000:

bash
python manage.py runserver 0.0.0.0:8000


## Estrutura do projeto


.
├── manage.py             # Arquivo de gerenciamento do Django
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências do projeto
├── app/                  # Diretório do aplicativo principal
│   ├── admin.py          # Configurações do admin do Django
│   ├── apps.py           # Configurações do aplicativo
│   ├── forms.py          # Formulários do Django
│   ├── models.py         # Modelos do Django
│   ├── tests.py          # Testes do aplicativo
│   ├── urls.py           # URLs do aplicativo
│   ├── views.py          # Views do aplicativo
│   ├── migrations/       # Arquivos de migrações do banco de dados
│   │   ├── 0001_initial.py
│   │   ├── 0002_role_alter_employee_role.py
│   │   ├── 0003_employee_salary.py
│   │   ├── 0004_remove_reservation_date_remove_reservation_time.py
│   │   ├── 0005_customer_has_table.py
│   │   ├── 0006_reservation_quantity.py
│   │   ├── 0007_alter_order_status_alter_order_total_amount.py
│   │   ├── 0008_remove_order_items_remove_order_total_amount_and_more.py
│   │   ├── 0009_order_items.py
│   ├── static/           # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/
│   │   │   └── template.css
│   │   ├── img/
│   │   │   └── food-and-restaurant.png
│   │   └── js/
│   │       └── app.js
│   ├── templates/        # Templates HTML
│   │   ├── header.html
│   │   ├── index.html
│   │   ├── template.html
│   │   ├── customer/
│   │   │   ├── customer.html
│   │   │   ├── edit_customer.html
│   │   ├── employee/
│   │   │   ├── edit_employee.html
│   │   │   ├── edit_role.html
│   │   │   ├── employee.html
│   │   │   ├── manage_employee.html
│   │   │   ├── role.html
│   │   ├── feedback/
│   │   │   ├── edit_feedback.html
│   │   │   ├── feedback.html
│   │   ├── menu/
│   │   │   ├── category.html
│   │   │   ├── edit_category.html
│   │   │   ├── edit_item.html
│   │   │   ├── items.html
│   │   │   ├── menu.html
│   │   ├── order/
│   │   │   ├── create_order.html
│   │   │   ├── order_list.html
│   │   └── reserve/
│   │       ├── edit_table.html
│   │       ├── manage_reserve.html
│   │       ├── reservation.html
│   │       └── table.html
│   └── templatetags/     # Tags de template personalizadas
│       ├── currency.py
└── core/                 # Configurações principais do projeto
    ├── asgi.py           # Configurações ASGI
    ├── settings.py       # Configurações do Django
    ├── urls.py           # URLs principais do projeto
    └── wsgi.py           # Configurações WSGI

## Requisitos Funcionais

1. *Gerenciamento de Clientes*
   - Cadastro de novos clientes.
   - Atualização de informações de clientes.
   - Exclusão de clientes.
   - Visualização de lista de clientes.

2. *Gerenciamento de Reservas*
   - Criação de novas mesas e reservas.
   - Atualização de mesas e reservas existentes.
   - Cancelamento de reservas e exclusão de mesas.
   - Visualização de reservas por data e visualização de lista de mesas.

3. *Gerenciamento de Pedidos*
   - Criação de novos pedidos.
   - Cancelamento de pedidos.
   - Visualização de histórico de pedidos.

4. *Gerenciamento de Menu*
   - Adição de novos itens e categorias ao menu.
   - Atualização de itens e categorias do menu.
   - Remoção de itens e categorias do menu.
   - Visualização de todos os itens e categorias do menu.

5. *Gerenciamento de Funcionário*
   - Cadastro de novos funcionários e cargos.
   - Atualização de informações de funcionários e cargos.
   - Exclusão de funcionários e cargos.
   - Visualização de lista de funcionários e cargos.

6. *Feedback de Clientes*
   - Recebimento de feedback dos clientes.
   - Visualização de feedbacks recebidos