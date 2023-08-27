import gtts
import threading
import time

def text_to_speech(text):
    engine = gtts.engine('neural')
    speech = engine.synthesize(text)
    return speech

def main():
    texts = ['This is a text to speech live like an human AI', 'This is the second text', 'This is the third text']
    threads = []
    for text in texts:
        thread = threading.Thread(target=text_to_speech, args=(text,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
