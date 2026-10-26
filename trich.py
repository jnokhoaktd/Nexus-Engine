import re
p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8").read()
found = {}
def add(s, kind, pos):
    s = s.strip()
    if len(s) < 2 or not re.search(r"[A-Za-z]{2,}", s) or s in found:
        return
    found[s] = (kind, src.count("\n", 0, pos) + 1)
for m in re.finditer(r">([^<>{}\n]{2,}?)<", src):
    add(m.group(1), "chu trong the", m.start(1))
for m in re.finditer(r'(?:placeholder|title|aria-label|alt)="([^"]+)"', src):
    add(m.group(1), "thuoc tinh", m.start(1))
for m in re.finditer(r"""(["'`])([^"'`\n]{3,80})\1""", src):
    s = m.group(2)
    if " " in s.strip() and not re.search(r"[{}()=/\\<>_]", s):
        add(s, "chuoi trong ma", m.start(2))
with open(r"D:\nghien-cuu-ck\chuoi.txt", "w", encoding="utf-8") as f:
    for i, (s, (k, ln)) in enumerate(found.items(), 1):
        f.write(f"{i} | dong {ln} | {k} | {s}\n")
print(len(found), "chuoi, da ghi vao D:\\nghien-cuu-ck\\chuoi.txt")
