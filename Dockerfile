FROM node:22-bookworm-slim

WORKDIR /workspace
RUN npx playwright@1.46.0 install chromium --with-deps
RUN apt install -y xauth

COPY . /workspace
RUN npm install
ENTRYPOINT npm run server