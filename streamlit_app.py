import streamlit as st

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="AI 진로 추천 프로그램", page_icon="🤖", layout="centered")
st.title("🤖 인공지능 진로 추천 프로그램")
st.write("관심 있는 인공지능 분야를 선택하시면 관련 직업을 추천해 드립니다.")
st.markdown("---")

# 2. 데이터 준비
fields = ["선택하세요", "인공지능 개발", "로봇", "AI 서비스"]

jobs = {
    "인공지능 개발": ["인공지능 개발자", "머신러닝 엔지니어", "데이터 과학자"],
    "로봇": ["로봇 개발자", "자율주행 엔지니어", "로봇 연구원"],
    "AI 서비스": ["AI 서비스 기획자", "챗봇 개발자", "AI 컨설턴트"]
}

# 3. 사용자 인터페이스 (UI) 구성
# 대화형 셀렉트박스를 통해 분야 선택 (기존의 번호 입력 대체)
selected_field = st.selectbox(
    "💡 관심 있는 분야를 선택하세요:",
    options=fields,
    index=0
)

# 4. 조건문 및 결과 출력
if selected_field != "선택하세요":
    st.success(f"### 🎯 [{selected_field}] 분야 추천 직업")
    
    # 추천 직업 리스트를 깔끔한 카드나 리스트 형태로 출력
    recommend_list = jobs[selected_field]
    
    for job in recommend_list:
        st.markdown(f"📌 **{job}**")
        
    # 세션 상태(Session State)를 활용해 '마지막 추천 결과' 저장 (선택 사항)
    st.session_state['last_recommend'] = (selected_field, recommend_list)

else:
    st.info("분야를 선택하시면 추천 결과가 아래에 표시됩니다.")

# 5. 마지막 추천 결과 보여주기 (옵션)
if 'last_recommend' in st.session_state:
    st.markdown("---")
    with st.expander("🔍 최근 확인한 추천 결과 보기"):
        last_field, last_jobs = st.session_state['last_recommend']
        st.write(f"**최근 본 분야:** {last_field}")
        for job in last_jobs:
            st.write(f"- {job}")