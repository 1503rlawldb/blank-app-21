# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --------------------------
# 페이지 기본 설정
# --------------------------
st.set_page_config(
    page_title="물러서는 땅, 다가오는 바다",
    page_icon="🌊",
    layout="wide"
)

st.title("📘 물러서는 땅, 다가오는 바다: 해수면 상승 위험 & 대응")

# --------------------------
# 사이드바: 옵션
# --------------------------
st.sidebar.header("보기 옵션")
year = st.sidebar.slider("년도 선택", 1800, 2025, 2024)
region = st.sidebar.selectbox(
    "지역 선택",
    ["전 세계", "대한민국", "투발루", "몰디브", "방글라데시", "네덜란드"]
)

# --------------------------
# 지도용 가상 데이터 생성
# --------------------------
lats = np.linspace(-60, 80, 50)
lons = np.linspace(-180, 180, 100)
lat_grid, lon_grid = np.meshgrid(lats, lons)
lat_flat = lat_grid.flatten()
lon_flat = lon_grid.flatten()

# 기온 이상치 예시: -5~+5°C
np.random.seed(42)
temp_anomaly = np.random.uniform(-5, 5, size=len(lat_flat))

df_map = pd.DataFrame({
    "lat": lat_flat,
    "lon": lon_flat,
    "temp": temp_anomaly
})

# --------------------------
# Plotly 지도 시각화
# --------------------------
fig = px.scatter_mapbox(
    df_map,
    lat="lat",
    lon="lon",
    color="temp",
    color_continuous_scale=["blue","orange","red"],  # 낮은-중간-높은
    range_color=[-5,5],
    size_max=10,
    zoom=1,
    opacity=0.7,
    mapbox_style="carto-positron"  # 대륙 회색
)

st.subheader(f"🌍 기온 변화 지도 ({year}년 기준)")
st.plotly_chart(fig, use_container_width=True)

# --------------------------
# 피해 사례 및 대처 방안
# --------------------------
case_study = {
    "투발루": {
        "피해": "국토의 40% 이상이 침수 위협에 직면, 농경지와 식수원 오염, 환경 난민 발생.",
        "대처": "국제 사회에 기후 난민 보호 요청, 해안 방벽 설치 시도."
    },
    "몰디브": {
        "피해": "리조트와 주거지가 반복적인 홍수 피해.",
        "대처": "인공섬 건설, 해안 방파제 강화."
    },
    "방글라데시": {
        "피해": "델타 지역 농경지와 마을 침수.",
        "대처": "방조제 건설, 홍수 예측 시스템 개발."
    },
    "네덜란드": {
        "피해": "과거 해수면 상승과 폭풍으로 국토 침수 경험.",
        "대처": "세계적 수준의 방조제·수문 관리 시스템 구축."
    },
    "대한민국": {
        "피해": "인천·부산 등 해안 도시 침수 위험 증가.",
        "대처": "연안관리 기본계획 수립, 해안 방벽·배수 시설 확충."
    }
}

if region in case_study:
    st.subheader(f"📍 {region} 피해 사례 & 대처 방안")
    st.write(f"**피해 사례:** {case_study[region]['피해']}")
    st.write(f"**대처 방안:** {case_study[region]['대처']}")

# --------------------------
# 해수면 상승 수치 비교
# --------------------------
st.subheader("📊 해수면 상승 수치 비교")
current_sea_level = 21.0  # cm (예시)
selected_sea_level = round(np.random.uniform(0, current_sea_level), 2)
col1, col2 = st.columns(2)
col1.metric(f"{year}년 해수면 상승(cm)", selected_sea_level)
col2.metric("2025년 해수면 상승(cm)", current_sea_level, delta=f"{current_sea_level-selected_sea_level:.2f} cm")

# --------------------------
# 성찰용 체크박스
# --------------------------
st.subheader("📝 나는 얼마나 알고 있을까?")
st.checkbox("해수면 상승이 내 삶에 영향을 줄 수 있다.")
st.checkbox("국제 사회가 함께 해결해야 한다.")
st.checkbox("개인적으로 기후 행동에 참여할 의향이 있다.")

# --------------------------
# 참고 자료
# --------------------------
st.markdown("---")
st.subheader("📚 참고 자료")
st.markdown("""
- 기상청 기후정보포털: https://www.climate.go.kr  
- NASA Climate Change: https://climate.nasa.gov  
- IPCC Reports: https://www.ipcc.ch  
- NOAA Sea Level Rise: https://coast.noaa.gov/slr  
""")
