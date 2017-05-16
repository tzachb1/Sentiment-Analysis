from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D

def base(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(Flatten())
    model.add(Dense(250, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

def conv(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(250, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

def conv2(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(Convolution1D(64, 3, border_mode='same'))
    model.add(Convolution1D(32, 3, border_mode='same'))
    model.add(Convolution1D(16, 3, border_mode='same'))
    model.add(Flatten())
    model.add(Dropout(0.2))
    model.add(Dense(180,activation='sigmoid'))
    model.add(Dropout(0.2))
    model.add(Dense(1,activation='sigmoid'))
    return model   
    
def lstm(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))
    return model
    
def lstm2(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(LSTM(200))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    return model
