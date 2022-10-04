import pyttsx3
from crochet_parser import crochet_parse_file, read_r


engine = pyttsx3.init()
engine.setProperty('rate', 190)

# engine.say("Round 1. Chain 2, 6 single crochet in first chain. 6 stitches total.")

pattern = crochet_parse_file("../json/rocky_the_ram.pattern.json")
num_rs = len(pattern["pattern"]["rs"])

for r in range(num_rs):
    engine.say(read_r(pattern, r))
    engine.runAndWait()
    print()
