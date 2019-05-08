import os

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import io
from google.cloud import speech_v1p1beta1 as speech

client = speech.SpeechClient()
speech_file = r'C:\Users\aammg\Documents\Nice POC\Voice Comments\GregK_10232018.wav'
with io.open(speech_file, 'rb') as audio_file:
    content = audio_file.read()
    
audio = speech.types.RecognitionAudio(content=content)
config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code='en-US',
    # Enhanced models are only available to projects that
    # opt in for audio data collection.
    use_enhanced=True,
    # A model must be specified to use enhanced model.
    model='phone_call')
response = client.recognize(config, audio)
for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}'.format(i))
    print('Transcript: {}'.format(alternative.transcript))

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = alternative.transcript
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))