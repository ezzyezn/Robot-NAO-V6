from speech_to_text import transcribe_audio

audio_path = "work/question.wav"

text = transcribe_audio(audio_path)

print("Rozpoznany tekst:",text)
