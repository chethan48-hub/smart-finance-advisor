import streamlit as st
from investments import investments

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Finance & Investment Advisor",
    page_icon="💰",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("💰 Smart Finance & Investment Advisor")

st.write(
    "Analyze your monthly finances and discover investment "
    "options that may suit your financial profile."
)

st.divider()

# --------------------------------------------------
# USER FINANCIAL INFORMATION
# --------------------------------------------------

st.header("👤 Your Financial Profile")

col1, col2 = st.columns(2)

with col1:

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

with col2:

    amount_to_invest = st.number_input(
        "Amount You Want to Invest Monthly (₹)",
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

# --------------------------------------------------
# INVESTMENT PREFERENCES
# --------------------------------------------------

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

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if st.button(
    "🔍 Analyze My Finances",
    use_container_width=True
):

    # --------------------------------------------------
    # FINANCIAL CALCULATIONS
    # --------------------------------------------------

    remaining = income - expenses

    if income > 0:
        savings_rate = (remaining / income) * 100
    else:
        savings_rate = 0

    # --------------------------------------------------
    # FINANCIAL SUMMARY
    # --------------------------------------------------

    st.header("📊 Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Monthly Income",
            f"₹{income:,.0f}"
        )

    with col2:
        st.metric(
            "Monthly Expenses",
            f"₹{expenses:,.0f}"
        )

    with col3:
        st.metric(
            "Remaining Amount",
            f"₹{remaining:,.0f}"
        )

    # --------------------------------------------------
    # FINANCIAL VALIDATION
    # --------------------------------------------------

    if expenses > income:

        st.error(
            "⚠️ Your expenses are higher than your income. "
            "Consider improving your cash flow before investing."
        )

        st.stop()

    if amount_to_invest > remaining:

        st.warning(
            "⚠️ Your planned investment amount is higher "
            "than your remaining monthly income."
        )

        st.stop()

    # --------------------------------------------------
    # SAVINGS INFORMATION
    # --------------------------------------------------

    st.success(
        f"Your planned monthly investment of "
        f"₹{amount_to_invest:,.0f} is within your available amount."
    )

    st.write(
        f"**Estimated Savings Rate:** {savings_rate:.1f}%"
    )

    # --------------------------------------------------
    # USER PROFILE SUMMARY
    # --------------------------------------------------

    st.header("📋 Investment Profile")

    profile_col1, profile_col2, profile_col3 = st.columns(3)

    with profile_col1:
        st.write("**Risk Appetite**")
        st.info(risk)

    with profile_col2:
        st.write("**Investment Horizon**")
        st.info(horizon)

    with profile_col3:
        st.write("**Investment Goal**")
        st.info(goal)

    # --------------------------------------------------
    # RECOMMENDATION ENGINE
    # --------------------------------------------------

    st.header("💡 Recommended Investment Options")

    recommended = []

    for investment in investments:

        score = 0
        reasons = []

        # ----------------------------------------------
        # RISK MATCH
        # ----------------------------------------------

        if investment["risk"] == risk:

            score += 40
            reasons.append("✓ Matches your risk appetite")

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

            score += 15
            reasons.append(
                "△ Higher risk than your selected profile"
            )

        # ----------------------------------------------
        # HORIZON MATCH
        # ----------------------------------------------

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
                        "△ Longer recommended horizon"
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

            elif horizon == "Less than 3 years":

                if investment["risk"] == "Low":

                    score += 15
                    reasons.append(
                        "✓ Lower-risk option for a shorter horizon"
                    )

        # ----------------------------------------------
        # GOAL MATCH
        # ----------------------------------------------

        if goal in investment["goal"]:

            score += 30
            reasons.append(
                "✓ Matches your investment goal"
            )

        # ----------------------------------------------
        # SAVE RESULT
        # ----------------------------------------------

        recommended.append(
            {
                "investment": investment,
                "score": score,
                "reasons": reasons
            }
        )

    # --------------------------------------------------
    # SORT BY SUITABILITY
    # --------------------------------------------------

    recommended.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # --------------------------------------------------
    # DISPLAY RECOMMENDATIONS
    # --------------------------------------------------

    st.write(
        "The following options are ranked according to "
        "your selected risk appetite, investment horizon "
        "and financial goal."
    )

    for item in recommended[:5]:

        investment = item["investment"]
        score = item["score"]
        reasons = item["reasons"]

        with st.container(border=True):

            st.subheader(
                investment["name"]
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Type:** {investment['type']}"
                )

            with col2:

                st.write(
                    f"**Risk:** {investment['risk']}"
                )

            with col3:

                st.write(
                    f"**Suitability:** {score}/100"
                )

            st.progress(
                min(score, 100) / 100
            )

            st.write(
                f"**Recommended Horizon:** "
                f"{investment['horizon']}"
            )

            st.write(
                investment["description"]
            )

            st.write(
                "**Why this option appears:**"
            )

            for reason in reasons:

                st.write(reason)

    # --------------------------------------------------
    # DISCLAIMER
    # --------------------------------------------------

    st.divider()

    st.caption(
        "⚠️ Educational project only. The recommendations are "
        "generated using predefined rules and user inputs. "
        "They are not professional financial advice and do not "
        "guarantee investment returns. Investment products carry "
        "different levels of risk and should be evaluated carefully."
    )