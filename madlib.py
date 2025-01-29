import random

def get_word(prompt):
    # Solicit a word from the user - be sure to strip it and turn it to lowercase 
    w = input(prompt).strip().lower()
    return w

def build_story(noun, verb, adjective, person, place):
    templates = [
        # Template 1: Celebrity Scandal 🌟
        f"BREAKING NEWS! {person.upper()} was caught {verb}ing with a {adjective} {noun} at {place.upper()}! "
        f"Witnesses say, 'It screamed *{verb.upper()} MORE!* and flew away.' "
        "The FBI is now involved. #ScandalOfTheYear",

        # Template 2: Alien Invasion 👽
        f"Alert! A {adjective} {noun} invaded {place} and kidnapped {person}! "
        f"To everyone's surprise, {person} taught the aliens to {verb}. "
        "Now they run a intergalactic bakery. Delicious.",

        # Template 3: Royal Romance 👑
        f"Once upon a time, Prince {person} fell in love with a {adjective} {noun} from {place}. "
        f"They vowed to {verb} together forever. The kingdom rejoiced... until the {noun} ate the royal throne. Oops.",

        # Template 4: Sports Drama 🏈
        f"At the {place} Olympics, {person} won gold by {verb}ing a {adjective} {noun}! "
        f"Critics called it 'the weirdest sport ever,' but the crowd chanted, '{verb.upper()}! {verb.upper()}!' "
        "The trophy? A giant {noun}. History was made.",

        # Template 5: Make Your own 
        # GET CREATIVE!
    ]
    return random.choice(templates)

def main():
    print("\n🌟📚 THE ULTIMATE SILLY STORY GENERATOR 2.0 📚🌟\n")
    noun = get_word("Please enter a noun: ")
    verb = get_word("Please enter a verb: ")
    adjective = get_word("Please entre an adjective: ")
    person = get_word("Please enter a person: ")
    place = get_word("Please entre a place: ")
   
    # Print out the Story
    story = build_story(noun, verb, adjective, person, place)
  
    print("\n🔥📖 HERE IS YOUR STORY 📖🔥")
    print("=" * 45)
    print(story)
    print("=" * 45)

if __name__ == "__main__":
    main()
