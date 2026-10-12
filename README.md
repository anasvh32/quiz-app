# Quiz App

Barname-ye azmoon-e khat-e farman ke soal ro az file JSON mikhoone, javab migire, va natije ro zakhire mikone.

## Ejra

```
python quiz.py
```

## Fayl-ha

- questions.json: soalat-e azmoon
- quiz.py: ravabet-e khat-e farman (faghat input va print)
- models.py: shekl-e dade-ha (kelas-e Question)
- question.py: khandan va check-e soalat
- grading.py: tashih-e javab
- storage.py: zakhire-ye natije
- results.json: natije-ye zakhire-shode (khodkar sakhte mishe)

## Vizhegi-ha

- Mahdoodiyat-e zamani: 120 sanie baraye kol-e azmoon
- Modiriyat-e khata: agar file soalat peyda nashe ya kharab bashe, payame ghabel-fahm mide
- Namayesh-e soalhaye ghalat be hamrah javab-e dorost, dar payan-e azmoon
- Soal-e chandgozine-i: gozine-ha zir-e soal ba shomare miyan va karbar shomare ya matn-e gozine ro minevise
- Check-e soal-e tekrari: agar yek soal do bar dar questions.json bashe, barname khata mide

## Ezafe kardan-e soal

Har soal dar questions.json yek object ast. Soal-e matni:

```json
{"question": "Paytakht Iran kojast?", "answer": "Tehran"}
```

Soal-e chandgozine-i (jawab, matn-e gozine-ye dorost ast):

```json
{"question": "Paytakht Fransa kodoom ast?", "kind": "choice", "choices": ["Landan", "Paris", "Roum"], "answer": "Paris"}
```