import os

p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()

test_route = '''
@app.get("/test", response_class=HTMLResponse)
async def get_test_page():
    test_path = os.path.join(os.path.dirname(__file__), "test_web.html")
    if os.path.exists(test_path):
        with open(test_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Chua tim thay test_web.html</h3>"
'''

if "/test" not in src:
    # Chen ngay truoc route root "/"
    target = '@app.get("/", response_class=HTMLResponse)'
    if target in src:
        src = src.replace(target, test_route + "\n" + target)
        open(p, "w", encoding="utf-8", newline="").write(src)
        print("Da them route /test thanh cong!")
    else:
        print("Khong tim thay vi tri chen trong server.py")
else:
    print("Route /test da co san")
