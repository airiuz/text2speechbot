import torch
from IPython.display import Audio

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='uz',
                                     speaker='v3_uz')

model.to(torch.device('cpu'))  # gpu or cpu

def get_audio(text):
    audio = model.apply_tts(text=text,
                        speaker='dilnavoz',
                        sample_rate=48000,
                        put_accent=True,
                        put_yo=True)
    return Audio(audio, rate=48000).data