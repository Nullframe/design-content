# Notices: fallback fonts pack

The fallback fonts pack (`fallback-fonts`) holds the CJK, colour emoji and per-script Noto faces that Voyager Design's headless runtime doesn't ship. It installs them on demand with `voyager-design fonts install --fallback` (or `voyager-design content install fallback-fonts`).

Every font in it is licensed under the **SIL Open Font License 1.1** (OFL-1.1, https://openfontlicense.org). The OFL allows redistribution, including bundled with software, as long as each font keeps its copyright notice and licence. The fonts are unmodified upstream files, the same bytes the Voyager Design app bundles. Each archive carries the full licence texts:

- `fonts/noto/OFL.txt`: the OFL, with the copyright line of every per-script Noto family below.
- `wasm-degraded-fonts/OFL-NotoSansCJKsc.txt`: the OFL, with Adobe's copyright notice and its Reserved Font Name "Source". The font is unmodified, so the name is kept.
- `wasm-degraded-fonts/OFL-NotoColorEmoji.txt`: the OFL, with Google's copyright notice.

`MANIFEST.json` in each archive is Voyager Design's own file list: every file's SHA-256 and size, the pack's SHA-256 over them, and the families and scripts it covers. It is metadata, not font data.

## Fonts

The copyright is each font's own `name` table entry (ID 0). The licence file is its path inside the archive.

| Family | File | Upstream | Copyright | Licence | Licence file |
|---|---|---|---|---|---|
| Noto Sans Adlam | `fonts/noto/NotoSansAdlam-Regular.ttf` | [notofonts/adlam](https://github.com/notofonts/adlam) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Armenian | `fonts/noto/NotoSansArmenian[wdth,wght]-Regular.ttf` | [notofonts/armenian](https://github.com/notofonts/armenian) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Bengali | `fonts/noto/NotoSansBengali[wdth,wght]-Regular.ttf` | [notofonts/bengali](https://github.com/notofonts/bengali) | Copyright 2025 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Brahmi | `fonts/noto/NotoSansBrahmi-Regular.ttf` | [notofonts/brahmi](https://github.com/notofonts/brahmi) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Devanagari | `fonts/noto/NotoSansDevanagari[wdth,wght]-Regular.ttf` | [notofonts/devanagari](https://github.com/notofonts/devanagari) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Ethiopic | `fonts/noto/NotoSansEthiopic[wdth,wght]-Regular.ttf` | [notofonts/ethiopic](https://github.com/notofonts/ethiopic) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Georgian | `fonts/noto/NotoSansGeorgian[wdth,wght]-Regular.ttf` | [notofonts/georgian](https://github.com/notofonts/georgian) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Gujarati | `fonts/noto/NotoSansGujarati[wdth,wght]-Regular.ttf` | [notofonts/gujarati](https://github.com/notofonts/gujarati) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Gurmukhi | `fonts/noto/NotoSansGurmukhi[wdth,wght]-Regular.ttf` | [notofonts/gurmukhi](https://github.com/notofonts/gurmukhi) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Hanifi Rohingya | `fonts/noto/NotoSansHanifiRohingya-Regular.ttf` | [notofonts/hanifi-rohingya](https://github.com/notofonts/hanifi-rohingya) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Hebrew | `fonts/noto/NotoSansHebrew[wdth,wght]-Regular.ttf` | [notofonts/hebrew](https://github.com/notofonts/hebrew) | Copyright 2024 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Kannada | `fonts/noto/NotoSansKannada[wdth,wght]-Regular.ttf` | [notofonts/kannada](https://github.com/notofonts/kannada) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Khmer | `fonts/noto/NotoSansKhmer[wdth,wght]-Regular.ttf` | [notofonts/khmer](https://github.com/notofonts/khmer) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Lao | `fonts/noto/NotoSansLao[wdth,wght]-Regular.ttf` | [notofonts/lao](https://github.com/notofonts/lao) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Limbu | `fonts/noto/NotoSansLimbu-Regular.ttf` | [notofonts/limbu](https://github.com/notofonts/limbu) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Malayalam | `fonts/noto/NotoSansMalayalam[wdth,wght]-Regular.ttf` | [notofonts/malayalam](https://github.com/notofonts/malayalam) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Mandaic | `fonts/noto/NotoSansMandaic-Regular.ttf` | [notofonts/mandaic](https://github.com/notofonts/mandaic) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Mongolian | `fonts/noto/NotoSansMongolian-Regular.ttf` | [notofonts/mongolian](https://github.com/notofonts/mongolian) | Copyright 2023 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Myanmar | `fonts/noto/NotoSansMyanmar[wdth,wght]-Regular.ttf` | [notofonts/myanmar](https://github.com/notofonts/myanmar) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans NKo | `fonts/noto/NotoSansNKo-Regular.ttf` | [notofonts/nko](https://github.com/notofonts/nko) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Oriya | `fonts/noto/NotoSansOriya[wdth,wght]-Regular.ttf` | [notofonts/oriya](https://github.com/notofonts/oriya) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Samaritan | `fonts/noto/NotoSansSamaritan-Regular.ttf` | [notofonts/samaritan](https://github.com/notofonts/samaritan) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Sinhala | `fonts/noto/NotoSansSinhala[wdth,wght]-Regular.ttf` | [notofonts/sinhala](https://github.com/notofonts/sinhala) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Syriac | `fonts/noto/NotoSansSyriac-Regular.ttf` | [notofonts/syriac](https://github.com/notofonts/syriac) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Tai Tham | `fonts/noto/NotoSansTaiTham-Regular.ttf` | [notofonts/tai-tham](https://github.com/notofonts/tai-tham) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Tamil | `fonts/noto/NotoSansTamil[wdth,wght]-Regular.ttf` | [notofonts/tamil](https://github.com/notofonts/tamil) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Telugu | `fonts/noto/NotoSansTelugu[wdth,wght]-Regular.ttf` | [notofonts/telugu](https://github.com/notofonts/telugu) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Thaana | `fonts/noto/NotoSansThaana-Regular.ttf` | [notofonts/thaana](https://github.com/notofonts/thaana) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Sans Thai | `fonts/noto/NotoSansThai[wdth,wght]-Regular.ttf` | [notofonts/thai](https://github.com/notofonts/thai) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Serif Tibetan | `fonts/noto/NotoSerifTibetan[wght]-Regular.ttf` | [notofonts/tibetan](https://github.com/notofonts/tibetan) | Copyright 2022 The Noto Project Authors | OFL-1.1 | `fonts/noto/OFL.txt` |
| Noto Color Emoji | `wasm-degraded-fonts/NotoColorEmoji.ttf` | [googlefonts/noto-emoji](https://github.com/googlefonts/noto-emoji) | Copyright 2022 Google Inc | OFL-1.1 | `wasm-degraded-fonts/OFL-NotoColorEmoji.txt` |
| Noto Sans CJK SC | `wasm-degraded-fonts/NotoSansCJKsc-Regular.otf` | [notofonts/noto-cjk](https://github.com/notofonts/noto-cjk) | © 2014-2021 Adobe | OFL-1.1 | `wasm-degraded-fonts/OFL-NotoSansCJKsc.txt` |
