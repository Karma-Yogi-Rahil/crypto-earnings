from dataclasses import dataclass
import fiateRates as fr
import cryptoRates as cr 
import streamlit as st 


st.write("# Total earning in inr")



today_inr_rate = f"1 Dollar = {fr.inr}INR "
st.write("### "+today_inr_rate)


last_time_updated = f" updated at {fr.time_last_updated}"
st.write(last_time_updated)


st.write("## Crypto")
crypto_symbol = st.text_input("Enter the crypto Symbol",value = 'ELON', max_chars=10)
no_of_crypto = st.number_input("",min_value=0.0000000000000000,value=1.0,step=0.00000000,format="%.10f")



st.write("## Dollar")
no_of_dollar = "{0:.10f}".format(float(no_of_crypto) * float(cr.crpto_rates(crypto_symbol)))
st.write("### "+ str(no_of_dollar))


st.write("## INR")
inr = float(no_of_dollar) * float(fr.inr)
st.write("### "+str(inr))


