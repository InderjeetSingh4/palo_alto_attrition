<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=Workforce%20Attrition&fontSize=54&fontColor=E8EAF0&fontAlignY=38&desc=Diagnostic%20Intelligence%20Dashboard%20%C2%B7%20Palo%20Alto%20Networks&descAlignY=58&descSize=17&descColor=5E6AD2&animation=fadeIn" />

<br/>

<a href="#"><img src="https://img.shields.io/badge/Python-3.9%2B-5E6AD2?style=for-the-badge&logo=python&logoColor=white"/></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Plotly-5.x-00C8A0?style=for-the-badge&logo=plotly&logoColor=white"/></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white"/></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/ReportLab-4.x-FF6B35?style=for-the-badge&logoColor=white"/></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/License-MIT-3A3F56?style=for-the-badge"/></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Status-Production%20Ready-00C8A0?style=for-the-badge"/></a>

<br/><br/>

<table>
  <tr>
    <td align="center" width="110"><b>📊</b><br/><code>6</code><br/><sub>Charts</sub></td>
    <td align="center" width="110"><b>🎯</b><br/><code>4</code><br/><sub>Live KPIs</sub></td>
    <td align="center" width="110"><b>🔍</b><br/><code>5</code><br/><sub>Filters</sub></td>
    <td align="center" width="110"><b>📄</b><br/><code>4</code><br/><sub>PDF Pages</sub></td>
    <td align="center" width="110"><b>🖱️</b><br/><code>560px</code><br/><sub>Glow Orb</sub></td>
    <td align="center" width="110"><b>⚡</b><br/><code>~0ms</code><br/><sub>Re-render</sub></td>
  </tr>
</table>

<br/>

<blockquote>
<h3><i>"HR data doesn't have to look like a spreadsheet."</i></h3>

A <b>cinematic dark-mode analytics system</b> that transforms raw workforce CSV data into a
living diagnostic layer — complete with a physics-based cursor glow, glassmorphic cards,
six interactive Plotly charts, and an auto-generated 4-page PDF intelligence report.
</blockquote>

<br/>

</div>

---

## 📑 &nbsp;Table of Contents

| # | Section |
|---|---------|
| 01 | [✦ What Makes This Different](#-what-makes-this-different) |
| 02 | [🖼️ UI Layout Preview](#️-ui-layout-preview) |
| 03 | [✦ Feature Highlights](#-feature-highlights) |
| 04 | [📊 Charts & Analytics Deep Dive](#-charts--analytics-deep-dive) |
| 05 | [📄 PDF Report Generator](#-pdf-report-generator) |
| 06 | [🎨 Design System](#-design-system) |
| 07 | [🚀 Quick Start](#-quick-start) |
| 08 | [🗂️ Project Structure](#️-project-structure) |
| 09 | [📋 Dataset Reference](#-dataset-reference) |
| 10 | [🔧 Customization Guide](#-customization-guide) |
| 11 | [🧩 Architecture](#-architecture) |
| 12 | [❓ FAQ](#-faq) |

---

## ✦ &nbsp;What Makes This Different

Most HR dashboards look like this:

```
┌─────────────────────────────────────────────────────┐
│  [White background]  [Default bar chart colors]     │
│  Exits: 237          [Pie chart from 2008]          │
│  [Exported from Excel]                              │
└─────────────────────────────────────────────────────┘
```

This one looks like this:

```
╔═════════════════════════════════════════════════════╗
║  ░░░░  CURSOR GLOW FOLLOWS YOUR MOUSE  ░░░░         ║
║                                                     ║
║  ◈ Palo Alto Networks · People Analytics           ║
║  ─────────────────────────────────────────────────  ║
║  Glassmorphic KPI cards  ·  gradient borders       ║
║  Charts that LIFT and GLOW on hover                ║
║  Indigo + Teal on #07090F void  ·  DM Mono nums    ║
║                                                     ║
║  + Auto-exports a 4-page cinematic PDF report      ║
╚═════════════════════════════════════════════════════╝
```

The philosophy: **data should be felt, not just read.**

Every design decision — the dark void background, the physics-based cursor orb, the
DM Mono font on every number, the `translateY(-4px)` on hover — exists to make
the analyst feel in control of the data, not the other way around.

---

## 🖼️ &nbsp;UI Layout Preview

```
┌──────────────────┬──────────────────────────────────────────────────────────┐
│   S I D E B A R  │   Palo Alto Networks · People Analytics                  │
│  ──────────────  │                                                           │
│  ◈ [Brand Logo]  │   ██  Workforce Attrition                                │
│  Palo Alto Nets  │   Diagnostic Intelligence Dashboard                       │
│                  │   ──────────────────────────────────────────────────────  │
│  ┌────────────┐  │                                                           │
│  │   1,470    │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐  │
│  │  Employees │  │  │  1,470   │  │   237    │  │  16.1%   │  │ 2.7/4.0 │  │
│  └────────────┘  │  │Headcount │  │  Exits   │  │Attrition │  │  Sat.   │  │
│  ┌────────────┐  │  └──────────┘  └──────────┘  └──────────┘  └─────────┘  │
│  │ 16.1% ●RED │  │                                                           │
│  │  Exit Rate │  │  ┌──────────────────┐  ┌───────────────────────────────┐ │
│  └────────────┘  │  │                  │  │  ▬▬▬▬▬▬▬▬  Overtime  30.5%  │ │
│  ┌────────────┐  │  │  ○  16.1%        │  │  ▬▬▬▬  No OT  10.4%         │ │
│  │ 7.0 ●AMBER │  │  │  (donut chart)   │  │                               │ │
│  │  Avg Tenure│  │  │                  │  └───────────────────────────────┘ │
│  └────────────┘  │  └──────────────────┘                                    │
│  ┌────────────┐  │                                                           │
│  │  3  ●TEAL  │  │  ┌──────────────────┐  ┌───────────────────────────────┐ │
│  │   Depts    │  │  │  Age Histogram   │  │  ●  Dept Risk Bubbles         │ │
│  └────────────┘  │  │  Retained+Exited │  │  size = attrition rate        │ │
│                  │  └──────────────────┘  └───────────────────────────────┘ │
│  ── SEGMENT ──   │                                                           │
│  [Dept filter ]  │  ┌──────────────────┐  ┌───────────────────────────────┐ │
│  [Role filter ]  │  │ Job Role Bars    │  │  Tenure Exit Curve  ~~~~      │ │
│                  │  │ color-scaled     │  │  area chart                   │ │
│  ── TENURE ──    │  └──────────────────┘  └───────────────────────────────┘ │
│  [0 ──────── 40] │                                                           │
│                  │                                                           │
│  ── OVERTIME ──  │                                                           │
│  ● All  ○ Y  ○ N │                                                           │
│                  │                                                           │
│  CONFIDENTIAL    │                                                           │
└──────────────────┴──────────────────────────────────────────────────────────┘
```

---

## ✦ &nbsp;Feature Highlights

| Feature | Description | Tech |
|---|---|---|
| 🖱️ **Cursor Glow Orb** | 560px radial gradient with 9% ease-out lerp per `requestAnimationFrame` frame — silky smooth | Vanilla JS |
| 📊 **6 Interactive Charts** | Donut · H-Bars · Histogram · Bubble Scatter · Color Bars · Area Line | Plotly |
| 🃏 **Glassmorphic KPI Cards** | Gradient top-border, bloom shadow, `translateY(-4px)` hover lift | CSS |
| ✨ **Chart Glow Wrappers** | Each chart panel lifts + gets indigo halo on cursor hover | CSS `.chart-wrapper` |
| 🗂️ **Smart Sidebar** | Live stat pills (4 metrics) + brand header + 4 filter widgets | Streamlit + CSS |
| 📄 **PDF Report Generator** | Auto-generates a 4-page dark-themed intelligence report with Matplotlib charts | ReportLab + Matplotlib |
| 🎨 **Cinema Dark Theme** | `#07090F` void, DM Sans + DM Mono, `#5E6AD2` indigo + `#00C8A0` teal | CSS variables |
| ⚡ **Instant Re-renders** | `@st.cache_data` means filters feel like client-side JS — no full reloads | Streamlit cache |
| 🔒 **Bulletproof Data Coercion** | Handles `Yes/No` strings **and** `1/0` integers for the Attrition column | Pandas |
| 🎯 **Pulled Donut Slice** | The "Exited" segment uses `pull=0.05` to visually isolate the risk metric | Plotly |
| 📍 **Live Center Annotation** | Exit % is rendered directly inside the donut hole via Plotly annotation | Plotly |
| 🏷️ **Risk Color Coding** | Red / Amber / Teal signals on tables and sidebar pills for instant threat detection | CSS + Python |

---

## 📊 &nbsp;Charts & Analytics Deep Dive

<details>
<summary><b>🍩 &nbsp;Retention Donut — Breakdown at a glance</b></summary>

<br/>

An ultra-thin ring chart (`hole=0.72`) with the live exit rate % rendered directly
inside the hole as a Plotly annotation. The "Exited" segment pulls out by `5%` for
instant visual emphasis.

```python
fig_pie = px.pie(pie_df, values='Count', names='Status', hole=0.72)
fig_pie.update_traces(pull=[0.05 if s == 'Exited' else 0 for s in pie_df['Status']])
fig_pie.add_annotation(text=f"<b>{rate:.1f}%</b>", x=0.5, y=0.5, showarrow=False)
```

- **Colors:** Exited = `#5E6AD2` · Retained = `#3A3F56`
- **Separator:** 3px dark ring between segments for surgical clarity
- **Hover:** Shows label, count, and percentage share

</details>

<details>
<summary><b>📊 &nbsp;Overtime Impact Bars — Strongest signal in the dataset</b></summary>

<br/>

Horizontal bars comparing attrition rates between overtime vs non-overtime employees.
This is consistently the **single strongest predictor** of voluntary departure.

```
No Overtime  ▬▬▬▬        10.4%
Overtime     ▬▬▬▬▬▬▬▬▬▬  30.5%   ← 2.9× multiplier
```

- **Corner radius:** `7px` pill shape for a modern feel
- **Finding:** Overtime employees exit at nearly **3× the rate** of those without
- **Recommendation trigger:** If OT% rises above 25% in any team, flag for intervention

</details>

<details>
<summary><b>📉 &nbsp;Age Distribution Histogram — Life-stage risk mapping</b></summary>

<br/>

Overlaid histograms (`barmode='overlay'`) with 25 bins showing the exact age bands
where exits spike relative to the retained workforce.

- **Peak risk band:** Ages 25–29 — early career mobility is the dominant driver
- **Stabilization:** The 35–44 band shows retention improving with seniority
- **Late career:** 50+ shows consistently low exits — institutional knowledge concentration risk

</details>

<details>
<summary><b>🫧 &nbsp;Department Risk Bubbles — Executive summary in one glance</b></summary>

<br/>

Bubble scatter where both **size and color** encode attrition rate for
redundant visual encoding — optimal for board-level presentations.

```
● Sales          20.6%  — BLUE (high risk)
● Human Res.     19.0%  — BLUE (high risk)
● Research &Dev  13.8%  — TEAL (below median)
```

- Color switches at the **median** attrition rate: above = indigo, below = teal
- Hover shows department name, exact rate, exits, and total headcount

</details>

<details>
<summary><b>🎨 &nbsp;Job Role Color Bars — Sorted risk ladder</b></summary>

<br/>

Horizontal bars with a continuous `colorscale` from muted gray → indigo, sorted
ascending so the highest-risk roles "burn brightest" at the top of the chart.

```python
marker=dict(
    color=role_df['Rate_pct'],
    colorscale=[[0, '#3A3F56'], [1, '#5E6AD2']],
    cornerradius=6,
)
```

**Risk ranking snapshot:**
| Rank | Role | Rate |
|---|---|---|
| 🔴 #1 | Sales Executive | 30.0% |
| 🔴 #2 | Lab Technician | 23.9% |
| 🟢 #9 | Research Director | 2.5% |

</details>

<details>
<summary><b>📈 &nbsp;Tenure Exit Curve — When do people actually leave?</b></summary>

<br/>

Area line chart revealing the exact career anniversaries where employees are most
likely to resign. The filled area creates a visual "risk mountain."

```
Year 0   ████████████  62.5%  ← Onboarding crisis
Year 1   ███████       35.1%  ← Honeymoon end
Year 5   ████          15.0%  ← First career review
Year 10  █████         18.2%  ← Career plateau
Year 20  ██            11.0%  ← Pre-retirement spike
```

- **Mode:** `lines+markers` — dots at each point for precision hover targeting
- **Fill:** `tozeroy` with `rgba(94,106,210,0.07)` — atmospheric, not distracting

</details>

---

## 📄 &nbsp;PDF Report Generator

The project ships with a standalone **`generate_report.py`** that produces a
4-page, print-ready PDF intelligence report — fully dark-themed, using the same
color system as the dashboard.

### Report Structure

```
┌────────────────────────────────────────────────────────────┐
│  PAGE 1 — Executive Overview                               │
│  ─────────────────────────────────────────────────────     │
│  Gradient hero header  ·  CONFIDENTIAL badge               │
│  4 KPI metric cards (color-coded borders)                  │
│  4 insight callout boxes with key findings                 │
│  Donut chart  +  Overtime impact bars                      │
├────────────────────────────────────────────────────────────┤
│  PAGE 2 — Demographics & Department Risk                   │
│  ─────────────────────────────────────────────────────     │
│  Age distribution histogram (Retained vs Exited overlay)   │
│  Department risk bubble scatter chart                      │
│  Department breakdown table (🔴 HIGH / 🟠 MED / 🟡 LOW)   │
│  3 age-based insight callout boxes                         │
├────────────────────────────────────────────────────────────┤
│  PAGE 3 — Role Analysis & Tenure Dynamics                  │
│  ─────────────────────────────────────────────────────     │
│  Job role attrition bars (color-scaled, sorted)            │
│  Tenure exit curve (area line chart)                       │
│  Critical tenure windows callout box                       │
│  Full role risk ranking table with #rank badges            │
├────────────────────────────────────────────────────────────┤
│  PAGE 4 — Recommendations & Action Plan                    │
│  ─────────────────────────────────────────────────────     │
│  5 priority-badged strategic recommendations               │
│  Executive Scorecard (Current vs Target vs Status)         │
└────────────────────────────────────────────────────────────┘
```

### Generate the Report

```bash
python generate_report.py
# → outputs: Workforce_Attrition_Report.pdf
```

### Report Tech Stack

| Component | Library | Purpose |
|---|---|---|
| PDF canvas | `reportlab.pdfgen.canvas` | Dark backgrounds, custom layouts |
| Charts | `matplotlib` (Agg backend) | All 6 chart types rendered as PNGs |
| Chart embedding | `reportlab.platypus.Image` | PNG buffer → PDF canvas |
| Text wrapping | Custom word-wrap loop | Handles variable-length insight text |
| Color system | `reportlab.lib.colors.HexColor` | Same palette as dashboard |

### PDF Design Details

```
EVERY PAGE:
  • #07090F full-page dark background
  • Indigo→Teal gradient top bar (3pt)
  • Footer: gradient line + page counter + confidential stamp
  • Left accent stripe (4pt) in section color

PAGE HEADERS use 3 accent colors:
  • Page 1 → #5E6AD2 (indigo)   — Overview
  • Page 2 → #5E6AD2 (indigo)   — Demographics
  • Page 3 → #00C8A0 (teal)     — Roles
  • Page 4 → #FBBF24 (amber)    — Recommendations

CARDS & TABLES:
  • Rounded rect cards with #0F1120 fill + #1E2440 border
  • Table rows alternate between #07090F and #0C0E1A
  • Rate cells color-coded: >20% = red · >12% = amber · else = teal
```

### Recommendations in the Report

| Priority | Recommendation | Target |
|---|---|---|
| 🔴 CRITICAL | Overtime Policy Reform | Reduce OT attrition by 40% in 2Q |
| 🟠 HIGH | Onboarding Reinforcement Program | Year-0 rate below 30% |
| 🔵 MEDIUM | Sales Department Retention Sprint | < 15% by year end |
| 🟢 OPPORTUNITY | Research Director Playbook | Apply success formula to other roles |
| 🔵 MEDIUM | Mid-Career Mobility Pathways | Compete with external offers internally |

---

## 🎨 &nbsp;Design System

### Color Palette

<table>
  <tr>
    <th>Token</th><th>Hex</th><th>Swatch</th><th>Usage</th>
  </tr>
  <tr><td><code>BG_DARK</code></td><td><code>#07090F</code></td><td>⬛</td><td>Full page background — deep space void</td></tr>
  <tr><td><code>SURFACE</code></td><td><code>#0F1120</code></td><td>⬛</td><td>Card backgrounds, sidebar</td></tr>
  <tr><td><code>SURFACE2</code></td><td><code>#141728</code></td><td>⬛</td><td>Hover tooltip backgrounds</td></tr>
  <tr><td><code>BORDER</code></td><td><code>#1E2440</code></td><td>⬛</td><td>Card borders, table rules</td></tr>
  <tr><td><code>ACCENT_BLUE</code></td><td><code>#5E6AD2</code></td><td>🟦</td><td>Primary — high-risk, selected, active</td></tr>
  <tr><td><code>ACCENT_TEAL</code></td><td><code>#00C8A0</code></td><td>🟩</td><td>Success — low-risk, positive signal</td></tr>
  <tr><td><code>ACCENT_RED</code></td><td><code>#F87171</code></td><td>🟥</td><td>Danger — critical attrition, alerts</td></tr>
  <tr><td><code>ACCENT_AMBER</code></td><td><code>#FBBF24</code></td><td>🟨</td><td>Warning — medium risk, caution</td></tr>
  <tr><td><code>MUTED</code></td><td><code>#3A3F56</code></td><td>⬜</td><td>Retained employees, background bars</td></tr>
  <tr><td><code>TEXT_PRIMARY</code></td><td><code>#E8EAF0</code></td><td>⬜</td><td>Headlines, KPI values</td></tr>
  <tr><td><code>TEXT_MUTED</code></td><td><code>#9094AC</code></td><td>⬜</td><td>Body copy, chart labels</td></tr>
  <tr><td><code>TEXT_DIMMED</code></td><td><code>#6B7196</code></td><td>⬜</td><td>Axis ticks, captions, footnotes</td></tr>
</table>

### Typography

```
DISPLAY     DM Sans   weight 600  →  Page title, section headings
SUBHEADING  DM Sans   weight 500  →  Sidebar brand, chart subtitles
BODY        DM Sans   weight 400  →  Filter labels, body copy, captions
MONO        DM Mono   weight 500  →  ALL numbers — KPI values, axis ticks,
                                     chart annotations, table data
```

> **Rule:** Every number that communicates data uses `DM Mono`. This creates
> a visual grammar where numerical content is instantly distinguishable from
> descriptive text — a technique borrowed from financial terminal design.

### Motion Spec

```
CURSOR GLOW
  Loop:        requestAnimationFrame
  Algorithm:   cx += (mx - cx) * 0.09   ← ease-out lerp
  Size:        560 × 560 px
  Blend:       mix-blend-mode: screen
  Filter:      blur(1px)

KPI CARD HOVER
  Transform:   translateY(-4px)
  Duration:    0.3s ease
  Shadow:      0 20px 40px rgba(94,106,210, 0.28)
  Border:      rgba(94,106,210, 0.45)

CHART WRAPPER HOVER
  Transform:   translateY(-3px)
  Duration:    0.35s ease
  Shadow:      0 20px 60px rgba(94,106,210, 0.22)
               0 0 0 1px rgba(94,106,210, 0.07)
  Border:      rgba(94,106,210, 0.32)

SIDEBAR STAT PILL HOVER
  Background:  rgba(94,106,210, 0.12)
  Border:      rgba(94,106,210, 0.28)
  Duration:    0.2s ease
```

### Spacing & Geometry

```
Border radius (cards):     16px
Border radius (pills):     10px
Border radius (badges):     6px
Card padding:              22px 26px 18px
Gradient top border:        2px
Left accent stripe:         4px
KPI font size:             2.0rem  (DM Mono)
Section label size:        0.60rem (7pt, uppercase, 0.15em tracking)
Chart header size:         0.62rem (DM Sans Bold)
```

---

## 🚀 &nbsp;Quick Start

### Prerequisites

```bash
python --version    # 3.9 or higher required
pip --version       # any recent version
```

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourname/workforce-attrition-dashboard.git
cd workforce-attrition-dashboard

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place your dataset
cp /path/to/your/data.csv "Palo Alto Networks.csv"

# 5. Launch the dashboard 🚀
streamlit run app.py

# 6. (Optional) Generate the PDF report
python generate_report.py
```

Open **[http://localhost:8501](http://localhost:8501)** — the cursor glow activates immediately.

### requirements.txt

```txt
streamlit>=1.30.0
pandas>=2.0.0
plotly>=5.18.0
reportlab>=4.0.0
matplotlib>=3.8.0
numpy>=1.24.0
```

---

## 🗂️ &nbsp;Project Structure

```
workforce-attrition-dashboard/
│
├── 📊 app.py                        ← Streamlit dashboard (single-file)
│    │
│    ├── ① Page config               (set_page_config)
│    ├── ② CSS + cursor glow JS      (st.markdown unsafe_allow_html)
│    ├── ③ Data loader               (@st.cache_data, type-safe coercion)
│    ├── ④ BASE_LAYOUT theme dict    (shared across all Plotly figures)
│    ├── ⑤ Sidebar                   (brand, stat pills, 4 filter widgets)
│    ├── ⑥ Filter engine             (boolean mask, 4 dimensions + OT)
│    ├── ⑦ Page header               (title, subtitle)
│    ├── ⑧ KPI row                   (4 st.metric cards)
│    ├── ⑨ Chart grid                (3 rows × 2 cols of chart-wrapper divs)
│    └── ⑩ Footer                    (confidential stamp)
│
├── 📋 generate_report.py            ← Standalone PDF report generator
│    │
│    ├── Matplotlib chart renderers  (6 chart functions → PNG buffers)
│    ├── Canvas drawing helpers      (bg, header, footer, KPI cards)
│    ├── Insight box renderer        (color-coded callout cards)
│    ├── Table renderer              (styled dark-theme tables)
│    └── build_report()              (assembles all 4 pages)
│
├── 📁 Palo Alto Networks.csv        ← HR dataset (add your own)
├── 📋 requirements.txt              ← Python dependencies
└── 📖 README.md                     ← You are here
```

### Data Flow

```
CSV on disk
    │
    ▼
@st.cache_data ──→ pd.read_csv() ──→ type coercion (Attrition Yes/No → 1/0)
    │
    ▼
Sidebar filter widgets
    │
    ▼
Boolean mask (Department ∩ JobRole ∩ YearsAtCompany ∩ OverTime)
    │
    ▼
filtered_df ──→ KPI metrics ──→ 6 Plotly charts ──→ rendered in browser
                    │
                    ▼
            generate_report.py ──→ Matplotlib PNGs ──→ ReportLab PDF
```

---

## 📋 &nbsp;Dataset Reference

Your CSV must include these columns (extra columns are silently ignored):

| Column | Type | Required | Values | Notes |
|---|---|---|---|---|
| `Department` | string | ✅ | e.g. `Sales`, `R&D`, `Human Resources` | Used in filter + dept chart |
| `JobRole` | string | ✅ | e.g. `Sales Executive`, `Manager` | Used in filter + role chart |
| `Attrition` | int **or** string | ✅ | `1`/`0` **or** `Yes`/`No` | Both encodings auto-handled |
| `OverTime` | string | ✅ | `Yes` / `No` | Used in filter + OT chart |
| `YearsAtCompany` | int | ✅ | `0` – `40` | Tenure slider + curve chart |
| `Age` | int | ✅ | Employee age | Age histogram |
| `EnvironmentSatisfaction` | int | ✅ | `1` – `4` scale | Avg Satisfaction KPI |
| `MonthlyIncome` | float | ⬜ optional | Monthly salary | Sidebar reference stat |

> **Compatible dataset:** This schema exactly matches the
> [IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
> on Kaggle — you can drop it in and run immediately with no changes.

### Sample Row

```csv
Department,JobRole,Attrition,OverTime,YearsAtCompany,Age,EnvironmentSatisfaction,MonthlyIncome
Sales,Sales Executive,Yes,Yes,3,29,2,4500
Research & Development,Research Scientist,No,No,8,36,3,7200
```

---

## 🔧 &nbsp;Customization Guide

<details>
<summary><b>🎨 Change the accent color scheme</b></summary>

Find and replace `#5E6AD2` (indigo) with any hex across `app.py` and `generate_report.py`.
The secondary teal `#00C8A0` can be swapped similarly.

```python
# In app.py
BLUE  = '#5E6AD2'   # ← swap for your brand color
TEAL  = '#00C8A0'   # ← swap for secondary

# In generate_report.py
ACCENT_BLUE = colors.HexColor('#5E6AD2')   # ← same
ACCENT_TEAL = colors.HexColor('#00C8A0')   # ← same
```

</details>

<details>
<summary><b>🖱️ Tune cursor glow physics</b></summary>

In the `<script>` block inside `app.py`:

```js
// Smoothness — lower = dreamier lag, higher = snappier follow
cx += (mx - cx) * 0.09;   // range: 0.04 (dreamy) → 0.25 (sharp)

// Size — in the CSS block
width:  560px;             // try 300px (subtle) to 800px (dramatic)
height: 560px;

// Intensity — in the radial-gradient
rgba(94, 106, 210, 0.14)   // try 0.06 (ghost) to 0.30 (vivid)
```

</details>

<details>
<summary><b>➕ Add a new chart to the dashboard</b></summary>

Any chart wrapped in `.chart-wrapper` inherits the hover glow for free:

```python
# Build your Plotly figure
fig = go.Figure(...)
fig.update_layout(**BASE_LAYOUT, height=300)

# Wrap in the hover card
st.markdown(
    '<div class="chart-wrapper">'
    '<p class="chart-header">SECTION LABEL</p>'
    '<p class="chart-sub">Chart Title Here</p>',
    unsafe_allow_html=True
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
st.markdown('</div>', unsafe_allow_html=True)
```

</details>

<details>
<summary><b>📊 Add a new KPI to the metric row</b></summary>

```python
# Expand to 5 columns
c1, c2, c3, c4, c5 = st.columns(5)

# Add the new metric
c5.metric("Avg Tenure", f"{filtered['YearsAtCompany'].mean():.1f} yrs")
```

The KPI card CSS applies automatically — gradient border, hover lift, DM Mono font.

</details>

<details>
<summary><b>📄 Add a new page to the PDF report</b></summary>

Each page in `generate_report.py` follows this structure:

```python
def build_report(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)

    # ── YOUR NEW PAGE ─────────────────────────────
    draw_page_bg(c, w, h)              # dark background
    draw_gradient_bar(c, 0, h-3, w, 3) # top accent bar
    draw_footer(c, w, PAGE_NUM, TOTAL)  # footer

    # Section header
    c.setFillColor(SURFACE)
    c.rect(0, h-50, w, 50, fill=1, stroke=0)
    # ... your content here ...

    c.showPage()  # ← always end page with this
```

</details>

<details>
<summary><b>🌐 Deploy to Streamlit Cloud</b></summary>

1. Push your project (including the CSV) to a public GitHub repo
2. Go to **[share.streamlit.io](https://share.streamlit.io)**
3. Connect your repo and set `app.py` as the entry point
4. Click **Deploy**

> ⚠️ If your CSV contains sensitive employee data, use a
> [Streamlit secret](https://docs.streamlit.io/library/advanced-features/secrets-management)
> or anonymize the dataset before pushing to GitHub.

</details>

---

## 🧩 &nbsp;Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         BROWSER  (localhost:8501)                        │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐  │
│  │  PRESENTATION LAYER                                                │  │
│  │  CSS:  dark theme · glassmorphism · hover animations              │  │
│  │  JS:   cursor glow orb (requestAnimationFrame physics loop)       │  │
│  └───────────────────────────────────┬────────────────────────────────┘  │
│                                      │ injected via st.markdown()        │
│                                      ▼                                   │
│  ┌──────────────────┐   ┌────────────────────────────────────────────┐  │
│  │   SIDEBAR        │   │   MAIN CONTENT AREA                        │  │
│  │                  │   │                                            │  │
│  │  st.multiselect  │   │  st.columns(4) → st.metric() × 4         │  │
│  │  st.multiselect  │──▶│                                            │  │
│  │  st.slider       │   │  st.columns([1,1.5]) → chart-wrapper × 2  │  │
│  │  st.radio        │   │  st.columns(2)       → chart-wrapper × 2  │  │
│  │                  │   │  st.columns(2)       → chart-wrapper × 2  │  │
│  └──────────────────┘   └────────────────────────────────────────────┘  │
│           │                               ▲                              │
│           └───────────── filter mask ─────┘                              │
│                         (boolean, 4-dim)                                 │
│                                ▲                                         │
│  ┌─────────────────────────────┴──────────────────────────────────────┐  │
│  │  DATA LAYER                                                        │  │
│  │  @st.cache_data  →  pd.read_csv()  →  type coercion  →  DataFrame │  │
│  │                       Palo Alto Networks.csv                      │  │
│  └────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────┘

                                    +
┌──────────────────────────────────────────────────────────────────────────┐
│                         PDF PIPELINE  (generate_report.py)               │
│                                                                          │
│  Simulated stats  →  Matplotlib chart funcs  →  PNG buffers (io.BytesIO)│
│       ↓                                              ↓                   │
│  ReportLab canvas  ←  embed_chart()  ←  RLImage(buf, width, height)    │
│       ↓                                                                  │
│  draw_page_bg() · draw_top_header() · draw_kpi_card()                   │
│  draw_section_header() · draw_insight_box() · draw_table()              │
│  draw_footer() · c.showPage() × 4                                        │
│       ↓                                                                  │
│  Workforce_Attrition_Report.pdf  (A4 · dark theme · 4 pages)            │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## ❓ &nbsp;FAQ

<details>
<summary><b>The cursor glow isn't showing — what's wrong?</b></summary>

Streamlit injects HTML via `unsafe_allow_html=True`. Make sure you're running
the app in a **standard browser tab** (not an embedded iframe or VS Code's
Simple Browser). JavaScript must be enabled.

If the glow still doesn't appear, check your browser console for errors — some
browsers block `mix-blend-mode: screen` on dark backgrounds in strict mode.

</details>

<details>
<summary><b>My Attrition column has Yes/No strings — will it work?</b></summary>

Yes, completely. The data loader handles both encodings automatically:

```python
if df['Attrition'].dtype == object:
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['Attrition'] = pd.to_numeric(df['Attrition'], errors='coerce').fillna(0).astype(int)
```

</details>

<details>
<summary><b>Can I use a different company's data?</b></summary>

Absolutely. Change the CSV filename in `pd.read_csv()`, update the header text
in the app, and adjust the sidebar brand name. The only hard requirement is that
your CSV columns match the names in the [Dataset Reference](#-dataset-reference) table.

</details>

<details>
<summary><b>Why does the PDF use simulated data instead of the live CSV?</b></summary>

`generate_report.py` is a standalone script that runs independently of the
Streamlit session. To connect it to your live filtered data, export `filtered_df`
to a temp CSV from the dashboard and load it in `generate_report.py`:

```python
# In app.py — add a download button
csv = filtered_df.to_csv(index=False)
st.download_button("Export filtered data", csv, "filtered.csv")

# In generate_report.py — load the export
df = pd.read_csv('filtered.csv')
```

</details>

<details>
<summary><b>Why does the sidebar show full-dataset stats even when filters are applied?</b></summary>

By design. The sidebar stat pills are **baseline reference numbers** from the
full unfiltered dataset — they tell you what "100%" looks like while you slice.
The KPI cards above the charts always reflect the currently filtered data.

</details>

<details>
<summary><b>The cornerradius property is throwing an error on my Plotly version.</b></summary>

`cornerradius` on `go.Bar` requires **Plotly ≥ 5.12**. Update with:

```bash
pip install --upgrade plotly
```

</details>

---

## 🛡️ &nbsp;Notes & Gotchas

- **`pointer-events: none`** on the cursor glow — it never intercepts clicks, hovers, or focus events
- **`mix-blend-mode: screen`** — the glow brightens the background rather than covering it
- **`@st.cache_data`** — the CSV is read only once; all filter changes re-use the cached DataFrame
- **`config={'displayModeBar': False}`** — hides the Plotly toolbar for a clean, chrome-free look
- **Streamlit re-runs the full script on every widget change** — keep all data transforms after the filter mask, not before
- All chart `.chart-wrapper` divs are purely decorative — Streamlit renders `st.plotly_chart()` outside the div in the DOM, so the hover effect applies to the surrounding card, not the iframe

---

<div align="center">

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=130&section=footer&animation=fadeIn"/>

<br/>

```
WORKFORCE ANALYTICS  ·  PALO ALTO NETWORKS  ·  CONFIDENTIAL
```

**Built with** &nbsp;
[Streamlit](https://streamlit.io) &nbsp;·&nbsp;
[Plotly](https://plotly.com) &nbsp;·&nbsp;
[Pandas](https://pandas.pydata.org) &nbsp;·&nbsp;
[ReportLab](https://www.reportlab.com) &nbsp;·&nbsp;
[Matplotlib](https://matplotlib.org) &nbsp;·&nbsp;
[DM Sans](https://fonts.google.com/specimen/DM+Sans)

<br/>

*If this dashboard gave your HR data a glow-up, drop a ⭐ — it keeps the orb alive.*

<br/>

</di
