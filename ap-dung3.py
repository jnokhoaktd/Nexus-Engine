p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()
subs = [
 ('("/models", "Models")', '("/models", "Các mô hình")', 1),
 ('("/health", "Health")', '("/health", "Tình trạng")', 1),
 ('("/docs", "API docs")', '("/docs", "Tài liệu API")', 1),
 ('("fields", "fields", "Fields")', '("fields", "fields", "Trường")', 1),
 ('("form", "form", "Form")', '("form", "form", "Biểu mẫu")', 1),
 ('("answers", "Answers")', '("answers", "Câu trả lời")', 1),
 ('("code", "Code")', '("code", "Mã")', 1),
 ('{text: "Key & instructions"}', '{text: "Khóa & hướng dẫn"}', 1),
 ('{text: calibrated.toFixed(4)}), "calibrated")', '{text: calibrated.toFixed(4)}), "đã hiệu chỉnh")', 1),
 ('"Nothing has run yet. Press "', '"Chưa chạy lần nào. Nhấn "', 1),
 ('" to answer these questions about the state."', '" để trả lời các câu hỏi về nội dung."', 1),
 (r'"Waiting for the server\u2026"', r'"Đang chờ máy chủ\u2026"', 1),
 ('"The request changed since this run"', '"Yêu cầu đã thay đổi kể từ lần chạy trước"', 1),
 ('"The run failed: "', '"Chạy thất bại: "', 1),
]
for old, new, want in subs:
    n = src.count(old)
    if n == want:
        src = src.replace(old, new)
        print("OK     ", n, "lan:", old)
    else:
        print("BO QUA ", n, "lan (mong doi", str(want) + "):", old)
open(p, "w", encoding="utf-8", newline="").write(src)
