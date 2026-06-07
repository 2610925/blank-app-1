import streamlit as st

st.title("햄버거 키오스크")

# 리스트
menu_list = ["불고기버거", "치즈버거", "새우버거", "치킨버거"]
price_list = [4500, 5000, 5500, 6000]

# 장바구니 초기화
if "cart" not in st.session_state:
    st.session_state.cart = []

# 메뉴 출력 (반복문 사용)
st.subheader("메뉴")
for i in range(len(menu_list)):
    st.write(f"{i+1}. {menu_list[i]} - {price_list[i]}원")

# 메뉴 선택
menu = st.selectbox("주문할 메뉴를 선택하세요", menu_list)

# 장바구니 담기
if st.button("장바구니 담기"):
    st.session_state.cart.append(menu)
    st.success(f"{menu}가 장바구니에 추가되었습니다.")

# 장바구니 출력
st.subheader("장바구니")

total = 0

# 반복문 사용
for item in st.session_state.cart:
    index = menu_list.index(item)
    st.write(f"- {item} ({price_list[index]}원)")
    total += price_list[index]

st.write(f"총 금액: {total}원")

# 결제
money = st.number_input("지불할 금액을 입력하세요", min_value=0, step=100)

if st.button("결제하기"):

    # 조건문 사용
    if money >= total:
        st.success("결제가 완료되었습니다!")
        st.write(f"거스름돈: {money - total}원")
    else:
        st.error(f"금액이 부족합니다. {total - money}원이 더 필요합니다.")