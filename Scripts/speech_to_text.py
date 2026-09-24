from faster_whisper import WhisperModel

# Load the model once and reuse it for later questions.
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8",
)


def transcribe_audio(filename):
    segments, info = model.transcribe(
        filename,
        language="pl",
    )

    parts = []

    # Iterating over segments performs the transcription.
    for segment in segments:
        text = segment.text.strip()
        if text:
            parts.append(text)

    return " ".join(parts)
