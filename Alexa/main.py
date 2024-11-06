# we need to pip install these packages and two more packages that are pyaudio and setuptools

import speech_recognition as sr  # Library for recognizing speech (converting speech to text).
import pyttsx3  # Text-to-speech conversion library.
import pywhatkit  # A library for sending WhatsApp messages at a scheduled time, playing a YouTube video, etc.
import datetime  # Module for working with dates and times
import pyjokes  # Library to get random jokes
import wikipedia  # Library to get information from Wikipedia
import winsound  # Module to access sound-playing capabilities in Windows.
import random  # Library for generating random numbers
import cv2  # OpenCV library for computer vision tasks.

# Recognizing the voice and initializing the program
listener = sr.Recognizer()  # Initialize recognizer for speech recognition
speaker = pyttsx3.init()  # Initialize text-to-speech engine

# Retrieving and setting properties for the speaker
voices = speaker.getProperty('voices')  # Retrieves a list of available voices from the pyttsx3 engine.
speaker.setProperty('voice', voices[0].id)  # Set the voice to the first available voice.

# Setting the speaker to talk
def talk(text):
    speaker.say(text)  # Adds the text to the speech engine's queue.
    speaker.runAndWait()  # Processes the queue and converts the text to speech.

# Setting the listener to listen
def listen():
    try:
        with sr.Microphone() as source:  # Use the default microphone as the audio source
            print('listening...')  # Indicate that the program is listening
            voice = listener.listen(source)  # Listen for the first phrase and extract it into audio data
            command = listener.recognize_google(voice)  # Recognize speech using Google Web Speech API
            command = command.lower()  # Convert the command to lower case for consistency
            talk("Hii There ! Let me help you. You said"+ command)
            print(f"You said: {command}")  # Print the recognized command
            return command  # Return the recognized command
    except Exception as e:
        print("Sorry, I could not understand. Please say that again.")  # Print an error message
        return ""  # Return an empty string if there was an error

# Define the main function to run the assistant
def run():
    command = listen()  # Get the voice command from the user

    if "play" in command:
        # If the command includes "play", play a song on YouTube
        song = command.replace('play', '').strip()  # Remove "play" from the command and strip any extra spaces
        print('playing ' + song)  # Print the song being played
        talk('playing ' + song)  # Speak out the song being played
        pywhatkit.playonyt(song)  # Play the song on YouTube

    elif "whatsapp" in command:
        # If the command includes "whatsapp", send a WhatsApp message
        talk('Write the number')  # Prompt for the phone number
        number = input("Write the number: ")  # Get the phone number from the user
        talk('Write the message')  # Prompt for the message
        message = input("Write the message: ")  # Get the message from the user
        talk('Write the hour (24 hour format)')  # Prompt for the hour
        hour = int(input("Write the hour: "))  # Get the hour from the user
        talk('Write the minutes')  # Prompt for the minutes
        minutes = int(input("Write the minutes: "))  # Get the minutes from the user
        pywhatkit.sendwhatmsg(number, message, hour, minutes)  # Send the WhatsApp message at the specified time

    elif "who is" in command:
        # If the command includes "who is", provide information from Wikipedia
        person = command.replace('who is', '').strip()  # Remove "who is" from the command and strip any extra spaces
        info = wikipedia.summary(person, 4)  # Get a summary of the person from Wikipedia
        print(info)  # Print the information
        talk(info)  # Speak out the information

    elif "joke" in command:
        # If the command includes "joke", tell a joke
        joke = True  # Initialize a flag to keep telling jokes
        while joke:
            Joke = pyjokes.get_joke()  # Get a random joke
            print(Joke)  # Print the joke
            talk(Joke)  # Speak out the joke
            commandJoke = listen()  # Listen for any command after telling the joke
            if "no more" in commandJoke:
                talk('OK')  # If the command is "no more", stop telling jokes
                joke = False  # Set the flag to False to exit the loop
                break

    elif "camera" in command:
        # If the command includes "camera", open the camera
        camera = cv2.VideoCapture(0)  # Open the default camera
        while camera.isOpened():
            ret, frame1 = camera.read()  # Read the first frame
            ret, frame2 = camera.read()  # Read the second frame
            diff = cv2.absdiff(frame1, frame2)  # Compute the absolute difference between the two frames
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)  # Convert the difference to grayscale
            _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)  # Apply a binary threshold to the grayscale image
            dilated = cv2.dilate(thresh, None, iterations=3)

            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find movements in the thresholded image

            for c in contours:
                if cv2.contourArea(c) < 5000:
                    continue  # Ignore small contours
                x, y, w, h = cv2.boundingRect(c)  # Get the bounding box for the contour
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a rectangle around the contour (x,y) are the cordinates of top-left and other is of bottom-right
                winsound.PlaySound('alert.wav', winsound.SND_ASYNC)  # Play a sound asynchronously when motion is detected

            if cv2.waitKey(10) == ord('k'):
                break  # Break the loop if 'k' key is pressed
            cv2.imshow("Kunal's Cam", frame1)  # Show the frame with the detected motion

    else:
        # If the command doesn't match any predefined commands, perform a web search
        search = command  # Use the command as the search query
        talk('please wait')  # Indicate that the program is performing the search
        print('please wait...')  # Print a waiting message
        pywhatkit.search(search)  # Perform a web search using the command

run()  # Run the assistant
