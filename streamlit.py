import streamlit as st 
from options import Call, Put

st.title("Options Pricer using the Black-Scholes Model")

st.sidebar.header("Options Parameters")

S = st.sidebar.number_input("Spot Price", min_value = 0.0, value=100.0, step=1.0)
K = st.sidebar.number_input("Strike Price", min_value = 0.0, value=100.0, step=1.0)
T = st.sidebar.number_input("Maturity", min_value=0.0, value=0.5, step=0.01)
r = st.sidebar.number_input("Interest Rate", min_value=0.0, value=0.05, step=0.01)
sigma = st.sidebar.number_input("Volatility (annualized)", min_value=0.0, value=0.2, step=0.01)

if st.sidebar.button("Compute the option's price and its sensitivities"):
    call = Call(S,K,T,r,sigma)
    st.subheader("Result")
    st.write(f"The option's price is : {call.price()} euros")
    st.write(f"The option's delta is : {call.delta()}")
    st.write(f"The option's gamma is : {call.gamma()}")
    st.write(f"The option's vega is : {call.vega()}")
    st.write(f"The option's theta is : {call.theta()}")
    st.write(f"The option's rho is : {call.rho()}")