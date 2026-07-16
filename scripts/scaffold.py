#!/usr/bin/env python3
"""Generate idempotent, content-free publication templates for MANDAL VIGYAN."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    ("01", "Introduction", "परिचय"), ("02", "What is Mandala", "मण्डल क्या है"),
    ("03", "Universe according to Vedas", "वेदों के अनुसार ब्रह्माण्ड"), ("04", "Nasadiya Sukta", "नासदीय सूक्त"),
    ("05", "Hiranyagarbha", "हिरण्यगर्भ"), ("06", "Brahmanda", "ब्रह्माण्ड"),
    ("07", "Fourteen Lokas", "चौदह लोक"), ("08", "Bhu Mandala", "भू-मण्डल"),
    ("09", "Sapta Dvipa", "सप्त-द्वीप"), ("10", "Meru Mountain", "मेरु पर्वत"),
    ("11", "Jyotir Mandala", "ज्योतिर्मण्डल"), ("12", "Surya", "सूर्य"),
    ("13", "Chandra", "चन्द्र"), ("14", "Nakshatra", "नक्षत्र"), ("15", "Graha", "ग्रह"),
    ("16", "Time", "काल"), ("17", "Kalpa", "कल्प"), ("18", "Manvantara", "मन्वन्तर"),
    ("19", "Yuga", "युग"), ("20", "Earth", "पृथ्वी"), ("21", "Flat Earth Claims", "समतल पृथ्वी के दावे"),
    ("22", "ISKCON Cosmology", "इस्कॉन ब्रह्माण्ड-विज्ञान"), ("23", "Modern Astronomy", "आधुनिक खगोल-विज्ञान"),
    ("24", "Galaxy", "आकाशगंगा"), ("25", "Milky Way", "क्षीर-पथ आकाशगंगा"), ("26", "Black Holes", "कृष्ण विवर"),
    ("27", "Dark Matter", "डार्क मैटर"), ("28", "Dark Energy", "डार्क एनर्जी"), ("29", "Dimensions", "आयाम"),
    ("30", "Consciousness", "चेतना"), ("31", "Soul", "आत्मा"), ("32", "Vaikuntha", "वैकुण्ठ"),
    ("33", "Goloka", "गोलोक"), ("34", "Scientific Comparison", "वैज्ञानिक तुलना"),
    ("35", "Common Misconceptions", "सामान्य भ्रांतियाँ"), ("36", "FAQs", "अक्सर पूछे जाने वाले प्रश्न"),
    ("37", "References", "सन्दर्भ"), ("38", "Glossary", "शब्दावली"), ("39", "Appendix", "परिशिष्ट"),
]
SOURCES = ["rigveda", "yajurveda", "atharvaveda", "samaveda", "upanishads", "bhagavad-gita", "bhagavata-purana", "vishnu-purana", "brahmanda-purana", "padma-purana", "garuda-purana", "surya-siddhanta", "aryabhatiya", "nasa", "esa", "jwst", "hubble", "peer-reviewed-papers"]
ASSETS = ["meru", "lokas", "bhu-mandala", "solar-system", "galaxy", "milky-way", "cosmic-web", "timeline"]

TEMPLATE = """# {number}. {hindi} — {english}

> **स्थिति:** Draft template only · **Citation status:** स्रोत जोड़ना शेष

## परिचय

<!-- इस chapter की सीमा, प्रश्न और पाठक-उद्देश्य लिखें। प्रत्येक तथ्यात्मक दावे का citation दें। -->

## इतिहास

<!-- कालक्रम/पाठ-इतिहास; स्रोत आवश्यक। -->

## संस्कृत स्रोत

<!-- ग्रन्थ, संस्करण, अध्याय/श्लोक और प्रकाशन विवरण। -->

## मूल संस्कृत

<!-- केवल सत्यापित पाठ, edition citation सहित। -->

## हिन्दी अनुवाद

<!-- अनुवादक, edition और citation दें। -->

## शब्दार्थ

| शब्द | व्याकरण/अर्थ | स्रोत |
| --- | --- | --- |
| <!-- --> | <!-- --> | <!-- --> |

## व्याख्या

### पुराणिक कथन

<!-- स्रोत के शब्दों/दावों का सीमित वर्णन; citation आवश्यक। -->

### पारम्परिक व्याख्या

<!-- आचार्य/सम्प्रदाय/टीकाकार का नाम और स्रोत स्पष्ट करें। -->

### आधुनिक वैज्ञानिक दृष्टि

<!-- peer-reviewed अथवा institutional source पर आधारित वर्णन। -->

## वैज्ञानिक विश्लेषण

<!-- विधि, प्रेक्षण, सीमाएँ और evidence level लिखें। असंगत प्रमाण: Evidence Inconclusive. -->

## तुलना तालिका

| विषय | पुराणिक कथन | पारम्परिक व्याख्या | आधुनिक वैज्ञानिक दृष्टि | प्रमाण/स्रोत |
| --- | --- | --- | --- | --- |
| <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> |

## महत्वपूर्ण टिप्पणियाँ

!!! warning "पद्धति"
    आस्था, रूपक और अनुभवजन्य वैज्ञानिक दावे अलग रखें। अपर्याप्त प्रमाण को **Evidence Inconclusive** लिखें।

## आरेख

<!-- [वर्णनात्मक alt text](../diagrams/asset-name.md) और scale/interpretation नोट। -->

## सन्दर्भ

<!-- [^key]: Author. *Title*. Edition/year. DOI, archive ID, या स्थिर URL. -->

## सारांश

<!-- स्रोतों के आधार पर संक्षिप्त निष्कर्ष; नए दावे नहीं। -->

## प्रश्न

1. <!-- स्रोत-आधारित अध्ययन प्रश्न -->
2. <!-- तुलनात्मक/पद्धतिगत प्रश्न -->
"""

def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        path.write_text(text, encoding="utf-8")

def sync_copy(source: Path, destination: Path) -> None:
    """Mirror publication Markdown into MkDocs' required docs directory."""
    content = source.read_text(encoding="utf-8")
    # Canonical chapters live one directory above docs/ and therefore use
    # ../docs/assets/. Published copies live in docs/chapters/ and must use
    # ../assets/ so MkDocs can resolve and publish the SVG files.
    content = content.replace("../docs/assets/", "../assets/")
    destination.write_text(content, encoding="utf-8")

def main() -> None:
    summary = ["# विषय-सूची", "", "यह प्रकाशन-अवसंरचना है; chapter templates में अभी शोध-गद्य नहीं है।", ""]
    for number, english, hindi in CHAPTERS:
        filename = f"{number}-{english.lower().replace(' ', '-')}".replace("--", "-") + ".md"
        path = ROOT / "chapters" / filename
        write_if_missing(path, TEMPLATE.format(number=number, english=english, hindi=hindi))
        summary.append(f"- [{number}. {hindi} — {english}](chapters/{filename})")
    write_if_missing(ROOT / "SUMMARY.md", "\n".join(summary) + "\n")
    write_if_missing(ROOT / "chapters" / "_template.md", TEMPLATE.format(number="XX", english="English title", hindi="हिन्दी शीर्षक"))
    for source in SOURCES:
        write_if_missing(ROOT / "references" / source / "README.md", f"# {source.replace('-', ' ').title()}\n\nCitation metadata और source notes यहाँ जोड़ें।\n")
    for asset in ASSETS:
        write_if_missing(ROOT / "diagrams" / f"{asset}.md", f"# {asset.replace('-', ' ').title()} — placeholder\n\n- **स्थिति:** चित्र जोड़ा जाना शेष\n- **Alt text:** [यहाँ दृश्य का सटीक, तटस्थ वर्णन जोड़ें]\n- **Source/licence:** [अनिवार्य]\n- **Scale/interpretation note:** [अनिवार्य]\n")
        write_if_missing(ROOT / "images" / f"{asset}.md", f"# {asset.replace('-', ' ').title()} image — placeholder\n\n- **स्थिति:** Image asset जोड़ा जाना शेष\n- **Alt text:** [अनिवार्य]\n- **Source/licence:** [अनिवार्य]\n")
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    website_readme = (ROOT / "README.md").read_text(encoding="utf-8").replace("(docs/contributing.md)", "(contributing.md)").replace("(docs/code-of-conduct.md)", "(code-of-conduct.md)")
    hero = "# मण्डल विज्ञान — MANDAL VIGYAN\n\n> **पुराणिक ब्रह्माण्ड-विज्ञान और आधुनिक विज्ञान: स्रोत-आधारित, बहु-दृष्टिकोण शोध-पुस्तक।**"
    website_readme = website_readme.replace(hero, f'<section class="mv-home-hero" markdown>\n\n{hero}\n\n</section>')
    (docs / "index.md").write_text(website_readme, encoding="utf-8")
    sync_copy(ROOT / "SUMMARY.md", docs / "summary.md")
    sync_copy(ROOT / "CONTRIBUTING.md", docs / "contributing.md")
    sync_copy(ROOT / "CODE_OF_CONDUCT.md", docs / "code-of-conduct.md")
    sync_copy(ROOT / "LICENSE", docs / "LICENSE")
    docs_styles = docs / "stylesheets"
    docs_styles.mkdir(exist_ok=True)
    write_if_missing(docs_styles / "print.css", (ROOT / "stylesheets" / "print.css").read_text(encoding="utf-8"))
    docs_chapters = docs / "chapters"
    docs_chapters.mkdir(exist_ok=True)
    for number, english, _ in CHAPTERS:
        filename = f"{number}-{english.lower().replace(' ', '-')}".replace("--", "-") + ".md"
        sync_copy(ROOT / "chapters" / filename, docs_chapters / filename)

if __name__ == "__main__":
    main()
