# 🛵 Phân Tích Dữ Liệu Đặt Xe Công Nghệ Tại Việt Nam

> **Đề tài Cuối Kỳ – Môn Khoa Học Dữ Liệu**  
> Phân tích hành vi đặt xe công nghệ (Grab, Be, Gojek) tại TP. Hồ Chí Minh năm 2024  
> Link yuotube:https://youtu.be/KWfLhR64Ri8?si=4ZMVRUzRTWz2jxxr

---

## 📋 Thông Tin Sinh Viên

| Thông tin   | Chi tiết            |
|-------------|---------------------|
| **Sinh viên** | Đặng Đình Đạt     |
| **MSSV**    | K225480106003       |
| **Dataset** | Dữ liệu đặt xe công nghệ (TP.HCM, Tháng 1–6/2024) |
| **Tổng số bản ghi** | 20,000 chuyến đi |

---

## 📖 Giới Thiệu Đề Tài

Đề tài thực hiện phân tích toàn diện bộ dữ liệu chuyến xe công nghệ được mô phỏng thực tế tại **Thành phố Hồ Chí Minh** trong giai đoạn **tháng 1 đến tháng 6 năm 2024**. Dữ liệu bao gồm các chuyến đi từ các ứng dụng phổ biến như **Grab**, **Be**, và **Gojek** tại 5 quận trọng điểm: Quận 1, Quận 2, Quận 3, Quận 7 và Tân Bình.

Mục tiêu chính của đề tài là khám phá và trả lời **7 câu hỏi phân tích dữ liệu** quan trọng, từ thống kê mô tả, trực quan hóa dữ liệu đến áp dụng các mô hình học máy.

---

## 🗂️ Cấu Trúc Dự Án

```
cuoiKy_KHDL/
│
├── 📓 PhanTich_GoiXeVN.ipynb        # Notebook phân tích chính
├── 🐍 generate_data_vn.py           # Script tạo bộ dữ liệu mẫu
├── 📁 data/
│   └── doxe_vn_data.csv             # Bộ dữ liệu (20,000 bản ghi)
├── 📄 Bao_Cao_Nghien_Cuu_KHDL_Hoan_Thien.pdf   # Báo cáo nghiên cứu
├── 📊 Slide_Bao_Cao_Cuoi_Ky_HOAN_CHINH.pptx    # Slide báo cáo
└── 📝 README.md
```

---

## 📊 Mô Tả Dữ Liệu

Bộ dữ liệu **`data/doxe_vn_data.csv`** gồm **20,000 chuyến đi** với các trường hoàn toàn bằng tiếng Việt:

| Tên cột          | Mô tả                                     | Ví dụ                    |
|------------------|-------------------------------------------|--------------------------|
| `Thoi_gian`      | Thời gian đặt xe (timestamp)              | `2024-01-15 08:30:00`    |
| `Vi_do`          | Vĩ độ điểm đón tại TP.HCM               | `10.7755`                |
| `Kinh_do`        | Kinh độ điểm đón tại TP.HCM             | `106.6983`               |
| `Dich_vu`        | Loại dịch vụ đặt xe                      | `GrabBike`, `BeCar`, ... |
| `Quan_Huyen`     | Quận/Huyện tại TP.HCM                   | `Quận 1`, `Tân Bình`, ...|
| `Quang_duong_km` | Quãng đường chuyến đi (km)              | `5.32`                   |
| `Thoi_gian_phut` | Thời gian dự kiến của chuyến đi (phút) | `18.5`                   |

### Phân bố dịch vụ:
| Dịch vụ   | Tỷ lệ |
|-----------|--------|
| GrabBike  | 45%    |
| GrabCar   | 25%    |
| BeBike    | 15%    |
| BeCar     | 10%    |
| Gojek     | 5%     |

### Phạm vi địa lý:
| Quận/Huyện | Tỷ lệ |
|------------|--------|
| Quận 1     | 40%    |
| Quận 3     | 20%    |
| Tân Bình   | 15%    |
| Quận 2     | 15%    |
| Quận 7     | 10%    |

---

## 🔍 Câu Hỏi Phân Tích

Notebook thực hiện phân tích 7 câu hỏi nghiên cứu:

| # | Câu hỏi phân tích | Phương pháp |
|---|-------------------|-------------|
| 1 | Khung giờ nào có nhiều chuyến đi nhất? | Thống kê, Biểu đồ cột, Đường xu hướng |
| 2 | Ngày nào trong tuần đông khách nhất? | Thống kê, Biểu đồ tròn |
| 3 | Khu vực nào tại TP.HCM có nhu cầu cao nhất? | Thống kê, Bản đồ tọa độ |
| 4 | Quãng đường trung bình (km) mỗi chuyến? | Histogram, Boxplot |
| 5 | Mối quan hệ giữa thời gian và số chuyến? | Time Series, Heatmap |
| 6 | Dự đoán số chuyến giờ tiếp theo? | **Random Forest, Gradient Boosting** |
| 7 | Phân cụm khu vực có nhu cầu tương đồng? | **K-Means Clustering** |

---

## 🛠️ Công Nghệ Sử Dụng

### Ngôn ngữ & Môi trường
- **Python 3.x**
- **Jupyter Notebook**
- **Anaconda** (môi trường `my_ml_dev_env`)

### Thư viện chính

| Thư viện       | Phiên bản | Mục đích                              |
|----------------|-----------|---------------------------------------|
| `pandas`       | 2.3.3     | Xử lý và thao tác dữ liệu            |
| `numpy`        | 2.3.5     | Tính toán số học                      |
| `matplotlib`   | 3.10.7    | Trực quan hóa dữ liệu cơ bản         |
| `seaborn`      | 0.13.2    | Trực quan hóa dữ liệu nâng cao       |
| `scikit-learn` | 1.7.1     | Mô hình học máy (Random Forest, K-Means) |

---

## 🚀 Hướng Dẫn Chạy

### 1. Clone repository
```bash
git clone <repository-url>
cd cuoiKy_KHDL
```

### 2. Cài đặt thư viện
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. (Tuỳ chọn) Tạo lại bộ dữ liệu
```bash
python generate_data_vn.py
```
> Script sẽ tạo file `data/doxe_vn_data.csv` với 20,000 bản ghi mô phỏng.

### 4. Mở và chạy Notebook
```bash
jupyter notebook PhanTich_GoiXeVN.ipynb
```
> Chạy tuần tự từng cell từ đầu đến cuối để xem kết quả phân tích.

---

## 📈 Kết Quả Nổi Bật

- 🕐 **Giờ cao điểm**: Xác định được các khung giờ có lưu lượng đặt xe cao nhất trong ngày
- 📅 **Ngày bận rộn**: Phân tích xu hướng theo ngày trong tuần để tối ưu hóa nguồn lực tài xế
- 🗺️ **Điểm nóng**: Bản đồ tọa độ trực quan hóa các khu vực có nhu cầu cao tại TP.HCM
- 🤖 **Dự đoán ML**: Mô hình Random Forest & Gradient Boosting dự đoán lượng chuyến xe theo giờ
- 🔵 **Phân cụm K-Means**: Nhóm các khu vực theo đặc điểm nhu cầu tương đồng

---

## 📁 Tài Liệu Kèm Theo

| Tài liệu | Mô tả |
|----------|-------|
| `Bao_Cao_Nghien_Cuu_KHDL_Hoan_Thien.pdf` | Báo cáo nghiên cứu chi tiết, phân tích đầy đủ |
| `Slide_Bao_Cao_Cuoi_Ky_HOAN_CHINH.pptx`  | Slide trình bày báo cáo cuối kỳ |

---

## 📝 Ghi Chú

> **Về bộ dữ liệu**: Dữ liệu trong project này là **dữ liệu mô phỏng** (synthetic data) được tạo bằng script `generate_data_vn.py`, nhằm phản ánh thực tế hoạt động đặt xe công nghệ tại TP.HCM với phân phối xác suất dựa trên đặc điểm thực tế của từng quận và loại dịch vụ. Dữ liệu **không chứa thông tin cá nhân** của bất kỳ người dùng nào.

---

<div align="center">

**Đặng Đình Đạt** · MSSV: K225480106003  
*Đề tài Cuối Kỳ – Khoa Học Dữ Liệu · 2024*

</div>
