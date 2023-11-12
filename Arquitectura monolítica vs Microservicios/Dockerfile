# DockerFile para crear una imagen de acuerdo a nuestro JS que utilizaremos
FROM node:18

WORKDIR /nodejs/app

COPY package*.json ./
RUN npm install

EXPOSE 8080

COPY . .
CMD [ "node", "index.js" ]