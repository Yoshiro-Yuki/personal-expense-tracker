import streamlit as st
from comms_sheet import save_deposit

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ipon Tracker - Modern Philippine Savings App",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if "amount" not in st.session_state:
    st.session_state.amount = 2500.00

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Emergency Fund"

# -----------------------------------------------------------------------------
# PROSPER GREEN DESIGN SYSTEM CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
    
    <style>
        /* Base Canvas & Typography */
        .stApp {
            background-color: #fff8f5;
            font-family: 'Inter', sans-serif;
            color: #1f1b17;
        }
        
        /* Constrain width to mimic mobile canvas frame */
        .block-container {
            max-width: 440px !important;
            padding-top: 1.5rem !important;
            padding-bottom: 3rem !important;
        }

        h1, h2, h3, .jakarta-font {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        .material-symbols-outlined {
            font-variation-settings: 'FILL' 1, 'wght' 500, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }

        /* Top App Bar */
        .top-app-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fff8f5;
            padding: 10px 4px 16px 4px;
            border-bottom: 1px solid rgba(191, 201, 195, 0.35);
            margin-bottom: 20px;
        }
        .brand-wrap {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .brand-icon {
            width: 38px;
            height: 38px;
            border-radius: 9999px;
            background-color: rgba(130, 245, 193, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #003527;
        }
        .brand-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 18px;
            font-weight: 700;
            color: #003527;
            margin: 0;
            line-height: 1.2;
        }
        .brand-subtitle {
            font-size: 11px;
            font-weight: 600;
            color: #404944;
            margin: 0;
        }
        .php-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background-color: #fcf2eb;
            padding: 5px 12px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 700;
            color: #003527;
            border: 1px solid rgba(191, 201, 195, 0.45);
        }

        /* Amount Card */
        .amount-card {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 20px 16px 14px 16px;
            border: 1px solid rgba(191, 201, 195, 0.45);
            box-shadow: 0 4px 20px -2px rgba(6, 78, 59, 0.04);
            text-align: center;
            margin-bottom: 12px;
        }
        .section-eyebrow {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: #404944;
        }
        .currency-hero {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 38px;
            font-weight: 800;
            color: #003527;
            letter-spacing: -0.02em;
            margin: 6px 0 4px 0;
            font-feature-settings: "tnum" 1;
        }
        .currency-hero .peso-sign {
            font-size: 28px;
            color: rgba(0, 53, 39, 0.55);
            margin-right: 4px;
        }

        /* Section Header Row */
        .section-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 2px 8px 2px;
        }
        .options-count {
            font-size: 11px;
            font-weight: 700;
            color: #006c4a;
        }

        /* Button Overrides for Preset & Category Grid */
        div.stButton > button {
            width: 100%;
            border-radius: 12px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            transition: all 0.15s ease !important;
        }

        /* Secondary (Unselected) Buttons */
        div.stButton > button[kind="secondary"] {
            background-color: #ffffff !important;
            color: #1f1b17 !important;
            border: 1px solid rgba(191, 201, 195, 0.6) !important;
            padding: 12px 6px !important;
        }
        div.stButton > button[kind="secondary"]:hover {
            background-color: #f6ece6 !important;
            border-color: #006c4a !important;
        }

        /* Primary (Selected / Active) Buttons */
        div.stButton > button[kind="primary"] {
            background-color: #fcf2eb !important;
            color: #003527 !important;
            border: 2px solid #006c4a !important;
            padding: 12px 6px !important;
            box-shadow: 0 2px 8px rgba(0, 108, 74, 0.12) !important;
        }

        /* Custom Main CTA Wrapper */
        .cta-container div.stButton > button {
            background-color: #064e3b !important;
            color: #ffffff !important;
            border: none !important;
            height: 52px !important;
            border-radius: 14px !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            box-shadow: 0 6px 16px rgba(6, 78, 59, 0.2) !important;
        }
        .cta-container div.stButton > button:hover {
            background-color: #003527 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# TOP APP BAR
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="top-app-bar">
        <div class="brand-wrap">
            <div class="brand-icon">
                <span class="material-symbols-outlined">savings</span>
            </div>
            <div>
                <p class="brand-title">Ipon Tracker</p>
                <p class="brand-subtitle">Mag-ipon (Deposit)</p>
            </div>
        </div>
        <div class="php-badge">
            <span class="material-symbols-outlined" style="font-size:16px; color:#006c4a;">payments</span>
            <span>PHP ₱</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# MAIN DEPOSIT SCREEN
# -----------------------------------------------------------------------------

# 1. Amount Hero Display Card
st.markdown(
    f"""
    <div class="amount-card">
        <div class="section-eyebrow">Enter Amount</div>
        <div class="currency-hero">
            <span class="peso-sign">₱</span>{st.session_state.amount:,.2f}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Custom Amount Number Input
new_amt = st.number_input(
    "Custom Deposit Amount (₱)",
    min_value=0.0,
    max_value=1000000.0,
    value=float(st.session_state.amount),
    step=100.0,
    format="%.2f",
    label_visibility="collapsed",
)
if new_amt != st.session_state.amount:
    st.session_state.amount = new_amt
    st.rerun()

# 2. Quick Preset Chips (+₱100, +₱500, +₱2,500, +₱5,000)
presets = [
    ("+₱100", 100.0),
    ("+₱500", 500.0),
    ("+₱2,500", 2500.0),
    ("+₱5,000", 5000.0),
]
preset_cols = st.columns(4)
for idx, (label, val) in enumerate(presets):
    is_active = st.session_state.amount == val
    with preset_cols[idx]:
        if st.button(
            label,
            key=f"preset_{val}",
            type="primary" if is_active else "secondary",
            use_container_width=True,
        ):
            st.session_state.amount = val
            st.rerun()

# 3. Category / Vault Selector (3x2 Grid)
st.markdown(
    """
    <div class="section-header-row">
        <span class="section-eyebrow">Select Category / Vault</span>
        <span class="options-count">6 Options</span>
    </div>
    """,
    unsafe_allow_html=True,
)

categories = [
    {"id": "Emergency Fund", "short": "Emergency", "emoji": "🛡️"},
    {"id": "Travel Fund", "short": "Travel", "emoji": "✈️"},
    {"id": "Food", "short": "Food", "emoji": "🍽️"},
    {"id": "Gadgets", "short": "Gadgets", "emoji": "💻"},
    {"id": "MP2 Pag-IBIG", "short": "MP2 Fund", "emoji": "📈"},
    {"id": "Education", "short": "Education", "emoji": "🎓"},
]

row1_cols = st.columns(3)
row2_cols = st.columns(3)
grid_cols = row1_cols + row2_cols

for idx, cat in enumerate(categories):
    is_selected = st.session_state.selected_category == cat["id"]
    with grid_cols[idx]:
        btn_label = f"{cat['emoji']}\n\n**{cat['short']}**"
        if st.button(
            btn_label,
            key=f"cat_{cat['id']}",
            type="primary" if is_selected else "secondary",
            use_container_width=True,
        ):
            st.session_state.selected_category = cat["id"]
            st.rerun()

st.write("")

# 4. Primary CTA Action
st.markdown('<div class="cta-container">', unsafe_allow_html=True)
cta_label = f"💼 Save ₱{st.session_state.amount:,.2f} to {st.session_state.selected_category}"
if st.button(cta_label, key="save_cta_btn", use_container_width=True):
    amount = st.session_state.amount
    category = st.session_state.selected_category

    if amount > 0:
        result = save_deposit(amount, category)   # values passed here
        if result["status"] == "ok":
            st.toast(f"Naidagdag sa Ipon! 🎉 +₱{amount:,.2f} saved to {category}")
            # trigger other events here, e.g.:
            st.session_state.amount = 0.0
            st.rerun()
    else:
        st.warning("Please enter an amount greater than ₱0.00.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<p style="text-align:center; font-size:12px; color:#404944; margin-top:4px;">Free and instant transfer</p>',
    unsafe_allow_html=True,
)