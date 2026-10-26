p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()

cors_import = "from fastapi.middleware.cors import CORSMiddleware\n"
cors_code = '''
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''

if "CORSMiddleware" not in src:
    # Them import va middleware
    src = cors_import + src
    target = 'app = FastAPI('
    if target in src:
        idx = src.find('\n', src.find(target))
        src = src[:idx+1] + cors_code + src[idx+1:]
        open(p, "w", encoding="utf-8", newline="").write(src)
        print("Da bat CORS cho server.py thanh cong!")
    else:
        print("Khong tim thay vi tri app = FastAPI()")
else:
    print("CORS da duoc bat tu truoc")
