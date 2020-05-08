
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, url_for
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
#from datetime import datetime
import hashlib
import json
#import jsonify
import os, time

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'hostdatabaseanda'
app.config['MYSQL_USER'] = 'usernamedatabaseanda'
app.config['MYSQL_PASSWORD'] = 'passworddatabaseanda'
app.config['MYSQL_DB'] = 'namadatabaseanda'
mysql = MySQL(app)
cors = CORS(app)
app.config['CORS_ORIGIN'] = '*'
app.config['CORS_METHODS'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
app.config['CORS_HEADERS'] = 'Content-Type, Authorization, clientId, hash, User-Agent'
setClientID = 'b09218e436dd137d454d3d54488108e1';

os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()
#time.strftime('%X %x %Z')

@app.route('/')
def hello_world():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    #return 'Hello from Flask!'
    #return '''<b>Welcome to Wira Dwi Susanto's API</b>''';
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.errorhandler(405)
def mna(e):
  #return '<b>405 Method Not Allowed</b>'
  return json.dumps({'statusCode':405, 'status':False, 'code':'01', 'message':'Method Not Allowed'}), 405, {'Content-Type':'application/json'}

@app.errorhandler(400)
def bdr(e):
  #return '<b>400 Bad Request</b>'
  return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Bad Request'}), 400, {'Content-Type':'application/json'}

@app.errorhandler(500)
def ise(e):
  #return '<b>500 Internal Server Error</b>'
  return json.dumps({'statusCode':500, 'status':False, 'code':'01', 'message':'Internal Server Error'}), 500, {'Content-Type':'application/json'}

@app.errorhandler(404)
def not_found(e):
  #return '<b>404 Not Found</b>'
  return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}

@app.route('/api')
def api():
    return '''<b>Welcome to Wira Dwi Susanto's API</b>''';

@app.route('/api/v1')
def apiv1():
    return '''<b>Welcome to Wira Dwi Susanto's API</b>''';

##HASH
def hashLogin(hash_string):
    hash_sha256 = hashlib.sha256(hash_string.encode()).hexdigest()
    return hash_sha256

##HOME DASHBOARD
@app.route('/api/v1/home_dashboard', methods=['GET', 'OPTIONS'])
@cross_origin()
def homedashboardv1():
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            hasilData = cur.fetchall()
            for row in hasilData:
                getAccessTokenTimestamp = str(row[6])
                getNamaLengkap = str(row[1])
            getAccessTokenTimestamp2 = int(getAccessTokenTimestamp)
            timeNow = int(time.time())
            selisihWaktu = getAccessTokenTimestamp2 - timeNow
            if selisihWaktu <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktu > 0:
                return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Berhasil menampilkan data', 'nama_lengkap':getNamaLengkap}), 200, {'Content-Type':'application/json'}
                exit(0)

##UPDATE TOKEN
@app.route('/api/v1/update_token', methods=['PATCH', 'OPTIONS'])
@cross_origin()
def updatetokenv1():
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        cek = cur.rowcount
        hasilData = cur.fetchall()
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            details = request.form
            getRefreshToken = details['refresh_token']
            if not getRefreshToken:
                return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Refresh Token Must Be Included!'}), 200, {'Content-Type':'application/json'}
                exit(0)
            for bacaUser in hasilData:
                getUsername = str(bacaUser[3])
                getPassword = str(bacaUser[4])
            accessTokenTime = int(time.time() + 1800)
            generateAccessToken = hashLogin(getUsername + getPassword + str(accessTokenTime) + "/wiradwisoke/iniadalahaccesstokennya/9003d081345e9f0451884146e9ea2cff6e4cc4deac9ffd4a9ee98b318a49/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")
            newBearerToken = str(generateAccessToken)
            timeNow = int(time.time())
            cur2 = mysql.connection.cursor()
            cur2.execute("SELECT * FROM users WHERE BINARY refresh_token=%s", [getRefreshToken])
            cek2 = cur2.rowcount
            if cek2 <= 0:
                return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Invalid Refresh Token'}), 200, {'Content-Type':'application/json'}
                exit(0)
            if cek2 > 0:
                hasilData2 = cur2.fetchall()
                for row in hasilData2:
                    getRefreshTokenTimestamp = int(row[7])
            selisihWaktuRefreshToken = getRefreshTokenTimestamp - timeNow
            tambahWaktuToken = timeNow + 1800
            if selisihWaktuRefreshToken <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktuRefreshToken > 0:
                inputData = [str(newBearerToken), int(tambahWaktuToken), str(getRefreshToken)]
                cur3 = mysql.connection.cursor()
                cur3.execute("UPDATE users SET access_token=%s, access_token_timestamp=%s WHERE BINARY refresh_token=%s", inputData)
                mysql.connection.commit()
                cur3.close()
                cek3 = cur3.rowcount
                if cek3 <= 0:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'An error occured when updating your session!'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                if cek3 > 0:
                    return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Token Updated', 'new_access_token':newBearerToken, 'token_type':'Bearer', 'expires_in':1800}), 200, {'Content-Type':'application/json'}
                    exit(0)

##GET ACTIVITY
@app.route('/api/v1/get_activity', methods=['GET', 'OPTIONS'])
@cross_origin()
def getactivityv1():
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            hasilData = cur.fetchall()
            for row in hasilData:
                getAccessTokenTimestamp = str(row[6])
                getUsername = str(row[2])
            getAccessTokenTimestamp2 = int(getAccessTokenTimestamp)
            getUsername2 = str(getUsername)
            timeNow = int(time.time())
            selisihWaktu = getAccessTokenTimestamp2 - timeNow
            if selisihWaktu <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktu > 0:
                cur2 = mysql.connection.cursor()
                cur2.execute("SELECT aktivitas.id, aktivitas.nama_aktivitas, aktivitas.start_plan as 'start_plan_timestamp', CONCAT(CONVERT_TZ(DATE_FORMAT(FROM_UNIXTIME(aktivitas.start_plan), '%%Y-%%m-%%d %%H:%%i:%%s'), 'UTC', 'Asia/Jakarta'), ' WIB') as 'real_start_plan', aktivitas.end_plan as 'end_plan_timestamp', CONCAT(CONVERT_TZ(DATE_FORMAT(FROM_UNIXTIME(aktivitas.end_plan), '%%Y-%%m-%%d %%H:%%i:%%s'), 'UTC', 'Asia/Jakarta'), ' WIB') as 'real_end_plan', aktivitas.status, aktivitas_status.status_text FROM aktivitas_status INNER JOIN aktivitas ON BINARY aktivitas.status=aktivitas_status.status WHERE BINARY aktivitas.username=%s ORDER BY aktivitas.id ASC", [getUsername2])
                #cur2.execute("SELECT * FROM aktivitas WHERE BINARY username=%s ORDER BY id DESC", [getUsername2])
                row_headers = [x[0] for x in cur2.description]
                hasilData2 = cur2.fetchall()
                json_data = []
                #for row2 in hasilData2:
                for result in hasilData2:
                    #getId = int(result[0])
                    json_data.append(dict(zip(row_headers, result)))
                json_string = str(json.dumps(json_data))
                json_string_encode = json.loads(json_string.replace("\'", '"'))
                return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Sukses menampilkan data aktivitas', 'data':json_string_encode}), 200, {'Content-Type':'application/json'}

##CHECK LOGIN
@app.route('/api/v1/check_login', methods=['GET', 'OPTIONS'])
@cross_origin()
def checkloginv1():
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        #row_headers=[x[0] for x in cur.description]
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            hasilData = cur.fetchall()
            #json_data=[]
            #for result in hasilData:
            #    json_data.append(dict(zip(row_headers,result)))
            #    return json.dumps(json_data[0])
            for row in hasilData:
                getAccessTokenTimestamp = str(row[6])
            getAccessTokenTimestamp2 = int(getAccessTokenTimestamp)
            timeNow = int(time.time())
            selisihWaktu = getAccessTokenTimestamp2 - timeNow
            if selisihWaktu <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktu > 0:
                return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'ACTIVE', 'expires_in':selisihWaktu, 'token_type':'Bearer'}), 200, {'Content-Type':'application/json'}
                exit(0)

##REGISTER
@app.route('/api/v1/register', methods=['POST', 'OPTIONS'])
@cross_origin()
def registerv1():
    getHash = request.headers['hash']
    getBasicToken = str(request.headers.get('Authorization'))
    substrBasicCaption = str(getBasicToken[:5])
    substrBasicToken = str(getBasicToken[6:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBasicCaption != "Basic":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if substrBasicToken != "dXNlcnRlc3RhcGlmbGFzazpwYXNzdGVzdGFwaWZsYXNr":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        details = request.form
        nama = details['nama']
        username = details['username']
        password = details['password']
        validateHashLogin = hashLogin(nama + username + password + "/wiradwisoke/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")
        if validateHashLogin != getHash:
            return json.dumps({'statusCode':403, 'status':False, 'code':'01', 'message':'Registration Request Rejected. Invalid Signature Hash'}), 403, {'Content-Type':'application/json'}
            exit(0)
        if not nama or not username or not password:
            return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Lengkapi bagian yang kosong'}), 200, {'Content-Type':'application/json'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", [username])
        cek = cur.rowcount
        if cek > 0:
            return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Username telah digunakan'}), 200, {'Content-Type':'application/json'}
            exit(0)
        if cek <= 0:
            cur2 = mysql.connection.cursor()
            cur2.execute("INSERT INTO users(nama, username, password) VALUES(%s, %s, %s)", (nama, username, password))
            mysql.connection.commit()
            cur2.close()
            cek2 = cur2.rowcount
            if cek2 <= 0:
                return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Terjadi kesalahan saat registrasi!'}), 200, {'Content-Type':'application/json'}
                exit(0)
            if cek2 > 0:
                return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Registrasi Akun Sukses'}), 200, {'Content-Type':'application/json'}

##ADD ACTIVITY
@app.route('/api/v1/add_activity', methods=['POST', 'OPTIONS'])
@cross_origin()
def addactivityv1():
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            hasilData = cur.fetchall()
            for row in hasilData:
                getAccessTokenTimestamp = str(row[6])
                getUsername = str(row[2])
            getAccessTokenTimestamp2 = int(getAccessTokenTimestamp)
            getUsername2 = str(getUsername)
            timeNow = int(time.time())
            selisihWaktu = getAccessTokenTimestamp2 - timeNow
            if selisihWaktu <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktu > 0:
                details = request.form
                namaaktivitas = details['nama_aktivitas'] #STRING
                startplan = details['start_plan'] #HARUS TIMESTAMP
                endplan = details['end_plan'] #HARUS TIMESTAMP
                statusplan = details['status'] #HARUS INT
                statusplan2 = int(statusplan)
                if not namaaktivitas or not startplan or not endplan or not statusplan:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Bagian field ada yang kosong!'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                if statusplan2 != 0 and statusplan2 != 1 and statusplan2 != 2:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Status plan must be 1 or 2 or 3'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                dataInput = [str(getUsername2), str(namaaktivitas), int(startplan), int(endplan), int(statusplan)]
                cur2 = mysql.connection.cursor()
                cur2.execute("INSERT INTO aktivitas(username, nama_aktivitas, start_plan, end_plan, status) VALUES(%s, %s, %s, %s, %s)", dataInput)
                mysql.connection.commit()
                cur2.close()
                cek2 = cur2.rowcount
                if cek2 <= 0:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Terjadi kesalahan saat menambahkan daftar aktivitas!'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                if cek2 > 0:
                    return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Sukses menambahkan daftar aktivitas!'}), 200, {'Content-Type':'application/json'}
                    exit(0)

##UPDATE ACTIVITY
@app.route('/api/v1/update_activity/<id>', methods=['PUT', 'OPTIONS'])
@cross_origin()
def updateactivityv1(id):
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            hasilData = cur.fetchall()
            for row in hasilData:
                getAccessTokenTimestamp = str(row[6])
                getUsername = str(row[2])
            getAccessTokenTimestamp2 = int(getAccessTokenTimestamp)
            getUsername2 = str(getUsername)
            getAktivitasId = id
            timeNow = int(time.time())
            selisihWaktu = getAccessTokenTimestamp2 - timeNow
            if selisihWaktu <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktu > 0:
                dataInput = [str(getUsername2), int(getAktivitasId)]
                cur2 = mysql.connection.cursor()
                cur2.execute("SELECT * FROM aktivitas WHERE BINARY username=%s AND id=%s", dataInput)
                cek2 = cur2.rowcount
                if cek2 <= 0:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Aktivitas tidak dapat ditemukan'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                if cek2 > 0:
                    details = request.form
                    namaaktivitas = details['nama_aktivitas'] #STRING
                    startplan = details['start_plan'] #HARUS TIMESTAMP
                    endplan = details['end_plan'] #HARUS TIMESTAMP
                    statusplan = details['status'] #HARUS INT
                    statusplan2 = int(statusplan)
                    if not namaaktivitas or not startplan or not endplan or not statusplan:
                        return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Bagian field ada yang kosong!'}), 200, {'Content-Type':'application/json'}
                        exit(0)
                    if statusplan2 != 0 and statusplan2 != 1 and statusplan2 != 2:
                        return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Status plan must be 1 or 2 or 3'}), 200, {'Content-Type':'application/json'}
                        exit(0)
                    dataInput2 = [str(getUsername2), str(namaaktivitas), int(startplan), int(endplan), int(statusplan), str(getUsername2), int(getAktivitasId)]
                    cur3 = mysql.connection.cursor()
                    cur3.execute("UPDATE aktivitas SET username=%s, nama_aktivitas=%s, start_plan=%s, end_plan=%s, status=%s WHERE BINARY username=%s AND id=%s", dataInput2)
                    mysql.connection.commit()
                    cur3.close()
                    cek3 = cur3.rowcount
                    if cek3 <= 0:
                        return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Terjadi kesalahan saat update aktivitas Anda!'}), 200, {'Content-Type':'application/json'}
                        exit(0)
                    if cek3 > 0:
                        return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Sukses update aktivitas Anda!'}), 200, {'Content-Type':'application/json'}
                        exit(0)

##DELETE ACTIVIY
@app.route('/api/v1/delete_activity/<id>', methods=['DELETE', 'OPTIONS'])
@cross_origin()
def deleteactivityv1(id):
    #return 'Delete Activity'
    #return "%d"%time.time()
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            hasilData = cur.fetchall()
            for row in hasilData:
                getAccessTokenTimestamp = str(row[6])
                getUsername = str(row[2])
            getAccessTokenTimestamp2 = int(getAccessTokenTimestamp)
            getUsername2 = str(getUsername)
            getAktivitasId = id
            timeNow = int(time.time())
            selisihWaktu = getAccessTokenTimestamp2 - timeNow
            if selisihWaktu <= 0:
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Session Expired'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Session Expired"'}
                exit(0)
            if selisihWaktu > 0:
                dataInput = [int(getAktivitasId), str(getUsername2)]
                cur2 = mysql.connection.cursor()
                cur2.execute("SELECT * FROM aktivitas WHERE BINARY id=%s AND username=%s", dataInput)
                cek2 = cur2.rowcount
                if cek2 <= 0:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Aktivitas tidak dapat ditemukan!'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                if cek2 > 0:
                    dataInput2 = [str(getUsername2), int(getAktivitasId)]
                    cur3 = mysql.connection.cursor()
                    cur3.execute("DELETE FROM aktivitas WHERE BINARY username=%s AND id=%s", dataInput2)
                    mysql.connection.commit()
                    cur3.close()
                    cek3 = cur3.rowcount
                    if cek3 <= 0:
                        return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Terjadi kesalahan saat menghapus aktivitas!'}), 200, {'Content-Type':'application/json'}
                        exit(0)
                    if cek3 > 0:
                        return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Aktivitas berhasil dihapus'}), 200, {'Content-Type':'application/json'}
                        exit(0)

##LOGOUT
@app.route('/api/v1/logout', methods=['GET', 'OPTIONS'])
@cross_origin()
def logoutv1():
    getBearerToken = str(request.headers.get('Authorization'))
    substrBearerCaption = str(getBearerToken[:6])
    substrBearerToken = str(getBearerToken[7:])
    getClientId = request.headers.get('clientId')
    getContentType = request.headers.get('Content-Type')
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        if getClientId != setClientID:
            return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
            exit(0)
        if substrBearerCaption != "Bearer":
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if not substrBearerToken:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE BINARY access_token=%s ORDER BY id DESC LIMIT 1", [substrBearerToken])
        mysql.connection.commit()
        cur.close()
        cek = cur.rowcount
        if cek <= 0:
            return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
            exit(0)
        if cek > 0:
            cur2 = mysql.connection.cursor()
            cur2.execute("UPDATE users SET access_token='', refresh_token='', access_token_timestamp='', refresh_token_timestamp='' WHERE BINARY access_token=%s", [substrBearerToken])
            mysql.connection.commit()
            cur2.close()
            cek2 = cur2.rowcount
            if cek2 <= 0:
                return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Terjadi kesalahan saat logout!'}), 200, {'Content-Type':'application/json'}
                exit(0)
            if cek2 > 0:
                return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Logout Akun Berhasil!'}), 200, {'Content-Type':'application/json'}

##LOGIN
@app.route('/api/v1/login', methods=['POST', 'OPTIONS'])
@cross_origin()
def loginv1():
    getBasicToken = str(request.headers.get('Authorization'))
    substrBasicCaption = str(getBasicToken[:5])
    substrBasicToken = str(getBasicToken[6:])
    getHash = request.headers['hash']
    getClientId = request.headers['clientId']
    getContentType = request.headers['Content-Type']
    if getContentType != "application/x-www-form-urlencoded":
        return json.dumps({'statusCode':404, 'status':False, 'code':'01', 'message':'The resource could not be found'}), 404, {'Content-Type':'application/json'}
    else:
        #return 'benar'
        if request.method == "POST":
            if getClientId != setClientID:
                return json.dumps({'statusCode':400, 'status':False, 'code':'01', 'message':'Invalid ClientId'}), 400, {'Content-Type':'application/json'}
                exit(0)
            details = request.form
            username = details['username']
            password = details['password']
            validateHashLogin = hashLogin(username + password + "/wiradwisoke/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")
            if validateHashLogin != getHash:
                return json.dumps({'statusCode':403, 'status':False, 'code':'01', 'message':'Login Request Rejected. Invalid Signature Hash'}), 403, {'Content-Type':'application/json'}
                exit(0)
            if substrBasicCaption != "Basic":
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
                exit(0)
            if substrBasicToken != "dXNlcnRlc3RhcGlmbGFzazpwYXNzdGVzdGFwaWZsYXNr":
                return json.dumps({'statusCode':401, 'status':False, 'code':'01', 'message':'Authentication token is required and has failed or has not yet been provided'}), 401, {'Content-Type':'application/json', 'WWW-Authenticate':'Bearer realm="Authentication Required"'}
                exit(0)
            if not username or not password:
                return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Username atau Password Kosong'}), 200, {'Content-Type':'application/json'}
                exit(0)
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE BINARY username=%s AND password=%s", (username, password))
            mysql.connection.commit()
            cur.close()
            cek = cur.rowcount
            if cek <= 0:
                return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Username atau Password Salah'}), 200, {'Content-Type':'application/json'}
                exit(0)
            if cek > 0:
                accessTokenTime = int(time.time() + 1800)
                refreshTokenTime = int(time.time() + 604800)
                generateAccessToken = hashLogin(username + password + str(accessTokenTime) + "/wiradwisoke/iniadalahaccesstokennya/9003d081345e9f0451884146e9ea2cff6e4cc4deac9ffd4a9ee98b318a49/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")
                generateRefreshToken = hashLogin(username + password + str(refreshTokenTime) + "/wiradwisoke/iniadalahrefreshtokennya/44962520aa458852bbd40ac5553dd1431f6367ab31f39ee7650b57136d9a/Ku1zKM3PvYAIAAABmeyJvcmlnaW4iOiJ")
                data = [str(generateAccessToken), str(generateRefreshToken), int(accessTokenTime), int(refreshTokenTime), str(username)]
                curnew = mysql.connection.cursor()
                curnew.execute("UPDATE users SET access_token=%s, refresh_token=%s, access_token_timestamp=%s, refresh_token_timestamp=%s WHERE BINARY username=%s", data)
                mysql.connection.commit()
                curnew.close()
                ceknew = curnew.rowcount
                if ceknew <= 0:
                    return json.dumps({'statusCode':200, 'status':False, 'code':'01', 'message':'Gagal Login. Silakan coba lagi'}), 200, {'Content-Type':'application/json'}
                    exit(0)
                if ceknew > 0:
                    return json.dumps({'statusCode':200, 'status':True, 'code':'00', 'message':'Login Sukses', 'access_token':generateAccessToken, 'refresh_token':generateRefreshToken, 'token_type':'Bearer', 'expires_in':1800}), 200, {'Content-Type':'application/json'}
                    exit(0)
        else:
            return json.dumps({'statusCode':405, 'status':False, 'code':'01', 'message':'Method Not Allowed'}), 405, {'Content-Type':'application/json'}

if __name__ == '__main__':
    app.run()