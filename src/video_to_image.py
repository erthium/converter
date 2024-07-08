"""
This script is used to convert an image file to another image file.\n
It includes the following functions:
- resize
- resize_by_ratio
- jpg_to_png
- png_to_jpg
- reduce_size
"""

import moviepy.editor as mp
import argparse

def mp4_to_gif(video_path: str, gif_path: str) -> None:
    """
    Converts a video file to a gif file.\n
    video_path: str: The path to the MP4 file.\n
    gif_path: str: The output path to the GIF file.
    """
    try:    
      clip = mp.VideoFileClip(video_path)
      clip.write_gif(gif_path, fps=60)
    except Exception as e:
      print(e)
      print("The video file could not be converted to a gif file.")
    finally:
      print("Closed")
      clip.close()
    

def main():
    parser = argparse.ArgumentParser(description = "Converts a video file to a gif file.")
    parser.add_argument("input", type = str, help = "The path to the MP4 file.")
    parser.add_argument("output", type = str, help = "The output path to the GIF file.")
    args = parser.parse_args()
    mp4_to_gif(args.input, args.output)

if __name__ == "__main__":
   main()