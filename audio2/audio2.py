import urllib.request
from pydub import AudioSegment
from pydub.playback import play

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