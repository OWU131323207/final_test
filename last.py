import streamlit as st
import pandas as pd

def load_data():
    return pd.read_csv("idol.csv")

st.title("=LOVEの曲紹介")
st.markdown("-----")

df = load_data()

category = st.sidebar.selectbox(
    "どんな曲を聴きたい？",
    df["テーマ"].unique()
)

filtered_df = df[df["テーマ"] == category]

if 'favorites' not in st.session_state:
    st.session_state.favorites = []  

if not filtered_df.empty:
    for idx, row in filtered_df.iterrows():
        st.markdown(f"### 🎵 {row['曲名']}")
        st.text(f"センター：{row['センター']}")
        st.markdown(f"{row['紹介文']}")
        if pd.notna(row.get('YouTube', None)):
            st.video(row['YouTube'])
        
        button_key = f"favorite_button_{idx}" 
        if st.button(f"♡", key=button_key):
            if row['曲名'] not in st.session_state.favorites:
                st.session_state.favorites.append(row['曲名'])

        st.markdown("---")

if st.session_state.favorites:
    st.markdown("### お気に入りリスト")
    for favorite in st.session_state.favorites:
        st.write(favorite)

st.caption("本アプリ内のYouTubeリンクはすべて公式チャンネルから取得しています。")
st.caption("[公式YouTubeチャンネルはこちら](https://www.youtube.com/c/OfficialChannelName)")