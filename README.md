# Tradutor-legenda-online-python

Python script that translates an English `.srt` subtitle file to Portuguese using Google Translate through the [mtranslate](https://github.com/mouuff/mtranslate) library.

## How it works

`tradutor_legenda_final.py` runs in two passes:

1. **Translate**: reads `legenda_ingles.srt` line by line, sends the text lines to `mtranslate.translate(..., 'pt', 'en')` and writes `legenda_traduzida.srt`. Blank lines and the cue number after them are copied unchanged; the other lines, timestamps included, go through the translator.
2. **Clean up**: re-reads the translated file and fixes the spacing that translation introduces in the timestamps (around digits and `-->`), writing `legenda_final.srt`.

## Usage

```bash
pip install mtranslate
# put the English subtitle next to the script as legenda_ingles.srt
python3 tradutor_legenda_final.py
# result: legenda_final.srt (legenda_traduzida.srt is the intermediate file)
```

File names and languages (`pt` ← `en`) are hard-coded in the script. An internet connection is required.

## License

MIT, see [LICENSE](LICENSE).
