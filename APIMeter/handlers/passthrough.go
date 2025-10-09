package handlers

import (
	"github.com/chanakya-ex3/APIMeter/config"
	"fmt"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func PassthroughHandler(c *gin.Context) {
	targetURL := fmt.Sprintf("%s%s", config.TargetAPI, c.FullPath())
	req, err := http.NewRequest(c.Request.Method, targetURL, c.Request.Body)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to create request"})
		return
	}
	for k, v := range c.Request.Header {
		for _, vv := range v {
			req.Header.Add(k, vv)
		}
	}
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error reaching target API: %v\n", err)
		c.JSON(http.StatusBadGateway, gin.H{"error": "Failed to reach target API"})
		return
	}
	defer resp.Body.Close()
	for k, v := range resp.Header {
		for _, vv := range v {
			c.Writer.Header().Add(k, vv)
		}
	}
	c.Status(resp.StatusCode)
	_, _ = io.Copy(c.Writer, resp.Body)
}
