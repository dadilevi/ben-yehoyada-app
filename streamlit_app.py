import streamlit as st
import openai

# הגדר את מפתח ה־API שלך כאן או דרך הגדרות סביבתיות
openai.api_key = st.secrets.get("OPENAI_API_KEY")

st.set_page_config(page_title="בן יהוידע אינטראקטיבי", layout="wide")

# --- כותרת ראשית ---
st.title("📖 בן יהוידע – סנהדרין ק״ח ע״ב")
st.markdown("### עיון ולימוד עם פרשנות חיה")

# --- קטע מהספר ---
ben_yehoyada_text = """
**אורשינא** – עוף ושמו "חול", בלשון המקרא, ואינו מת לעולם.  
אמר לו נח: מדוע אינך אוכל?  
אמר לו: ראיתי אותך טרוד, ולא רציתי להטריח אותך.  
אמר לו: יהי רצון שלא תמות לעולם.

👉 מכאן למדנו: מידה של ענווה והתחשבות יכולה להעניק חיים מעבר לגבולות הטבע.
"""

with st.expander("📜 קטע מתוך בן יהוידע"):
    st.markdown(ben_yehoyada_text)

# --- תיבת שיחה עם GPT ---
st.markdown("---")
st.markdown("### 🤖 שאל את בן יהוידע")

user_question = st.text_input("מה תרצה לשאול על הקטע הזה?", placeholder="למה דווקא ענווה מזכה בחיי נצח?")

if user_question:
    with st.spinner("חושב יחד איתך..."):
        prompt = f"""
        אתה פרשן חכם ורגיש, המתמחה בפירוש אגדות חז״ל. קיבלת את הקטע הבא מתוך ספר 'בן יהוידע' על סנהדרין ק״ח ע״ב:

        {ben_yehoyada_text}

        והשאלה שנשאלה היא:
        {user_question}

        השב תשובה מעמיקה, בהירה, עם נגיעה מוסרית או קבלית לפי ההקשר.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a wise and empathetic Talmudic commentator."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            answer = response["choices"][0]["message"]["content"]
            st.markdown("#### ✨ תשובה:")
            st.markdown(answer)
        except Exception as e:
            st.error("שגיאה בתקשורת עם OpenAI. ודא שמפתח ה־API שלך תקין.")
