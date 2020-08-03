# made by aayush swodari
import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search edureka:search youtube]')
    print('speak now')
    audio = r3.listen(source)

if 'edureka' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)
    try:
        get = r2.recognize_google(audio)
        print(get)
        wb.get().open_new(url + get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

        '''

with sr.Microphone() as source:  # using microphone as source aayush
    print('search anything on youtube')
    print('speak now')  # prompting user to speak aayush
    audio2 = r3.listen(source)  # listening the speakers voice comming from source or mics aayush

url2 = 'https://www.youtube.com/results?search_query='  # giving url aayush

try:  # giving try
    get2 = r2.recognize_google(audio2)  # converting speech to text and assigning to varriable aayush
    print(get2)
    wb.get().open_new(url2 + get2)  # opening browser and searching query aayush
except sr.UnknownValueError:  # if unknown vale error occured then printing error aayush
    print('error')
except sr.RequestError:
    print('failed')
    '''

# for searching website in webbrowser aayush

'''

with sr.Microphone() as source:  # source
    print('search any website name')  # prmpting aayush
    print('speak now')
    audio3 = r3.listen(source)  # listening speech aayush

if 'facebook' in r2.recognize_google(audio3):  # if user speak facebook aayush
    r2 = sr.Recognizer()
    url3 = 'www.facebook.com'  # url aayush
    try:
        print(r2.recognize_google(audio3))  # converting aayush
        wb.get().open_new(url3)  # new webbrowser opening and searching url3 aayush

        # error exception aayush
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')
# if user search instagram aayush
# same as facebbok code aayush
 
elif 'instagram' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.instagram.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')

elif 'youtube' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.youtube.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')
elif 'amazon' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.amazon.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')

elif 'google' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.google.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')

elif 'daraz' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.daraz.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')

elif 'twitter' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.twitter.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed')

elif 'gmail' in r2.recognize_google(audio3):
    r2 = sr.Recognizer()
    url3 = 'www.gmail.com'
    try:
        print(r2.recognize_google(audio3))
        wb.get().open_new(url3)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError:
        print('failed') '''
