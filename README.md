# Global Olympic Sports Performance Analysis (1992–2022)
**Project Submission Documentation & Interactive Web Portal**

---

## Executive Summary & Deliverables

This project transforms 30 years of historical Olympic Games data (1992–2022 across 17 Games editions, 135 countries, and 68 sports disciplines) into interactive Tableau analytics dashboards, narrative story points, and a full-stack Flask web application deployed live on Render.

| Project Deliverable | Live Published Link |
| :--- | :--- |
| **Live Deployed Web Application** | [https://olympic-games-analysis-1.onrender.com](https://olympic-games-analysis-1.onrender.com) |
| **Tableau Public Dashboard 1** | [Global Olympic Performance Analysis](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1/GLOBALOLYMPICPERFORMANCEANALYSIS) |
| **Tableau Public Dashboard 2** | [Athlete & Regional Insights](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/ATHLETEREGIONALINSIGHTS) |
| **Tableau Public Dashboard 3** | [Host & Investment Insights](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/HOSTINVESTMENTINSIGHTS) |
| **Tableau Story 1** | [Global Performance Trends](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story1GlobalOlympicGamesPerformanceTrends) |
| **Tableau Story 2** | [Athlete & Regional Insights Narrative](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story2AthleteRegionalInsights) |
| **Tableau Story 3** | [Host Advantage & Investment Patterns](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story3HostAdvantageInvestmentPatterns) |
| **Tableau Story 4** | [Key Findings & Conclusion Narrative](https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story4KeyFindingsConclusion) |

---

## 1. Problem Statement & Business Scenarios

Analyzing historical trends in medal distribution, regional efficiency, athlete delegation sizes, and host nation boosts provides crucial strategic insights for national athletic committees, sports media channels, and policy researchers.

### Stakeholder Personas

* **Elena Rostova (High-Performance Director, National Olympic Committee):** Requires insights into sport-specific medal yields relative to delegation sizes and the measurable boost provided by home host status.
* **Marcus Vance (Sports Analytics Consultant, International Media Network):** Analyzes historical nation rankings, multi-decade medal trends, and regional performance shifts for broadcast commentary.
* **Dr. Aris Thorne (Sports History & Policy Researcher):** Evaluates long-term athlete participation growth, regional efficiency ratios, and host country performance spikes over 30 years.

---

## 2. Dataset Architecture

The analysis is powered by pre-aggregated relational CSV datasets derived from historical Olympedia data:

1. **`country_edition_summary.csv`:** Contains national delegation counts (`athletes_sent`), gold/silver/bronze/total medals, host indicators (`is_host`), and pre-calculated `medal_efficiency_pct`.
2. **`games_summary.csv`:** Summary per Olympic edition detailing participating countries, total medals awarded, and total athlete participation.
3. **`sport_summary.csv`:** Disciplinary metrics covering 68 sports, unique athlete counts, total medals awarded, and normalized `medals_per_100_athletes`.
4. **`region_sport_medals.csv`:** Breakdown of medal yield grouped across 7 geographic regions and sports categories.

---

## 3. Key Technical & Visualizations Overview

* **Dynamic Measures:** Built a `KPI Selector Parameter` in Tableau paired with a calculated `CASE` statement to dynamically toggle bar charts between Total, Gold, Silver, and Bronze views.
* **Delegation Size Proxy Note:** Analyzed `athletes_sent` (delegation size) as an operational proxy for national sports participation and efficiency.
* **Interactive Views:** Integrated filled world maps, trend line charts across Summer/Winter editions, regional efficiency pie/donut charts, delegation vs. medal scatter plots, and host nation advantage comparisons.

---

## 4. Flask Web Integration & Render Deployment

The web application is built using Python (Flask) and deployed via Render's Web Service infrastructure using **Gunicorn**:

* **Backend:** Flask routing (`app.py`) managing endpoints for `/`, `/dashboard`, and `/story`.
* **Frontend:** Responsive HTML pages (`index.html`, `dashboard.html`, `story.html`) styled with a custom dark-teal sports theme.
* **Embedding API:** Integrates Tableau's JavaScript Embedding API (`tableau-2.min.js`) with custom URL embed parameters (`:embed=y&:showVizHome=n`) to ensure seamless cross-origin web rendering without `X-Frame-Options` blocks.

---

## 5. Summary of Analytical Findings

1. **Top Country Dominance:** United States, China, Russia, and Great Britain lead overall historical medal volume, driving high podium concentrations in Summer editions.
2. **Delegation Efficiency:** Strong positive correlation exists between national delegation sizes (`athletes_sent`) and overall medal output.
3. **Host Country Boost:** Host nations consistently exhibit a marked upward spike in total medal counts during the edition in which they hold host status compared to non-hosting editions.
4. **Regional Yield:** Regional delegation efficiency demonstrates distinct discipline-level specializations across continents.