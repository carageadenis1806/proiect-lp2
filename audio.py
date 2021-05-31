import urllib.request
from pydub import AudioSegment
from pydub.playback import play

#introducem fisierul in pydub

beat1 = AudioSegment.from_wav("beat1.wav")

 #se repeta beat-ul de 2 ori

loop = beat1 * 2

# lungimea in milisecunde

length = len(beat1)

# fade time

fade_time = int(length * 0.5)

# fade in/fade out
faded = beat1.fade_in(fade_time).fade_out(fade_time)

#se introduce al doilea beat in pydub

beat2 = AudioSegment.from_wav("beat2.wav")

#se mixeaza cu primul beat

mixed = beat2[:length].overlay(beat1)

filtered = beat2.low_pass_filter(300)

filtered.export("filtered.wav",format="wav")

filtered2 = beat2.high_pass_filter(3000)
filtered2.export("filtered2.wav",format="wav")

#####

song1 = AudioSegment.from_wav("song1.wav")
#impartim melodia in mai multe parti

ten_seconds = 10 * 1000

first_ten_seconds = song1[:ten_seconds]

last_5_seconds = song1[-5000:]

beginning = first_ten_seconds + 6
end = last_5_seconds - 3

concatenate = beginning +  end
concatenate == 15.0

reverse = song1.reverse()
style = beginning.append(end, crossfade=1500)

repeat = style * 2

result = repeat.fade_in(2000).fade_out(3000)
result.export("result.wav",format = "wav")

