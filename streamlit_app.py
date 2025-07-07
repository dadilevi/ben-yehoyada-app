import streamlit as st
from openai import OpenAI

# טען את מפתח ה־API בצורה מאובטחת
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="בן יהוידע – סנהדרין ק״ח ע״ב", layout="centered")

st.title("📖 בן יהוידע – סנהדרין ק״ח ע״ב")
st.subheader("עיון ולימוד עם פרשנות חיה")

with st.expander("📜 קטע מתוך בן יהוידע"):
    st.markdown("""
**אורשינא** – עוף ושמו "חול", בלשון המקראי, ואינו מת לעולם  
אמר לו נח: מדוע אינך אוכל?  
אמר לו: ראיתי אותך טרוד, ולא רציתי להטריח אותך  
אמר לו: יהי רצון שלא תמות לעולם

👉 מכאן למדנו: מידה של ענווה והתחשבות יכולה להעניק חיים מעבר לגבולות הטבע.
""")

st.markdown("---")
st.markdown("### 🤖 שאל את בן יהוידע")
question = st.text_input("מה תרצה לשאול על הקטע הזה?")

if question:
    with st.spinner("בן יהוידע חושב על תשובה..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "אתה בן יהוידע, חכם מקובל ופילוסוף יהודי. ענה לשאלות בעומק, בשפה נגישה ובנימה מלמדת, בהתבסס על הקטע שניתן."
                    },
                    {
                        "role": "user",
                        "content": f"הנה הקטע: \"אורשינא – עוף ושמו חול...\". והשאלה שלי: {question}"
                    }
                ]
            )
            answer = response.choices[0].message.content
            st.markdown("**✍️ תשובת בן יהוידע:**")
            st.write(answer)
        except Exception as e:
            st.error(f"שגיאה בהתקשרות עם OpenAI: {e}")
