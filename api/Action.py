# Filename: Action.py
# Created By: Mackenly Jones on 07/13/2022
# Web: mackenly.com
# Twitter: @mackenlyjones


class Action:
    """
    Action class allows for executing actions on the switcher's specified ME.
    """

    def __init__(self, switcher):
        """
        Initialize the tally class.
        :param switcher: the switcher object that we're getting the tally from.
        """
        self.switcher = switcher
        self.me = 0

    def set_me(self, me):
        """
        Set the ME to use.
        :param me: the ME to use.
        :return: the current ME.
        """
        self.me = int(me)
        return self.me

    def cut(self, source=None):
        """
        Cut the specified input (if provided) from preview to program.
        :param source: source to cut to
        :return: the current input number in preview and program.
        """
        if source is not None:
            self.switcher.setPreviewInputVideoSource(self.me, source)
        self.switcher.execCutME(self.me)
        return {
            "program": self.switcher.programInput[self.me].videoSource.value,
            "preview": self.switcher.previewInput[self.me].videoSource.value,
        }

    def auto(self, source=None):
        """
        Auto mix the specified input (if provided) from preview to program.
        :param source: source to auto mix to.
        :return: current program/preview with the transition state.
        """
        if source is not None:
            self.switcher.setPreviewInputVideoSource(self.me, source)
        self.switcher.execAutoME(self.me)
        return {
            "program": self.switcher.programInput[self.me].videoSource.value,
            "preview": self.switcher.previewInput[self.me].videoSource.value,
            "inTransition": self.switcher.transition[self.me].inTransition,
            "framesRemaining": self.switcher.transition[self.me].framesRemaining,
        }

    def ftb(self):
        """
        Fade to black.
        :return: FTB rate, frames remaining, if it's fully in FTB, and if it's in transition to FTB.
        """
        self.switcher.execFadeToBlackME(self.me)
        return {
            "rate": self.switcher.fadeToBlack[self.me].rate,
            "framesRemaining": self.switcher.fadeToBlack[self.me].state.framesRemaining,
            "fullyBlack": self.switcher.fadeToBlack[self.me].state.fullyBlack,
            "inTransition": self.switcher.fadeToBlack[self.me].state.inTransition,
        }

    def dsk_cut(self, dsk=None):
        """
        Cut to this DSK
        :param dsk: DSK to use
        :return: current program input.
        """
        if dsk is not None:
            self.switcher.setDownstreamKeyerOnAir(dsk, not self.switcher.downstreamKeyer[dsk].onAir)
        return {
            "result": self.switcher.downstreamKeyer[dsk].onAir,
        }

    def dsk_tie(self, dsk=None):
        """
        Tie this DSK
        :param dsk: DSK to use
        :return: current program input.
        """
        if dsk is not None:
            self.switcher.setDownstreamKeyerTie(dsk, not self.switcher.downstreamKeyer[dsk].Tie)
        return {
            "result": self.switcher.downstreamKeyer[dsk].Tie,
        }

    def preview(self, source=None):
        """
        Set the preview input.
        :param source: source to set preview to.
        :return: current preview input.
        """
        if source is not None:
            self.switcher.setPreviewInputVideoSource(self.me, source)
        return {
            "preview": self.switcher.previewInput[self.me].videoSource.value,
        }

    def program(self, source=None):
        """
        Set the program input.
        :param source: source to set program to.
        :return: current program input.
        """
        if source is not None:
            self.switcher.setProgramInputVideoSource(self.me, source)
        return {
            "program": self.switcher.programInput[self.me].videoSource.value,
        }
