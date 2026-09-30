# design-content

Downloadable third-party content for Voyager Design (`voyager-design`). This repo contains no Voyager Design source code.

Voyager Design fetches these files on demand (`voyager-design content install <pack>`) and checks every file against the SHA-256 its runtime pins. They are published as **GitHub release assets**. The repo itself holds this README, the licence notices, the pack manifests and a workflow that checks the published assets.

| Pack | Releases | Upstream | Licence |
|---|---|---|---|
| Fallback fonts: CJK, colour emoji and 30 per-script Noto faces, see [`packs/fallback-fonts`](packs/fallback-fonts) | `fonts-fallback-<date>` | Noto (notofonts, noto-cjk, noto-emoji) | OFL-1.1 |

[`NOTICES.md`](NOTICES.md) lists every pack and its licences. Each pack's own `NOTICES.md` has per-file attribution and is attached to each of its releases.

## How Voyager Design finds a pack

Each Voyager Design runtime's `runtime.json` lists every on-demand pack by name, with its SHA-256 and an ordered list of mirror URLs. The first mirror is this repository's release. The install tries the mirrors in order and checks every file against the pack's `MANIFEST.json` and the pinned SHA-256, so any host serving the same archive works.

- `VOYAGER_DESIGN_CONTENT_BASE=<url>` replaces the mirrors: the pack is fetched from `<url>/<archive name>` only. Use it for a CDN or an air-gapped mirror. Copy the release assets there under their own names.
- `VOYAGER_OFFLINE=1` forbids every download. Install from a local copy with `--from <archive>`.

## Checks

[`verify-packs`](.github/workflows/verify-packs.yml) runs on every pull request, on pushes to `main`, weekly and by hand. It downloads every archive listed in `packs/*/pack.json` anonymously (no token) and checks:

- the archive's SHA-256 and size;
- its `MANIFEST.json`: every file present with its SHA-256, and the pack's SHA-256 over them;
- that every font file is listed in the pack's `NOTICES.md`, and that the licence file named for it is in the archive.

Run it locally with `python3 scripts/verify_packs.py`.
