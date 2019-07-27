import numpy as np
from keras import losses, optimizers
from keras.models import model_from_json
from tqdm import tqdm

import voice_preprocess


class EmotionPrediction:
    def __init__(self):
        self.model = None

    def load_model(self):
        self.model = model_from_json(open('net1.json').read())
        self.model.load_weights('net1.h5')
        self.model.compile(
            loss=losses.categorical_crossentropy,
            optimizer=optimizers.Adam(),
            metrics=['accuracy']
        )

    def predict(self, buffers, sample_rate):
        cropped_buffers = voice_preprocess.crop(buffers, sample_rate)

        if len(cropped_buffers) < 1:
            return 0

        periodograms = []
        for cropped_buffer in tqdm(cropped_buffers):
            periodograms.append(voice_preprocess.create_periodogram(cropped_buffer))

        test_data = np.reshape(periodograms, (len(periodograms), 28, 28, 1)) / 127

        # Evaluation
        results = self.model.predict(test_data, test_data.shape[0], 1)

        ave = np.average(results, 0)

        if ave[0] > ave[1]:
            return 0
        else:
            return 1
