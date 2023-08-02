import fridayfunctions as FF
from fridayfunctions import playmusic
import speakandrecognizefunctions as SRF
import datetime


WAKE_WORD = "friday"
USER = "jace"


#def success():
    #print("Command executed succesfully :)")


# GREETINGS ON THE START
FF.wishme()

while True:

    text = SRF.takecommandbackground()

    if text.count(WAKE_WORD) > 0:

        SRF.speak("How may i help you ?")
        print("\nListening....")

        text = SRF.takecommand()

        WISH_STR = ["hello", "hey", "hai", "hi", "hola"]
        for phrase in WISH_STR:
            if phrase in text:
                SRF.speak("Hello" + USER)

        # This is for taking notes
        NOTE_STRS = ["take note", "take a note", "make a note",
                     "write this down", "remember this"]
        for phrase in NOTE_STRS:
            if phrase in text:
                SRF.speak("what would you like me write down")
                note_text = SRF.takecommand()
                FF.note(note_text)
                SRF.speak("Ok i Have taken the note")

        if 'wikipedia' in text:
            FF.wikipediasearch(text)

        if 'open' in text:
            FF.open_programs_websites(text)

        # this is for telling the current time
        TIME_STRS = ["whats the time", "tell the time", "the time"]
        for phrase in TIME_STRS:
            if phrase in text:
                hour = datetime.datetime.now().strftime("%I")
                minute = datetime.datetime.now().strftime("%M%p")
                SRF.speak(f"It's  {hour} {minute} ")

        GOOGLE_STRS = ["search on google",
                       "google search", "search google for"]
        for phrase in GOOGLE_STRS:
            if phrase in text:
                query = text.replace(phrase, "")
                FF.googlesearch(query)

        MUSIC_STRS = ["play music", "start music"]
        for phrase in MUSIC_STRS:
            if phrase in text:
                playmusic()

# This is if u want to exit the program
        EXIT_STRS = ["exit", "go away", "bye bye", "good day", "mute", "talk to you later", ""]
        for phrase in EXIT_STRS:
            if phrase in text:
                exit()

