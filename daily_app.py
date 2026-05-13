import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="每日健康練功房", page_icon="🧘")

# --- 標題區 ---
st.title("🧘 每日減重與練功追蹤 App")
st.markdown("---")

# --- 側邊欄：輸入數據 ---
with st.sidebar:
    st.header("📋 個人數據輸入")
    name = "Yaojie"
    # 使用 slider 或 number_input
    current_weight = st.number_input("目前體重 (kg)", min_value=30.0, max_value=200.0, value=55.0, step=0.1)
    
    st.subheader("💧 今日進度")
    water_intake = st.number_input("今日已飲水 (cc)", min_value=0, step=50)
    
    st.subheader("🔥 練功統計")
    days_practiced = st.slider("本週堅持練功天數 (10分鐘/日)", 0, 7, 0)

# --- 核心邏輯計算 ---
# 1. 自動計算減重目標 (減 5kg)
target_weight = current_weight - 5

# 2. 個人化飲水公式 (體重 x 35cc)
recommended_water = current_weight * 35

# --- 主畫面顯示 ---

# 第一區：體重目標
col1, col2 = st.columns(2)
with col1:
    st.metric(label="目前體重", value=f"{current_weight} kg")
with col2:
    st.metric(label="5公斤減重目標", value=f"{target_weight} kg", delta="-5.0 kg")

st.markdown("---")

# 第二區：喝水大挑戰
st.header("💧 喝水挑戰")
water_progress = min(water_intake / recommended_water, 1.0) # 限制最高 100%
st.progress(water_progress)

if water_intake >= recommended_water:
    st.success(f"🎊 達成目標！你已經喝了 {water_intake} cc，身體代謝正在飛速運轉！")
else:
    gap = recommended_water - water_intake
    st.warning(f"還差 {gap:.0f} cc 就能達到建議量 ({recommended_water:.0f} cc)。")
    st.info("💡 建議：現在就去喝一杯 200cc 的溫水吧！")

st.markdown("---")

# 第三區：練功與金句
st.header("⚔️ 功力進度")
st.write(f"本週已練功 **{days_practiced}** 天")

if days_practiced >= 7:
    st.balloons() # 滿分噴氣球
    st.title("🏆 全勤達成：道心堅定！")
elif days_practiced >= 4:
    st.write("✨ 漸入佳境，繼續保持每日 10 分鐘的頻率。")
else:
    st.write("💪 沒關係，修行在於呼吸之間，明天重新開始。")

# --- 頁尾鼓勵 ---
st.markdown("---")
st.caption(f"星光提醒：{name}，減肥 5 公斤不是終點，健康的習慣才是。加油！")