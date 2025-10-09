package handlers

import (
	"github.com/chanakya-ex3/APIMeter/redis"
	"context"
	"net/http"

	"github.com/gin-gonic/gin"
)

func FlushCacheHandler(c *gin.Context) {
	ctx := context.Background()
	err := redis.Client.FlushDB(ctx).Err()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to flush cache"})
		return
	}
	c.JSON(http.StatusOK, gin.H{"message": "Redis cache flushed"})
}
