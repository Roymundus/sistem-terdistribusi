FROM golang:1.18-alpine

RUN mkdir /app

RUN addgroup -S humangroup
RUN adduser -S -D -h /app humanuser humangroup
RUN chown -R humanuser:humangroup /app
USER humanuser

COPY main.go /app

EXPOSE 8080
CMD go run /app/main.go
