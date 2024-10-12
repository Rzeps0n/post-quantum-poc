FROM alpine AS clone
RUN apk fix && apk --no-cache --update add git
RUN git clone https://github.com/cuinjune/chat-room.git
RUN echo '{"numVisitors": 0,"data": []}' > ./chat-room/db/data.json
FROM node:lts-alpine
COPY --from=clone /chat-room/ /chat-room/
WORKDIR /chat-room
RUN npm install dependencies
CMD [ "npm", "start" ]
EXPOSE 3000
