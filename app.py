
import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="🏦",
    layout="centered"
)

# Tiêu đề
st.title("🏦 CÔNG CỤ TÍNH LÃI GỬI TIẾT KIỆM_NGỌC BÍCH")
st.write("Tính toán tiền lãi dự kiến dựa trên số tiền gửi, kỳ hạn và lãi suất.")

st.divider()

# Hàm định dạng tiền Việt Nam
def format_vnd(amount):
    return f"{amount:,.0f} VNĐ".replace(",", ".")

# Nhập thông tin
st.subheader("📋 Thông tin tiền gửi")

col1, col2 = st.columns(2)

with col1:
    so_tien = st.number_input(
        "Số tiền gửi (VNĐ)",
        min_value=0,
        value=10000000,
        step=1000000,
        format="%d"
    )

with col2:
    ky_han = st.number_input(
        "Kỳ hạn (tháng)",
        min_value=1,
        max_value=120,
        value=12,
        step=1
    )

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# Tính toán khi nhấn nút
if st.button("🧮 TÍNH TIỀN LÃI", type="primary", use_container_width=True):

    if so_tien <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")
    else:
        # Tính lãi đơn theo lãi suất năm
        lai_mot_thang = so_tien * (lai_suat / 100) / 12

        tong_lai = lai_mot_thang * ky_han
        tong_tien = so_tien + tong_lai

        # Xác định tiền lãi định kỳ
        if hinh_thuc == "Cuối kỳ":
            lai_dinh_ky = tong_lai
            chu_ky = "Cuối kỳ"
            so_lan_nhan = 1
        elif hinh_thuc == "Hàng tháng":
            lai_dinh_ky = lai_mot_thang
            chu_ky = "Mỗi tháng"
            so_lan_nhan = ky_han
        else:
            lai_dinh_ky = lai_mot_thang * 3
            chu_ky = "Mỗi quý"
            so_lan_nhan = ky_han // 3

        # Hiển thị kết quả
        st.subheader("📊 Kết quả tính toán")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="💰 Tiền lãi định kỳ",
                value=format_vnd(lai_dinh_ky)
            )

        with col2:
            st.metric(
                label="📈 Tổng tiền lãi",
                value=format_vnd(tong_lai)
            )

        st.metric(
            label="🏦 Tổng tiền gốc và lãi",
            value=format_vnd(tong_tien)
        )

        st.divider()

        # Chi tiết kết quả
        st.subheader("📝 Chi tiết khoản tiết kiệm")

        st.write(f"**Số tiền gửi:** {format_vnd(so_tien)}")
        st.write(f"**Kỳ hạn:** {ky_han} tháng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
        st.write(f"**Số lần nhận lãi:** {so_lan_nhan}")
        st.write(f"**Tiền lãi định kỳ:** {format_vnd(lai_dinh_ky)}")
        st.write(f"**Tổng tiền lãi:** {format_vnd(tong_lai)}")
        st.write(f"**Tổng tiền khi đáo hạn:** {format_vnd(tong_tien)}")

        st.info(
            "Lưu ý: Kết quả được tính theo phương pháp lãi đơn, "
            "chưa tính thuế, phí hoặc các điều kiện riêng của ngân hàng. "
            "Với kỳ hạn không chia hết cho 3 tháng, hình thức nhận lãi "
            "hàng quý được tính theo số tháng trọn quý."
        )
