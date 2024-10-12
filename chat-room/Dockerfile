FROM alpine:3.20 AS clone

RUN apk --no-cache add git
RUN git clone https://github.com/cuinjune/chat-room.git
RUN mkdir -p /chat-room/db && echo '{"numVisitors": 0,"data": []}' > /chat-room/db/data.json

FROM node:lts-alpine
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.schema-version="1.0"
LABEL maintainer=adamrzepka@student.agh.edu.pl
LABEL org.opencontainers.image.source=https://github.com/cuinjune/chat-room
COPY --from=clone /chat-room /chat-room
WORKDIR /chat-room
RUN npm install --omit=dev
EXPOSE 3000
CMD ["npm", "start"]
