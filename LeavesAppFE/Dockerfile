#base image
FROM node:current-alpine

#create working dir
RUN mkdir -p /app/src

#set working dir
WORKDIR /app/src

#copy and install dependencies
COPY package*.json .
RUN npm install

COPY . .

EXPOSE 8080

#Start app
CMD ["npm", "run", "dev"]