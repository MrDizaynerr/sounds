import random

from data.atomic.key import Key
from data.atomic.keysenum import KeyEnum
from gamma import Gamma
from synth import Synth
from synth import generate_random_midi_melody_from_sequence


def main0():
    gamma: Gamma = Gamma("F")
    print(gamma.get_minor())


def main1():
    synth: Synth = Synth(["A", "F"])
    intro: list[list[str]] = synth.generate_random_sequence("F", True, tacts=1)
    verse: list[list[str]] = synth.generate_random_sequence("A", True, tacts=2)
    bridge: list[list[str]] = synth.generate_random_sequence("A", True, tacts=1)
    solo1: list[list[str]] = synth.generate_random_sequence("F", True, tacts=4)
    solo2: list[list[str]] = synth.generate_random_sequence("A", True, tacts=2)
    chorus: list[list[str]] = synth.generate_random_sequence("F", True, tacts=2)

    chords: str = f"""Вступление: {intro}
Куплет: 
{verse}
Бридж: 
{bridge}
Припев:
{chorus}
Соло: 
{solo1} 
{solo2}

Аутро:
{intro}
"""
    print(chords)


def main2():
    from midiutil import MIDIFile
    degrees = [60, 62, 64, 65, 67, 69, 71]
    track = 0
    channel = 0
    time = 0
    duration = 1
    tempo = 90
    volume = 100
    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)
    for note in degrees:
        midi.addNote(track, channel, note, time, duration, volume)
        time += 1
    with open("out/test.midi", "wb") as out:
        midi.writeFile(out)


def main3():
    from midiutil import MIDIFile
    chords: list[Key] = [KeyEnum.by_name(x) for x in random.choices(Gamma("E").get_major(), k=4)]
    degrees = generate_random_midi_melody_from_sequence(chords, max_notes_in_beat=30)
    track = 0
    channel = 0
    time = 0
    tempo = 100
    volume = 100
    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    for idx_beat, beat in enumerate(degrees):
        note_length: float = (4 * tempo / 60) / len(beat)
        for idx_note, note in enumerate(beat):
            midi.addNote(track, channel, note, time, note_length, volume)
            time += note_length

    with open("out/test1.midi", "wb") as out:
        midi.writeFile(out)
    print("Generation complete!")


main: list = [main0, main1, main2, main3]

if __name__ == "__main__":
    selected_main: int = 3
    main[selected_main]()
