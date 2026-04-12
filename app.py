import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── 1. Page Config ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Workforce Attrition · Palo Alto Networks",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 2. CSS + JS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: #07090F !important;
    color: #E8EAF0 !important;
}

/* ── Cursor Glow Orb ── */
#cursor-glow {
    position: fixed;
    top: 0; left: 0;
    width: 560px;
    height: 560px;
    border-radius: 50%;
    background: radial-gradient(circle,
        rgba(94,106,210,0.14) 0%,
        rgba(0,200,160,0.07) 35%,
        transparent 68%
    );
    pointer-events: none;
    transform: translate(-50%, -50%);
    z-index: 9999;
    mix-blend-mode: screen;
    filter: blur(1px);
    will-change: left, top;
}

/* ── Background ── */
[data-testid="stAppViewContainer"] {
    background: #07090F !important;
    background-image:
        radial-gradient(ellipse 70% 50% at 15% 5%,  rgba(94,106,210,0.06) 0%, transparent 60%),
        radial-gradient(ellipse 50% 40% at 85% 85%, rgba(0,200,160,0.04) 0%, transparent 60%) !important;
}
[data-testid="stHeader"] { background: transparent !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(9,11,20,0.97) !important;
    border-right: 1px solid rgba(94,106,210,0.12) !important;
    backdrop-filter: blur(32px);
}
[data-testid="stSidebar"] * { font-family: 'DM Sans', sans-serif !important; }

.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 0 20px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 24px;
}
.sidebar-brand-dot {
    width: 32px; height: 32px;
    border-radius: 9px;
    background: linear-gradient(135deg, #5E6AD2 0%, #00C8A0 100%);
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(94,106,210,0.4);
}
.sidebar-brand-text {
    font-size: 0.78rem;
    font-weight: 600;
    color: #9094AC;
    letter-spacing: 0.03em;
    line-height: 1.3;
}
.sidebar-brand-text span {
    display: block;
    font-size: 0.62rem;
    color: #4E5470;
    font-weight: 400;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.sidebar-section {
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #5E6AD2;
    margin: 22px 0 10px;
    display: flex;
    align-items: center;
    gap: 7px;
}
.sidebar-section::before {
    content: '';
    width: 14px; height: 1px;
    background: #5E6AD2;
    flex-shrink: 0;
}

.sidebar-stats { display: flex; flex-direction: column; gap: 7px; margin-bottom: 4px; }
.stat-pill {
    background: rgba(94,106,210,0.07);
    border: 1px solid rgba(94,106,210,0.14);
    border-radius: 10px;
    padding: 10px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: border-color 0.2s, background 0.2s;
}
.stat-pill:hover {
    background: rgba(94,106,210,0.12);
    border-color: rgba(94,106,210,0.28);
}
.stat-pill-label { font-size: 0.7rem; color: #6B7196; font-weight: 500; }
.stat-pill-value { font-family:'DM Mono',monospace; font-size:0.82rem; color:#A0A8D8; font-weight:500; }
.stat-pill-value.danger  { color: #F87171; }
.stat-pill-value.success { color: #00C8A0; }
.stat-pill-value.warn    { color: #FBBF24; }

[data-testid="stSidebar"] label p {
    color: #6B7196 !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
}
[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background: rgba(94,106,210,0.14) !important;
    border: 1px solid rgba(94,106,210,0.28) !important;
    border-radius: 6px !important;
    color: #A0A8D8 !important;
    font-size: 0.68rem !important;
}
[data-testid="stSlider"] [role="slider"] { background: #5E6AD2 !important; }
[data-testid="stSlider"] > div > div > div > div { background: #5E6AD2 !important; }
[data-testid="stRadio"] label { color: #9094AC !important; font-size: 0.82rem !important; }

/* ── KPI Cards ── */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.028);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 22px 26px 18px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
}
div[data-testid="metric-container"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #5E6AD2, #00C8A0);
    opacity: 0.7;
}
div[data-testid="metric-container"]:hover {
    border-color: rgba(94,106,210,0.45);
    transform: translateY(-4px);
    box-shadow: 0 20px 40px -12px rgba(94,106,210,0.28), 0 0 0 1px rgba(94,106,210,0.1);
}
[data-testid="stMetricLabel"] p {
    color: #6B7196 !important;
    font-size: 0.66rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.13em !important;
    text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
    color: #E8EAF0 !important;
    font-size: 2rem !important;
    font-weight: 600 !important;
    letter-spacing: -0.03em !important;
    font-family: 'DM Mono', monospace !important;
}
[data-testid="stMetricDelta"] { display: none; }

/* ── Chart wrapper hover glow ── */
.chart-wrapper {
    background: rgba(255,255,255,0.022);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 18px 18px 2px;
    transition: border-color 0.35s ease, box-shadow 0.35s ease, transform 0.35s ease;
}
.chart-wrapper:hover {
    border-color: rgba(94,106,210,0.32);
    box-shadow:
        0 20px 60px -16px rgba(94,106,210,0.22),
        0 0 0 1px rgba(94,106,210,0.07),
        inset 0 1px 0 rgba(255,255,255,0.04);
    transform: translateY(-3px);
}
.chart-header {
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #5E6AD2;
    margin: 0 0 2px;
}
.chart-sub {
    font-size: 1.08rem;
    font-weight: 500;
    color: #CDD0E0;
    margin: 0 0 8px;
}

/* ── Misc ── */
hr { border-color: rgba(255,255,255,0.06) !important; }
h1 {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 600 !important;
    letter-spacing: -0.04em !important;
    color: #E8EAF0 !important;
    line-height: 1.1 !important;
}
header, #MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stMain"] > div { padding-top: 2rem; }
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(94,106,210,0.3); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(94,106,210,0.55); }
</style>

<!-- Cursor Glow Orb element -->
<div id="cursor-glow"></div>

<script>
(function() {
    // Wait for DOM then attach smooth cursor glow
    function initGlow() {
        const glow = document.getElementById('cursor-glow');
        if (!glow) { setTimeout(initGlow, 200); return; }

        let mx = window.innerWidth / 2;
        let my = window.innerHeight / 2;
        let cx = mx, cy = my;
        let raf;

        document.addEventListener('mousemove', function(e) {
            mx = e.clientX;
            my = e.clientY;
        });

        function animate() {
            // Ease-out follow for silky smooth feel
            cx += (mx - cx) * 0.09;
            cy += (my - cy) * 0.09;
            glow.style.left = cx + 'px';
            glow.style.top  = cy + 'px';
            raf = requestAnimationFrame(animate);
        }
        animate();
    }
    initGlow();
})();
</script>
""", unsafe_allow_html=True)


# ── 3. Load Data ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('Palo Alto Networks.csv')
    df['YearsAtCompany'] = pd.to_numeric(df['YearsAtCompany'], errors='coerce').fillna(0).astype(int)
    if df['Attrition'].dtype == object:
        df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0}).fillna(df['Attrition'])
    df['Attrition'] = pd.to_numeric(df['Attrition'], errors='coerce').fillna(0).astype(int)
    return df

df = load_data()

# ── Shared chart theme ───────────────────────────────────────────────────────
BLUE  = '#5E6AD2'
TEAL  = '#00C8A0'
MUTED = '#3A3F56'

BASE_LAYOUT = dict(
    margin=dict(t=10, b=10, l=10, r=10),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(family='DM Sans', color='#6B7196', size=11),
    hoverlabel=dict(
        bgcolor='#141728',
        bordercolor='rgba(94,106,210,0.45)',
        font=dict(family='DM Sans', color='#E8EAF0', size=12),
    ),
)

# ── 4. Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-dot">◈</div>
        <div class="sidebar-brand-text">
            Palo Alto Networks
            <span>People Analytics</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Live dataset stats (pre-filter reference)
    total_all = len(df)
    exits_all = int(df['Attrition'].sum())
    rate_all  = exits_all / total_all * 100
    avg_tenure = df['YearsAtCompany'].mean()

    st.markdown(f"""
    <div class="sidebar-stats">
        <div class="stat-pill">
            <span class="stat-pill-label">Total Employees</span>
            <span class="stat-pill-value">{total_all:,}</span>
        </div>
        <div class="stat-pill">
            <span class="stat-pill-label">Overall Exit Rate</span>
            <span class="stat-pill-value danger">{rate_all:.1f}%</span>
        </div>
        <div class="stat-pill">
            <span class="stat-pill-label">Avg Tenure</span>
            <span class="stat-pill-value warn">{avg_tenure:.1f} yrs</span>
        </div>
        <div class="stat-pill">
            <span class="stat-pill-label">Departments</span>
            <span class="stat-pill-value success">{df['Department'].nunique()}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">Segment</div>', unsafe_allow_html=True)

    selected_dept = st.multiselect(
        "Department",
        options=df['Department'].unique(),
        default=list(df['Department'].unique()),
    )
    selected_role = st.multiselect(
        "Job Role",
        options=df['JobRole'].unique(),
        default=list(df['JobRole'].unique()),
    )

    st.markdown('<div class="sidebar-section">Tenure Range</div>', unsafe_allow_html=True)
    min_t, max_t = int(df['YearsAtCompany'].min()), int(df['YearsAtCompany'].max())
    tenure_range = st.slider("Years", min_t, max_t, (min_t, max_t), label_visibility="collapsed")
    st.caption(f"· {tenure_range[0]} – {tenure_range[1]} years selected")

    st.markdown('<div class="sidebar-section">Overtime</div>', unsafe_allow_html=True)
    ot_toggle = st.radio("OT Filter", ['All', 'Yes', 'No'], label_visibility="collapsed")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.6rem;color:#1E2440;letter-spacing:0.1em;
                text-align:center;padding-top:14px;
                border-top:1px solid rgba(255,255,255,0.04);
                font-family:"DM Mono",monospace;'>
        CONFIDENTIAL · HR USE ONLY
    </div>
    """, unsafe_allow_html=True)

# ── 5. Filter ────────────────────────────────────────────────────────────────
mask = (
    df['Department'].isin(selected_dept) &
    df['JobRole'].isin(selected_role) &
    df['YearsAtCompany'].between(tenure_range[0], tenure_range[1])
)
filtered = df[mask].copy()
if ot_toggle != 'All':
    filtered = filtered[filtered['OverTime'] == ot_toggle]

# ── 6. Header ────────────────────────────────────────────────────────────────
st.markdown("""
<div style='margin-bottom:4px'>
  <span style='font-size:0.62rem;font-weight:700;letter-spacing:0.18em;
               text-transform:uppercase;color:#5E6AD2;'>
    Palo Alto Networks · People Analytics
  </span>
</div>
""", unsafe_allow_html=True)
st.title("Workforce Attrition")
st.markdown(
    "<p style='color:#4A5070;font-size:0.87rem;margin-top:-4px;margin-bottom:20px;'>"
    "Diagnostic Intelligence Dashboard</p>",
    unsafe_allow_html=True
)
st.divider()

# ── 7. KPIs ──────────────────────────────────────────────────────────────────
n       = len(filtered)
exits   = int(filtered['Attrition'].sum())
rate    = (exits / n * 100) if n > 0 else 0
avg_sat = filtered['EnvironmentSatisfaction'].mean() if n > 0 else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Headcount",        f"{n:,}")
c2.metric("Total Exits",      f"{exits:,}")
c3.metric("Attrition Rate",   f"{rate:.1f}%")
c4.metric("Avg Satisfaction", f"{avg_sat:.1f} / 4.0")

st.markdown("<br>", unsafe_allow_html=True)

# ── 8. Row 1 ─────────────────────────────────────────────────────────────────
r1c1, r1c2 = st.columns([1, 1.5])

with r1c1:
    pie_df = (filtered['Attrition']
              .map({1: 'Exited', 0: 'Retained'})
              .value_counts().reset_index())
    pie_df.columns = ['Status', 'Count']

    fig_pie = px.pie(pie_df, values='Count', names='Status', hole=0.72,
                     color='Status',
                     color_discrete_map={'Retained': MUTED, 'Exited': BLUE})
    fig_pie.update_traces(
        textinfo='none',
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Share: %{percent}<extra></extra>',
        marker=dict(line=dict(color='#07090F', width=3)),
        pull=[0.05 if s == 'Exited' else 0 for s in pie_df['Status']],
    )
    fig_pie.add_annotation(
        text=f"<b>{rate:.1f}%</b><br><span style='font-size:10px;color:#6B7196'>exit rate</span>",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=22, color='#E8EAF0', family='DM Mono'), align='center',
    )
    fig_pie.update_layout(**BASE_LAYOUT, height=300, showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=-0.1, xanchor='center', x=0.5,
                    font=dict(color='#6B7196', size=11)))

    st.markdown('<div class="chart-wrapper">'
                '<p class="chart-header">Breakdown</p>'
                '<p class="chart-sub">Retention Overview</p>', unsafe_allow_html=True)
    st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

with r1c2:
    ot_df = (filtered.groupby('OverTime')['Attrition'].mean().reset_index()
             .rename(columns={'Attrition': 'Rate'}))
    ot_df['Rate_pct'] = ot_df['Rate'] * 100
    ot_df['Color'] = ot_df['OverTime'].map({'Yes': BLUE, 'No': MUTED})

    fig_ot = go.Figure()
    for _, row in ot_df.iterrows():
        fig_ot.add_trace(go.Bar(
            x=[row['Rate_pct']], y=[row['OverTime']], orientation='h',
            marker=dict(color=row['Color'], cornerradius=7, line=dict(width=0)),
            text=[f"{row['Rate_pct']:.1f}%"], textposition='outside',
            textfont=dict(color='#9094AC', size=12, family='DM Mono'),
            hovertemplate=f"<b>{row['OverTime']}</b>: {row['Rate_pct']:.1f}%<extra></extra>",
            name=row['OverTime'],
        ))
    fig_ot.update_layout(**BASE_LAYOUT, height=300, showlegend=False, barmode='group',
        xaxis=dict(visible=False, showgrid=False,
                   range=[0, ot_df['Rate_pct'].max() * 1.35]),
        yaxis=dict(showgrid=False, title='', tickfont=dict(color='#9094AC', size=14)))

    st.markdown('<div class="chart-wrapper">'
                '<p class="chart-header">Overtime</p>'
                '<p class="chart-sub">Attrition Impact</p>', unsafe_allow_html=True)
    st.plotly_chart(fig_ot, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ── 9. Row 2 ─────────────────────────────────────────────────────────────────
r2c1, r2c2 = st.columns(2)

with r2c1:
    fig_age = px.histogram(
        filtered, x='Age',
        color=filtered['Attrition'].map({1: 'Exited', 0: 'Retained'}),
        barmode='overlay', color_discrete_map={'Retained': MUTED, 'Exited': BLUE},
        opacity=0.85, nbins=25)
    fig_age.update_traces(marker=dict(line=dict(width=0)))
    fig_age.update_layout(**BASE_LAYOUT, height=300, showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5,
                    font=dict(color='#6B7196', size=11)),
        xaxis=dict(showgrid=False, zeroline=False, title='Age',
                   tickfont=dict(color='#6B7196')),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.04)',
                   zeroline=False, title='', tickfont=dict(color='#6B7196')),
        bargap=0.1)

    st.markdown('<div class="chart-wrapper">'
                '<p class="chart-header">Demographics</p>'
                '<p class="chart-sub">Age Distribution</p>', unsafe_allow_html=True)
    st.plotly_chart(fig_age, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

with r2c2:
    dept_df = (filtered.groupby('Department')['Attrition']
               .agg(['mean', 'sum', 'count']).reset_index()
               .rename(columns={'mean': 'Rate', 'sum': 'Exits', 'count': 'Total'})
               .sort_values('Rate'))
    dept_df['Rate_pct'] = dept_df['Rate'] * 100

    fig_dept = go.Figure()
    for _, row in dept_df.iterrows():
        color = BLUE if row['Rate_pct'] > dept_df['Rate_pct'].median() else TEAL
        fig_dept.add_trace(go.Scatter(
            x=[row['Rate_pct']], y=[row['Department']], mode='markers+text',
            marker=dict(size=max(18, row['Rate_pct'] * 2.8), color=color, opacity=0.85,
                        line=dict(color='rgba(255,255,255,0.15)', width=1)),
            text=[f"  {row['Rate_pct']:.1f}%"], textposition='middle right',
            textfont=dict(color='#9094AC', size=12, family='DM Mono'),
            hovertemplate=(f"<b>{row['Department']}</b><br>"
                           f"Rate: {row['Rate_pct']:.1f}%<br>"
                           f"Exits: {row['Exits']} / {row['Total']}<extra></extra>"),
            name=row['Department'],
        ))
    fig_dept.update_layout(**BASE_LAYOUT, height=300, showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, title='Attrition Rate (%)',
                   tickfont=dict(color='#6B7196'),
                   range=[0, dept_df['Rate_pct'].max() * 1.6]),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.04)',
                   title='', tickfont=dict(color='#9094AC', size=12)))

    st.markdown('<div class="chart-wrapper">'
                '<p class="chart-header">Risk Profile</p>'
                '<p class="chart-sub">Department Attrition</p>', unsafe_allow_html=True)
    st.plotly_chart(fig_dept, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ── 10. Row 3 ────────────────────────────────────────────────────────────────
r3c1, r3c2 = st.columns(2)

with r3c1:
    role_df = (filtered.groupby('JobRole')['Attrition'].mean().reset_index()
               .rename(columns={'Attrition': 'Rate'}).sort_values('Rate'))
    role_df['Rate_pct'] = role_df['Rate'] * 100

    fig_role = go.Figure(go.Bar(
        x=role_df['Rate_pct'], y=role_df['JobRole'], orientation='h',
        marker=dict(color=role_df['Rate_pct'],
                    colorscale=[[0, MUTED], [1, BLUE]],
                    line=dict(width=0), cornerradius=6),
        text=[f"{v:.1f}%" for v in role_df['Rate_pct']],
        textposition='outside',
        textfont=dict(color='#6B7196', size=10, family='DM Mono'),
        hovertemplate='<b>%{y}</b>: %{x:.1f}%<extra></extra>',
    ))
    fig_role.update_layout(**BASE_LAYOUT, height=340,
        xaxis=dict(visible=False, range=[0, role_df['Rate_pct'].max() * 1.45]),
        yaxis=dict(showgrid=False, title='', tickfont=dict(color='#9094AC', size=10)))

    st.markdown('<div class="chart-wrapper">'
                '<p class="chart-header">Roles</p>'
                '<p class="chart-sub">Attrition by Job Role</p>', unsafe_allow_html=True)
    st.plotly_chart(fig_role, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

with r3c2:
    tenure_df = (filtered.groupby('YearsAtCompany')['Attrition'].mean().reset_index()
                 .rename(columns={'Attrition': 'Rate'}))
    tenure_df['Rate_pct'] = tenure_df['Rate'] * 100

    fig_tenure = go.Figure()
    fig_tenure.add_trace(go.Scatter(
        x=tenure_df['YearsAtCompany'], y=tenure_df['Rate_pct'],
        fill='tozeroy', fillcolor='rgba(94,106,210,0.07)',
        line=dict(color=BLUE, width=2.5), mode='lines+markers',
        marker=dict(size=5, color=BLUE, line=dict(color='#07090F', width=1.5)),
        hovertemplate='Year %{x}: <b>%{y:.1f}%</b><extra></extra>', name='',
    ))
    fig_tenure.update_layout(**BASE_LAYOUT, height=340, showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, title='Years at Company',
                   tickfont=dict(color='#6B7196')),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.04)', zeroline=False,
                   title='', tickfont=dict(color='#6B7196'), ticksuffix='%'))

    st.markdown('<div class="chart-wrapper">'
                '<p class="chart-header">Tenure</p>'
                '<p class="chart-sub">Exit Rate by Years at Company</p>', unsafe_allow_html=True)
    st.plotly_chart(fig_tenure, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;padding:32px 0 16px;color:#1A1E30;
            font-size:0.6rem;letter-spacing:0.12em;
            font-family:"DM Mono",monospace;'>
    WORKFORCE ANALYTICS · PALO ALTO NETWORKS · CONFIDENTIAL
</div>
""", unsafe_allow_html=True)