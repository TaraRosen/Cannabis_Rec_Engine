def color(x):
    #effect colors:
    if x == 'happy':
        return 'background-color: #5F9F9F'
    elif x == 'relaxed':
        return 'background-color: #C0D9D9'
    elif x == 'euphoric':
        return 'background-color: #79CDCD'
    elif x == 'uplifted':
        return 'background-color: #66CCCC'
    elif x == 'creative':
        return 'background-color: #37FDFC'
    elif x == 'energetic':
        return 'background-color: #00CDCD'
    elif x == 'focused':
        return 'background-color: #39B7CD'
    elif x == 'aroused':
        return 'background-color: #9AC0CD'
    elif x == 'sleepy':
        return 'background-color: #0099CC'
    elif x == 'hungry':
        return 'background-color: #6996AD'
    elif x == 'giggly':
        return 'background-color: #87CEFF'
    elif x == 'talkative':
        return 'background-color: #74BBFB'

    #medical colors:
    elif x == 'stress':
        return 'background-color: #458B00'
    elif x == 'depression':
        return 'background-color: #66CD00'
    elif x == 'pain':
        return 'background-color: #9CBA7F'
    elif x == 'insomnia':
        return 'background-color: #659D32'
    elif x == 'fatigue':
        return 'background-color: #BCED91'
    elif x == 'headaches':
        return 'background-color: #CFDBC5'
    elif x == 'eyepressure':
        return 'background-color: #567E3A'
    elif x == 'lackofappetite':
        return 'background-color: #84BE6A'
    elif x == 'inflammation':
        return 'background-color: #93DB70'
    elif x == 'cramps':
        return 'background-color: #86C67C'
    elif x == 'musclespasms':
        return 'background-color: #63AB62'
    elif x == 'nausea':
        return 'background-color: #90EE90'
    elif x == 'spasticity':
        return 'background-color: #00CD00'
    elif x == 'seizures':
        return 'background-color: #F0FFF0'

    #negative colors:
    elif x == 'drymouth':
        return 'background-color: #EED2EE'
    elif x == 'dryeyes':
        return 'background-color: #DB70DB'
    elif x == 'anxious':
        return 'background-color: #CD00CD'
    elif x == 'dizzy':
        return 'background-color: #FF00FF'
    elif x == 'paranoid':
        return 'background-color: #B5509C'
    elif x == 'headache':
        return 'background-color: #CDB5CD'

    #flavor colors:
    elif x == 'earthy':
        return 'background-color: #8B6508'
    elif x == 'sweet':
        return 'background-color: #ee918d'
    elif x == 'citrus':
        return 'background-color: #FFE700'
    elif x == 'berry':
        return 'background-color: #9b4466'
    elif x == 'diesel':
        return 'background-color: #696969'
    elif x == 'lemon':
        return 'background-color: #FFF44F'
    elif x == 'pine':
        return 'background-color: #01796f'
    elif x == 'blueberry':
        return 'background-color: #4f86f7'
    elif x == 'flowery':
        return 'background-color: #f4bfc7'
    elif x == 'pungent':
        return 'background-color: #808080'
    elif x == 'woody':
        return 'background-color: #554545'
    elif x == 'grape':
        return 'background-color: #6f2da8'
    elif x == 'spicy/herbal':
        return 'background-color: #FF0000'
    elif x == 'skunk':
        return 'background-color: #808080'
    elif x == 'cheese':
        return 'background-color: #FFF8DC'
    elif x == 'tropical':
        return 'background-color: #ff8aa1'
    elif x == 'orange':
        return 'background-color: #FFA500'
    elif x == 'pineapple':
        return 'background-color: #563c0d'
    elif x == 'strawberry':
        return 'background-color: #d53032'
    elif x == 'apple':
        return 'background-color: ##ff0800'
    elif x == 'chemical':
        return 'background-color: #778899'
    elif x == 'mango':
        return 'background-color: #ffcd48'
    elif x == 'pepper':
        return 'background-color: #2F4F4F'
    elif x == 'lavender':
        return 'background-color: #E6E6FA'
    elif x == 'coffee':
        return 'background-color: #6f4e37'
    elif x == 'mint':
        return 'background-color: #98ff98'
    elif x == 'honey':
        return 'background-color: #a98307'
    elif x == 'lime':
        return 'background-color: #00FF00'
    elif x == 'grapefruit':
        return 'background-color: #edadaa'
    elif x == 'vanilla':
        return 'background-color: #f3e5ab'
    elif x == 'sage':
        return 'background-color: #77815c'
    elif x == 'butter':
        return 'background-color: #fdf6c5'
    elif x == 'nutty':
        return 'background-color: #cd9141'
    elif x == 'bluecheese':
        return 'background-color: #87CEEB'
    elif x == 'tobacco':
        return 'background-color: #6d5843'
    elif x == 'plum':
        return 'background-color: #DDA0DD'
    elif x == 'pear':
        return 'background-color: #d1e231'
    elif x == 'violet':
        return 'background-color: #9400D3'
    elif x == 'tar':
        return 'background-color: #383838'
    elif x == 'menthol':
        return 'background-color: #c1f9a2 '
    elif x == 'ammonia':
        return 'background-color: #FFFF33'
    elif x == 'rose':
        return 'background-color: #ff007f '
    elif x == 'tea':
        return 'background-color: #832400'
    elif x == 'peach':
        return 'background-color: #ffe5b4'
    elif x == 'apricot':
        return 'background-color: #fbceb1'
    elif x == 'chestnut':
        return 'background-color: #954535'
    elif x == 'treefruit':
        return 'background-color: #8db600'

    #type colors:
    elif x == 'sativa':
        return 'background-color: #cc5500'
    elif x == 'indica':
        return 'background-color: #800080'
    elif x == 'hybrid':
        return 'background-color: #758b72'

    #none and strain colors:xz
    elif x == 'none':
        return 'background-color: black'
    else:
        return 'background-color: white'
