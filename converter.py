# -*- coding: utf-8 -*-
#                           ██╗██████╗ ██╗           
#                           ██║╚════██╗██║           
#                           ██║ █████╔╝██║           
#                      ██   ██║██╔═══╝ ██║           
#                      ╚█████╔╝███████╗███████╗      
#                       ╚════╝ ╚══════╝╚══════╝      
#                       https://jusdeliens.com
#
# Designed with 💖 by Jusdeliens
# Under CC BY-NC-ND 4.0 licence 
# https://creativecommons.org/licenses/by-nc/4.0/deed.en

import pyanalytx.logger as anx

octave = ['C','D','E','F','G','A','B']
toneLetterToIndex = {'C':-9,'D':-7,'E':-5,'F':-4,'G':-2,'A':0,'B':2}

def toneToFreq(tone:int or str) -> int | None:
    """
    Convert the specified tone into an int frequency. Tone can be either
    - a str for an anglosaxon tone (i.e. A4, D#5, Gb7) 
    - a int for a frequency in Hz (i.e. 440) 
    - a int for a tone index (i.e. 0 for A4, 1 for A#4, 2 for B4 ...) 
    Returns None if error occurs
    """
    toneIndex = None
    if ( type(tone)==str ):
        if ( len(tone)>3):
            anx.warning("⚠️ Incorrect tone. 3 letters max using anglosaxon notation (i.e. A4, D#5, Gb7)")
            return None
        if ( tone[0] not in toneLetterToIndex ):
            anx.warning("⚠️ Incorrect frequency. Use letters C,D,E,F,G,A or B!")
            return None
        toneIndex = toneLetterToIndex[tone[0]]
        if ( tone[1] == '#' ):
            toneIndex += 12*(ord(tone[2])-52)+1
        elif ( tone[1] == 'b' ):
            toneIndex += 12*(ord(tone[2])-52)-1
        else:
            toneIndex += 12*(ord(tone[1])-52)
    elif ( type(tone)==int ):
        if ( tone<0 or tone > 8000 ):
            anx.warning("⚠️ Incorrect frequency. Must be between 110Hz and 8000Hz or in index from 0 to 100!")
            return None
        if ( tone < 100 ):
            toneIndex = tone
    else:
        anx.warning("⚠️ Incorrect tone height. Must be between 110Hz and 8000Hz or in index from 0 to 100 or a str using anglosaxon notation")
        return None
    if ( toneIndex != None ):
        tone = int(440 * pow(2, toneIndex / 12.0))
    return tone