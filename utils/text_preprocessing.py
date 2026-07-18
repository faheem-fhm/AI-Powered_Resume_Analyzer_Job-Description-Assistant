import re
import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))


# ==========================================
# Convert to Lowercase
# ==========================================

def to_lowercase(text):

    return text.lower()


# ==========================================
# Remove Punctuation
# ==========================================

def remove_punctuation(text):

    return text.translate(
        str.maketrans("", "", string.punctuation)
    )


# ==========================================
# Remove Numbers
# ==========================================

def remove_numbers(text):

    return re.sub(r"\d+", "", text)


# ==========================================
# Remove Extra Spaces
# ==========================================

def remove_extra_spaces(text):

    return re.sub(r"\s+", " ", text).strip()


# ==========================================
# Tokenization
# ==========================================

def tokenize_text(text):

    return word_tokenize(text)


# ==========================================
# Remove Stop Words
# ==========================================

def remove_stopwords(tokens):

    cleaned = []

    for word in tokens:

        if word not in stop_words:

            cleaned.append(word)

    return cleaned


# ==========================================
# Lemmatization
# ==========================================

def lemmatize_words(tokens):

    result = []

    for word in tokens:

        result.append(
            lemmatizer.lemmatize(word)
        )

    return result


# ==========================================
# Complete NLP Pipeline
# ==========================================

def preprocess_text(text):

    text = to_lowercase(text)

    text = remove_punctuation(text)

    text = remove_numbers(text)

    text = remove_extra_spaces(text)

    tokens = tokenize_text(text)

    tokens = remove_stopwords(tokens)

    tokens = lemmatize_words(tokens)

    cleaned_text = " ".join(tokens)

    return cleaned_text