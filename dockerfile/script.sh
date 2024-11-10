
# FROM Instruction
docker build -t roymunduss/from from

docker image ls 

# RUN Instruction
docker build -t roymundus/run run

docker build -t roymundus/run run --progress=plain --no-cache

# CMD Instruction
docker build -t roymunduss/command command

docker image inspect roymunduss/command 

docker container create --name command roymunduss/command

docker container start command

docker container logs command

# LABEL Instruction
docker build -t roymunduss/label label

docker image inspect roymunduss/label

# ADD Instruction
docker build -t roymunduss/add add

docker container create --name add roymunduss/add 

docker container start add

docker container logs add

# COPY Instrcutin
docker build -t roymunduss/copy copy

docker container create --name copy roymunduss/copy

docker container start copy

docker container logs copy

# IGNORE Instruction
docker build -t roymunduss/ignore ignore

docker container create --name ignore roymunduss/ignore

docker container start ignore

docker container logs ignore


# EXPOSE Instruction
docker build -t roymunduss/expose expose

docker image inspect roymunduss/expose

docker container create --name expose -p 8080:8080 roymunduss/expose

docker container start expose

docker container ls

docker container stop expose

# ENV Instruction
docker build -t roymunduss/env env

docker image inspect roymunduss/env

docker container create --name env --env APP_PORT=9090 -p 9090:9090 roymunduss/env

docker container start env

docker container ls

docker container logs env   

# VOLUME Instruction
docker build -t roymunduss/volume volume

docker image inspect roymunduss/volume

docker container create --name volume -p 8080:8080 roymunduss/volume

docker container start volume

docker container ls

docker container logs volume

docker container inspect volume
6643a833ca0d42f757afef3ffe070565b4a2908a89b1896197c0395b1fd5425a


# WORKDIR Instruction
docker build -t roymunduss/workdir workdir

docker image inspect roymunduss/workdir

docker container create --name workdir -p 8080:8080 roymunduss/workdir

docker container start workdir

docker container exec -i -t workdir /bin/sh

docker container ls

docker container logs workdir

# USER Instruction
docker build -t roymunduss/user user

docker container create --name user -p 8080:8080 roymunduss/user

docker container start user

docker container exec -i -t user /bin/sh

docker container ls

# ARG Instruction
docker build -t roymunduss/arg arg --build-arg app=humanuser

docker container create --name arg -p 8080:8080 roymunduss/arg

docker container start arg

docker container exec -i -t arg /bin/sh

docker container logs arg

# HEALTHCHECK Instruction
docker build -t roymunduss/health health

docker container create --name health -p 8080:8080 roymunduss/health

docker container start health

docker container ls

docker container inspect health

# ENTRYPOINT Instruction
docker build -t roymunduss/entrypoint entrypoint

docker image inspect roymunduss/entrypoint

docker container create --name entrypoint -p 8080:8080 roymunduss/entrypoint

docker container start entrypoint

# Multi Stage Build
docker build -t roymunduss/multi multi

docker image ls

docker container create --name multi -p 8080:8080 roymunduss/multi

docker container start multi

# Docker Push
docker tag roymunduss/multi registry.digitalocean.com/programmerzamannow/multi

docker --config /Users/roymunduss/.docker-digital-ocean/ push registry.digitalocean.com/programmerzamannow/multi

docker --config /Users/roymunduss/.docker-digital-ocean/ pull registry.digitalocean.com/programmerzamannow/multi