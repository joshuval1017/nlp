import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

def process_text(text):
    # Tokenization and stop word removal
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]  # Filters out stop words and non-alphabetical tokens

    # Lemmatization (substituting for stemming as well)
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

    return tokens, lemmatized_tokens

# Example usage
if __name__ == "__main__":
    # Accept input text from the user
    user_text = input("Enter a sentence or paragraph: ")
    
    # Process the user input
    tokens, lemmatized_tokens = process_text(user_text)
    
    # Print results
    print("\nOriginal Tokens:")
    print(tokens)
    
    print("\nLemmatized Tokens:")
    print(lemmatized_tokens)
