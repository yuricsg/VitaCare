# VitaCare
VitaCare é uma plataforma online que facilita o acesso a cuidados de saúde, conectando usuários a profissionais de saúde voluntários. A plataforma oferece suporte psicológico, orientação médica básica e recursos de promoção do bem-estar, visando atender pessoas em situação de vulnerabilidade ou residentes em áreas remotas. Com base no Objetivo de Desenvolvimento Sustentável 3 (ODS 3) da ONU, a VitaCare busca democratizar o acesso à saúde, criando uma rede de apoio eficiente e acessível para todos.

## Funcionalidades
- Cadastro de Usuários: Usuários podem se registrar como pacientes ou profissionais de saúde (psicólogos, médicos, nutricionistas, etc.).
- Agendamento de Sessões: Os pacientes podem procurar por profissionais disponíveis e agendar consultas online.
- Chat e Videoconferência: Integração com ferramentas que permitem consultas por chat ou vídeo.
- Recursos Educacionais: Seção com artigos, vídeos e outros materiais focados em saúde mental, nutrição e bem-estar.
- Feedback e Avaliações: Sistema de avaliação para garantir a qualidade do serviço oferecido pelos profissionais.
- Área de Doações: Opção para que usuários façam doações para apoiar o funcionamento da plataforma ou patrocinar consultas para aqueles que não podem pagar.

## Tecnologias utilizadas
- Django
- SQL
- Bootsrap
- HTML5 & CSS
- JavaScript

## Trello do projeto
![trello vitacare](https://github.com/user-attachments/assets/72961577-d0af-4bfb-9d15-cc47706c6ce4)
Link: https://trello.com/invite/b/66e9691e12219c61e45a9da9/ATTIebc39c44416c27ab650faffabc5d4a09FEB93348/vitacare

## Video do projeto:
Link do vídeo: “https://youtu.be/8K-Lz5WUwMI?si=lgCnOtuJhccfQ7vS“

## Nosso diagrama de atividades:
Link: https://lucid.app/lucidchart/4f8f07e2-2861-4839-9e3a-6ab4bd0dc132/edit?view_items=VicVHzzAZ2cT&invitationId=inv_e307535c-b71c-49fb-8f6f-29598655392a

## Deploy do projeto
### Requisitos
Antes de começar, certifique-se de que você tem as seguintes dependências instaladas no seu sistema:
- Python 3.13 ou superior (https://www.python.org/downloads/)
- Django 5.x (instalado via `pip`)
- MySQL (https://dev.mysql.com/downloads/installer/)
- Virtualenv (https://virtualenv.pypa.io/en/stable/)

## Issues do nosso projeto
![image](https://github.com/user-attachments/assets/838d29cc-12f2-4ad4-94c8-6bd278f7be03)

### Passos de configuração
#### 1. Clonar o repositório
Primeiro, faça o clone do projeto em sua máquina local:
```bash
git clone https://github.com/seu-usuario/vitacare.git
```
#### 2. Criar o ambiente virtual
```bash
# Criando o ambiente virtual
python -m venv venv
```
```bash
# Ativando o ambiente virtual (Windows)
venv\Scripts\activate
```
```bash
# Ativando o ambiente virtual (Linux/macOS)
source venv/bin/activate
```

#### 3. Instalar as dependências
Instale todas as bibliotecas necessárias a partir do arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### 4. Configurar o banco de dados MySQL
  ##### 1. Criar o banco de dados: 
  Acesse seu MySQL e crie um banco de dados para o projeto:
  ```sql
  CREATE DATABASE VitaCare;
  ```

  ##### 2. Atualizar as credenciais:
  No arquivo `settings.py`, certifique-se que as credenciais estão corretas:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'VitaCare',
          'USER': 'seu_usuario',
          'PASSWORD': 'sua_senha',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```
#### 5. Aplicar as migrações
Execute as migrações para criar as tabelas do banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Criar um Superusuário
Crie um superusuário para acessar a interface administrativa:
```bash
python manage.py createsuperuser
```

#### 7. Coletar arquivos estáticos
No ambiente de produção, você precisa coletar todos os arquivos estáticos (CSS, JavaScript, etc.) em um único diretório para servir ao cliente final:
```bash
python manage.py collectstatic
```

#### 8. Executar o Servidor Django
Agora você pode executar o servidor.
```bash
python manage.py runserver
```


