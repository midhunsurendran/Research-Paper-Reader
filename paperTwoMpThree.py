import gtts
import os
import argparse


def synthesize_text(filetext):
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=filetext)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(os.path.splitext(path)[0] + ".mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


path = input('Enter the location of your PDF file with filename: ')

with open(f'{path}', "r", encoding="utf-8", errors='ignore') as file:
    filetext = file.read()
    synthesize_text(filetext)
