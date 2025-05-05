
#generate video from text and image inputs
# from moviepy.editor import *
# from moviepy import VideoFileClip, TextClip, CompositeVideoClip
# from PIL import Image, ImageDraw, ImageFont
# import textwrap


# def create_text_image(text, width, height, font_path="C:/WINDOWS/FONTS/ARIAL.TTF", font_size=40,
#                       text_color='black', bg_color='white', align='center', line_spacing=1.5):
#     image = Image.new('RGB', (width, height), color=bg_color)
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype(font_path, font_size)

#     wrapped_text = []
#     for line in text.split('\n'):
#         wrapped_text.extend(textwrap.wrap(line, width=40))
#         wrapped_text.append('')  # line break

#     y_text = 50
#     for line in wrapped_text:
#         width_text, height_text = draw.textsize(line, font=font)
#         if align == 'center':
#             x_text = (width - width_text) / 2
#         elif align == 'right':
#             x_text = width - width_text - 50
#         else:
#             x_text = 50
#         draw.text((x_text, y_text), line, font=font, fill=text_color)
#         y_text += int(height_text * line_spacing)

#     return image

# def generate_video_with_text(image_path, output_path, text, duration=5,
#                              font_size=40, text_color='black', align='center',
#                              line_spacing=1.5, transition='fade'):
#     bg_image = Image.open(image_path).convert('RGB')
#     W, H = bg_image.size

#     text_img = create_text_image(text, W, H, font_size=font_size,
#                                  text_color=text_color, align=align, line_spacing=line_spacing)

#     # Convert PIL images to clips
#     bg_clip = ImageClip(bg_image).set_duration(duration)
#     text_clip = ImageClip(text_img).set_duration(duration)

#     if transition == 'fade':
#         text_clip = text_clip.crossfadein(1)

#     video = CompositeVideoClip([bg_clip, text_clip])
#     video.write_videofile(output_path, fps=24)

# # Example usage
# generate_video_with_text(
#     image_path="persona types\for_video\extracts\page_1-image_104.png",
#     output_path="output_video_new.mp4",
#     text="""YOUR FIRST HOME\nCOMPLEMENTED BY\n\nA FUTURE READY LIFE""",
#     duration=6,
#     font_size=48,
#     text_color='white',
#     align='center',
#     line_spacing=1.5,
#     transition='fade'
# )

# from moviepy.editor import TextClip
# clip = TextClip("Hello, world!", fontsize=70, color='white', bg_color='black')
# clip = clip.set_duration(3)
# clip.write_videofile("test_output.mp4", fps=24)



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



# from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# # Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# # Reduce the audio volume to 80% of its original volume

# clip = (
#     VideoFileClip("20250502_1706_Urban Highway Panorama_simple_compose.mp4")
#     .subclipped(0, 5)
#     .with_volume_scaled(0.8)
# )

# font_path = "C:/WINDOWS/FONTS/ARIAL.TTF"

# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip(
#     font=font_path,
#     text="Hello there!",
#     font_size=50,
#     color='white'
# ).with_duration(2).with_position('center')

# # Overlay the text clip on the first video clip
# final_video = CompositeVideoClip([clip, txt_clip])
# final_video.write_videofile("result.mp4")

#working code
# from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# # Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# # Reduce the audio volume to 80% of its original volume

# clip = (
#     VideoFileClip("example2.mp4")
#     .subclipped(10, 20)
#     .with_volume_scaled(0.8)
# )

# font_path = "C:/WINDOWS/FONTS/ARIAL.TTF"

# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip(
#     font=font_path,
#     text="Hello there!",
#     font_size=70,
#     color='white'
# ).with_duration(5).with_position('center')

# # Overlay the text clip on the first video clip
# final_video = CompositeVideoClip([clip, txt_clip])
# final_video.write_videofile("result.mp4")