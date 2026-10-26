import json
import urllib.request
import time

dataset = [
    {"text": "Áo mỏng dính, mặc vào bị ngứa, may ẩu kinh khủng.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Giao hàng lâu khủng khiếp, tận 7 ngày mới nhận được hàng.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Đặt size L mà giao size S sao mặc vừa hả shop?", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Giá quá đắt so với chất lượng, quần mỏng như tờ giấy.", "true_type": "price_value", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Không biết cách lắp ráp kệ, shop không đưa sách hướng dẫn.", "true_type": "instructions", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Đóng gói cẩn thận, giao hàng nhanh, sản phẩm đẹp xuất sắc!", "true_type": "no_issue", "true_sent": "dont care", "true_ret": False},
    {"text": "Giày đi vừa vặn, đế êm, mang rất thích.", "true_type": "no_issue", "true_sent": "dont care", "true_ret": False},
    {"text": "Sản phẩm bị vỡ rách bao bì khi nhận, đền tiền lại cho tôi.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Vải bị xù lông sau 1 lần giặt, muốn trả lại hàng lập tức.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Áo chật nách, dài tay quá, không chuẩn form như ảnh.", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Thức ăn nguội ngắt, giao muộn 40 phút so với hẹn.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Mặt hàng này đáng đồng tiền bát gạo, sẽ ủng hộ tiếp.", "true_type": "no_issue", "true_sent": "dont care", "true_ret": False},
    {"text": "Hộp bị móp xốp bung bét, ảnh hưởng chất lượng bên trong.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Shop gửi thiếu 1 món trong đơn, yêu cầu hoàn tiền món đó.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Bảng quy đổi kích cỡ bị sai hoàn toàn, rộng thùng thình.", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Đèn xài được 5 phút thì chập điện khét lẹt, quá nguy hiểm.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Quá đắt, chất lượng chỉ bằng hàng chợ vài chục nghìn.", "true_type": "price_value", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Hướng dẫn sử dụng toàn tiếng Trung không đọc được gì cả.", "true_type": "instructions", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Nhân viên giao hàng thái độ cộc lốc, vô lễ với khách.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Hàng giống hình, giao nhanh, nhân viên thân thiện 5 sao.", "true_type": "no_issue", "true_sent": "dont care", "true_ret": False},
    {"text": "Quần ngắn hơn mô tả 5cm, mặc như quần đùi.", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Áo phai màu lem hết ra các đồ giặt chung khác.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Mua đợt sale mà giá còn cao hơn ngày thường, treo đầu dê bán thịt chó.", "true_type": "price_value", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Màn hình bị sọc ngang ngay khi mở nguồn, đổi cái mới cho tôi.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Nút bấm bị kẹt không nhấn được, đồ thanh lý hay sao vậy?", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Đã nhận đủ hàng, chất lượng bình thường tạm chấp nhận được.", "true_type": "no_issue", "true_sent": "neutral", "true_ret": False},
    {"text": "Không có sơ đồ lắp ghép nên xoay xở cả buổi chiều không xong.", "true_type": "instructions", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Shipper quăng hàng qua cổng làm vỡ đồ bên trong.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Màu sắc bên ngoài tối hơn trên ảnh chụp rất nhiều.", "true_type": "quality", "true_sent": "neutral", "true_ret": False},
    {"text": "So với mức giá này thì vải hơi mỏng, không đáng tiền lắm.", "true_type": "price_value", "true_sent": "neutral", "true_ret": False},
    {"text": "Cài đặt ứng dụng kèm theo toàn bị lỗi kết nối.", "true_type": "instructions", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Kích thước quá to so với bàn làm việc tiêu chuẩn.", "true_type": "sizing_fit", "true_sent": "neutral", "true_ret": True},
    {"text": "Táo bị dập nát phân nửa, đề nghị hoàn tiền lại.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Hàng đi từ nước ngoài về hơi lâu nhưng thông cảm được.", "true_type": "no_issue", "true_sent": "neutral", "true_ret": False},
    {"text": "Chỉ may bị bung rách một đường dài ở sườn áo.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Shop tư vấn size sai bét, bảo 60kg mặc vừa mà giờ nín thở không kéo được khóa.", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Phí ship đắt gấp đôi giá trị sản phẩm, quá bất hợp lý.", "true_type": "price_value", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Bị thiếu mất bộ ốc vít kèm theo nên không lắp được.", "true_type": "instructions", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Son thỏi bị gãy làm đôi khi mở nắp, đóng gói quá kém.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Dùng được 2 ngày thì ngưng hoạt động hẳn.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Giày đi bị đau gót và kích ngón chân.", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Mùi thơm dịu, giao hàng siêu nhanh, đốm may chắc chắn.", "true_type": "no_issue", "true_sent": "dont care", "true_ret": False},
    {"text": "Chất liệu nhựa rẻ tiền, giòn dễ gãy.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Thất vọng vì chờ nửa tháng mới nhận được đồ.", "true_type": "shipping", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Scan mã QR không ra link hướng dẫn sử dụng.", "true_type": "instructions", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Sản phẩm bị dính bẩn nhiều chỗ không giặt ra được.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Mua đắt hơn shop khác 100k mà chất lượng y hệt.", "true_type": "price_value", "true_sent": "very unhappy", "true_ret": False},
    {"text": "Mũ bảo hiểm quá chật chèn ép hai bên tai.", "true_type": "sizing_fit", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Bình nước bị rò rỉ chảy nước ra ngoài.", "true_type": "quality", "true_sent": "very unhappy", "true_ret": True},
    {"text": "Cực kỳ hài lòng, lần sau sẽ mua tiếp!", "true_type": "no_issue", "true_sent": "dont care", "true_ret": False}
]

questions = {
    "complaint_type": {
        "type": "choice",
        "instructions": "What is the main issue in this product review?",
        "criteria": {
            "sizing_fit": "size, dimensions or fit is wrong",
            "quality": "poor material, defects or broke quickly",
            "shipping": "late, damaged in transit or missing items",
            "instructions": "hard to assemble or unclear instructions",
            "price_value": "not worth the price",
            "no_issue": "no complaint"
        }
    },
    "sentiment": {
        "type": "score",
        "instructions": "How satisfied is the customer?",
        "criteria": ["very unhappy", "neutral", "dont care"]
    },
    "wants_return": {
        "type": "noul",
        "instructions": "Does the customer say they returned or want to return the product?"
    }
}

print(f"--- BẮT ĐẦU BACKTEST NEXUS TRÊN {len(dataset)} MẪU PHẢN HỒI TIẾNG VIỆT ---")

correct_type = 0
correct_sent = 0
correct_ret = 0
total = len(dataset)

url = "http://127.0.0.1:8000/predict"

def extract_answer(obj):
    if isinstance(obj, dict):
        if "answer" in obj:
            return obj["answer"]
        if "choice" in obj:
            return obj["choice"]
        if "value" in obj:
            return obj["value"]
    return obj

for i, item in enumerate(dataset, 1):
    payload = {
        "state": item["text"],
        "questions": questions,
        "language": "vietnam"
    }
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            
            ans = res.get("answers", res)
            
            pred_type = extract_answer(ans.get("complaint_type", {}))
            pred_sent = extract_answer(ans.get("sentiment", {}))
            pred_ret = extract_answer(ans.get("wants_return", {}))
            
            is_type_ok = (pred_type == item["true_type"])
            is_sent_ok = (pred_sent == item["true_sent"])
            is_ret_ok = (pred_ret == item["true_ret"])
            
            if is_type_ok: correct_type += 1
            if is_sent_ok: correct_sent += 1
            if is_ret_ok: correct_ret += 1
            
            print(f"Mẫu {i:02d}/{total}: '{item['text'][:28]}...' -> Lỗi: {pred_type} ({'ĐÚNG' if is_type_ok else 'SAI'})")
            
    except Exception as e:
        print(f"Mẫu {i:02d} LỖI: {e}")

print("\n================ BÁO CÁO KẾT QUẢ BACKTEST ================")
print(f"1. Độ chính xác Phân loại lỗi (complaint_type): {correct_type}/{total} ({correct_type/total*100:.1f}%)")
print(f"2. Độ chính xác Thái độ khách (sentiment)     : {correct_sent}/{total} ({correct_sent/total*100:.1f}%)")
print(f"3. Độ chính xác Ý định trả hàng (wants_return) : {correct_ret}/{total} ({correct_ret/total*100:.1f}%)")
print("==========================================================")
