FROM golang:1.22-alpine3.20 AS build
ENV GO111MODULE=on CGO_ENABLED=0
RUN apk add --no-cache git
RUN git clone https://github.com/xtaci/kcptun.git
RUN cd kcptun && go build -mod=vendor -ldflags "-X main.VERSION=$(date -u +%Y%m%d) -s -w" -o /server github.com/xtaci/kcptun/server

FROM alpine:3.20
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.schema-version="1.0"
LABEL maintainer=adamrzepka@student.agh.edu.pl
LABEL org.opencontainers.image.source=https://github.com/xtaci/kcptun
RUN apk add --no-cache iptables
COPY --from=build /server /kcptun/
ENV TUNNELED_IP=0.0.0.0 TUNNELED_PORT=3000
WORKDIR /kcptun
CMD ["sh", "-c", "./server -t \"$TUNNELED_IP:$TUNNELED_PORT\" -l ':4000' -mode fast3 -nocomp -sockbuf 16777217 -dscp 46 -QPP -QPPCount 61"]
EXPOSE 4000
