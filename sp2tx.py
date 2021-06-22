# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import speech_recognition as sr
END_PHRASE = 'پایان'


# %%
def get_audio():
    r=sr.Recognizer()  
    r.dynamic_energy_adjustment_damping      
    with sr.Microphone(device_index=1) as source:       
        r.adjust_for_ambient_noise(source)
        print ('Say Something')
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language = 'fa-IR')
        except:
            return 'متوجه نشدم'


# %%
while True:
    print(f'اگه میخوای خارج شی بگو "{END_PHRASE}"')
    print('دارم بهت گوش میدم')
    text = get_audio()
    print(text)
    if text.find(END_PHRASE)==0:
        print('خدافظ')
        break


