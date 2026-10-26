p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()
subs = [
 ('const plural = (n, w) => n + " " + w + (n === 1 ? "" : "s");',
  'const plural = (n, w) => n + " " + ({question: "câu hỏi", option: "lựa chọn", level: "mức", field: "trường"}[w] || w + (n === 1 ? "" : "s"));', 1),
 ('"no options yet"', '"chưa có lựa chọn"', 1),
 ('"no levels yet"', '"chưa có mức"', 1),
 ('" (unknown)"', '" (không rõ)"', 1),
 ('"Run the request to answer "', '"Chạy yêu cầu để trả lời "', 1),
]
for old, new, want in subs:
    n = src.count(old)
    if n == want:
        src = src.replace(old, new)
        print("OK     ", n, "lan:", old[:60])
    else:
        print("BO QUA ", n, "lan (mong doi", str(want) + "):", old[:60])
open(p, "w", encoding="utf-8", newline="").write(src)
