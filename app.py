import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘 먹을 점심 메뉴를 랜덤으로 골라드립니다!")

# 점심 메뉴 리스트
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "햄버거",
    "파스타",
    "쌀국수",
    "비빔밥",
    "순대국밥",
    "칼국수",
    "마라탕",
    "샌드위치",
]

# 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
    selected_menu = random.choice(lunch_menus)
    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
