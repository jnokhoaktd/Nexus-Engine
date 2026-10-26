import ast
p = r"D:\nghien-cuu-ck\nexus-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()
if "def _nexus_page" in src:
    print("DA CO san, khong lam gi them."); raise SystemExit
target = None
for n in ast.walk(ast.parse(src)):
    if (isinstance(n, ast.Assign) and isinstance(n.value, ast.Call)
        and getattr(n.value.func, "id", None) == "FastAPI"
        and any(isinstance(t, ast.Name) and t.id == "app" for t in n.targets)):
        target = n; break
if not target:
    print("KHONG TIM THAY 'app = FastAPI(...)'. Dung lai, bao Claude."); raise SystemExit
nl = "\r\n" if "\r\n" in src else "\n"
add = [
 '# --- Nexus: trang web 1 cham, cung nguon voi API nen khong can CORS ---',
 '@app.get("/nexus", include_in_schema=False)',
 'def _nexus_page():',
 '    import pathlib',
 '    from fastapi.responses import HTMLResponse',
 '    f = pathlib.Path(__file__).resolve().parents[2] / "Nexus-1-cham.html"',
 '    if not f.exists():',
 '        return HTMLResponse("Khong tim thay file Nexus-1-cham.html", status_code=404)',
 '    return HTMLResponse(f.read_text(encoding="utf-8"))',
]
ind = " " * target.col_offset
lines = src.split(nl)
lines[target.end_lineno:target.end_lineno] = [ind + l for l in add]
open(p, "w", encoding="utf-8", newline="").write(nl.join(lines))
print("OK: da them duong dan /nexus sau dong", target.end_lineno)
