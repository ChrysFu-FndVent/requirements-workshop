# Measurement plan

The project tracks adoption and requirement quality without adding analytics code to the Skill.

| Metric | Definition | Source | Review cadence |
|---|---|---|---|
| Installs or clones | Marketplace installs when available; otherwise unique repository clones and release-asset downloads | Codex marketplace reporting, GitHub Traffic, GitHub Releases API | Monthly |
| Example engagement | Visits that enter through an example or comparison link | GitHub referral data where available; tagged campaign links for external posts | Per campaign |
| New requirement categories | Distinct user-submitted scenarios not represented by current examples | `New requirement pattern` issue form | Monthly |
| Stars per unique visitor | New stars divided by unique repository visitors in the same period | GitHub Traffic and stargazer history | Monthly |
| Independent-visit conversion | Non-owner unique visitors who reach install or release actions | GitHub Traffic plus release downloads; report as a proxy, not exact attribution | Monthly |

## Reporting rules

1. Record the date range and data source with every number.
2. Do not combine GitHub's rolling 14-day traffic window with monthly totals without noting the mismatch.
3. Label unavailable marketplace or per-file view data as unavailable; do not estimate it silently.
4. Use issue labels to group new scenarios into product, feature change, external integration, and other.
5. Treat comparison-page engagement as a content signal, not proof that the Skill reduced engineering time.
