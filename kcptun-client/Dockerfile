FROM golang:1.22-alpine3.20 AS build
ENV GO111MODULE=on CGO_ENABLED=0
RUN apk add --no-cache git
RUN git clone https://github.com/xtaci/kcptun.git
RUN cd kcptun && go build -mod=vendor -ldflags "-X main.VERSION=$(date -u +%Y%m%d) -s -w" -o /client github.com/xtaci/kcptun/client

FROM alpine:3.20
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.schema-version="1.0"
LABEL maintainer=adamrzepka@student.agh.edu.pl
LABEL org.opencontainers.image.source=https://github.com/xtaci/kcptun
RUN apk add --no-cache iptables
COPY --from=build /client /kcptun/
ENV TUNNELED_IP=0.0.0.0 TUNNELED_PORT=4000 LISTEN_PORT=3000
ENV PARAMS="-mode fast3 -nocomp -crypt Salsa20 -QPP -QPPCount 101 -smuxver 2"
WORKDIR /kcptun
CMD ["sh", "-c", "./client -r \"$TUNNELED_IP:$TUNNELED_PORT\" -l ':$LISTEN_PORT' $PARAMS"]
EXPOSE 3000
