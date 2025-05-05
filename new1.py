import streamlit as st
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import tempfile
import os

st.set_page_config(page_title="Video Text Overlay", layout="centered")

st.title("📹 Video Text Overlay App")

uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
overlay_text = st.text_input("Enter the text to overlay")
font_size = st.slider("Font size", 20, 100, 50)
position = st.selectbox("Text position", ["top", "center", "bottom"])

if uploaded_video and overlay_text:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_video.read())
        tmp_path = tmp.name

    clip = VideoFileClip(tmp_path)

    txt_clip = TextClip(
        overlay_text,
        fontsize=font_size,
        color="white",
        font="Arial"
    ).set_duration(clip.duration)

    # Set text position
    if position == "top":
        txt_clip = txt_clip.set_position(("center", "top"))
    elif position == "center":
        txt_clip = txt_clip.set_position("center")
    else:
        txt_clip = txt_clip.set_position(("center", "bottom"))

    video = CompositeVideoClip([clip, txt_clip])
    
    output_path = os.path.join(tempfile.gettempdir(), "output.mp4")
    video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    st.video(output_path)
    with open(output_path, "rb") as file:
        st.download_button(label="Download Output Video", data=file, file_name="output.mp4")
