import streamlit as st
error = bool()
st.title('Toán')
col1,col2,col3 = st.columns(3)
with col1:
    a = st.number_input('a')
with col2:
    ph = st.radio('Phép toán',('\+','\-','x',':'),horizontal=True)
with col3:
    b = st.number_input('b')
ketqua = st.number_input('Nhập kết quả')
if ph == '\+':
    prod = a+b
elif ph == '\-':
    prod = a-b
elif ph == 'x':
    prod = a*b
elif ph == ':':
    if b != 0:
      prod = a/b
      error = False
    else: error = True
    prod = None

if st.button('Kiểm tra'):
    if error:
        st.error('b phải khác 0')
    elif ketqua == prod:
        st.info(':blue[Correct]')
        st.balloons()
    elif ketqua != prod:
      st.error(':red[Wrong]')



