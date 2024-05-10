import threading
import queue
import speech_recognition as sr


def worker(task_queue):
    while True:
        task_id, task_type, data = task_queue.get()
        print(f'Working on task {task_id} of type {task_type}')

        if task_type == 'file':
            process_audio_file(data)
        elif task_type == 'mic':
            process_microphone_input(data)

        print(f'Finished task {task_id}')
        task_queue.task_done()


def process_audio_file(filename):
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print(f'Audio file text: {text}')


def process_microphone_input(recognizer):
    print("Start speaking.")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    print('End.')
    text = recognizer.recognize_google(audio)
    print(f'Text from microphone: {text}')


if __name__ == '__main__':
    task_queue = queue.Queue()
    recognizer = sr.Recognizer()

    # Starting the worker thread
    threading.Thread(target=worker, args=(task_queue,), daemon=True).start()

    filename = "sample_audio.wav"
    # Queue tasks for processing audio files
    for i in range(2):
        print("Reading audio file...")
        task_queue.put((i, 'file', filename))

    # Queue tasks for processing microphone input
    for i in range(2, 4):
        task_queue.put((i, 'mic', recognizer))

    # Block until all tasks are done
    task_queue.join()
    print('All work completed')
