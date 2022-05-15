import asyncio
import os
import sys
import json
import anitopy
import time
from bot import ffmpeg
from subprocess import call, check_output
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from subprocess import Popen, PIPE

async def encode(filepath):
    basefilepath, extension = os.path.splitext(filepath)
    output_filepath = basefilepath + "R136A1_Encodes" + ".mkv"
    nam = output_filepath.replace("_", " ")
    nam = nam.replace(".", " ")
    nam = nam.replace("/bot/downloads/", "")
    nam = nam + '.mkv'
    new_name = anitopy.parse(nam)
    anime_name = new_name["anime_title"]
    joined_string = f"[{anime_name}]"
    if "anime_season" in new_name.keys():
      animes_season = new_name["anime_season"]
      joined_string = f"{joined_string}" + f" [Season {animes_season}]"
    if "episode_number" in new_name.keys():
      episode_no = new_name["episode_number"]
      joined_string = f"{joined_string}" + f" [Episode {episode_no}]"
    og = joined_string + " [@Cinema_Dudes]" + ".mkv"
    fmd = '-preset ultrafast -map 0:v -map 0:a -c:v copy -c:a copy -ss 00:30 -t 60'
    call(['ffmpeg', '-i', filepath] + fmd.split() + [output_filepath])
    return output_filepath, og

def get_thumbnail(in_filename, path, ttl):
    out_filename = 'thumb1.jpg'
    cmd = '-map 0:v -ss 00:20 -frames:v 1'
    call(['ffmpeg', '-i', in_filename] + cmd.split() + [out_filename])
    return out_filename
    except:
      pass 
  
def get_duration(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("duration"):
      return metadata.get('duration').seconds
    else:
      return 0

def get_width_height(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("width") and metadata.has("height"):
      return metadata.get("width"), metadata.get("height")
    else:
      return 1280, 720
