import re
p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()

# Thay nội dung hàm get_gui
pattern = r'@app\.get\("/gui".*?\n\s*def get_gui.*?:.*?\n(\s+return .*?\n)'
gui_code = '''@app.get("/gui", response_class=HTMLResponse)
async def get_gui():
    gui_path = os.path.join(os.path.dirname(__file__), "gui.html")
    if os.path.exists(gui_path):
        with open(gui_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Chua tim thay gui.html</h3>"
'''

# Thay thế đơn giản dựa trên route /gui sẵn có
if '@app.get("/gui"' in src:
    lines = src.split('\n')
    new_lines = []
    skip = False
    for line in lines:
        if '@app.get("/gui"' in line:
            new_lines.append(gui_code)
            skip = True
        elif skip and line.startswith('    @app.get('):
            skip = False
            new_lines.append(line)
        elif not skip:
            new_lines.append(line)
    src = '\n'.join(new_lines)
    open(p, "w", encoding="utf-8", newline="").write(src)
    print("Cap nhat route /gui thanh cong!")
else:
    print("Khong tim thay /gui")
