# मण्डल विज्ञान — MANDAL VIGYAN

> **पुराणिक ब्रह्माण्ड-विज्ञान और आधुनिक विज्ञान: स्रोत-आधारित, बहु-दृष्टिकोण शोध-पुस्तक।**

यह मुक्त-स्रोत परियोजना हिन्दी में एक शोध-पुस्तक, प्रलेखन वेबसाइट, प्रिंट/PDF और EPUB संस्करण बनाने का Markdown-first ढाँचा है। यह repository अभी जानबूझकर केवल प्रकाशन-अवसंरचना और chapter templates रखती है; इसे दावों या निष्कर्षों से भरा हुआ ग्रंथ न समझें।

## सिद्धांत

- प्रत्येक कथन के साथ सत्यापनीय स्रोत दें।
- **पुराणिक कथन**, **पारम्परिक व्याख्या**, और **आधुनिक वैज्ञानिक दृष्टि** अलग-अलग रखें।
- अनिश्चित प्रमाण को `Evidence Inconclusive` के रूप में चिह्नित करें।
- आस्था या दार्शनिक व्याख्या को वैज्ञानिक तथ्य के रूप में प्रस्तुत न करें।
- संस्कृत मूलपाठ के साथ संस्करण, अध्याय/श्लोक और अनुवादक का विवरण अनिवार्य है।

## स्थानीय पूर्वापेक्षाएँ

Python 3.11+, `pip install -r requirements.txt`, और PDF/EPUB के लिए [Pandoc](https://pandoc.org/)।

```bash
python scripts/validate_markdown.py
mkdocs serve
python scripts/build_book.py
```

निर्मित सामग्री `site/`, `pdf/mandal-vigyan.pdf` और `epub/mandal-vigyan.epub` में आती है।

## संरचना

- `chapters/` — क्रमांकित अध्याय और उनका एक-समान शोध template
- `references/` — स्रोत-वर्गों के लिए citation metadata स्थान
- `diagrams/` और `images/` — चित्रों के licences सहित assets
- `appendix/` — परिशिष्ट और editorial policies
- `scripts/` — validation और publication builds
- `.github/workflows/` — CI और GitHub Pages deployment

## योगदान

कृपया [योगदान मार्गदर्शिका](docs/contributing.md) और [आचार संहिता](docs/code-of-conduct.md) पढ़ें। सभी योगदान UTF-8 Markdown में, citations के साथ, और source-separation policy का पालन करते हुए करें।

## लाइसेंस

पाठ और मूल चित्र [CC BY-SA 4.0](LICENSE) के अंतर्गत हैं, जब तक किसी asset की अपनी licence file अन्यथा न कहे।
