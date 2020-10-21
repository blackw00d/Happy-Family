# Happy Family
Сайт для продажи электрокаров для детей. 

## Оглавление
0. [Описание проекта](#Описание-проекта)
1. [Установка](#Установка)

## Описание проекта

### Основные функции сайта

#### Отображение списка товаров
* Фотографии электрокаров, в виде карусели
* Техническая информация об электрокарах
    * Возраст ребенка
    * Вес ребенка
    * Характеристики электрокара
* Цена продажи
* Скидка на электротовар

Список товаров меняется при смене города, товар отображается по наличию в выбранном городе.

#### Корзина
Хранение информации о выбранных пользователем товарах в сессии Django с последующим оформлением заказа.

#### Форма обратной связи
Возможность заказать обратный звонок. 

#### Личный кабинет
Возможность зарегистрироваться/авторизоваться на сайте для последующего отслеживания заказа.

В личном кабинете есть возможность указать социальные сети(при подписке на социальные сети проекта активируется скидка 5%).
Скидка применяется в ручную.

## Установка
Далее будет показана установка на чистый debian сервер (Описание на английском).
 
В данном примере использовался Yandex.Cloud.

Update packages
```bash
sudo apt-get update;
sudo apt-get install -y vim htop git curl wget unzip zip gcc build-essential make
```
Configure SSH:
```bash
sudo vim /etc/ssh/sshd_config
    AllowUsers www
    PermitRootLogin no
    PasswordAuthentication no
```
Restart SSH server, change www user password:
```bash
sudo service ssh restart
```
Change locale
```bash
sudo localedef ru_RU.UTF-8 -i ru_RU -fUTF-8 ; \
export LANGUAGE=ru_RU.UTF-8 ; \
export LANG=ru_RU.UTF-8 ; \
export LC_ALL=ru_RU.UTF-8 ; \
sudo locale-gen ru_RU.UTF-8 ; \
sudo dpkg-reconfigure locales 
Init — must-have packages & ZSH
sudo apt-get install -y zsh tree redis-server nginx zlib1g-dev libbz2-dev libreadline-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev liblzma-dev python3-dev python-pil python3-lxml libxslt-dev python-libxml2 python-libxslt1 libffi-dev libssl-dev python-dev gnumeric libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libfreetype6-dev libcurl4-openssl-dev supervisor
```
#### Install python 3.8
Build from source python 3.8, install with prefix to ~/.python folder:
```bash
wget https://www.python.org/ftp/python/3.8.4/Python-3.8.4.tgz ; \
tar xvf Python-3.8.* ; \
cd Python-3.8.4 ; \
mkdir ~/.python ; \
./configure --enable-optimizations --prefix=/home/www/.python ; \
make -j8 ; \
sudo make altinstall
```
Now python3.8 in /home/www/.python/bin/python3.8. 

Add Python 3.8 to BASH
```bash
vim ~/.bashrc
    export PATH=$PATH:/home/www/.python/bin
```
Ok, now we can pull our project from Git repository (or create own), create and activate Python virtual environment:
```bash
mkdir ~/code
cd code
mkdir Happy-Family
cd Happy-Family
git clone https://github.com/blackw00d/HappyFamily.git
cd ..
python3.8 -m venv env
. ./env/bin/activate
```
Update pip:
```bash
pip install -U pip
pip install –r requirements.txt
```
#### Configure Project
```bash
create .env:
vim .env
```
Add export parameters to .env file and save (Code just for example).
```bash
export SECRET_KEY="dfsfsdfksjdkfls324242"
export DEBUG="0"
export DJANGO_ALLOWED_HOSTS="PUBLIC_ADDRESS 127.0.0.1"
export SQL_ENGINE="django.db.backends.postgresql"
export SQL_DATABASE="hf_db"
export SQL_USER="admin"
export SQL_PASSWORD="some_password"
export SQL_HOST="localhost"
export SQL_PORT="5432"
export AUTH_USER_MODEL="HFhtml.Users"
export EMAIL_HOST="smtp.yandex.ru"
export EMAIL_HOST_USER="user@yandex.ru"
export EMAIL_HOST_PASSWORD="pass"
export EMAIL_PORT="587"
export EMAIL_USE_TLS="1"
```
Add .env to PATH:
```bash
. .env
```
Install(if not in requirements) and configure Gunicorn
```bash
pip install gunicorn
vim gunicorn_config.py
```
```bash
command = '/home/www/code/Happy-Family/env/bin/gunicorn'
pythonpath = '/home/www/code/Happy-Family/HappyFamily'
bind = '127.0.0.1:8001'
workers = 5
user = 'www'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=HappyFamily.settings'
```
Make shell file for start Gunicorn and start it
```bash
mkdir bin
vim bin/start_gunicorn.sh
```
```bash
#!bin/bash
. /home/www/code/Happy-Family/HappyFamily/.env
. /home/www/code/Happy-Family/env/bin/activate
```
```bash
exec gunicorn -c "/home/www/code/Happy-Family/HappyFamily/gunicorn_config.py" HappyFamily.wsgi:application
chmod +x bin/start_gunicorn.sh
. ./bin/start_gunicorn.sh
```
#### Install and configure PostgreSQL
Install PostgreSQL 11 and configure locales.
```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - ; \
RELEASE=$(lsb_release -cs) ; \
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main | sudo tee  /etc/apt/sources.list.d/pgdg.list ; \
sudo apt update ; \
sudo apt -y install postgresql-11 ; \
```
Add locales to /etc/profile:
```bash
sudo vim /etc/profile
    export LANGUAGE=ru_RU.UTF-8
    export LANG=ru_RU.UTF-8
    export LC_ALL=ru_RU.UTF-8
```
Change postges password, create clear database named hf_db:
```bash
sudo passwd postgres
su - postgres
export PATH=$PATH:/usr/lib/postgresql/11/bin
createdb --encoding UNICODE hf_db --username postgres
exit
```
Create dbms db user and grand privileges to him:
```bash
sudo -u postgres psql
postgres=# ...
create user admin with password 'some_password';
ALTER USER admin CREATEDB;
grant all privileges on database hf_db to admin;
\c hf_db
GRANT ALL ON ALL TABLES IN SCHEMA public to admin;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to admin;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to admin;
CREATE EXTENSION pg_trgm;
ALTER EXTENSION pg_trgm SET SCHEMA public;
UPDATE pg_opclass SET opcdefault = true WHERE opcname='gin_trgm_ops';
\q
exit
```
Now we can test connection. Create ~/.pgpass with login and password to db for fast connect:
```bash
vim ~/.pgpass
	localhost:5432:hf_db:admin:some_password
chmod 600 ~/.pgpass
psql -h localhost -U admin hf_db
```
Run SQL dump, if you have:
```bash
psql -h localhost hf_db admin < dump.sql
```
#### Configure NGINX
```bash
sudo vim /etc/nginx/sites-enabled
default@
```
##### Delete all and write:
```bash
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location /static {
                alias /home/www/code/Happy-Family/HappyFamily/static;
                try_files $uri $uri =404;
        }

        location /media {
                alias /home/www/code/Happy-Family/HappyFamily/media;
                try_files $uri $uri =404;
        }

        location / {
                proxy_pass http://127.0.0.1:8001;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
                add_header Access-Control-Allow-Origin *;
        }
}
```
##### Restart NGINX
```bash
sudo service nginx restart
```
#### Options for static
##### Don’t forget create folder static in root directory and then
```bash
python manage.py collectstatic
```
#### Install and configure supervisor
```bash
sudo vim /etc/supervisor/conf.d/HappyFamily.conf
```
Add to file
```bash
[program:www_gunicorn]
command=/home/www/code/Happy-Family/bin/start_gunicorn.sh
user=www
process_name=%(program_name)s
numprocs=1
autostart=true
autorestart=true
redirect_stderr=true
```
#### Configure Gmail
https://myaccount.google.com/security

Untrusted apps that have access to your account

Set ON
