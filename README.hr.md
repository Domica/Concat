[English](README.md) | [Hrvatski](README.hr.md)

<div align="center">
<table width="100%">
  <tr>
    <td align="left" width="120">
      <img src="https://cdn.jsdelivr.net/gh/jub0t/Concat@main/assets/logo-dark.png" alt="Concat" width="100" />
    </td>
    <td align="right">
      <h1>Concat</h1>
      <h3 style="margin-top: -10px;">Uistinu slobodna i open-source cross-platform zamjena za CapCut.</h3>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/jub0t/Concat/releases"><img src="https://img.shields.io/github/downloads/jub0t/concat/total?style=flat&logo=github&logoColor=F8F8F8&label=Downloads&labelColor=000000&color=c6f432" alt="Total Downloads" /></a>
  <a href="https://github.com/jub0t/Concat/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/jub0t/Concat/ci.yml?style=flat&logo=githubactions&logoColor=F8F8F8&label=Build&labelColor=000000" alt="Build Status" /></a>
  <a href="https://github.com/jub0t/Concat/releases"><img src="https://img.shields.io/badge/Version-0.2.3-c6f432?style=flat&logo=semver&logoColor=F8F8F8&labelColor=000000" alt="Concat Version 0.2.3" /></a>
  <a href="https://discord.gg/DVuPfpXfqP"><img src="https://img.shields.io/badge/Discord-Join%20the%20server-5865F2?style=flat&logo=discord&logoColor=F8F8F8&labelColor=000000" alt="Join Concat Discord" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL%20v3-c6f432?style=flat&logo=gnu&logoColor=F8F8F8&labelColor=000000" alt="License: AGPL-3.0-or-later" /></a>
</p>

<img src="https://cdn.jsdelivr.net/gh/jub0t/Concat@main/assets/editor.png" alt="Concat editor" width="100%" />

</div>

---

## O projektu

Concat je sve što koristiš CapCut za. Bez vodenih žigova. Bez plaćanja. Bez pretplata.

Radi u cijelosti na tvom računalu, pokreće ga nativni Rust engine. Instaliraj ga i počni rezati. Bez računa, bez postavljanja.

## Istaknuto

- 🚫 **Bez vodenih žigova.** Bez računa. Bez plaćanja.
- 🔒 **100% lokalno.** Ništa ne napušta tvoje računalo.
- 🎬 **Montaža s više traka.** Nekoliko vremenskih crta po projektu.
- ✂️ **Brzo reži.** Podijeli, obreži, spoji, prijelazi, kontrola brzine.
- 💬 **Automatski titlovi.** Rade na tvom računalu, offline.
- 🗣️ **Pretvorba teksta u govor.** Besplatni lokalni glasovi.
- 🎙️ **Filtri glasa.** Počisti ili se poigraj sa zvukom.
- 📝 **Naslovi i stilizirani tekst.**
- 📦 **Predlošci.** Napravi montažu jednom, koristi je uvijek.
- 🖥️ **macOS, Windows i Linux.** Ista aplikacija svugdje.
- 🌍 **Dvanaest jezika.** Dodaj svoj jednim JSON dokumentom, vidi [TRANSLATING.md](TRANSLATING.md).

## Početak

Concat je trenutno u **Beta verziji (pred-izdanje)**. **Preuzmi** najnoviju verziju sa [Releases](https://github.com/jub0t/Concat/releases).

**Prijava problema:** svako pokretanje zapisuje log, a Settings › About ima gumb koji ga otvara, uz onaj koji kopira informacije o tvom sustavu. Priloži oboje na [issue](https://github.com/jub0t/Concat/issues) i prijava dolazi sa svime što joj treba. Zadnjih deset pokretanja se čuva, tako da je jučerašnje još uvijek tu; ništa se nikamo ne šalje samo od sebe.

**Podržane platforme:**

- ✅ **Windows**
  - ✅ x86_64
- ✅ **macOS** — nepotpisani binarni fajlovi; pokreni:
  `xattr -dr com.apple.quarantine /Applications/Concat.app`
  - ✅ Intel
  - ✅ Silicon
- ✅ **Linux**
  - ✅ ARM
  - ✅ x86_64
- ✅ **Android**
  - ✅ Telefoni
  - ✅ Tableti
- 🧪 **iOS / iPadOS**
  - 🧪 iPhone
  - 🧪 iPad

**Status:** ✅ Podržano · 🚧 U izradi · 🧪 Za testiranje

**Sistemski zahtjevi:**

Concat sve izvodi na tvom računalu, pa hardver postavlja granicu. Stupac minimuma kaže na čemu će se build uopće pokrenuti; stupac preporučenog kaže što čini da montaža u 1080p teče glatko i da izvoz u 4K i titlovi ne budu čekanje.

| | Minimum | Preporučeno |
|---|---|---|
| **CPU** | Bilo koji 64-bitni procesor iz 2013. ili noviji | 6 jezgri ili više |
| **GPU** | Nema. Bez upotrebljivog GPU-a prozor i monitor prelaze na CPU | Bilo koji GPU s Metal (macOS), DirectX 12 (Windows) ili Vulkan (Linux) |
| **RAM** | **4 GB** | **16 GB** za 4K vremenske crte i veće modele za titlove |
| **Pohrana** | **500 MB** za aplikaciju i najmanji model za titlove | **2 GB** za sve opcionalne modele, plus mjesta za projekte i izvoz |

Opcionalni modeli preuzimaju se iz panela postavki pri prvom korištenju i nakon toga više ne trebaju mrežu: automatski titlovi 78 MB do 488 MB ovisno o whisper veličini koju odabereš, pretvorba teksta u govor 132 MB ili 349 MB, izrezivanje osobe 15 MB, izrezivanje objekta 179 MB, i četkica za izrezivanje 40 MB.

## Kako doprinijeti

> [!IMPORTANT]
> Najbolji način da doprineseš jest da uzmeš build sa [Releases](https://github.com/jub0t/Concat/releases) stranice i koristiš ga: pronađi gdje puca, i reci gdje bi moglo biti bolje.
>
> Spreman pisati kod? [CONTRIBUTING.md](./CONTRIBUTING.md) pokriva postavljanje, raspored stabla, provjere koje treba pokrenuti, i kako se doprinosi licenciraju. Želiš umjesto toga napisati efekt, filter ili prijelaz? [EFFECTS.md](./EFFECTS.md) je sve o tome: mapa, manifest, i lanac ili shader, učitani iz tvoje mape s efektima dok aplikacija radi. Pokrećeš Concat iz skripte, servisa ili agenta? [docs/](./docs/README.md) je razvojna referenca za Concat API i njegove transporte: JSON-RPC, gRPC i MCP. [ROADMAP.MD](./ROADMAP.MD) kaže kamo projekt ide, a [ova rasprava](https://github.com/jub0t/Concat/discussions/3) je gdje je najavljen.
> 
> Suradnici mogu slobodno zatražiti `@Contributor` ulogu na Discord serveru, samo pitaj.

## Suradnici

<a href="https://github.com/jub0t/Concat/graphs/contributors">
  <img alt="Contributors" src="https://contrib.rocks/image?repo=jub0t/concat">
</a>

## Star History

<a href="https://www.star-history.com/?repos=jub0t%2Fconcat&type=timeline&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=jub0t/concat&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=jub0t/concat&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=jub0t/concat&type=date&legend=top-left" />
 </picture>
</a>
