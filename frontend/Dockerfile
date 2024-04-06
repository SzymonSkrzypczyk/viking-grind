FROM node:lts AS build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/public /usr/share/nginx/html

EXPOSE 90

CMD ["nginx", "-g", "daemon off;"]
