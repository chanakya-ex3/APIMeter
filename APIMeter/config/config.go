package config

import (
	"fmt"
	"os"
	"strings"
)

var (
	Endpoints        = map[string]int{}
	DefaultRateLimit = 10
	TargetAPI        string
)

func LoadEndpointsFromEnv() {
	envEndpoints := os.Getenv("ENDPOINTS")
	for _, pair := range strings.Split(envEndpoints, ",") {
		parts := strings.Split(pair, ":")
		if len(parts) == 2 {
			path := parts[0]
			var limit int
			fmt.Sscanf(parts[1], "%d", &limit)
			Endpoints[path] = limit
		}
	}
}

func LoadTargetAPI() {
	TargetAPI = os.Getenv("TARGET_API_URL")
}
