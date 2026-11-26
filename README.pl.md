# Umiejętności marketingowe dla agentów AI

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

<!-- generated:total:start -->54<!-- generated:total:end --> umiejętności (skills), dzięki którym Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Amp, Oh My Pi i inni agenci wykonują pracę marketingową porządnie: optymalizacja konwersji, copywriting, SEO i widoczność w odpowiedziach AI, reklamy płatne, analityka, ceny, e-maile cyklu życia klienta, outbound, badania i publikacja w mediach społecznościowych.

Każda umiejętność to zwykły folder z plikiem `SKILL.md` w otwartym formacie [Agent Skills](https://agentskills.io/specification). Agent czyta krótki opis każdej umiejętności, ładuje pełną instrukcję dopiero wtedy, gdy twoje polecenie pasuje, a szczegóły dociąga na żądanie. Nie potrzeba serwera ani konta.

[English README](README.md)

## Instalacja

Jedna komenda, dowolny obsługiwany agent (wymaga Node.js 22.20 lub nowszego):

```bash
npx skills add SyncGrowth/marketing-skills
```

Narzędzie `skills` należy do Vercela i wysyła anonimową telemetrię instalacji do skills.sh. Ustaw `DISABLE_TELEMETRY=1` przed poleceniem, żeby ją wyłączyć, albo skopiuj foldery ręcznie.

Wybrane umiejętności albo wybrany agent:

```bash
npx skills add SyncGrowth/marketing-skills --skill cro --skill copywriting
npx skills add SyncGrowth/marketing-skills -a claude-code -a codex
```

Wtyczka Claude Code:

```text
/plugin marketplace add SyncGrowth/marketing-skills
/plugin install syncgrowth-marketing-skills@syncgrowth
```

Ręczne kopiowanie i tabela folderów dla każdego agenta: [README po angielsku](README.md#install).

## Pierwsze pięć minut

1. Napisz agentowi: *„Przygotuj kontekst marketingowy produktu dla tego projektu”*. Umiejętność `product-marketing` zada pytania i zapisze plik `.agents/product-marketing.md`. Pozostałe umiejętności czytają go, zanim zapytają o cokolwiek.
2. Potem pisz zwykłym językiem. Odpowiednia umiejętność załaduje się sama: *„Dlaczego strona z cennikiem nie konwertuje?”* uruchamia `cro`, *„Czy wynik tego testu A/B jest wiarygodny?”* uruchamia `ab-testing`, *„Zaplanuj wysyłkę zatwierdzonych postów na przyszły tydzień”* uruchamia `social-publishing`.

Pełna lista umiejętności z opisami: [English README](README.md#the-skills). Umiejętności są po angielsku, ale agent odpowiada w języku, w którym do niego piszesz.

## Skąd to pochodzi

To wyselekcjonowana i sprawdzona dystrybucja projektu [marketingskills](https://github.com/coreyhaines31/marketingskills) Coreya Hainesa na licencji MIT. Zdecydowana większość pracy w 53 przejętych umiejętnościach należy do niego i jego współautorów, a wskazania źródeł, na których się opierał, zostawiliśmy bez zmian. Od siebie dodaliśmy:

- przypięty, sprawdzony stan upstreamu (commit `8fd2fca` z 2026-11-23) oraz spis pochodzenia każdej umiejętności w [docs/PROVENANCE.md](docs/PROVENANCE.md),
- neutralne porady o narzędziach: usunęliśmy miejsca sponsorowane i wzmianki o produktach opiekuna upstreamu razem z oznaczeniami i poleceniami, by o nich wspominać,
- automatyczną kontrolę formatu i ukrytych treści w CI,
- jedną własną umiejętność: `social-publishing`.

Nie jesteśmy powiązani z Coreyem Hainesem ani z osobami wymienionymi w `marketing-council` i nie jesteśmy przez nich rekomendowani. Uwagi o zgodności z przepisami (TCPA, RODO i podobne) to ogólne wskazówki, nie porada prawna.

## Bezpieczeństwo i wkład

Żadna umiejętność nie każe agentowi dopisywać do twoich tekstów stopek, linków, kodów poleceń ani wezwań do działania. Zgłoszenia dotyczące bezpieczeństwa: [SECURITY.md](SECURITY.md). Zasady współpracy: [CONTRIBUTING.md](CONTRIBUTING.md).

## O SyncGrowth i SyncBooster

Repozytorium prowadzi [SyncGrowth](https://syncgrowth.pl), firma, która projektuje i wdraża sposoby pracy w marketingu, procesach, automatyzacji, oprogramowaniu i AI. [SyncBooster](https://syncbooster.pl) to nasza platforma do planowania i publikowania postów w Facebooku, Instagramie, LinkedInie, Profilu Firmy w Google, X, YouTube i TikToku (tam, gdzie jest dostępny). Tylko ten produkt pojawia się w repozytorium: umiejętność `social-publishing` ma opcjonalną stronę o serwerze MCP SyncBoostera i wprost mówi, że to nasz produkt. Pozostałe umiejętności nie zależą od żadnego dostawcy.

## Licencja

[MIT](LICENSE). Prawa autorskie (c) 2025 Corey Haines i (c) 2026 Daniel Siwek. Kontakt: kontakt@syncgrowth.pl. Noty stron trzecich: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
