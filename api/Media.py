# Filename: Media.py
# Created By: Mackenly Jones on 09/04/2022
# Web: mackenly.com
# Twitter: @mackenlyjones


class Media:
    """
    Media class allows for getting the media state of the switcher's media bank and setting items and properties.
    """

    def __init__(self, switcher):
        """
        Initialize the media class.
        :param switcher: the switcher object that we're getting the media data from.
        """
        self.switcher = switcher

    def get_media(self):
        """
        Get the state of the media bank.
        """
        stills = []
        clips = []
        for bank in range(0, self.switcher.mediaPlayer.stillBanks):
            stills.append({
                "number": bank,
                "fileName": self.switcher.mediaPlayer.stillFile[bank].fileName,
                "isUsed": self.switcher.mediaPlayer.stillFile[bank].isUsed
            })
        for clip in range(0, self.switcher.mediaPlayer.clipBanks):
            clips.append({
                "number": clip,
                "fileName": self.switcher.mediaPlayer.clipSource[clip].fileName,
                "frames": self.switcher.mediaPlayer.clipSource[clip].frames,
                "isUsed": self.switcher.mediaPlayer.clipSource[clip].isUsed
            })
        return {
            "player": [
                {
                    "clipIndex": self.switcher.mediaPlayer.source[1].clipIndex,
                    "stillIndex": self.switcher.mediaPlayer.source[1].stillIndex,
                    "type": {
                        "name": self.switcher.mediaPlayer.source[1].type.name,
                        "value": self.switcher.mediaPlayer.source[1].type.value
                    }
                },
                {
                    "clipIndex": self.switcher.mediaPlayer.source[2].clipIndex,
                    "stillIndex": self.switcher.mediaPlayer.source[2].stillIndex,
                    "type": {
                        "name": self.switcher.mediaPlayer.source[2].type.name,
                        "value": self.switcher.mediaPlayer.source[2].type.value
                    }
                }
            ],
            "stills": {
                "available": self.switcher.mediaPlayer.stillBanks,
                "stills": stills,
            },
            "clips": {
                "available": self.switcher.mediaPlayer.clipBanks,
                "clips": clips,
            },
            "storage": {
                "clipOneMaxLength": self.switcher.mediaPoolStorage.clip1MaxLength,
                "clipTwoMaxLength": self.switcher.mediaPoolStorage.clip2MaxLength
            }
        }

    def set_loop(self, player=1, loop=True):
        """
        Set the loop state of the given player.
        :param player: the player to set the loop state of.
        :param loop: the loop state to set the player to.
        """
        self.switcher.setClipPlayerLoop(player, bool(loop))
        return {
            "player": player,
            "loop": bool(loop)
        }

    def set_playing(self, player=1, playing=True):
        """
        Set the playing state of the given player.
        :param player: the player to set the playing state of.
        :param playing: the playing state to set the player to.
        """
        self.switcher.setClipPlayerPlaying(player, bool(playing))
        return {
            "player": player,
            "playing": bool(playing)
        }

    def set_beginning(self, player=1, beginning=True):
        """
        Set the beginning state of the given player.
        :param player: the player to set the beginning state of.
        :param beginning: if the player should be at the beginning or not.
        """
        self.switcher.setClipPlayerAtBeginning(player, bool(beginning))
        return {
            "player": player,
            "beginning": bool(beginning)
        }

    def set_frame(self, player=1, frame=0):
        """
        Set the frame of the given player.
        :param player: the player to set the frame of.
        :param frame: the frame to set the player to.
        """
        self.switcher.setClipPlayerClipFrame(player, int(frame))
        return {
            "player": player,
            "frame": int(frame)
        }

    def set_type(self, player=1, media_type="still"):
        """
        Set the type of the given player.
        :param player: the player to set the type of.
        :param media_type: the type to set the player to. "clip" or "type"
        """
        self.switcher.setMediaPlayerSourceType(player, media_type)
        return {
            "player": player,
            "type": media_type
        }

    def set_still(self, player=1, still=1):
        """
        Set the still of the given player.
        :param player: the player to set the still of.
        :param still: the still to set the player to.
        """
        self.switcher.setMediaPlayerSourceType(player, "still")
        self.switcher.setMediaPlayerSourceStillIndex(player, int(still))
        return {
            "player": player,
            "still": int(still)
        }

    def set_clip(self, player=1, clip=1):
        """
        Set the clip of the given player.
        :param player: the player to set the clip of.
        :param clip: the clip to set the player to.
        """
        self.switcher.setMediaPlayerSourceType(player, "clip")
        self.switcher.setMediaPlayerSourceClipIndex(player, int(clip))
        return {
            "player": player,
            "clip": int(clip)
        }
