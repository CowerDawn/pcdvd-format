from pydub import AudioSegment
import os

def convert_to_pcdvd(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        return

    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return

    audio = audio.set_frame_rate(8000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(1)

    try:
        audio.export(output_file, format="mp3", bitrate="8k")
    except Exception as e:
        print(f"Error exporting audio file: {e}")
        return

def convert_to_mp3(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        return

    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return

    try:
        audio.export(output_file, format="mp3", bitrate="192k")
    except Exception as e:
        print(f"Error exporting audio file: {e}")
        return

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python convert_audio.py <input file> <output file> <mode: pcdvd or mp3>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    mode = sys.argv[3]

    if mode == "pcdvd":
        convert_to_pcdvd(input_file, output_file)
    elif mode == "mp3":
        convert_to_mp3(input_file, output_file)
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)

    print(f"Conversion completed: {input_file} -> {output_file}")
