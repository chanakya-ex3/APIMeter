FROM golang:1.24.5-alpine

# Install Git (needed for go mod tidy)
RUN apk add --no-cache git

WORKDIR /app

# Copy mod files and download deps early
COPY go.mod go.sum ./
RUN go mod tidy

# Copy rest of the source code
COPY . .

# Build
RUN go build -o server .

EXPOSE 8080
CMD ["./server"]
