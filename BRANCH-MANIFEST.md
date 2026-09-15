# Concat — manifest brancheva i commitova
Zadnje ažurirano: 2026-09-15 · remote: upstream=jub0t/Concat, origin=Domica/Concat

## 1. Mergeano u upstream/main (branch smije obrisati)
| PR | Branch | Commiti (isti SHA-ovi su u upstream/main) | Sadržaj |
|----|--------|-------------------------------------------|---------|
| #61 | translate-hr | 64ba18f, 1261532 | hrvatski locale |
| #62 | pr/art-jpeg-cache | f4b3527 | artwork cache kao project JPEG |
| #63 | pr/media-sort | 1652816, 568be62, 5b68f22, f4a98b6 | sort/filter media bina |
| #64 | pr/export-speed | 79db7e1 | x264 veryfast + ETA |
| #65 | pr/open-project | 5901eb0, 3d68475 | Open Project u File meniju |
| #75 | clear-project-cache | 7e45ae8, 41b8241, 653ebc0, 44a1493 | Clear cache command |
| #76 | relink-missing-media-v2 | 4296aa3, 593aaf1, 80fe0e6, 5e28b5b, 1fe6a7c, 8f8d095, 64eb9b6, 2256594, e7d7776, b4d4062, 8d4ab3f, 6cbf9c4, 585ff72, 22a43f4, 140c470 | relink dialog za missing media |

Izolacija kasnije: `git cherry-pick <sha>` ili `https://github.com/jub0t/Concat/pull/<N>.patch`

## 2. OTVOREN PR — branch NE brisati
| PR | Branch | Sadržaj |
|----|--------|---------|
| #68 | pr_export_fix | audio mix/mux fixevi + CONCAT_ENCODER (19 commitova, vidi niže mapiranje) |

## 3. concat_fixed (osobni sve-u-jednom branch, nikad za upstream PR)
Commiti iznad upstream/main (stanje 2026-09-15):
- 38fbdc6 feat: flip/reverse keyboard shortcuts (H/J/R) + settings toggle — SAMO OVDJE, kandidat za budući PR
- d2bd07c ci: fork nightly workflows — SAMO OVDJE, osobni CI, NIKAD za upstream
- cfcd11c, cf84762 style: cargo fmt
- d0c7835, 1e691d6, 42150dc encoder field + CONCAT_ENCODER
- e4b7dd6, 22b5428, b77fd9c, caefc65 build/mux sitni fixevi
- e8c5b0e, dfb009e, bd0d779, 86dc818, 5157e7d, 02e7737, d978ce8 audio mix/mux fixevi

### Mapiranje stari SHA (pr_export_fix / PR #68) → novi SHA (concat_fixed, nakon rebasea)
| stari | novi | opis |
|-------|------|------|
| faaa3e7 | d978ce8 | filtergraph EOF = graceful end |
| 19ac2ad | 02e7737 | heal timestamp discontinuities |
| a9be455 | 5157e7d | trim audio po sample countu |
| 7adc7e1 | 86dc818 | in-point trim u graph, out-point u Rust |
| 329f763 | bd0d779 | stamp mix input PTS |
| 4889661 | dfb009e | mux po timestampu |
| 40b57e5 | e8c5b0e | compare mux PTS u istoj jedinici |
| 8eaa24c | 42150dc | CONCAT_ENCODER env var |
| e282a79 | 1e691d6 | encoder field u preview_plan shim |
| d71ce86 | caefc65 | makni debug logging |
| e189baf | b77fd9c | nix: openssl + pkg-config |
| f09bdc9 | 22b5428 | preset field duplicate |
| 7b06281 | e4b7dd6 | unused mut |
| ebdf8dc | cf84762 | cargo fmt |
| 579456a | d0c7835 | encoder field u ExportSpec |
| 4323d8d | cfcd11c | cargo fmt |
| 7eac180 | — | izbačen rebaseom (već u upstream) |
| c25356f | — | izbačen rebaseom (već u upstream) |
| 3f17933 | — | SAMO u pr_export_fix! clippy suppress za mergeani kod |

## 4. Pravila
- concat_fixed = osobni build; prije svakog novog featurea: `git fetch upstream && git rebase upstream/main`
- Nakon mergea novog PR-a: dodaj red u tablicu 1 i obriši branch
- Feature za upstream: novi branch iz upstream/main, cherry-pick samo potrebne commite
