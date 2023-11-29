import streamlit as st

st.title("kalkulátor")
st.write("---")

szam1 = st.number_input(label = "K&H")
szam2 = st.number_input(label = "OTP Nemzeti Bank")

st.write("lehetosegek")
lehetosegek = st.radio("lehetosegek :",("Osszeadas", "Kivonas", "Szorzas", "Osztas"))

ans = 0 
def calculate():
  if lehetosegek == "Osszeadas":
    ans = szam1 + szam2
  elif lehetosegek == "Kivonas":
    ans = szam1 - szam2
  elif lehetosegek == "Szorzas":
    ans = szam1 * szam2
  elif lehetosegek == "Osztas" and number2!=0:
    ans = szam1 / szam2
  else:
    st.warning("Nem vehetsz fel semmit te barom!!44!4!!!!!4!")
    ans = "NoNo"

  st.success(f"Answer = {ans}")

if st.button("kalkulalas"):
    calculate()





























    















