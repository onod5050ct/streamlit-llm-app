from dotenv import load_dotenv
import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#load_dotenv()

st.title("趣味に関する質問アプリ")
st.write("このアプリは、趣味に関する質問を行うためのものです。") 

st.write("##### 動作モード1: ブラジリアン柔術")
st.write("ブラジリアン柔術のテクニックや練習方法について質問できます。")

st.write("##### 動作モード2: ピアノレッスン")
st.write("ピアノの曲や練習方法について質問できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["ブラジリアン柔術", "ピアノレッスン"]
)

st.divider()

if selected_item == "ブラジリアン柔術":
    input_message = st.text_input(label="教えて欲しいテクニックを入力してください")
else:
    input_message = st.text_input(label="教えて欲しい曲を入力してください")

if st.button("実行"):
    st.divider()

    api_key = st.secrets.get("OPENAI_API_KEY")

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if selected_item == "ブラジリアン柔術":
        if input_message:
            messages = [
                SystemMessage(content="あなたはブラジリアン柔術の専門家です。テクニックや練習方法について答えてください。"),
                HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(f"回答: **{result.content}**")
        else:
            st.error("教えて欲しいテクニックを入力してから「実行」ボタンを押してください。")
    else:
        if input_message:
            messages = [
                SystemMessage(content="あなたはピアノ教師です。曲について聞かれたらその曲の特徴と練習方法を答えてください。"),
                HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(f"回答: **{result.content}**")
        else:
            st.error("教えて欲しい曲を入力してから「実行」ボタンを押してください。")

