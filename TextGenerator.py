from requests import post
from .objects import *

class TextGenerator:
    _post = post
    _headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    @classmethod
    def style(cls) -> Style:
        style_case = {
            'aesthetic': 'aesthetic',
            'ancient': 'ancient',
            'arabian_night': 'arabian-night',
            'asian': 'asian',
            'black_bracket': 'black-bracket',
            'black_square': 'black-square',
            'bold': 'bold',
            'bold_gothic': 'bold-gothic',
            'bold_italic': 'bold-italic',
            'bold_script': 'bold-script',
            'bubble': 'bubble',
            'chinese': 'chinese',
            'currency': 'currency',
            'double_line': 'double-line',
            'double_struck': 'double-struck',
            'eastern': 'eastern',
            'efiopiya': 'efiopiya',
            'emoji': 'emoji',
            'fairy_tale': 'fairy-tale',
            'glyphs': 'glyphs',
            'gothic': 'gothic',
            'greek': 'greek',
            'indian': 'indian',
            'italic': 'italic',
            'kanadskiy_slog': 'kanadskiy-slog',
            'monospace': 'monospace',
            'old_italic': 'old-italic',
            'runy': 'runy',
            'script': 'script',
            'small_capital': 'small-capital',
            'smooth_curve': 'smooth-curve',
            'square': 'square',
            'squiggle': 'squiggle',
            'strike': 'strike',
            'tilde_strike': 'tilde-strike',
            'underline': 'underline',
            'upsidedown': 'upsidedown',
            'white_bracket': 'white-bracket'
        }
        return Style(**style_case)

    @classmethod
    def generate_text(cls, text: str, style: str):
        return cls._post(url = f'https://textgenerator.ru/font/{style}/ajax',
                                data = {'text': text},
                                headers = cls._headers).text