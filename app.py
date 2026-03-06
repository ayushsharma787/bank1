"""
Universal Bank Intelligence Dashboard
======================================
Entry point — Streamlit multi-page app
Run: streamlit run app.py
"""
import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from utils.styling import inject_css
from utils.data_loader import load_data, get_summary_stats

st.set_page_config(
    page_title="Universal Bank — Intelligence Platform",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# ── SIDEBAR BRANDING ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("# 🏦 Universal Bank")
    st.markdown("**Intelligence Platform**")
    st.markdown("---")
    st.markdown("""
    <div style='font-size:11px;color:#64748B;line-height:1.8'>
    📊 <b style='color:#94A3B8'>Overview</b> — Executive KPIs<br>
    👥 <b style='color:#94A3B8'>Customer Analytics</b><br>
    💳 <b style='color:#94A3B8'>Loan Analytics</b><br>
    🤖 <b style='color:#94A3B8'>AI Predictor</b> — Real-time ML<br>
    📈 <b style='color:#94A3B8'>Model Comparison</b><br>
    ⚠️ <b style='color:#94A3B8'>Risk Matrix</b>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style='font-size:10px;color:#475569;letter-spacing:1px'>
    DATASET<br>
    <span style='color:#D4A853'>Universal Bank · 5,000 records</span><br><br>
    ALGORITHMS<br>
    <span style='color:#D4A853'>Gradient Boosting · XGBoost · LightGBM<br>
    Random Forest · Extra Trees · AdaBoost<br>
    Decision Tree · Logistic Regression<br>
    KNN · SVM · Neural Network (MLP)</span>
    </div>
    """, unsafe_allow_html=True)

# ── HOME PAGE ─────────────────────────────────────────────────────────────────
df = load_data()
stats = get_summary_stats(df)

st.markdown('<div class="section-badge">WELCOME</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">Universal Bank <span>Intelligence Platform</span></div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Enterprise-grade ML-powered banking analytics dashboard · 5,000 customers · 11 ML algorithms</div>', unsafe_allow_html=True)

st.markdown("---")

# Quick stats
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Customers",        f"{stats['total_customers']:,}")
c2.metric("Loan Rate",        f"{stats['acceptance_rate']}%")
c3.metric("Avg Income",       f"${stats['avg_income']}K")
c4.metric("Avg CC Spend",     f"${stats['avg_cc']}K")
c5.metric("Online Banking",   f"{stats['online_pct']}%")
c6.metric("CD Account",       f"{stats['cd_pct']}%")

st.markdown("---")

# Navigation cards
st.markdown("### Navigate to a Section")
r1c1, r1c2, r1c3 = st.columns(3)

for col, icon, title, desc, page in [
    (r1c1, "📊", "Overview",         "Executive KPIs, income distribution, loan split, digital banking adoption.", "pages/1_Overview"),
    (r1c2, "👥", "Customer Analytics","Demographics, behavioral filters, income vs spend analysis.", "pages/2_Customer_Analytics"),
    (r1c3, "💳", "Loan Analytics",    "Acceptance rate drivers, income brackets, education & family impact.", "pages/3_Loan_Analytics"),
]:
    with col:
        st.markdown(f"""
        <div class="info-card">
            <strong>{icon} {title}</strong><br>{desc}
        </div>""", unsafe_allow_html=True)

r2c1, r2c2, r2c3 = st.columns(3)
for col, icon, title, desc in [
    (r2c1, "🤖", "AI Predictor",     "Real-time loan approval prediction with 11 algorithms + feature importance."),
    (r2c2, "📈", "Model Comparison",  "Full benchmark: accuracy, precision, recall, F1, AUC-ROC, confusion matrices."),
    (r2c3, "⚠️", "Risk Matrix",      "Risk tier scoring, correlation heatmap, portfolio health indicators."),
]:
    with col:
        st.markdown(f"""
        <div class="info-card">
            <strong>{icon} {title}</strong><br>{desc}
        </div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='font-size:11px;color:#475569;text-align:center'>
Universal Bank Intelligence Platform · Built with Streamlit & scikit-learn ·
Algorithms: Gradient Boosting · XGBoost · LightGBM · Random Forest · Decision Tree · Logistic Regression · KNN · SVM · MLP
</div>
""", unsafe_allow_html=True)
