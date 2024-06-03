## Инструкция по запуску Docker контейнера

Необходимо на хост-компьютере установить Docker для необходимой платформы, скачав его по
адресу https://docs.docker.com/get-docker/

### Запуск

- Воти в учетную запись postgres с помощью команды `sudo -i -u postgres`
  - Создать базу данных с помощью команды `createdb [database_name]`
  - Перейти в консоль postgresql с помощью команды `psql`
    - Создать пользователя с помощью команды `CREATE USER [user_name] WITH PASSWORD 'password';`
    - Дать созданному пользователю права суперпользователя с помощью команды `ALTER USER [user_name] WITH SUPERUSER;`
    - Выйти из консольного режима с помощью команды `\q`
  - Выйти из учетной записи postgres с помощью команды `exit`
- Собрать образ контейнера с помощью команды `docker-compose build`
- Запустить контейнеры с помощью команды `docker-compose up`