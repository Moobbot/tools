from bs4 import BeautifulSoup
import pandas as pd

# Bước 1: Đọc nội dung file HTML
with open("ds_loaikhamxetnghiem.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Bước 2: Dùng BeautifulSoup để phân tích cú pháp HTML
soup = BeautifulSoup(content, "html.parser")
rows = soup.find_all("tr")

# Bước 3: Trích xuất dữ liệu từ các dòng <tr>
data = []
for row in rows[1:]:  # Bỏ qua dòng tiêu đề đầu tiên
    cols = row.find_all("td")
    data.append([col.get_text(strip=True) for col in cols])

# Bước 4: Tạo DataFrame và đặt tên cột
columns = ["Id loại khám", "Tên xét nghiệm", "Tên xét nghiệm con", "Số thứ tự", "Giá thuê ngoài"]
df = pd.DataFrame(data, columns=columns)

# Bước 5: Ghi ra file CSV
df.to_csv("loai_kham_xet_nghiem.csv", index=False, encoding="utf-8-sig")
