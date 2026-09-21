from faster_whisper import WhisperModel

audio_path = "work/question.wav"

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)

segments, info = model.transcribe(
    audio_path,
    language="pl",
)

print("Wykryty jezyk:", info.language)
print("Rozpoznany tekst:")

for segment in segments:
    print(segment.text.strip())