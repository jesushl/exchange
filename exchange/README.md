### Exchange prototype

This prototype gets values from Banco de Mexico,  Diario Oficial de la Federacion and Fixer and show 
USD currecy value in MXN .

To un this project is possible use a docker project image

# Docker 

```
FROM ubuntu:latest
MAINTAINER "Jesus H. Ledon"
RUN     apt-get  update
RUN     apt-get install -y git  \
            && apt-get install -y python \
            && apt-get install -y python3-pip
RUN  exec git clone https://github.com/jesushl/exchange.git  
WORKDIR /exchange/
RUN pip3  install -r requirements.txt 
EXPOSE 80
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
```

# Settings
E