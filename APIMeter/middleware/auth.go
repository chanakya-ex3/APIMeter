package middleware

import (
	"os"
	"strings"

	"github.com/chanakya-ex3/APIMeter/handlers"
	"github.com/gin-gonic/gin"
)

func AuthMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		if strings.ToLower(os.Getenv("ENABLE_AUTH")) != "true" {
			c.Next()
			return
		}
		appid := c.GetHeader("X-App-Id")
		appKey := c.GetHeader("X-App-Key")
		if appid == "" || appKey == "" || !handlers.ValidateAppKey(appid, appKey) {
			c.AbortWithStatusJSON(401, gin.H{"error": "Invalid or missing appid/appKey"})
			return
		}
		c.Set("appid", appid)
		c.Next()
	}
}
