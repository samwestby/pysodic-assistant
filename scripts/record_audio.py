import pyaudio
import wave
import time


def record_audio():
	CHUNK = 1024 
	FORMAT = pyaudio.paInt16 #paInt8
	CHANNELS = 2 
	RATE = 44100 #sample rate
	RECORD_SECONDS = 4
	# timestr = time.strftime("%H%M%S")
	# WAVE_OUTPUT_FILENAME = "output" + timestr + ".wav"
	WAVE_OUTPUT_FILENAME = "output.wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK) #buffer

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data) # 2 bytes(16 bits) per channel

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	return WAVE_OUTPUT_FILENAME

# import script.py