from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D

def base_model(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(Flatten())
    model.add(Dense(250, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

def conv_model(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(250, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model
    
def lstm_model(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))
    return model
    
def bi_lstm_model(params):
    model = Sequential()
    model.add(Embedding(params['top_words'], params['embedding_vecor_length'], input_length=params['max_review_length']))
    model.add(Bidirectional(LSTM(64)))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    return model
