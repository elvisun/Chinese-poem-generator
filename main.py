'''Example script to generate text from Nietzsche's writings.
At least 20 epochs are required before the generated text
starts sounding coherent.
It is recommended to run this script on GPU, as recurrent
networks are quite computationally intensive.
If you try this script on new data, make sure your corpus
has at least ~100k characters. ~1M is better.
'''

from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file

import numpy as np
import random
import sys
import io

DATA_FILE = './poetry_no_title.txt'
TARGET_FILE = './result.txt'
WEIGHTS_FILE = './weights.h5'

class generator:
    def __init__(self):
        self.weight_file = WEIGHTS_FILE
        self.f = open(TARGET_FILE, 'w', encoding='utf-8')
        self.text = io.open(DATA_FILE, encoding='utf-8').read().lower()
        print('corpus length:', len(self.text))
        self.chars = sorted(list(set(self.text)))
        print('char space size:', len(self.chars))

    def sample(self, preds, temperature=1.0):
        # helper function to sample an index from a probability array
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)


    def generate_sample_result(self, epoch, logs):
        # Function invoked at end of each epoch. Prints generated text.
        print()
        print('----- Generating text after Epoch: %d' % epoch)

        start_index = random.randint(0, len(self.text) - self.maxlen - 1)
        diversity = 0.2
        generated = ''
        sentence = self.text[start_index: start_index + self.maxlen]
        generated += sentence

        for i in range(100):
            x_pred = np.zeros((1, self.maxlen, len(self.chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, self.char_indices[char]] = 1.

            preds = self.model.predict(x_pred, verbose=0)[0]
            next_index = self.sample(preds, diversity)
            next_char = self.indices_char[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char

            self.f.write(next_char)
            self.f.flush()
        print()

    def save(self, epoch, logs):
        print("saving")
        self.model.save_weights(self.weight_file)

    def build_model(self):
        print('Build model...')
        self.model = Sequential()
        self.model.add(LSTM(128, input_shape=(self.maxlen, len(self.chars))))
        self.model.add(Dense(len(self.chars)))
        self.model.add(Activation('softmax'))

        optimizer = RMSprop(lr=0.01)
        self.model.compile(loss='categorical_crossentropy', optimizer=optimizer)
        try:
            self.model.load_weights(self.weight_file, by_name=True)
        except Exception as e:
            print("wrong weight file size, starting with random weights")
        

    def train(self):
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))

        # cut the text in semi-redundant sequences of self.maxlen characters
        MINI_BATCH_SIZE = 2048
        number_of_epoch = len(self.text)/MINI_BATCH_SIZE
        self.maxlen = 5
        step = 1
        sentences = []
        next_chars = []

        self.build_model()

        print("training with epochs of: ", int(number_of_epoch))
        self.model.fit_generator(self.generate_batch(),
          steps_per_epoch=MINI_BATCH_SIZE,
          epochs=int(number_of_epoch),
          callbacks=[
          LambdaCallback(on_epoch_end=self.save), 
          LambdaCallback(on_epoch_end=self.generate_sample_result)])
    
    def generate_batch(self):
        i = 0
        while 1:
            x = self.text[i: i + self.maxlen]
            y = self.text[i + self.maxlen]

            x_vec = np.zeros((1, self.maxlen, len(self.chars)), dtype=np.bool)
            y_vec = np.zeros((1, len(self.chars)), dtype=bool)
            
            y_vec[0, self.char_indices[y]] = 1
            for t, char in enumerate(x):
                x_vec[0, t, self.char_indices[char]] = 1
            yield x_vec, y_vec
            i += 1

def main():
    g = generator()
    g.train()


if __name__ == '__main__':
    main()