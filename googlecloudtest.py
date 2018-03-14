'''import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname("/home/mgc/"),
    'test.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))'''

'''
import io
from google.cloud import speech
client = speech.SpeechClient()
config = speech.types.RecognitionConfig(
     encoding='LINEAR16',
     language_code='en-US',
     sample_rate_hertz=44100,
 )
with io.open('./test.wav', 'rb') as stream:
     requests = [speech.types.StreamingRecognizeRequest(
         audio_content=stream.read(),
     )]
results = sample.streaming_recognize(
     config=speech.types.StreamingRecognitionConfig(
         config=config,
         single_utterance=False,
     ),requests,)
for result in results:
     for alternative in result.alternatives:
         print('=' * 20)
         print('transcript: ' + alternative.transcript)
         print('confidence: ' + str(alternative.confidence))
     for result in results:
         for alternative in result.alternatives:
             print('=' * 20)
             print('transcript: ' + alternative.transcript)
             print('confidence: ' + str(alternative.confidence))
'''
import io
from google.cloud import speech
client = speech.SpeechClient()
config = speech.types.RecognitionConfig(
     encoding='LINEAR16',
     language_code='en-US',
     sample_rate_hertz=44100,
 )
with io.open('/home/mgc/test.wav', 'rb') as stream:
     requests = [speech.types.StreamingRecognizeRequest(
         audio_content=stream.read(),
     )]
config = speech.types.StreamingRecognitionConfig(config=config)
responses = client.streaming_recognize(config,requests)
for response in responses:
     for result in response:
         for alternative in result.alternatives:
             print('=' * 20)
             print('transcript: ' + alternative.transcript)
             print('confidence: ' + str(alternative.confidence))
             print('is_final:' + str(result.is_final))
