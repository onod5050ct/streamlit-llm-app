from dotenv import load_dotenv
import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

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

def get_llm_response(input_message: str, selected_item: str) -> str:
    api_key = st.secrets.get("OPENAI_API_KEY")
    if not api_key:
        st.error("OPENAI_API_KEYが設定されていません。StreamlitのSecretsにAPIキーを追加してください。")
        st.stop()
    os.environ["OPENAI_API_KEY"] = api_key

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if selected_item == "ブラジリアン柔術":
        system_prompt = "あなたはブラジリアン柔術の専門家です。テクニックや練習方法について答えてください。"
    else:
        system_prompt = "あなたはピアノ教師です。曲について聞かれたらその曲の特徴と練習方法を答えてください。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_message),
    ]
    result = llm(messages)
    return result.content

if st.button("実行"):
    st.divider()
    if not input_message:
        if selected_item == "ブラジリアン柔術":
            st.error("教えて欲しいテクニックを入力してから「実行」ボタンを押してください。")
        else:
            st.error("教えて欲しい曲を入力してから「実行」ボタンを押してください。")
    else:
        response = get_llm_response(input_message, selected_item)
        st.write(f"回答: **{response}**")