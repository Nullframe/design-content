# Fallback fonts pack

The CJK, colour emoji and per-script Noto faces that Voyager Design's headless runtime installs on demand (`voyager-design fonts install --fallback`), into `$VOYAGER_HOME/content/fonts/fallback/<id>/`. All OFL-1.1; [`NOTICES.md`](NOTICES.md) lists every font, its upstream, copyright and licence file.

- **Archive:** `voyager-design-fallback-fonts-<id>.tar.gz`, one top folder of the same name holding `MANIFEST.json`, `fonts/noto/` and `wasm-degraded-fonts/`. `<id>` is the first 16 hex digits of the pack's SHA-256, which is computed over its files' `<sha256>  <path>` lines. A pack with different fonts has a different id and archive name, so a published archive is never replaced.
- **Built by** Voyager Design's runtime build (`scripts/build-runtime.mjs` in the Voyager Design repository), from the fonts the app bundles. The pack is the same on every platform.
- **Pinned by** each Voyager Design runtime: its `runtime.json` (`extra.content["fallback-fonts"]`) names the pack's SHA-256 and an ordered list of mirror URLs. The first mirror is this repository's release. The runtime checks every file against the manifest and that SHA-256, whichever host served it.

## Publishing a new archive

1. Take `voyager-design-fallback-fonts-<id>.tar.gz` (and `.sha256`) from a runtime build.
2. Check every font is OFL-1.1 (or another licence that allows redistribution) and that its licence text is in the archive. Add any new font to `NOTICES.md`.
3. Create a release `fonts-fallback-<UTC date>` with the archive, its `.sha256`, its `MANIFEST.json` (as `<stem>.MANIFEST.json`) and `NOTICES.md`.
4. Add the archive to `pack.json` through a pull request. `verify-packs` downloads it anonymously and checks it.
5. Pin its pack SHA-256 and URL in Voyager Design's `packaging/runtime/content.json`.
