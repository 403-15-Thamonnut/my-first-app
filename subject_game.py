import time
import streamlit as st

st.title("⏱️ ห้องเรียนสายไหมต้องรอด ทายวิชาจับเวลา")

# 1. กำหนดค่าเริ่มต้นใน Session State
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

@st.dialog("📊 สรุปผลการเล่นเกม")
# แก้ไข: เพิ่ม ans5 เข้ามาใน arguments
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    # แก้ไข: เปลี่ยนเป็น .upper() เพื่อให้เช็คกับ "CAT" ได้ หรือถ้าอยากบังคับพิมพ์ใหญ่เท่านั้นให้ใช้ ans5.strip()
    u_ans5 = ans5.strip().upper()

    if u_ans1 == "คณิตศาสตร์":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    if u_ans2 == "ชีววิทยา":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    if u_ans3 == "พระพุทธศาสนา":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "พละศึกษา":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
      
    if u_ans5 == "CAT":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        # แสดงค่าดั้งเดิมที่ user พิมพ์ (ans5.strip()) เพื่อให้เห็นว่าเขาพิมพ์อะไรมา
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{ans5.strip()}')")

    # แก้ไข: จัดย่อหน้าให้ถูกต้อง
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("🎉 ระดับราชา")
    elif score >= 3:
        st.warning("😎 เอาใหม่ ๆ ราชาไม่มีวันยอมแพ้")
    elif score >= 1:
        st.error("😅 ไม่ได้ครึ่งของราชา")
    else:
        st.error("💀 กระจอกชะมัด")

# ปุ่มเริ่มเกม
st.button("🎮 เริ่มเล่นเกม / เริ่มใหม่", on_click=reset_game)

# 3. ส่วนจับเวลา
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 4. ช่องกรอกคำตอบ
ans1 = st.text_input(
    "ข้อ 1: วิชาอะไรที่ต้องใช้การคิดเลขเร็ว?",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: วิชาอะไรต้องเรียนเกี่ยวกับเซลล์?",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: วิชาอะไรที่เรียนเกี่ยวกับศาสนา?",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: วิชาอะไรที่ต้องยืดเส้นสายก่อนเรียน?",
    value=st.session_state.ans4_val,
)
# แก้ไข: เอาการกด Enter (บรรทัดใหม่) ออกจาก String 
ans5 = st.text_input(
    "ข้อ 5: แมว ภาษาอังกฤษสะกดอย่างไร? (สะกดด้วยตัวพิมพ์ใหญ่)",
    value=st.session_state.ans5_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

# 5. ปุ่มส่งคำตอบ และ Loop วนเวลา
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 6. แสดงผลลัพธ์ผ่าน Dialog
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)
