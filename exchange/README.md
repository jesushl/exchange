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
WORKDIR /exchange/exchange/
RUN pip3  install -r requirements.txt 
EXPOSE 80
ENV fixer=<fixer_token>
ENV banxico=<banxico_token>
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
```
(pleace edit it to add your token on the image)

# Settings 
This project requires two operation tokens ,
one for fixer and othrer eith enoght privileges 
to consult USD in fixer. 
This aplication consumes both from system environment 
as 'fixer' and 'banxico'
