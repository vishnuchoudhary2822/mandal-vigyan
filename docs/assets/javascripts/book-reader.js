const chapters = [
  ['01', 'परिचय', 'chapters/01-introduction/'], ['02', 'मण्डल क्या है', 'chapters/02-what-is-mandala/'], ['03', 'वेदों के अनुसार ब्रह्माण्ड', 'chapters/03-universe-according-to-vedas/'], ['04', 'नासदीय सूक्त', 'chapters/04-nasadiya-sukta/'], ['05', 'हिरण्यगर्भ', 'chapters/05-hiranyagarbha/'], ['06', 'ब्रह्माण्ड', 'chapters/06-brahmanda/'], ['07', 'चौदह लोक', 'chapters/07-fourteen-lokas/'], ['08', 'भू-मण्डल', 'chapters/08-bhu-mandala/'], ['09', 'सप्त-द्वीप', 'chapters/09-sapta-dvipa/'], ['10', 'मेरु पर्वत', 'chapters/10-meru-mountain/'], ['11', 'ज्योतिर्मण्डल', 'chapters/11-jyotir-mandala/'], ['12', 'सूर्य', 'chapters/12-surya/'], ['13', 'चन्द्र', 'chapters/13-chandra/'], ['14', 'नक्षत्र', 'chapters/14-nakshatra/'], ['15', 'ग्रह', 'chapters/15-graha/'], ['16', 'काल', 'chapters/16-time/'], ['17', 'कल्प', 'chapters/17-kalpa/'], ['18', 'मन्वन्तर', 'chapters/18-manvantara/'], ['19', 'युग', 'chapters/19-yuga/'], ['20', 'पृथ्वी', 'chapters/20-earth/'], ['21', 'समतल पृथ्वी के दावे', 'chapters/21-flat-earth-claims/'], ['22', 'इस्कॉन ब्रह्माण्ड-विज्ञान', 'chapters/22-iskcon-cosmology/'], ['23', 'आधुनिक खगोल-विज्ञान', 'chapters/23-modern-astronomy/'], ['24', 'आकाशगंगा', 'chapters/24-galaxy/'], ['25', 'क्षीर-पथ आकाशगंगा', 'chapters/25-milky-way/'], ['26', 'कृष्ण विवर', 'chapters/26-black-holes/'], ['27', 'डार्क मैटर', 'chapters/27-dark-matter/'], ['28', 'डार्क एनर्जी', 'chapters/28-dark-energy/'], ['29', 'आयाम', 'chapters/29-dimensions/'], ['30', 'चेतना', 'chapters/30-consciousness/'], ['31', 'आत्मा', 'chapters/31-soul/'], ['32', 'वैकुण्ठ', 'chapters/32-vaikuntha/'], ['33', 'गोलोक', 'chapters/33-goloka/'], ['34', 'वैज्ञानिक तुलना', 'chapters/34-scientific-comparison/'], ['35', 'सामान्य भ्रांतियाँ', 'chapters/35-common-misconceptions/'], ['36', 'अक्सर पूछे जाने वाले प्रश्न', 'chapters/36-faqs/'], ['37', 'सन्दर्भ', 'chapters/37-references/'], ['38', 'शब्दावली', 'chapters/38-glossary/'], ['39', 'परिशिष्ट', 'chapters/39-appendix/']
];

let current = 0;
let pageFlip;
const stage = document.querySelector('#bookStage');
const toc = document.querySelector('#bookToc');
const position = document.querySelector('#bookPosition');
const previousButtons = document.querySelectorAll('[data-book-action="previous"], #previousPage');
const nextButtons = document.querySelectorAll('[data-book-action="next"], #nextPage');

function cleanEmbeddedPage(frame) {
  try {
    const doc = frame.contentDocument;
    doc.querySelectorAll('.md-header, .md-tabs, .md-sidebar, .md-footer, .md-content__button, .md-footer-meta').forEach((element) => { element.style.display = 'none'; });
    doc.querySelector('.md-main__inner')?.style.setProperty('margin', '0');
    doc.querySelector('.md-content')?.style.setProperty('max-width', 'none');
  } catch (_) { /* The reader still works while an embedded page is loading. */ }
}

function updateReader(index) {
  current = index;
  const [number, title] = chapters[current];
  position.textContent = `अध्याय ${number} · ${title}`;
  [...toc.children].forEach((button, buttonIndex) => button.setAttribute('aria-current', buttonIndex === current ? 'page' : 'false'));
  previousButtons.forEach((button) => { button.disabled = current === 0; });
  nextButtons.forEach((button) => { button.disabled = current >= chapters.length - 1; });
}

function turnTo(index, corner = 'top') {
  if (!pageFlip || index < 0 || index >= chapters.length || index === current) return;
  const difference = index - current;
  if (Math.abs(difference) === 1) difference > 0 ? pageFlip.flipNext(corner) : pageFlip.flipPrev(corner);
  else pageFlip.flip(index, corner);
}

chapters.forEach(([number, title, path], index) => {
  const button = document.createElement('button');
  button.className = 'book-chapter';
  button.textContent = `${number}. ${title}`;
  button.addEventListener('click', () => turnTo(index));
  toc.append(button);

  const page = document.createElement('article');
  page.className = 'book-page';
  page.dataset.density = index === 0 || index === chapters.length - 1 ? 'hard' : 'soft';
  page.setAttribute('aria-label', `अध्याय ${number}: ${title}`);
  const chapterLabel = document.createElement('p');
  chapterLabel.className = 'book-page-label';
  chapterLabel.textContent = `अध्याय ${number} · ${title}`;
  const frame = document.createElement('iframe');
  frame.title = `अध्याय ${number}: ${title}`;
  frame.loading = index < 3 ? 'eager' : 'lazy';
  frame.src = `../${path}`;
  frame.addEventListener('load', () => cleanEmbeddedPage(frame));
  page.append(chapterLabel, frame);
  stage.append(page);
});

function initialiseBook() {
  if (!window.St?.PageFlip) { position.textContent = 'पुस्तक प्रभाव load नहीं हो सका।'; return; }
  pageFlip = new window.St.PageFlip(stage, {
    width: 640, height: 840, size: 'stretch', minWidth: 300, maxWidth: 1280,
    minHeight: 420, maxHeight: 920, maxShadowOpacity: 0.58, showCover: true,
    mobileScrollSupport: false, drawShadow: true, flippingTime: 900, usePortrait: true,
    showPageCorners: true, disableFlipByClick: false
  });
  pageFlip.loadFromHTML(stage.querySelectorAll('.book-page'));
  pageFlip.on('flip', (event) => updateReader(event.data));
  pageFlip.on('changeOrientation', () => updateReader(pageFlip.getCurrentPageIndex()));
  updateReader(0);
}

previousButtons.forEach((button) => button.addEventListener('click', () => turnTo(current - 1, 'bottom')));
nextButtons.forEach((button) => button.addEventListener('click', () => turnTo(current + 1, 'top')));
document.addEventListener('keydown', (event) => {
  if (event.target.matches('input, textarea, select')) return;
  if (event.key === 'ArrowRight') { event.preventDefault(); turnTo(current + 1, 'top'); }
  if (event.key === 'ArrowLeft') { event.preventDefault(); turnTo(current - 1, 'bottom'); }
});
initialiseBook();
