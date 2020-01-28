# Based off https://github.com/MITESHPUTHRANNEU/Speech-Emotion-Analyzer/blob/master/final_results_gender_test.ipynb

import numpy as np
from keras.models import model_from_json
import librosa
import librosa.display
import pandas as pd


def load_model():
	with open('model_2_cat.json', 'r') as file:
		loaded_model_json = file.read()

	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights('2_cat.h5')
	return loaded_model


def run_model(loaded_model, output_file='output.wav'):
	emotion_labels = ['happy', 'sad']
	data, sampling_rate = librosa.load(output_file, res_type='kaiser_fast', duration=2.5, sr=22050 * 2) 
	sampling_rate = np.array(sampling_rate)
	mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=13), axis=0)
	featurelive = mfccs
	# Because for some reason my model takes len 215 not len 216
	featurelive = featurelive[:-1]
	livedf2 = featurelive
	livedf2 = pd.DataFrame(data=livedf2)
	livedf2 = livedf2.stack().to_frame().T
	twodim = np.expand_dims(livedf2, axis=2)
	livepreds = loaded_model.predict(twodim, batch_size=64, verbose=1)
	livepreds1 = livepreds.argmax(axis=1)
	liveabc = livepreds1.astype(int).flatten()
	print(emotion_labels[liveabc[0]])
	return emotion_labels[liveabc[0]]
