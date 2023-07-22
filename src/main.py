import pyttsx3
from crochet_parser import crochet_parse_file, read_r

# text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# load and validate pattern
pattern = crochet_parse_file("../json/rocky_the_ram.pattern.json")
num_rs = len(pattern["pattern"]["rs"])
# print(pattern)
# display and speak pattern

for r in range(num_rs):
    engine.say(read_r(pattern, r))
    print()
engine.runAndWait()
