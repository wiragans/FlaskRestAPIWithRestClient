# FlaskRestAPIWithRestClient
Rest API Endpoint:

1. Login:
POST https://wirauhuy123.pythonanywhere.com/api/v1/login
Content-Type: application/x-www-form-urlencoded
Authorization: Basic dXNlcnRlc3RhcGlmbGFzazpwYXNzdGVzdGFwaWZsYXNr
clientId: b09218e436dd137d454d3d54488108e1
hash: sha256("usernamepassword/wiradwisoke/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")

username=xxxxxx&password=xxxxxx

{"statusCode": 200, "status": true, "code": "00", "message": "Login Sukses", "access_token": accessToken, "refresh_token": refreshToken, "token_type": "Bearer", "expires_in": 1800}

2. Register:
POST https://wirauhuy123.pythonanywhere.com/api/v1/register
Content-Type: application/x-www-form-urlencoded
Authorization: Basic dXNlcnRlc3RhcGlmbGFzazpwYXNzdGVzdGFwaWZsYXNr
clientId: b09218e436dd137d454d3d54488108e1
hash: sha256("namausernamepassword/wiradwisoke/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")

nama=xxxxxx&username=xxxxxx&password=xxxxxxx
