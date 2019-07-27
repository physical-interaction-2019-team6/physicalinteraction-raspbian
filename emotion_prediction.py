import numpy as np
from keras import losses, optimizers
from keras.models import model_from_json
from tqdm import tqdm
import matplotlib.pyplot as plt

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

        X_test = np.reshape(periodograms,(len(periodograms),28,28,1))

        X_test = X_test / 127

        # Evaluation
        result = self.model.predict(X_test, X_test.shape[0], 1)

        return result
