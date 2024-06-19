import streamlit as st
from PIL import Image

st.title("안녕하세요!")
st.header("김은심")
st.sidebar.header("로그인")
user_ID=st.sidebar.text_input("아이디 입력",value='streamlit',max_chars=15)
user_password=st.sidebar.text_input("패스워드 입력",value="",type="password")
st.sidebar.header("그림 목록")
sel_options=['제니','음바페','러시안 블루']
user_opt=st.sidebar.selectbox("좋아하는 인물은?",sel_options,index=0)

st.sidebar.write("**선택한 그림은 ",user_opt)

#main 화면 

st.subheader('메인화면')
image_files=["","0619_img\jennie.jpg","0619_img\mbappe.jpg","0619_img\russian-blue.jpg"]

sel_index=sel_options.index(user_opt)
img_file=image_files[sel_index]
img_local= Image.open(f"img/{img_file}")

st.image(img_local,caption=user_opt)



