from google.cloud import speech
print("hello google cloud")
client = speech.SpeechClient()
operation = client.long_running_recognize(audio=speech.types.RecognitionAudio(
       uri=".gs://my-bucket/recording.flac",
     ),
     config=speech.types.RecognitionConfig(
         encoding='LINEAR16',
         language_code='en-US',
         sample_rate_hertz=44100,
     ),
 )
print("get the dat form google cloud")
op_result = operation.result()
for result in op_result.results:
     for alternative in result.alternatives:
         print('=' * 20)
         print(alternative.transcript)
         print(alternative.confidence)
