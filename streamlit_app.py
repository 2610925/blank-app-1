import streamlit as st

# 리스트 준비
fields = ["인공지능 개발", "로봇", "AI 서비스"]

jobs = [
    ["인공지능 개발자", "머신러닝 엔지니어", "데이터 과학자"],
    ["로봇 개발자", "자율주행 엔지니어", "로봇 연구원"],
    ["AI 서비스 기획자", "챗봇 개발자", "AI 컨설턴트"]
]

# 제목 출력
st.title("인공지능 진로 추천 프로그램")

# 관심 분야 선택
choice = st.selectbox(
    "관심 분야를 선택하세요",
    fields
)

# 조건문 활용
if choice == "인공지능 개발":
    recommend_list = jobs[0]

elif choice == "로봇":
    recommend_list = jobs[1]

else:
    recommend_list = jobs[2]

# 결과 출력
st.subheader("추천 직업")

# 반복문 활용
for job in recommend_list:
    st.write("- " + job)