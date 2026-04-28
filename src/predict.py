# importing the libraries needed to load the model and tokenizer
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# loading the trained sentiment analysis model
model = load_model("model.h5")

# loading the tokenizer used during preprocessing
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# this function receives a text review and returns the predicted sentiment
def predict_sentiment(text: str) -> str:
    # converting the input text into a numeric sequence
    sequence = tokenizer.texts_to_sequences([text])

    # padding the sequence to match the length used during training
    padded_sequence = pad_sequences(
        sequence,
        maxlen=200,
        padding="post",
        truncating="post"
    )

    # getting the prediction score from the model
    prediction = model.predict(padded_sequence)[0][0]

    # converting the prediction score into a readable label
    if prediction >= 0.5:
        return "Positive"
    else:
        return "Negative"
