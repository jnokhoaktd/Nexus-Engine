import json, urllib.request

url = "http://127.0.0.1:8000/predict"
payload = {
    "state": "Áo mỏng dính, mặc vào bị ngứa, may ẩu kinh khủng.",
    "questions": {
        "complaint_type": {
            "type": "choice",
            "instructions": "What is the main issue in this product review?",
            "criteria": {
                "sizing_fit": "size, dimensions or fit is wrong",
                "quality": "poor material, defects or broke quickly"
            }
        }
    },
    "language": "vietnam"
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        print("PHẢN HỒI THÔ TỪ NEXUS:")
        print(json.dumps(res, indent=2, ensure_ascii=False))
except Exception as e:
    print("LỖI KẾT NỐI:", e)
