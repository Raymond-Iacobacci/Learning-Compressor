import numpy, sys, csv
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv1D
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#Read all corrections into file--whole filename must be specified at the beginning
inputFileName = sys.argv[1]
print(inputFileName+".corrections.csv")
inputFile = open(inputFileName+".corrections.csv", 'r')
csvreader = csv.reader(inputFile)
vals = []
vals = next(csvreader)
inputFile.close()
flips = list()
for i in range(3, len(vals)):
    flips.append(vals[i])
initString = vals[0]
n_vocab = int(vals[1])
totalLength = int(vals[2])
print(len(vals))
print(initString)
print(totalLength)



#need to add in data length

#Format data into model
for i in range(totalLength - 100):
    chars = sorted(list(set(initString)))
    charToInt = dict((c, i) for i, c in enumerate(chars))
    pattern = [charToInt[char] for char in initString]
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x/float(n_vocab)
chars = sorted(list(set(initString)))
charToInt = dict((c, i) for i, c in enumerate(chars))
#intToChar = dict((i, c) for i, c in enumerate(chars))
pattern = [charToInt[char] for char in initString]
x = numpy.reshape(pattern, (1, len(pattern), 1))
x = x/float(n_vocab)

#Build model
model = Sequential()
model.add(Conv1D(64, 3))
model.add(LSTM(64, input_shape=(100, 1)))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.built = True
model.load_weights(inputFileName + ".compress_weights")


#Build output and fill with model predictions
recreation = list()
for i in range(100):        #aka len(initString)
    recreation.append(initString[i])

for i in range(100, totalLength):
    chars = sorted(list(set(initString)))
    charToInt = dict((c, i) for i, c in enumerate(chars))
    intToChar = dict((i, c) for i, c in enumerate(chars))
    pattern = [charToInt[char] for char in initString]
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x/float(n_vocab)

    _101char = intToChar[numpy.argmax(model.predict(x, verbose=0))]
    if i in flips:
        _101char = 1 - _101char
    initString += _101char
    initString = initString[1:]
    recreation.append(_101char)


#CHECK
#need to compare to regular accuracy of model
print(len(recreation))
print(recreation)
