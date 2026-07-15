# योगदान मार्गदर्शिका

योगदान देने से पहले issue में प्रस्ताव रखें, विशेषकर किसी धार्मिक पाठ या वैज्ञानिक निष्कर्ष के बारे में।

## लेखन checklist

1. UTF-8 Markdown और chapter template का पालन करें।
2. हर तथ्यात्मक कथन के साथ stable citation दें; primary source को प्राथमिकता दें।
3. `पुराणिक कथन`, `पारम्परिक व्याख्या`, और `आधुनिक वैज्ञानिक दृष्टि` शीर्षक न मिलाएँ।
4. विवादित, अपूर्ण अथवा अपर्याप्त प्रमाण को **Evidence Inconclusive** लिखें।
5. संस्कृत उद्धरण के लिए पाठ-संस्करण, location और अनुवाद की attribution दें।
6. चित्र में alt text, स्रोत, और licence metadata जोड़ें।

PR में `python scripts/validate_markdown.py` और `mkdocs build --strict` चलाएँ।
