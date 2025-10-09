package handlers

var AppKeys = map[string]string{
	"demoappid": "demokey123", // appid: appKey
}

func ValidateAppKey(appid, appKey string) bool {
	if key, ok := AppKeys[appid]; ok {
		return key == appKey
	}
	return false
}
