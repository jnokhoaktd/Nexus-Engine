import re

p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()

# Route cho Trang 1 (No-Code cho Chủ shop)
app_route = '''
    @app.get("/app", response_class=HTMLResponse)
    async def get_app_page():
        app_path = os.path.join(os.path.dirname(__file__), "app.html")
        if os.path.exists(app_path):
            with open(app_path, "r", encoding="utf-8") as f:
                return f.read()
        return "<h3>Chua tim thay tep app.html</h3>"
'''

if "/app" not in src:
    # Chen ngay truoc route root "/"
    target = '    @app.get("/", response_class=HTMLResponse)'
    if target in src:
        src = src.replace(target, app_route + "\n" + target)
        open(p, "w", encoding="utf-8", newline="").write(src)
        print("Da them route /app thanh cong!")
    else:
        print("Khong tim thay vi tri chen trong server.py")
else:
    print("Route /app da co san trong server.py")
