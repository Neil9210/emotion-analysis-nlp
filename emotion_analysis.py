# Emotion Detection from Text
# Beginner Friendly NLP Project

def detect_emotion(text):

    text = text.lower()

    happy_words = ["happy", "joy", "great", "good", "awesome", "fantastic", "love", "excited"]
    sad_words = ["sad", "cry", "upset", "depressed", "unhappy", "bad", "hurt"]
    angry_words = ["angry", "mad", "hate", "annoyed", "furious", "irritated"]

    happy_score = sum(word in text for word in happy_words)
    sad_score = sum(word in text for word in sad_words)
    angry_score = sum(word in text for word in angry_words)

    if happy_score > sad_score and happy_score > angry_score:
        return "Happy 😊"
    elif sad_score > happy_score and sad_score > angry_score:
        return "Sad 😢"
    elif angry_score > happy_score and angry_score > sad_score:
        return "Angry 😠"
    else:
        return "Neutral 😐"


print("Emotion Analysis Tool")
user_text = input("Enter your text: ")

emotion = detect_emotion(user_text)

print("Detected Emotion:", emotion)
