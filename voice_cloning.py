import os
from gradio_client import Client, file
from pydub import AudioSegment
from pydub.playback import play

client = Client("tonyassi/voice-clone")

# Get the generated audio file path
result = client.predict(
    text="Hello!!",
    audio=file("03-01-08-02-02-02-24.wav"),
    api_name="/predict"
)

print("Generated Audio File Path:", result)  # Print the local file path

# Copy the file to a writable directory before playing
safe_path = os.path.join(os.getcwd(), "cloned_voice.wav")
os.rename(result, safe_path)  # Move the file

# Load and play the audio
audio = AudioSegment.from_wav(safe_path)
play(audio) 
