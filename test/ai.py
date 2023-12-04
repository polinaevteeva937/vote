import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

# Загрузка данных из файла
with open('opisanie.txt', encoding='utf-8') as f:
    data = f.read().lower()

# Токенизация текста
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts([data])
total_chars = len(tokenizer.word_index) + 1
print('Total unique chars:', total_chars)

# Создание последовательностей
max_sequence_len = 50
step = 3

sequences = []
next_char = []

for i in range(0, len(data) - max_sequence_len, step):
    sequences.append(data[i: i + max_sequence_len])
    next_char.append(data[i + max_sequence_len])

print('Number of sequences:', len(sequences))

# Векторизация текста
X = np.zeros((len(sequences), max_sequence_len, total_chars), dtype=np.bool_)
y = np.zeros((len(sequences), total_chars), dtype=np.bool_)

for i, sequence in enumerate(sequences):
    for t, char in enumerate(sequence):
        X[i, t, tokenizer.word_index[char]] = 1
    y[i, tokenizer.word_index[next_char[i]]] = 1

# Создание модели
model = Sequential([
    Embedding(total_chars, 64, input_length=max_sequence_len),
    LSTM(128),
    Dense(total_chars, activation='softmax'),
])

model.compile(loss='categorical_crossentropy', optimizer='adam')

# Обучение модели
model.fit(X, y, epochs=50)

# Генерация текста
def generate_text(length, temperature=1.0):
    generated = ''
    sequence = ' ' * max_sequence_len
    for _ in range(length):
        x_pred = np.zeros((1, max_sequence_len, total_chars))
        for t, char in enumerate(sequence):
            if char != ' ':
                x_pred[0, t, tokenizer.word_index[char]] = 1
        
        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = tokenizer.sequences_to_texts([[next_index]])[0]

        generated += next_char
        sequence = sequence[1:] + next_char

    return generated

def sample(preds, temperature=1.0):
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    return np.argmax(np.random.multinomial(1, preds, 1))

# Теперь, когда модель обучена, можно генерировать уникальные описания
unique_description = generate_text(length=500)
print(unique_description)

# В этом примере:
# - считываем данные из файла;
# - токенизируем текст на уровне отдельных символов;
# - создаем последовательности фиксированной длины и соответствующие метки (следующие символы);
# - строим и обучаем простую рекуррентную нейронную сеть с LSTM слоем;
# - генерируем новый текст на основе модели с функцией generate_text.