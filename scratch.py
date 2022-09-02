# Filename: scratch.py
# Created By: Mackenly Jones on 07/13/2022
# Web: mackenly.com
# Twitter: @mackenlyjones
import PyATEMMax

switcher = PyATEMMax.ATEMMax()
switcher.ping("127.0.0.1")
alive = switcher.waitForConnection()
print(f'Connected: {alive}')
switcher.setProgramInputVideoSource(0, 2)
switcher.execFadeToBlackME(0)
swsrc = PyATEMMax.ATEMVideoSources
sources = [
    swsrc.input1,
    swsrc.input2,
    swsrc.input3,
    swsrc.input4,
    swsrc.input5,
    swsrc.input6,
    swsrc.input7,
    swsrc.input8,
    swsrc.input9,
    swsrc.input10,
    swsrc.input11,
    swsrc.input12,
    swsrc.input13,
    swsrc.input14,
    swsrc.input15,
    swsrc.input16,
    swsrc.input17,
    swsrc.input18,
    swsrc.input19,
    swsrc.input20,
    swsrc.input21,
    swsrc.input22,
    swsrc.input23,
    swsrc.input24,
    swsrc.input25,
    swsrc.input26,
    swsrc.input27,
    swsrc.input28,
    swsrc.input29,
    swsrc.input30,
    swsrc.input31,
    swsrc.input32,
    swsrc.input33,
    swsrc.input34,
    swsrc.input35,
    swsrc.input36,
    swsrc.input37,
    swsrc.input38,
    swsrc.input39,
    swsrc.input40,
    swsrc.black,
    swsrc.colorBars,
    swsrc.color1,
    swsrc.color2,
    swsrc.mediaPlayer1,
    swsrc.mediaPlayer2,
    swsrc.mediaPlayer3,
    swsrc.mediaPlayer4,
]
for source in sources:
    print(f'{source.value}: {source.name}')
    print(f'\t{switcher.inputProperties[source.value].longName}: Program? {switcher.tally.bySource.flags[source.value].program}\n')
switcher.disconnect()
