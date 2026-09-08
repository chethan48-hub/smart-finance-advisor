import streamlit as st
from investments import investments

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Smart Finance Advisor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
<style>
.stApp {
    background-color: #f5f7fb;
}

.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ========================================================
   SIDEBAR
   ======================================================== */

[data-testid="stSidebar"] {
    background-color: #0f172a;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: white !important;
}

/* ========================================================
   HERO
   ======================================================== */

.hero {
    background: linear-gradient(135deg, #0f172a, #1e3a5f);
    padding: 40px;
    border-radius: 24px;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
}

.hero-small {
    color: #a7f3d0;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero-title {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero-text {
    color: #cbd5e1;
    font-size: 17px;
    line-height: 1.6;
}

/* ========================================================
   SECTION TITLE
   ======================================================== */

.section-title {
    color: #0f172a;
    font-size: 28px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 18px;
}

/* ========================================================
   METRIC CARDS
   ======================================================== */

.metric-card {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 22px;
    min-height: 120px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06);
}

.metric-label {
    color: #64748b;
    font-size: 13px;
    font-weight: 600;
}

.metric-value {
    color: #0f172a;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

.metric-description {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 5px;
}

/* ========================================================
   PROFILE CARDS
   ======================================================== */

.profile-card {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.06);
}

.profile-icon {
    font-size: 28px;
}

.profile-label {
    color: #64748b;
    font-size: 12px;
    margin-top: 8px;
}

.profile-value {
    color: #0f172a;
    font-size: 18px;
    font-weight: 700;
    margin-top: 5px;
}

/* ========================================================
   WELCOME CARDS
   ======================================================== */

.welcome-card {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 24px;
    min-height: 150px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
}

.welcome-icon {
    font-size: 30px;
}

.welcome-title {
    color: #0f172a;
    font-size: 18px;
    font-weight: 700;
    margin-top: 10px;
}

.welcome-text {
    color: #64748b;
    font-size: 13px;
    line-height: 1.5;
    margin-top: 8px;
}

/* ========================================================
   INFO BOX
   ======================================================== */

.info-box {
    background-color: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 15px;
    padding: 18px;
    color: #1e3a8a;
    margin: 20px 0;
}

/* ========================================================
   INVESTMENT CARD
   ======================================================== */

.investment-card {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 25px;
    margin-top: 20px;
    box-shadow: 0 7px 22px rgba(15, 23, 42, 0.06);
}

.investment-name {
    color: #0f172a;
    font-size: 22px;
    font-weight: 800;
}

.investment-type {
    color: #64748b;
    font-size: 13px;
    margin-top: 5px;
}

.rank-badge {
    display: inline-block;
    background-color: #e0f2fe;
    color: #0369a1;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 8px;
}

.score-box {
    background-color: #ecfdf5;
    border-radius: 15px;
    padding: 15px 20px;
    text-align: center;
    min-width: 130px;
}

.score {
    color: #047857;
    font-size: 28px;
    font-weight: 800;
}

.score-label {
    color: #64748b;
    font-size: 11px;
    font-weight: 600;
}

/* ========================================================
   DETAILS CARD
   ======================================================== */

.details-card {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 18px;
    min-height: 180px;
}

.details-title {
    color: #0f172a;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 15px;
}

.details-item {
    color: #475569;
    font-size: 13px;
    margin-bottom: 10px;
}

/* ========================================================
   REASON BOX
   ======================================================== */

.reason-box {
    background-color: #ecfdf5;
    border-radius: 9px;
    padding: 10px 12px;
    margin-top: 7px;
    color: #166534;
    font-size: 13px;
}

/* ========================================================
   DISCLAIMER
   ======================================================== */

.disclaimer {
    background-color: #fff7ed;
    border: 1px solid #fed7aa;
    border-radius: 14px;
    padding: 18px;
    color: #9a3412;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 30px;
}

/* ========================================================
   BUTTON
   ======================================================== */

.stButton > button {
    border-radius: 12px;
    font-weight: 700;
    min-height: 45px;
}

/* ========================================================
   PROGRESS BAR
   ======================================================== */

.stProgress > div > div > div {
    border-radius: 20px;
}

/* ========================================================
   HIDE STREAMLIT MENU
   ======================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
</style>
""",
    unsafe_allow_html=True
)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown(
    """
<div class="hero">
<div class="hero-small">💡 SMART FINANCIAL DECISION SUPPORT</div>
<div class="hero-title">Smart Finance Advisor</div>
<div class="hero-text">
Understand your finances and explore investment options based on
your risk profile, investment horizon and financial goals.
</div>
</div>
""",
    unsafe_allow_html=True
)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("# 💰 Smart Finance")

    st.markdown("### Your Financial Profile")

    st.write(
        "Enter your financial details to generate "
        "investment suitability results."
    )

    st.divider()

    income = st.number_input(
        "Monthly Income (₹)",
        min_value=0,
        value=50000,
        step=1000
    )

    expenses = st.number_input(
        "Monthly Expenses (₹)",
        min_value=0,
        value=30000,
        step=1000
    )

    amount_to_invest = st.number_input(
        "Monthly Investment Amount (₹)",
        min_value=0,
        value=10000,
        step=1000
    )

    risk = st.selectbox(
        "Risk Appetite",
        [
            "Conservative",
            "Moderate",
            "Aggressive"
        ]
    )

    horizon = st.selectbox(
        "Investment Duration",
        [
            "Less than 3 years",
            "3-5 years",
            "5-10 years",
            "10+ years"
        ]
    )

    goal = st.selectbox(
        "Investment Goal",
        [
            "Wealth Creation",
            "Retirement",
            "Education",
            "Buying a House",
            "Emergency Fund"
        ]
    )

    st.divider()

    analyze = st.button(
        "🔍 Analyze My Finances",
        use_container_width=True
    )

# ==========================================================
# WELCOME SCREEN
# ==========================================================

if not analyze:

    st.markdown(
        '<div class="section-title">👋 Welcome to your financial dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="info-box">
<b>Get started:</b><br>
Enter your financial information using the panel on the left
and click <b>Analyze My Finances</b>.
The system will rank investment options according to your profile.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">✨ What this advisor analyzes</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
<div class="welcome-card">
<div class="welcome-icon">💵</div>
<div class="welcome-title">Cash Flow</div>
<div class="welcome-text">
Analyze your income, expenses and available monthly amount.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
<div class="welcome-card">
<div class="welcome-icon">🎯</div>
<div class="welcome-title">Investor Profile</div>
<div class="welcome-text">
Consider your risk appetite, investment duration and financial goal.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
<div class="welcome-card">
<div class="welcome-icon">💡</div>
<div class="welcome-title">Investment Options</div>
<div class="welcome-text">
Rank available investments using predefined suitability rules.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown(
        """
<div class="disclaimer">
⚠️ <b>Educational Project:</b>
This application is developed for educational purposes.
Results are generated using predefined rules and should not
be considered professional financial advice.
</div>
""",
        unsafe_allow_html=True
    )

# ==========================================================
# ANALYSIS
# ==========================================================

if analyze:

    # ======================================================
    # FINANCIAL CALCULATIONS
    # ======================================================

    remaining = income - expenses

    if income > 0:
        savings_rate = (remaining / income) * 100
    else:
        savings_rate = 0

    # ======================================================
    # VALIDATION
    # ======================================================

    if expenses > income:

        st.error(
            "⚠️ Your expenses are higher than your monthly income. "
            "Please review your cash flow before considering investments."
        )

        st.stop()

    if amount_to_invest > remaining:

        st.warning(
            "⚠️ Your planned investment amount is higher than "
            "your available monthly amount."
        )

        st.stop()

    # ======================================================
    # FINANCIAL SNAPSHOT
    # ======================================================

    st.markdown(
        '<div class="section-title">📊 Financial Snapshot</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-label">MONTHLY INCOME</div>
<div class="metric-value">₹{income:,.0f}</div>
<div class="metric-description">Total monthly income</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-label">MONTHLY EXPENSES</div>
<div class="metric-value">₹{expenses:,.0f}</div>
<div class="metric-description">Regular monthly expenses</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-label">AVAILABLE AMOUNT</div>
<div class="metric-value">₹{remaining:,.0f}</div>
<div class="metric-description">Income after expenses</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-label">SAVINGS RATE</div>
<div class="metric-value">{savings_rate:.1f}%</div>
<div class="metric-description">Estimated monthly savings</div>
</div>
""",
            unsafe_allow_html=True
        )

    # ======================================================
    # INVESTMENT AMOUNT
    # ======================================================

    st.markdown(
        f"""
<div class="info-box">
💰 You plan to invest <b>₹{amount_to_invest:,.0f}</b>
per month from your available amount of
<b>₹{remaining:,.0f}</b>.
</div>
""",
        unsafe_allow_html=True
    )

    # ======================================================
    # INVESTOR PROFILE
    # ======================================================

    st.markdown(
        '<div class="section-title">🎯 Your Investor Profile</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
<div class="profile-card">
<div class="profile-icon">🛡️</div>
<div class="profile-label">RISK APPETITE</div>
<div class="profile-value">{risk}</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
<div class="profile-card">
<div class="profile-icon">⏳</div>
<div class="profile-label">INVESTMENT HORIZON</div>
<div class="profile-value">{horizon}</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
<div class="profile-card">
<div class="profile-icon">🎯</div>
<div class="profile-label">INVESTMENT GOAL</div>
<div class="profile-value">{goal}</div>
</div>
""",
            unsafe_allow_html=True
        )

    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    st.markdown(
        '<div class="section-title">💡 Recommended Investment Options</div>',
        unsafe_allow_html=True
    )

    st.write(
        "These options are ranked using your risk appetite, "
        "investment duration and financial goal."
    )

    # ======================================================
    # SCORING ENGINE
    # ======================================================

    recommended = []

    for investment in investments:

        score = 0
        reasons = []

        # --------------------------------------------------
        # RISK MATCHING
        # --------------------------------------------------

        if investment["risk"] == risk:

            score += 40

            reasons.append(
                "✓ Matches your risk appetite"
            )

        elif risk == "Moderate" and investment["risk"] == "Low":

            score += 30

            reasons.append(
                "✓ Lower-risk option than your selected profile"
            )

        elif risk == "Aggressive" and investment["risk"] == "Moderate":

            score += 25

            reasons.append(
                "✓ Moderate-risk option for diversification"
            )

        elif risk == "Conservative" and investment["risk"] == "Moderate":

            score += 10

            reasons.append(
                "△ Higher risk than your selected profile"
            )

        elif risk == "Conservative" and investment["risk"] == "Aggressive":

            score -= 20

            reasons.append(
                "⚠ Higher risk than your selected profile"
            )

        # --------------------------------------------------
        # INVESTMENT HORIZON
        # --------------------------------------------------

        if investment["horizon"] == horizon:

            score += 30

            reasons.append(
                "✓ Matches your investment duration"
            )

        else:

            if horizon == "5-10 years":

                if investment["horizon"] == "10+ years":

                    score += 15

                    reasons.append(
                        "△ Suitable for a longer investment horizon"
                    )

                elif investment["horizon"] == "3-5 years":

                    score += 15

                    reasons.append(
                        "△ Suitable for a somewhat shorter horizon"
                    )

            elif horizon == "10+ years":

                if investment["horizon"] == "5-10 years":

                    score += 15

                    reasons.append(
                        "△ Suitable for a somewhat shorter horizon"
                    )

            elif horizon == "3-5 years":

                if investment["horizon"] == "5-10 years":

                    score += 10

                    reasons.append(
                        "△ Longer recommended horizon"
                    )

                elif investment["horizon"] == "10+ years":

                    score += 5

                    reasons.append(
                        "△ Consider a longer-term commitment"
                    )

            elif horizon == "Less than 3 years":

                if investment["risk"] == "Low":

                    score += 15

                    reasons.append(
                        "✓ Lower-risk option for a shorter horizon"
                    )

                else:

                    score -= 10

                    reasons.append(
                        "⚠ May not be suitable for a short horizon"
                    )

        # --------------------------------------------------
        # GOAL MATCHING
        # --------------------------------------------------

        if goal in investment["goal"]:

            score += 30

            reasons.append(
                "✓ Matches your investment goal"
            )

        else:

            reasons.append(
                "• Does not directly match your selected goal"
            )

        # --------------------------------------------------
        # KEEP SCORE BETWEEN 0 AND 100
        # --------------------------------------------------

        score = max(0, min(score, 100))

        recommended.append(
            {
                "investment": investment,
                "score": score,
                "reasons": reasons
            }
        )

    # ======================================================
    # SORT INVESTMENTS
    # ======================================================

    recommended.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # ======================================================
    # TOP 5 INVESTMENTS
    # ======================================================

    for rank, item in enumerate(
        recommended[:5],
        start=1
    ):

        investment = item["investment"]
        score = item["score"]
        reasons = item["reasons"]

        # ==================================================
        # INVESTMENT HEADER
        # ==================================================

        st.markdown(
            f"""
<div class="investment-card">

<div class="rank-badge">
RANK #{rank}
</div>

<div style="display:flex;justify-content:space-between;align-items:center;gap:30px;">

<div style="flex:1;">

<div class="investment-name">
{investment["name"]}
</div>

<div class="investment-type">
{investment["type"]}
</div>

</div>

<div class="score-box">

<div class="score">
{score}/100
</div>

<div class="score-label">
SUITABILITY SCORE
</div>

</div>

</div>

</div>
""",
            unsafe_allow_html=True
        )

        # ==================================================
        # SCORE PROGRESS
        # ==================================================

        st.progress(
            score / 100
        )

        # ==================================================
        # DETAILS
        # ==================================================

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
<div class="details-card">

<div class="details-title">
📋 Investment Details
</div>

<div class="details-item">
<b>Type:</b> {investment["type"]}
</div>

<div class="details-item">
<b>Risk Level:</b> {investment["risk"]}
</div>

<div class="details-item">
<b>Recommended Horizon:</b> {investment["horizon"]}
</div>

</div>
""",
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                """
<div class="details-card">

<div class="details-title">
💡 Why this option appears
</div>

""",
                unsafe_allow_html=True
            )

            for reason in reasons:

                st.markdown(
                    f"""
<div class="reason-box">
{reason}
</div>
""",
                    unsafe_allow_html=True
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        # ==================================================
        # DESCRIPTION
        # ==================================================

        st.markdown(
            f"""
<div style="margin-top:15px;color:#475569;font-size:14px;line-height:1.6;">
<b>About this investment:</b><br>
{investment["description"]}
</div>
""",
            unsafe_allow_html=True
        )

        st.divider()

    # ======================================================
    # SCORE EXPLANATION
    # ======================================================

    st.markdown(
        '<div class="section-title">📈 How the suitability score works</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
<div class="welcome-card">
<div class="welcome-icon">🛡️</div>
<div class="welcome-title">Risk Match</div>
<div class="welcome-text">
Up to <b>40 points</b> are assigned based on how closely
the investment risk matches your risk appetite.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
<div class="welcome-card">
<div class="welcome-icon">⏳</div>
<div class="welcome-title">Time Horizon</div>
<div class="welcome-text">
Up to <b>30 points</b> are assigned based on the compatibility
between your investment duration and the product horizon.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
<div class="welcome-card">
<div class="welcome-icon">🎯</div>
<div class="welcome-title">Financial Goal</div>
<div class="welcome-text">
Up to <b>30 points</b> are assigned when the investment
supports your selected financial goal.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    # ======================================================
    # DISCLAIMER
    # ======================================================

    st.markdown(
        """
<div class="disclaimer">

⚠️ <b>Important Disclaimer</b>

<br><br>

This application is an educational engineering project.
The investment rankings are generated using predefined
rules and the information entered by the user.

<br><br>

The results are not professional financial advice,
do not guarantee returns and should not be treated as
a recommendation to buy or sell any investment.

<br><br>

Different investment products involve different levels
of risk. Users should conduct their own research and,
where appropriate, consult a qualified financial professional.

</div>
""",
        unsafe_allow_html=True
    )
