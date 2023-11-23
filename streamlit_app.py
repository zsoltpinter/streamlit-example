import streamlit as st

st.title("Kalkulátor")
st.write("---")

szam1 = st.number_input(label = "K&H")
szam2 = st.number_input(label = "OTP Nemzeti Bank")

st.write("Mit akarsz?")
st.radio("Lehetőségek :",("Hitel", "KamatosKamat", "Kölcsön", "Pénz felvétel"))

ans = 0 
def calculate():
  if Lehetőségek == "Hitel":
    ans = szam1 + szam2
  elif Lehetőségek == "KamatosKamat":
    ans = szam1 - szam2
  elif Lehetőségek == "Kölcsön":
    ans = szam1 * szam2
  elif Lehetőségek == "Pénz felvétel" and number2!=0:
    ans = szam1 / szam2
  else:
    st.warning("Nem vehetsz fel semmit te barom!!44!4!!!!!4!")
    ans = "NoNo"

st.succes(f"Tessek {ans}")

if st.button("Kalkulalas"):
  calculate()





























    















