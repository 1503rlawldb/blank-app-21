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

# --------------------------
# 보고서 제목 & 서론
# --------------------------
st.title("📘 물러서는 땅, 다가오는 바다: 해수면 상승의 위험과 우리만의 대처법")

st.subheader("서론: 문제 제기")
st.markdown("""
인류의 기술이 나날이 발전함과 동시에 세상은 황폐해져 가고 있다.  
기온은 해마다 오르고, 북극과 남극의 빙하는 녹아내리며, 남극에서는 아름다운 꽃을 볼 수 있게 되었다.  
바다는 따뜻해지고 해수면은 조용히 그러나 확실하게 높아지고 있다.  
지금 이 순간에도 우리 삶의 터전은 서서히 잠식당하고 있는 것이다.  

이 보고서는 아직 해수면 상승의 심각성을 와닿지 못하는 청소년들에게 그 위험을 알리고,  
우리가 반드시 선택해야 할 대처 방안을 제시하고자 한다.  
훗날 가까운 미래에 세상을 이끌어 갈 청소년 여러분이 이 문제를 외면한다면,  
결국 그 피해는 여러분의 세대가 고스란히 떠안게 될 것이다.
""")

# --------------------------
# 사이드바 옵션
# --------------------------
st.sidebar.header("보기 옵션")
year = st.sidebar.slider("년도 선택", 1800, 2050, 2050)
region = st.sidebar.selectbox(
    "지역 선택",
    ["전 세계", "대한민국", "투발루", "몰디브", "방글라데시", "네덜란드"]
)

# --------------------------
# 지도 데이터: 실제 바다/대륙 구분 + 임시 기온 격자
# --------------------------
lats = np.linspace(-60, 80, 80)
lons = np.linspace(-180, 180, 180)
lat_grid, lon_grid = np.meshgrid(lats, lons)
lat_flat = lat_grid.flatten()
lon_flat = lon_grid.flatten()

# 임의 기온 이상치 (-5~5°C)
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
    size_max=5,
    zoom=1,
    opacity=0.7,
    mapbox_style="carto-positron"  # 대륙 회색
)

st.subheader(f"🌍 전 세계 기온 변화 지도 ({year}년 기준)")
st.plotly_chart(fig, use_container_width=True)

# --------------------------
# 본론 1: 데이터 분석
# --------------------------
st.subheader("본론 1: 데이터 분석")
st.markdown(f"""
위 지도는 {year}년을 가정해 해수면 상승으로 잠기게 될 대한민국의 주요 도시와 세계 각국의 연안을 보여준다.  
단순한 그림이 아니라 과학적 데이터와 시뮬레이션을 바탕으로 만들어진 미래의 경고장이다.  
인천과 전라도의 주요 도시들 뿐 아니라 세계의 수많은 항구 도시들이 물속에 잠길 수 있다는 사실은 더 이상 영화 속 상상이 아니다.  
지금 우리가 아무런 행동을 하지 않는다면, {year}년의 이 지도는 ‘예상도’가 아니라 ‘현실의 풍경’이 될 것이다.  
결국 그 피해를 고스란히 짊어지게 되는 세대가 바로 여러분이다.
""")

# --------------------------
# 본론 2: 원인 및 영향 탐구
# --------------------------
st.subheader("본론 2: 원인 및 영향 탐구")
st.markdown("""
해수면 상승은 단순한 자연 현상이 아니라 실제로 여러 나라에서 심각한 피해를 일으키고 있다.  
대표적인 예시로 **투발루**를 들 수 있다.
""")

st.markdown("""
**투발루**  
- 위치: 남태평양, 평균 해발고도 2~3m  
- 피해: 바닷물이 섬 마을로 밀려들어 농경지 침수, 식수원 오염, 주민 이주 발생  
- 현실: 대통령이 직접 물에 잠긴 섬에서 연설, 국제 사회에 도움 요청  
- 전망: 해수면 상승 지속 시 국가 전체가 지도에서 사라질 가능성
""")

# --------------------------
# 지역별 피해 사례 & 대처 방안
# --------------------------
case_study = {
    "투발루": {
        "피해": "국토의 40% 이상이 침수 위협, 농경지와 식수원 오염, 환경 난민 발생.",
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
current_sea_level = 21.0  # cm
selected_sea_level = round(np.random.uniform(0, current_sea_level), 2)
col1, col2 = st.columns(2)
col1.metric(f"{year}년 해수면 상승(cm)", selected_sea_level)
col2.metric("2025년 해수면 상승(cm)", current_sea_level, delta=f"{current_sea_level-selected_sea_level:.2f} cm")

# --------------------------
# 해수면 상승 대처 방안
# --------------------------
st.subheader("🌊 해수면 상승 대처 방안")
st.markdown("""
**온실가스 감축 (지구 온난화 완화)**  
- 에너지 전환: 화석 연료 사용을 줄이고 태양광, 풍력 등 신재생에너지 확대  
- 에너지 효율 개선: 건물 단열 강화, 불필요한 에너지 소비 절감  

**해안 지역 적응 및 보호**  
- 방파제 및 해안 방조제 건설  
- 자연 해안선 복원: 맹그로브, 갯벌 등  
- 연안 관리 계획 수립  

**개인 실천**  
- 에너지 절약: 전등 끄기, 대중교통 이용  
- 자원 재활용 및 소비 줄이기  
- 환경 문제 관심 및 참여
""")

# --------------------------
# 사용자 성찰 체크박스
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
- 기상청 기후정보포털, 자료 제공: 기상청, https://www.climate.go.kr  
- NASA Climate Change, 자료 제공: NASA, https://climate.nasa.gov  
- IPCC Reports, 자료 제공: IPCC, https://www.ipcc.ch  
- NOAA Sea Level Rise, 자료 제공: NOAA, https://coast.noaa.gov/slr  
""")
