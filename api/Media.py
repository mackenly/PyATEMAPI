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
        for bank in range(1, self.switcher.mediaPlayer.stillBanks + 1):
            stills.append({
                "number": bank,
                "fileName": self.switcher.mediaPlayer.stillFile[bank].fileName,
                "isUsed": self.switcher.mediaPlayer.stillFile[bank].isUsed
            })
        for clip in range(1, self.switcher.mediaPlayer.clipBanks + 1):
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
