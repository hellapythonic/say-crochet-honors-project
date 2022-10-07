import pyttsx3
from crochet_parser import crochet_parse_file, read_r

# text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 190)

# load and validate pattern
pattern = crochet_parse_file("../json/rocky_the_ram.pattern.json")
num_rs = len(pattern["pattern"]["rs"])

# display and speak pattern
for r in range(num_rs):
    engine.say(read_r(pattern, r))
    engine.runAndWait()
    print()
