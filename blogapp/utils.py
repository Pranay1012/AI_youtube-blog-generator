from faster_whisper import WhisperModel
from transformers import pipeline
import os

print("Loading CPU-optimized models...")

# Whisper for transcription
whisper_model = WhisperModel(
    "medium",                    
    device="cpu",
    compute_type="int8",         
    cpu_threads=8                
)

# Text generation
text_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small", 
    device=-1,                    
    model_kwargs={"torchscript": True}  
)

# Download audio from YouTube
def download_audio(youtube_url, filename="temp.mp4"):
    from pytubefix import YouTube
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    return stream.download(filename=filename)

def transcribe_audio(audio_file):
    segments, _ = whisper_model.transcribe(
        audio_file,
        beam_size=1,           
        language="en"
    )
    
    transcript = " ".join(segment.text.strip() for segment in segments)
    
    # Clean up temporary file
    if os.path.exists(audio_file):
        os.remove(audio_file)
    
    return transcript.strip()

def generate_blog(transcript):
    
    # Limit 
    words = transcript.split()[:500]  
    transcript = " ".join(words)
    
    #prompt
    prompt = f"Write a blog post with introduction, main points, and conclusion based on: {transcript} /n Make it engaging and informative. Do not repeat phrases. You can use bullet points. You can reduce the length according to your needs"
    result = text_generator(
        prompt,
        max_length=650,        
        temperature=0.7,
        do_sample=False        
    )
    
    return result[0]["generated_text"]
