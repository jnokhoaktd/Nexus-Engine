import re
p = r"D:\nghien-cuu-ck\laya-main\examples\server.py"
src = open(p, encoding="utf-8", newline="").read()
tr = {
 "Laya": "Nexus",
 "raw answer": "câu trả lời thô",
 "uncertain": "chưa chắc chắn",
 "calibrated": "đã hiệu chỉnh",
 "Format": "Định dạng",
 "Billing email (example)": "Email thanh toán (ví dụ)",
 "edited": "đã chỉnh sửa",
 "Auto-route by language": "Tự chọn mô hình theo ngôn ngữ",
 "Revert": "Hoàn tác",
 "Run request": "Chạy yêu cầu",
 "Response": "Kết quả",
 "Preview": "Xem trước",
 "JavaScript is off, so this is the plain form: edit the JSON and the server renders the answers.": "JavaScript đang tắt nên đây là biểu mẫu đơn giản: hãy sửa JSON và máy chủ sẽ hiển thị các câu trả lời.",
 "State": "Nội dung",
 "Questions": "Câu hỏi",
 "Model": "Mô hình",
 "Language hint": "Gợi ý ngôn ngữ",
 "default": "mặc định",
 "Picked when": "Được chọn khi",
 "Open in playground": "Mở trong Playground",
 "Copy curl": "Sao chép curl",
 "Models": "Các mô hình",
 "Open the playground": "Mở Playground",
 "API docs": "Tài liệu API",
 "Health": "Tình trạng",
 "Router state and the settings this process was started with.": "Trạng thái bộ định tuyến và các thiết lập khi tiến trình này được khởi động.",
 "Configuration": "Cấu hình",
 "Endpoints": "Các điểm truy cập",
 "and": "và",
 "Refresh": "Làm mới",
 "Error": "Lỗi",
 "Answers": "Câu trả lời",
 "Collapse all": "Thu gọn tất cả",
 "Edit in playground": "Sửa trong Playground",
 "Key &amp; instructions": "Khóa &amp; hướng dẫn",
 "Answer &amp; calibrated confidence": "Câu trả lời &amp; độ tin cậy đã hiệu chỉnh",
}
for en, vi in tr.items():
    pat = re.compile(r"(>\s*)" + re.escape(en) + r"(\s*<)")
    src, n = pat.subn(lambda m: m.group(1) + vi + m.group(2), src)
    print(str(n).rjust(3), "lan:", en, "->", vi)
old = 'title="Laya Routing API"'
print(src.count(old), "lan: tieu de API")
src = src.replace(old, 'title="Nexus - API định tuyến"')
open(p, "w", encoding="utf-8", newline="").write(src)
print("Xong.")
