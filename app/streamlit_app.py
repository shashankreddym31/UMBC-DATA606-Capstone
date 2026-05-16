import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Crash Severity Prediction", page_icon="🚦", layout="centered")

# Load saved files
model = joblib.load("xgb_crash_severity_model.pkl")
training_columns = joblib.load("training_columns.pkl")
best_threshold = joblib.load("best_threshold.pkl")
metadata = joblib.load("metadata.pkl")

lane_cnt_median = metadata["lane_cnt_median"]

st.title("🚦 Crash Severity Prediction Tool")
st.write("Enter crash conditions below to predict whether the crash is likely to be severe.")

posted_speed_limit = st.number_input("Posted Speed Limit", min_value=0, max_value=100, value=30, step=5)
lane_cnt = st.number_input("Lane Count", min_value=1, max_value=10, value=int(round(lane_cnt_median)), step=1)
crash_hour = st.slider("Crash Hour", 0, 23, 12)
crash_day_of_week = st.slider("Crash Day of Week", 1, 7, 4)
crash_month = st.slider("Crash Month", 1, 12, 6)

traffic_control_device = st.selectbox("Traffic Control Device", ["NO CONTROLS", "TRAFFIC SIGNAL", "STOP SIGN/FLASHER", "YIELD", "UNKNOWN"])
device_condition = st.selectbox("Device Condition", ["FUNCTIONING PROPERLY", "NOT FUNCTIONING", "MISSING", "UNKNOWN"])
weather_condition = st.selectbox("Weather Condition", ["CLEAR", "RAIN", "SNOW", "CLOUDY/OVERCAST", "FOG/SMOKE/HAZE", "UNKNOWN"])
lighting_condition = st.selectbox("Lighting Condition", ["DAYLIGHT", "DARKNESS", "DARKNESS, LIGHTED ROAD", "DAWN", "DUSK", "UNKNOWN"])
first_crash_type = st.selectbox("First Crash Type", ["REAR END", "ANGLE", "TURNING", "PEDESTRIAN", "PEDALCYCLIST", "FIXED OBJECT", "PARKED MOTOR VEHICLE"])
trafficway_type = st.selectbox("Trafficway Type", ["NOT DIVIDED", "ONE-WAY", "DIVIDED - W/MEDIAN (NOT RAISED)", "DIVIDED - W/MEDIAN BARRIER", "PARKING LOT", "ALLEY", "UNKNOWN"])
alignment = st.selectbox("Alignment", ["STRAIGHT AND LEVEL", "STRAIGHT ON GRADE", "CURVE ON GRADE", "CURVE AND LEVEL", "HILLCREST", "UNKNOWN"])
roadway_surface_cond = st.selectbox("Roadway Surface Condition", ["DRY", "WET", "SNOW OR SLUSH", "ICE", "UNKNOWN"])
road_defect = st.selectbox("Road Defect", ["NO DEFECTS", "RUT, HOLES", "WORN SURFACE", "DEBRIS ON ROADWAY", "SHOULDER DEFECT", "UNKNOWN"])
prim_contributory_cause = st.selectbox("Primary Contributory Cause", ["UNABLE TO DETERMINE", "FAILING TO YIELD RIGHT-OF-WAY", "FOLLOWING TOO CLOSELY", "FAILING TO REDUCE SPEED TO AVOID CRASH", "DISTRACTION - FROM INSIDE VEHICLE", "UNDER THE INFLUENCE OF ALCOHOL/DRUGS", "PHYSICAL CONDITION OF DRIVER", "ANIMAL", "EXCEEDING AUTHORIZED SPEED LIMIT", "UNKNOWN"])
sec_contributory_cause = st.selectbox("Secondary Contributory Cause", ["NOT APPLICABLE", "UNABLE TO DETERMINE", "FAILING TO YIELD RIGHT-OF-WAY", "FOLLOWING TOO CLOSELY", "DISTRACTION - FROM INSIDE VEHICLE", "UNDER THE INFLUENCE OF ALCOHOL/DRUGS", "PHYSICAL CONDITION OF DRIVER", "ANIMAL", "EXCEEDING AUTHORIZED SPEED LIMIT", "UNKNOWN"])

if st.button("Predict Severity"):
    input_dict = {
        "POSTED_SPEED_LIMIT": posted_speed_limit,
        "TRAFFIC_CONTROL_DEVICE": traffic_control_device,
        "DEVICE_CONDITION": device_condition,
        "WEATHER_CONDITION": weather_condition,
        "LIGHTING_CONDITION": lighting_condition,
        "FIRST_CRASH_TYPE": first_crash_type,
        "TRAFFICWAY_TYPE": trafficway_type,
        "LANE_CNT": lane_cnt,
        "ALIGNMENT": alignment,
        "ROADWAY_SURFACE_COND": roadway_surface_cond,
        "ROAD_DEFECT": road_defect,
        "PRIM_CONTRIBUTORY_CAUSE": prim_contributory_cause,
        "SEC_CONTRIBUTORY_CAUSE": sec_contributory_cause,
        "CRASH_HOUR": crash_hour,
        "CRASH_DAY_OF_WEEK": crash_day_of_week,
        "CRASH_MONTH": crash_month
    }

    input_df = pd.DataFrame([input_dict])

    input_df["LANE_CNT"] = pd.to_numeric(input_df["LANE_CNT"], errors="coerce")
    input_df["LANE_CNT"] = input_df["LANE_CNT"].fillna(lane_cnt_median)

    for col in input_df.select_dtypes(include="object").columns:
        input_df[col] = input_df[col].fillna("UNKNOWN")

    input_encoded = pd.get_dummies(input_df, drop_first=True)
    input_encoded = input_encoded.reindex(columns=training_columns, fill_value=0)

    proba = model.predict_proba(input_encoded)[0][1]
    pred = int(proba >= best_threshold)

    st.subheader("Prediction Result")

    if pred == 1:
        st.error("🚨 Predicted Outcome: Severe Crash")
    else:
        st.success("✅ Predicted Outcome: Non-Severe Crash")

    st.write(f"Probability of severe crash: {proba:.2%}")
    st.write(f"Threshold used: {best_threshold:.2f}")