import httplib, urllib, base64
import json

f = open('test.jpg', 'rb')
jpgdata = f.read()
f.close()
 
# Request header
headers = {
# Request headers
'Content-Type': 'application/octet-stream',
'Ocp-Apim-Subscription-Key': 'd3d138ceb1f4470286dcaba79f7d2de9',
}
 
params = urllib.urlencode({
# Request parameters
'returnFaceId': 'true',
'returnFaceLandmarks': 'false',
'returnFaceAttributes': 'age,gender,smile,facialHair,headPose,glasses',
})
 
image_url = 'http://www.uni-regensburg.de/Fakultaeten/phil_Fak_II/Psychologie/Psy_II/beautycheck/english/durchschnittsgesichter/m(01-32)_gr.jpg'
 
body = {
# Request body
#'url': image_url

}
 
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    #conn.request("POST", "/face/v1.0/detect?%s" % params, json.dumps(body), headers)
    conn.request("POST", "/face/v1.0/detect?%s" % params, jpgdata, headers)
    response = conn.getresponse()   
    data = json.loads(response.read())
    print(json.dumps(data, indent=4))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
