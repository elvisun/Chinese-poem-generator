from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import Adam
from keras.utils.data_utils import get_file


import numpy as np
import random
import sys
import io
import preprocess_data

poetry_word_per_sentence = '5'
BIG_FILE = './poetry_no_title.txt'
DATA_FILE = './poetry_no_title_data_' + poetry_word_per_sentence +'.txt'
VALIDATION_FILE = './poetry_no_title_validation_' + poetry_word_per_sentence + '.txt'
TARGET_FILE = './result.txt'
WEIGHTS_FILE = './weights.h5'


class generator:
    def train(self):
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))

        # cut the text in semi-redundant sequences of self.maxlen characters
        TRAIN_TEST_SPLIT = 0.7
        MINI_BATCH_SIZE = 1024
        number_of_epoch = len(self.text)/MINI_BATCH_SIZE
        self.maxlen = 6
        step = 1
        sentences = []
        next_chars = []

        self.build_model()

        print("training with epochs of: ", int(number_of_epoch))
        self.model.fit_generator(self.text_2_vec_generator('data'),
            verbose=True,
            steps_per_epoch=MINI_BATCH_SIZE,
            epochs=int(number_of_epoch),
            validation_data=self.text_2_vec_generator('validation'),
            # To give same number of batch size
            validation_steps=MINI_BATCH_SIZE/TRAIN_TEST_SPLIT*(1-TRAIN_TEST_SPLIT),
            callbacks=[
              LambdaCallback(on_epoch_end=self.save), 
              LambdaCallback(on_epoch_end=self.generate_sample_result)])

    def __init__(self):
        preprocess_data.main()
        self.weight_file = WEIGHTS_FILE
        self.f = open(TARGET_FILE, 'w', encoding='utf-8')
        self.text = io.open(BIG_FILE, encoding='utf-8').read()
        print('corpus length:', len(self.text))
        self.chars = sorted(list(set(self.text)))
        print('char space size:', len(self.chars))

        self.data_text = io.open(DATA_FILE, encoding='utf-8').read()
        self.validation_text = io.open(VALIDATION_FILE, encoding='utf-8').read()
        self.log_file = open('log.txt', 'w', encoding='utf-8')

    # helper function to sample an index from a probability array
    def sample(self, preds, temperature=1.0):
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)

    # Function invoked at end of each epoch. Prints generated text.
    def generate_sample_result(self, epoch, logs):
        self.f.write("\n\n\n\n==================Epoch {}=====================\n".format(epoch))
        for diversity in [0.5,1.0,1.5]:
            self.f.write("\n\n------------Diversity {}--------------\n".format(diversity))
            start_index = random.randint(0, len(self.text) - self.maxlen - 1)
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


    def save(self, epoch, logs):
        self.model.save_weights(self.weight_file)

    def build_model(self):
        print('Build model...')
        self.model = Sequential()
        self.model.add(LSTM(512, return_sequences=True, input_shape=(self.maxlen, len(self.chars))))
        self.model.add(Dropout(0.6))
        self.model.add(LSTM(256))
        self.model.add(Dropout(0.6))
        self.model.add(Dense(len(self.chars)))
        self.model.add(Activation('softmax'))

        optimizer = Adam()
        self.model.compile(loss='categorical_crossentropy', optimizer=optimizer)
        try:
            self.model.load_weights('stablized_weights.h5', by_name=True)
            print("Loading model")
        except Exception as e:
            print("wrong weight file size, starting with random weights")
    
    def text_2_vec_generator(self, type):
        f = 0
        if type == 'data':
            f = self.data_text
        elif type == 'validation':
            f = self.validation_text
        else:
            assert('invalid type, specify data or valiation')

        i = 0
        while 1:
            x = f[i: i + self.maxlen]
            y = f[i + self.maxlen]
            #Make sure all data are from one poem
            if '\n' in x or '\n' in y:
                i += 1
                continue
            self.log_file.write(x)
            self.log_file.write("==>")
            self.log_file.write(y)
            self.log_file.write('\n\n')
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