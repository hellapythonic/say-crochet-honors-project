import json
import exceptions
from sys import exit


# TODO: MVC? Worth it?


# conversions from crochet shorthand for the speech engine
STITCH = {
    "ch": "chain",
    "sc": "single crochet",
    "dc": "double crochet",
    "tc": "triple crochet",
    "hdc": "half double crochet"
}


def crochet_parse_file(filename):
    """Parses the *.pattern.json file.

    Returns a json object.

    Throws IOError."""
    try:
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError as e:
                print(e)
                exit(1)
    except IOError as e:
        exit(1)

# TODO: (Jeremy's suggestion: string buffer for concat string) :: Concatenating immutable sequences always results
#  in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime
#  cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below:
#  if concatenating str objects, you can build a list and use str.join() at the end or else write to an io.StringIO
#  instance and retrieve its value when complete.


def read_r(pattern, idx=0) -> str:
    """Reads the round or row.

        Raises exceptions.PatternError."""

    try:
        def read_stitch(stitch_key, stitch_item, repeat=0):
            """Reads the stitch."""
            stitch_say_string = ""
            # print(f"{stitch_key = }, {stitch_item = }")
            if stitch_key in STITCH.keys():
                if isinstance(stitch_item, list):
                    ct = stitch_item[0]
                else:
                    ct = stitch_item
                print(f"{stitch_key} {ct}", end=" ")
                stitch_say_string += f"{STITCH[stitch_key].title()} {ct}"
                if isinstance(stitch_item, list) and len(stitch_item) > 1:
                    # extra instructions like "in 1st chain"
                    print(stitch_item[1])
                    stitch_say_string += " " + stitch_item[1]
                    # print(f"{stitch_key} {ct}")
                else:
                    print()
                stitch_say_string += ". "
                for i in range(1, ct + 1):
                    print(f"[{i}]", end=" ")
                print()
                if repeat:
                    if isinstance(repeat, int):
                        print(f"Repeat {repeat} times.")
                    else:
                        pass
                        # raise exceptions.PatternError

            return stitch_say_string

        def read_repeat(num_repeats, repeat):
            """private function to read the repeat."""
            # print(f"{repeat = }")
            for repeat_key, repeat_item in repeat.items():
                # print(f"before read_stitch:  {repeat_key = }, {repeat_item = } ")
                return read_stitch(repeat_key, repeat_item, repeat=num_repeats) + f"Repeat {num_repeats} times. "

        say_string = ""
        # for r in pattern[pattern]["rs"][idx]:
        for key, item in pattern["pattern"]["rs"][idx].items():
            # round or row
            if key == "r":
                print(f"{key.upper()} {item}")
                say_string = f"Round or row {item}. "

            # stitch
            if key in STITCH.keys():
                say_string += read_stitch(key, item)

            # repeat
            if key == "repeat":
                # print(f"DEBUG: {item[0] = } \n\n\t {item[1] = }")
                say_string += read_repeat(item[0], item[1])

            # stitch count
            if key == "sts":
                print(f"({item} sts)")
                say_string += f"{item} stitches at the end of round or row."

        # print(say_string)  # remove in production code
        return say_string
    except exceptions.PatternError as e:
        exit(e)


if __name__ == "__main__":
    print("This module is not meant to be run stand-alone.")
