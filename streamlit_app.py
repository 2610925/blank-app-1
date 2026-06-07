import streamlit as st

st.title("인공지능 진로 추천 프로그램")

choice = st.selectbox(
    "관심 분야를 선택하세요",
    ["인공지능 개발", "로봇", "AI 서비스"]
)

if choice == "인공지능 개발":
    jobs = ["인공지능 개발자", "머신러닝 엔지니어", "데이터 과학자"]

elif choice == "로봇":
    jobs = ["로봇 개발자", "자율주행 엔지니어", "로봇 연구원"]

else:
    jobs = ["AI 서비스 기획자", "챗봇 개발자", "AI 컨설턴트"]

st.write("추천 직업")
for job in jobs:
    st.write("-", job)