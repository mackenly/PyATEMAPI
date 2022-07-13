# Filename: Action.py
# Created By: Mackenly Jones on 07/13/2022
# Web: mackenly.com
# Twitter: @mackenlyjones


class Action:
    """
    Action class allows for executing actions on the switcher's specified ME.
    """

    def __init__(self, switcher, me=0):
        """
        Initialize the tally class.
        :param switcher: the switcher object that we're getting the tally from.
        """
        self.switcher = switcher
        self.me = me

    def cut(self):
        """
        Cut the current preview to program.
        :return: the current input number in preview and program.
        """
        self.switcher.execCutME(self.me)
        return {
            "program": self.switcher.programInput[self.me].videoSource,
            "preview": self.switcher.previewInput[self.me].videoSource,
        }

    def cut(self, source):
        """
        Cut the specified input from preview to program.
        :param source: source to cut to
        :return: the current input number in preview and program.
        """
        self.switcher.setPreviewInputVideoSource(self.me, source)
        self.switcher.execCutME(self.me)
        return {
            "program": self.switcher.programInput[self.me].videoSource,
            "preview": self.switcher.previewInput[self.me].videoSource,
        }

    def auto(self):
        """
        Auto mix the current preview to program.
        :return: current program/preview with the transition state.
        """
        self.switcher.execAutoME(self.me)
        return {
            "program": self.switcher.programInput[self.me].videoSource,
            "preview": self.switcher.previewInput[self.me].videoSource,
            "inTransition": self.switcher.transition[self.me].inTransition,
            "framesRemaining": self.switcher.transition[self.me].framesRemaining,
        }

    def auto(self, source):
        """
        Auto mix the specified input from preview to program.
        :param source: source to auto mix to.
        :return: current program/preview with the transition state.
        """
        self.switcher.setPreviewInputVideoSource(self.me, source)
        self.switcher.execAutoME(self.me)
        return {
            "program": self.switcher.programInput[self.me].videoSource,
            "preview": self.switcher.previewInput[self.me].videoSource,
            "inTransition": self.switcher.transition[self.me].inTransition,
            "framesRemaining": self.switcher.transition[self.me].framesRemaining,
        }

    def ftb(self):
        """
        Fade to black.
        :return: FTB rate, frames remaining, if it's fully in FTB, and if it's in transition to FTB.
        """
        self.switcher.execAutoME(self.me)
        return {
            "rate": self.switcher.fadeToBlack[self.me].rate,
            "framesRemaining": self.switcher.fadeToBlack[self.me].state.framesRemaining,
            "fullyBlack": self.switcher.fadeToBlack[self.me].state.fullyBlack,
            "inTransition": self.switcher.fadeToBlack[self.me].state.inTransition,
        }
