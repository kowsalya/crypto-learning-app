import streamlit as st

st.title("💰 Crypto Profit Calculator")

buy_price = st.number_input("Buy Price (₹)", min_value=0.0)
current_price = st.number_input("Current Price (₹)", min_value=0.0)
quantity = st.number_input("Quantity", min_value=0.0)

if st.button("Calculate"):
    investment = buy_price * quantity
    current_value = current_price * quantity
    profit = current_value - investment

    if investment > 0:
        roi = (profit / investment) * 100
    else:
        roi = 0

    st.write("Investment:", investment)
    st.write("Current Value:", current_value)
    st.write("Profit:", profit)
    st.write("ROI:", round(roi, 2), "%")