p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()
subs = [
 ('"Unexpected end of JSON; expected a value"', '"JSON kết thúc đột ngột; cần một giá trị"', 1),
 ('"Empty; expected a JSON value"', '"Trống; cần một giá trị JSON"', 1),
 (r'"Tab indents \u00b7 Esc, then Tab to leave"', r'"Tab để thụt lề \u00b7 Esc rồi Tab để thoát"', 1),
 ('"invalid JSON"', '"JSON không hợp lệ"', 2),
 ('"not an object"', '"không phải đối tượng"', 1),
 ('"true / false"', '"đúng / sai"', 1),
 ('"Possible answers"', '"Các đáp án có thể"', 1),
 ('Copy link</button>', 'Sao chép liên kết</button>', 1),
]
for old, new, want in subs:
    n = src.count(old)
    if n == want:
        src = src.replace(old, new)
        print("OK     ", n, "lan:", old)
    else:
        print("BO QUA ", n, "lan (mong doi", str(want) + "):", old)
open(p, "w", encoding="utf-8", newline="").write(src)
