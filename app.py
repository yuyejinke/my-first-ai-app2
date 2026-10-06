import streamlit as st
from openai import OpenAI

st.title("我的第一个AI助手")

# 换成你自己的智谱 API Key
client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

if prompt := st.chat_input("问我任何问题"):
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="glm-4",
        messages=[{"role": "user", "content": prompt}]
    )
    st.chat_message("assistant").write(response.choices[0].message.content)
