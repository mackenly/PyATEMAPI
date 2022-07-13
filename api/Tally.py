# Filename: Tally.py
# Created By: Mackenly Jones on 07/12/2022
# Web: mackenly.com
# Twitter: @mackenlyjones


class Tally:
    """
    Tally class allows for getting the tally state of the switcher's inputs.
    """

    def __init__(self, switcher):
        """
        Initialize the tally class.
        :param switcher: the switcher object that we're getting the tally from.
        """
        self.switcher = switcher

    def get(self, source):
        """
        Get the tally state of the given source.
        :param source: the source number to get the tally state of.
        :return: string - the tally state of the given source. Can be either 'preview', 'program', or 'none'
        """
        return {
            "source": source,
            "preview": self.switcher.tally.bySource.flags[source].preview,
            "program": self.switcher.tally.bySource.flags[source].program,
        }

    def get_all(self):
        """
        Get the tally state of all sources.
        :return: the tally state of all sources.
        """
        tallies = []
        for source in range(1, self.switcher.tally.byIndex.sources + 1):
            tallies.append(self.get(source))
        return tallies

    def get_program(self):
        """
        Get the current input id of the input currently in program.
        :return: the current input id of the input currently in program. -1 if no input is in program.
        """
        for source in range(1, self.switcher.tally.byIndex.sources + 1):
            if self.get(source)['program']:
                return {
                    "source": source,
                }
        return {
            "source": -1,
        }

    def get_preview(self):
        """
        Get the current input id of the input currently in preview.
        :return: the current input id of the input currently in preview. -1 if no input is in preview.
        """
        for source in range(1, self.switcher.tally.byIndex.sources + 1):
            if self.get(source)['preview']:
                return {
                    "source": source,
                }
        return {
            "source": -1,
        }
