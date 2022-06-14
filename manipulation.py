import parselmouth
from parselmouth.praat import call


def manipulate(audio):
    sound = parselmouth.Sound(audio, sampling_frequency=48000)
    manipulation = call(sound, "To Manipulation", 0.001, 15, 600)

    pitch_tier = call(manipulation, "Extract pitch tier")

    call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, 0.5)

    call([manipulation, pitch_tier], "Replace pitch tier")
    sound_octave_up = call(manipulation, "Get resynthesis (overlap-add)")

    return sound_octave_up.values
