import pyaudio
import wave
import time
import keyboard
import os
from pydub import AudioSegment
from pydub.playback import play


def augment_data():
	path = os.cwd()
    path = os.path.join(path, 'data')
    os.mkdir(os.path.join(path, 'augmented'))
    path = os.path.join(path, 'raw')
    out_path = os.path.join(path, 'data', 'augmented')
	for file in os.listdir(path):
		song = AudioSegment.from_wav(os.path.join(path, file))
		louder = song + 10
		quieter = song - 10
		louder.export(os.path.join(out_path, file[:-4]+'_l'+file[-4:]),format='wav')
		quieter.export(os.path.join(out_path, file[:-4]+'_q'+file[-4:]),format='wav')


def record_dataset():
	emotions = ['happy', 'sad']
	path = 'data'
	if not os.path.isdir(path):
		os.mkdir(path)
    path = os.path.join(path, 'raw')
    if not os.path.isdir(path):
		os.mkdir(path)
	for emotion in emotions:
		record_all_emotion_samples(emotion, path)
	augment_data()
    
    
def record_all_emotion_samples(emotion, path):
	max_count = 100
	for count in range(0, max_count):
		cur = count+1
        print('Hold \'p\' to pause. Press \'r\' to resume')
		print(emotion + ' ' + str(cur) + '/' + str(max_count) + ' RECORDING NOW :)')
		time.sleep(.2)
        check_and_pause()
		record_single_sample(emotion, count, path)
		check_and_pause()


def check_and_pause():
    if keyboard.is_pressed('p'):
			while True:
				if keyboard.is_pressed('r'):
					break


def record_single_sample(emotion, count, path):
# Method based on https://github.com/MITESHPUTHRANNEU/Speech-Emotion-Analyzer/blob/master/AudioRecorder.ipynb
	CHUNK = 1024 
	FORMAT = pyaudio.paInt16 #paInt8
	CHANNELS = 2 
	RATE = 44100 #sample rate
	RECORD_SECONDS = 2.5
	WAVE_OUTPUT_FILENAME = os.path.join(path, emotion + '_' + str(count) + ".wav")

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK) #buffer

	print("* recording " + WAVE_OUTPUT_FILENAME)

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data) # 2 bytes(16 bits) per channel

	print("* done recording " + WAVE_OUTPUT_FILENAME)

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	
	
if __name__ == "__main__":
	# augment_data()
	# # record_dataset()
