#!/usr/bin/env python3

import youtube_dl
import sys
import pprint

ytdl = youtube_dl.YoutubeDL({'dump_single_json': True, 'extract_flat': True})

with ytdl:
    result = ytdl.extract_info(sys.argv[1], False, extra_info={'uploader': None})

pprint.pprint(result)
