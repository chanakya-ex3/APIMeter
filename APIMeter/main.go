package main

import (
	"github.com/chanakya-ex3/APIMeter/config"
	"github.com/chanakya-ex3/APIMeter/handlers"
	"github.com/chanakya-ex3/APIMeter/middleware"
	"github.com/chanakya-ex3/APIMeter/redis"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	_ = godotenv.Load()
	config.LoadEndpointsFromEnv()
	redis.InitRedis()
	config.LoadTargetAPI()

	r := gin.Default()
	r.Use(middleware.AuthMiddleware())
	for path, limit := range config.Endpoints {
		r.Any(path, middleware.RateLimitMiddleware(limit), handlers.PassthroughHandler)
	}

	r.GET("/flush-cache", handlers.FlushCacheHandler)
	r.NoRoute(middleware.RateLimitMiddleware(config.DefaultRateLimit), handlers.PassthroughHandler)

	r.Run(":8080")
}
