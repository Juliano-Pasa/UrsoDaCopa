# Urso Da Copa
Readme em [português](#urso-da-copa-pt-br).  
Twitter Bot that counts down to FIFA World Cup Qatar 2022 every Friday.

This project consists of a Twitter Bot that posts the same video every Friday but at different times of the day.
It then collects data about the tweet several times, so this data can be analyzed to check if posting at different hours of the day has an effect on how popular the tweet can get. There are still some hardcoded numbers related to the usage of this specific bot, but there are plans to make everything easily editable in the future. 

The video used is not mine.


# System information
All code is being run in a Google Cloud Platform VM.  
OS: Debian 10 Buster v20211209  
Python: 3.7.3  


# Installation
To run this code, you must have Twitter API elevated access since it uses standard v1.1 endpoints and Twitter API v2. Enter this [link](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) to know more about how to get access to Twitter's API.


Currently, the process of automating the scripts for posting and retrieving tweet information only works on Linux because it uses crontab. There are plans to make an automation for Windows in the future.


## 1. Add your API Keys and root folder path to your environment variables

- On Linux, open your .bash_profile. You can use the text editor you prefer.
```
$ nano .bash_profile 
```

- Copy this into your file with your respective keys and path
```
export CONSUMER_KEY="Your consumer key"
export CONSUMER_KEY_SECRET="Your consumer key secret"
export ACCESS_TOKEN="Your access token"
export ACCESS_TOKEN_SECRET="Your access token secret"
export PYTHONPATH=Project Main Folder Absolute Path
```

- On Windows, you can follow this [tutorial](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/). Name your environment variables the same as you would in Linux.

## 2. Create your Python virtual environment in projetct main folder:

```
On Windows: python3 -m venv name

On Linux: $ python3 -m venv name 
# It's commom to use 'venv' as the folder name as well
```

## 3. Activate your Python virtual environment

```
On Windows: name\Scripts\activate

On Linux: $ source name/bin/activate
```

## 4. Install pip

```
On Windows: python3 -m pip install --upgrade pip

On Linux: $ sudo apt-get install python3-pip
```

## 5. Install requirements

```
$ pip install -r requirements.txt
```

## 6. Automate the scripts (Only on Linux)

- Launch the virtual environment from your main folder
```
$ source name/bin/activate
```
- Execute cronjob creation
```
$ cd Source
$ python3 cron_management.py your_user
```

# Urso Da Copa PT-BR
Bot do Twitter que realiza contagem regressiva pra Copa do Mundo FIFA Qatar 2022 toda sexta-feira.

Esse projeto consiste em um Bot do Twitter que posta o mesmo vídeo toda sexta-feira mas em diferentes horários do dia.
Ele então coleta informações sobre o tuíte várias vezes, para que esses possam ser analizados para checar se postar em diferentes horas do dia tem impacto no quão popular o tuíter pode ser. Ainda há alguns números específicos dentro do código relacionados ao uso de Bot, mas há planos para tornar tudo fácilmente editável no futuro.

O vídeo usado não é meu.

# Informações do sistema
Todo código está sendo rodado em uma MV do Google Cloud Platform.
SO: Debian 10 Buster v20211209  
Python: 3.7.3  


# Instalação
Para rodar esse código, você precisa ter o acesso elevado da API do Twitter já que ele usa funcionalidades do standard v1.1 e do Twitter API v2. Entre nesse [link](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) para saber mais sobre como conseguir acesso à API do Twitter.


Atualmente, o processo de automação dos códigos para postagem e recuperação de informação do tuíte só funciona no Linux porque ele usa o crontab. Há planos para fazer uma automação para o Windows no futuro.

## 1. Adicione as chaves de API e o caminho para a pasta principal do projeto nas variáveis de ambiente 

- No Linux, abra seu .bash_profile. Você pode utilizar o editor de texto que quiser.
```
$ nano .bash_profile 
```

- Copie isso para seu arquivo com suas respectivas chaves e caminho da pasta do projeto.
```
export CONSUMER_KEY="Sua chave de API"
export CONSUMER_KEY_SECRET="Sua chave secreta de API"
export ACCESS_TOKEN="Seu token de acesso"
export ACCESS_TOKEN_SECRET="Seu token de acesso secreto"
export PYTHONPATH=Caminho Absoluto da Pasta Principal do Projeto
```

- No Windows, você pode seguir esse [tutorial](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/). Nomeie suas variáveis de ambiente igual mostrado acima no Linux.

## 2. Crie seu ambiente virtual do Python na pasta principal do projeto
```
$ python3 -m venv nome 
# Você pode usar 'venv' como nome
```

## 3. Ative seu ambiente virtual do Python 

```
No Windows: nome/Scripts/activate

No Linux: $ source nome/bin/activate
```

## 4. Instale o pip

```
No Windows: python3 -m pip install --upgrade pip

No Linux: $ sudo apt-get install python3-pip
```

## 5. Instale os requisitos

```
$ pip install -r requirements.txt
```

## 6. Automatize os códigos (somente no Linux)

- Inicie o ambiente virtual na sua pasta principal do projeto 
```
$ source name/bin/activate
```
- Execute criação do cronjob
```
$ cd Source
$ python3 cron_management.py your_user
```
