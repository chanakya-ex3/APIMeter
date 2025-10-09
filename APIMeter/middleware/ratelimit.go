package middleware

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/chanakya-ex3/APIMeter/redis"

	"github.com/gin-gonic/gin"
)

var window = time.Minute

func RateLimitMiddleware(rateLimit int) gin.HandlerFunc {
	return func(c *gin.Context) {
		if rateLimit == 0 {
			c.Next()
			return
		}
		ctx := context.Background()
		var keyID string
		if strings.ToLower(os.Getenv("ENABLE_AUTH")) == "true" {
			appid, _ := c.Get("appid")
			keyID = appid.(string)
		} else {
			keyID = c.ClientIP()
		}
		key := fmt.Sprintf("ratelimit:%s:%s:%d", keyID, c.FullPath(), time.Now().Unix()/int64(window.Seconds()))
		count, err := redis.Client.Incr(ctx, key).Result()
		if err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{"error": "internal error"})
			return
		}
		if count == 1 {
			redis.Client.Expire(ctx, key, window+time.Second*5)
		}
		if count > int64(rateLimit) {
			c.AbortWithStatusJSON(http.StatusTooManyRequests, gin.H{"error": "rate limit exceeded"})
			return
		}
		c.Next()
	}
}
