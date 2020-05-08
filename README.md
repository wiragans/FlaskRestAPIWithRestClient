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

{"statusCode": 200, "status": true, "code": "00", "message": "Registrasi Akun Sukses"}

3. Check Login:

GET https://wirauhuy123.pythonanywhere.com/api/v1/check_login

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

{"statusCode": 200, "status": true, "code": "00", "message": "ACTIVE", "expires_in": 1591, "token_type": "Bearer"}

4. Get Activity:

GET https://wirauhuy123.pythonanywhere.com/api/v1/get_activity

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

{"statusCode": 200, "status": true, "code": "00", "message": "Sukses menampilkan data aktivitas", "data": [{"id": 1, "nama_aktivitas": "Tugas Web Service Image Transfer", "start_plan_timestamp": "1588749600", "real_start_plan": "2020-05-06 14:20:00 WIB", "end_plan_timestamp": "1589987400", "real_end_plan": "2020-05-20 22:10:00 WIB", "status": 1, "status_text": "Proses"}, {"id": 10, "nama_aktivitas": "OK", "start_plan_timestamp": "1588605720", "real_start_plan": "2020-05-04 22:22:00 WIB", "end_plan_timestamp": "1590506520", "real_end_plan": "2020-05-26 22:22:00 WIB", "status": 0, "status_text": "Belum Dilaksanakan"}, {"id": 19, "nama_aktivitas": "Sahur New", "start_plan_timestamp": "1588968420", "real_start_plan": "2020-05-09 03:07:00 WIB", "end_plan_timestamp": "1588986420", "real_end_plan": "2020-05-09 08:07:00 WIB", "status": 0, "status_text": "Belum Dilaksanakan"}, {"id": 20, "nama_aktivitas": "Sahur Baru", "start_plan_timestamp": "1588950360", "real_start_plan": "2020-05-08 22:06:00 WIB", "end_plan_timestamp": "1589569560", "real_end_plan": "2020-05-16 02:06:00 WIB", "status": 0, "status_text": "Belum Dilaksanakan"}]}

5. Add Activity:

POST https://wirauhuy123.pythonanywhere.com/api/v1/add_activity

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

nama_aktivitas=xxxxxx&start_plan=timestamp&end_plan=timestamp&status=0/1/2

{"statusCode": 200, "status": true, "code": "00", "message": "Sukses menambahkan daftar aktivitas!"}

6. Edit/Update Activity:

PUT https://wirauhuy123.pythonanywhere.com/api/v1/update_activity/{activity_id}

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

nama_aktivitas=xxxxxx&start_plan=timestamp&end_plan=timestamp&status=0/1/2

{"statusCode": 200, "status": true, "code": "00", "message": "Sukses update aktivitas Anda!"}

7. Delete Activity:

DELETE https://wirauhuy123.pythonanywhere.com/api/v1/delete_activity/{activity_id}

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

{"statusCode": 200, "status": true, "code": "00", "message": "Aktivitas berhasil dihapus"}

8. Update Token Session

PATCH https://wirauhuy123.pythonanywhere.com/api/v1/update_token

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer oldAccessToken

clientId: b09218e436dd137d454d3d54488108e1

refresh_token=refreshToken

{"statusCode": 200, "status": true, "code": "00", "message": "Token Updated", "new_access_token": accessToken, "token_type": "Bearer", "expires_in": 1800}

9. Home Dashboard (Welcome Text):

GET https://wirauhuy123.pythonanywhere.com/api/v1/home_dashboard

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

{"statusCode": 200, "status": true, "code": "00", "message": "Berhasil menampilkan data", "nama_lengkap": NamaAnda}

10. Logout:

GET https://wirauhuy123.pythonanywhere.com/api/v1/logout

Content-Type: application/x-www-form-urlencoded

Authorization: Bearer accessToken

clientId: b09218e436dd137d454d3d54488108e1

{"statusCode": 200, "status": true, "code": "00", "message": "Logout Akun Berhasil!"}
