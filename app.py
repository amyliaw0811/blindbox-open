import streamlit as st

# 頁面設置
st.set_page_config(page_title="盲盒開箱神器", page_icon="🧩", layout="centered")

# 啟動畫面
with st.spinner('正在召喚開箱神器…'):
    st.title("盲盒開箱神器")
    st.markdown("歡迎使用！輸入盒號，即可查詢可能出現的角色。")
    st.markdown("---")

# 盒號對應資料
box_mapping = {
    1: ['DADA', 'BABA'],
    2: ['ZIZI', 'QUQU'],
    3: ['BABA', 'HEHE'],
    4: ['QUQU', 'DADA'],
    5: ['DADA', 'SISI'],
    6: ['DADA', 'HEHE']
}

# 輸入框
box_input = st.text_input("請輸入盒號（多個請用逗號隔開，例如：1,3,5）")

if box_input:
    try:
        box_numbers = [int(x.strip()) for x in box_input.split(',')]
        st.success("好運！祝你開出大熱門角色！")
        for number in box_numbers:
            if number in box_mapping:
                roles = box_mapping[number]
                st.markdown(f"**盒號 {number}：{roles[0]} / {roles[1]}**")
            else:
                st.warning(f"盒號 {number}：未找到對應角色。")
    except ValueError:
        st.error("請確認輸入的是數字盒號，用逗號隔開！")
