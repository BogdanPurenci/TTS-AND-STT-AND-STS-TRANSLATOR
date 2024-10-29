
# Voice Translator

Acest script Python permite traducerea și funcționalități de text-to-speech (TTS) și speech-to-text (STT) între engleză și română. Utilizatorii pot introduce text sau voce, traduce la limba dorită și asculta traducerea vorbită.

## Funcționalități

- **Traducere Text-to-Speech**: Traduce textul introdus din engleză în română sau invers și îl redă vocal.
- **Traducere Speech-to-Text**: Recunoaște vorbirea în engleză sau română, o traduce în cealaltă limbă și redă traducerea vocală.

## Cerințe

- **Python 3.6+**
- **Pachete**:
  - `speech_recognition`: Pentru recunoașterea cuvintelor vorbite.
  - `gTTS`: Pentru conversia textului în vorbire.
  - `deep_translator`: Pentru traducerea textului între limbi.
  - `pygame`: Pentru redarea fișierelor audio.
- Instalează pachetele necesare:
  ```bash
  pip install speechrecognition gtts deep-translator pygame
  ```

## Utilizare

1. **Rularea Scriptului**:
   ```bash
   python voice_translator.py
   ```
2. **Alegeți o Opțiune**:
   - `1`: Traducere Text-to-Speech
   - `2`: Traducere Speech-to-Text
   - `3`: Ieșire

3. **Text-to-Speech**:
   - Introduceți textul, limba sursă (`en` pentru engleză sau `ro` pentru română) și limba țintă.
   - Textul tradus va fi afișat și redat vocal.

4. **Speech-to-Text**:
   - Alegeți limbile sursă și țintă.
   - Vorbiți în microfon după prompt.
   - Textul recunoscut va fi tradus și redat vocal.

## Prezentare Generală a Codului

- **`text_to_speech(text, lang)`**: Convertește textul tradus în audio și îl redă.
- **`translate_and_speak(text, src_lang, target_lang)`**: Traduce textul și îl transmite către funcția TTS.
- **`speech_to_text(lang)`**: Ascultă pentru intrare vocală, o recunoaște și returnează textul.

## Exemplu

```bash
Alegeți: (1) Text-to-speech, (2) Speech-to-text, (3) Exit: 1
Introduceți textul pentru traducere: Hello, how are you?
Introduceți limba sursă (en pentru engleză, ro pentru română): en
Introduceți limba țintă (en pentru engleză, ro pentru română): ro
Traducere: Bună, cum ești?
```

## Notițe

- Asigurați-vă că microfonul este funcțional dacă folosiți funcția Speech-to-Text.
- Limbile suportate sunt `en` pentru engleză și `ro` pentru română.

## Licență

Acest proiect este open-source și poate fi folosit gratuit.
