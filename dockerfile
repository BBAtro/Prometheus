FROM node:20

WORKDIR /app

# Install dependencies and build
COPY package.json package-lock.json ./
RUN npm install
RUN npm install vite -g
RUN npm run build

# Start the server
CMD ["npm", "run", "dev"]

# Start a new build stage
FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
