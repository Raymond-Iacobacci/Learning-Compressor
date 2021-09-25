import numpy
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv1D
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import sys
filename = sys.argv[1]
inputFileMaster = open(filename, 'r', encoding='utf-8')
raw_text = inputFileMaster.read()
inputFileMaster.close()
chars = sorted(list(set(raw_text)))
charToInt = dict((c, i) for i, c in enumerate(chars))
intToChar = dict((i, c) for i, c in enumerate(chars))
n_vocab = len(chars)
n_chars = len(raw_text)
seqLength = 100
dataX = []
dataY = []
for i in range(0, n_chars - seqLength, 1):
    seq_in = raw_text[i:i+seqLength]
    seq_out = raw_text[i+seqLength]
    dataX.append([charToInt[char] for char in seq_in])
    dataY.append(seq_out)
n_patterns = len(dataX)
X = numpy.reshape(dataX, (len(dataX), seqLength, 1))
X = X/float(n_vocab)
y = np_utils.to_categorical(dataY)
model = Sequential()
model.add(Conv1D(64, 3))
model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(32, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')
filepath = filename+".compress_weights"
checkpoint = ModelCheckpoint(filepath = filepath, monitor = 'accuracy', verbose=1, save_best_only = True, save_weights_only = True, mode = 'max')
history = model.fit(X, y, epochs=100, batch_size=32, callbacks=[checkpoint])

# Running the model against predictions

model.load_weights(filepath)
#model.compile(loss='categorical_crossentropy', optimizer='adam')
total = ""
import math
for i in range(len(dataX)):
    if i == math.ceil(len(dataX)/100):
        print(".", end='')
    pattern = dataX[i]
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x/float(n_vocab)
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = intToChar[index]
    total += str(result)
flips = list()
for i in range(len(total)):
    if not total[i] == raw_text[i+100]:
        flips.append(numpy.uint(i))
# Sending all flips to files

send_file = open(filename+".corrections", 'w', encoding='utf-8')
writeToCorrections = ""
for i in range(len(flips)):
    writeToCorrections+=str(flips[i])
    writeToCorrections+="."
send_file.write(writeToCorrections)

