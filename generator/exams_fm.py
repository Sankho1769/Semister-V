# Model Examination Questions for MIM501: Financial Management (10 Questions)

def get_fm_exams():
    return [
    {
        "id": "exam_fm_q1",
        "subject_id": "mim501",
        "question_no": 1,
        "title": "Compare Wealth Maximization with Profit Maximization as Core Corporate Financial Objectives.",
        "intro": {
            "definition": "The objective of financial management establishes the foundational benchmark guiding corporate decisions regarding capital allocation, debt financing, and dividend distribution.",
            "background": "Traditional corporate finance prioritized single-period accounting profit maximization until modern financial economics proved its failure to account for risk, cash flow timing, and long-term sustainability.",
            "significance": "Wealth maximization is universally accepted as the superior criterion because it aligns management actions with the net present value of equity shareholders' market wealth."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='280' height='80' rx='6' fill='#FFF2EB' stroke='#EF846B'/><text x='170' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#EF846B' text-anchor='middle'>Profit Maximization</text><text x='170' y='75' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Short-Term Accounting Profit | Ambiguous</text><text x='170' y='92' font-family='sans-serif' font-size='8' fill='#D65F64' text-anchor='middle'>Ignores Risk &amp; Time Value of Money</text><rect x='390' y='30' width='280' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='530' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Wealth Maximization</text><text x='530' y='75' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Maximizes Market Value of Shares (NPV)</text><text x='530' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Strictly Incorporates Risk &amp; Cash Timing</text></svg>",
            "explanation": "Contrasts the limitations of short-term accounting profit maximization with the comprehensive valuation framework of wealth maximization.",
            "caption": "Figure E1.4: Comparative Objectives: Profit Maximization vs Wealth Maximization"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Conceptual Clarity vs Definitional Ambiguity",
                "explanation": "Profit maximization is ambiguous (gross, net, pre-tax, after-tax profit?), whereas wealth maximization is unambiguously defined as maximizing the market price per equity share.",
                "terminology": "Wealth Maximization, Definitional Precision, Market Price per Share (MPS).",
                "example": "A firm maximizing EPS can cause share prices to collapse if excessive debt leverage elevates insolvency risk."
            },
            {
                "point_no": 2,
                "heading": "Incorporation of the Time Value of Money (TVM)",
                "explanation": "Profit maximization treats a dollar earned today identically to a dollar earned ten years later. Wealth maximization explicitly discounts cash flows across time using WACC.",
                "terminology": "Time Value of Money (TVM), Discounted Cash Flow (DCF), Present Value (PV).",
                "example": "$1,000 received in Year 1 possesses far higher present wealth value than $1,000 received in Year 5."
            },
            {
                "point_no": 3,
                "heading": "Rigorous Recognition of Risk and Uncertainty",
                "explanation": "Profit maximization ignores operating and financial risk. Wealth maximization adjusts the discount rate (hurdle rate) upward for higher risk cash streams.",
                "terminology": "Risk Premium, Hurdle Rate, Business Risk, Financial Risk.",
                "example": "High-risk exploratory mining cash flows are discounted at 18%, while utility projects are discounted at 8%."
            },
            {
                "point_no": 4,
                "heading": "Focus on Actual Cash Flows vs Accounting Accruals",
                "explanation": "Profit can be manipulated through accounting conventions (depreciation methods, revenue recognition). Wealth maximization evaluates actual, verifiable after-tax cash flows.",
                "terminology": "Cash Flow vs Accounting Profit, Accrual Distortion, Depreciation Add-Back.",
                "example": "A profitable company can still go bankrupt if cash is tied up in uncollected receivables."
            },
            {
                "point_no": 5,
                "heading": "Long-Term Enterprise Sustainability and Stakeholder Alignment",
                "explanation": "Wealth maximization prohibits short-sighted cost-cutting (slashing R&D, worker safety) that inflates immediate profits at the expense of terminal enterprise valuation.",
                "terminology": "Terminal Value, Sustainable Growth Rate, Long-Term Enterprise Value.",
                "example": "Investing in R&D depresses current year profits but creates multi-billion dollar long-term shareholder wealth."
            }
        ],
        "conclusion": "Wealth maximization is the definitive operational objective of financial management, harmonizing time value of money, risk management, and cash flow growth."
    },
    {
        "id": "exam_fm_q2",
        "subject_id": "mim501",
        "question_no": 2,
        "title": "Explain the Calculation of Weighted Average Cost of Capital (WACC) and Component Costs (Kd, Ke, Kp).",
        "intro": {
            "definition": "The Weighted Average Cost of Capital (WACC) is the composite overall hurdle rate of return a corporation must generate on its asset base to satisfy all providers of debt, preferred, and equity capital.",
            "background": "Evolved from capital structure economics to provide the foundational discount rate for enterprise discounted cash flow (DCF) valuation and capital budgeting.",
            "significance": "Acts as the strategic benchmark: any corporate project yielding returns below WACC destroys shareholder equity value."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Cost of Debt (Kd)</text><text x='110' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Kd = I(1 - t) / NP</text><text x='110' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Tax-Deductible Interest</text><rect x='220' y='30' width='160' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='300' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Cost of Equity (Ke)</text><text x='300' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Ke = (D1 / P0) + g</text><text x='300' y='92' font-family='sans-serif' font-size='8' fill='#786CE5' text-anchor='middle'>Dividend Growth / CAPM</text><rect x='410' y='30' width='260' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='540' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#1B6F61' text-anchor='middle'>WACC Equation (Ko)</text><text x='540' y='78' font-family='monospace' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>Ko = (Wd * Kd) + (We * Ke)</text><text x='540' y='95' font-family='sans-serif' font-size='8' fill='#28A994' text-anchor='middle'>Minimum Project Hurdle Rate</text></svg>",
            "explanation": "Illustrates individual component costs weighted proportionally by capital structure shares to calculate overall WACC.",
            "caption": "Figure E2.4: Component Costs and Weighted Average Cost of Capital (WACC) Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "After-Tax Cost of Debt (Kd) and Interest Tax Shield",
                "explanation": "Debt is the cheapest source of capital because debenture interest is tax-deductible; after-tax cost is calculated as Kd = [I * (1 - T)] / Net Proceeds.",
                "terminology": "Cost of Debt (Kd), Interest Tax Shield, Tax Rate (T), Net Proceeds.",
                "example": "A 10% debenture at 30% corporate tax rate costs an effective after-tax rate of only 7.0%."
            },
            {
                "point_no": 2,
                "heading": "Cost of Preference Capital (Kp)",
                "explanation": "Preference dividends are fixed contractual obligations but are paid out of post-tax profits (not tax-deductible); Kp = Preference Dividend / Net Issue Proceeds.",
                "terminology": "Cost of Preference (Kp), Non-Tax Deductible, Fixed Dividend.",
                "example": "9% Preference shares issued at par yield a Kp of exactly 9.0%."
            },
            {
                "point_no": 3,
                "heading": "Cost of Equity (Ke) via Dividend Growth & CAPM",
                "explanation": "Equity carries the highest risk and cost. Calculated using Gordon's Dividend Growth Model: Ke = (D1 / P0) + g, or CAPM: Ke = Rf + Beta * (Rm - Rf).",
                "terminology": "Cost of Equity (Ke), CAPM, Beta, Market Risk Premium, Gordon Growth.",
                "example": "If Rf = 6%, Beta = 1.2, and Market Return Rm = 12%: Ke = 6% + 1.2 * (12% - 6%) = 13.2%."
            },
            {
                "point_no": 4,
                "heading": "Book Value vs Market Value Weighting",
                "explanation": "WACC combines component costs using proportional weights (Wd, We, Wp). Market value weights are theoretically superior as they reflect current economic opportunity costs.",
                "terminology": "Book Value Weights, Market Value Weights, Target Capital Structure.",
                "example": "Using market capitalization of shares rather than historical par balance sheet value."
            },
            {
                "point_no": 5,
                "heading": "WACC as the Corporate Investment Hurdle Rate",
                "explanation": "WACC acts as the cutoff benchmark for evaluating all capital budgeting investments; projects with Return on Invested Capital (ROIC) > WACC expand shareholder value.",
                "terminology": "Hurdle Rate, Economic Value Added (EVA), ROIC vs WACC Spread.",
                "example": "A project generating 14% ROIC when WACC is 11% creates a positive 3% EVA spread."
            }
        ],
        "conclusion": "WACC aggregates debt and equity component costs into a unified hurdle rate, directing capital deployment into value-accretive corporate investments."
    },
    {
        "id": "exam_fm_q3",
        "subject_id": "mim501",
        "question_no": 3,
        "title": "Explain Financial Ratio Analysis and the DuPont 3-Step Decomposition of Return on Equity (ROE).",
        "intro": {
            "definition": "Ratio analysis is the quantitative evaluation of corporate liquidity, operational activity, leverage, and profitability through mathematical relationships extracted from final balance sheets and income statements.",
            "background": "Developed by the DuPont Corporation in 1919 to decompose Return on Equity (ROE) into three distinct operational drivers: profit margin, asset velocity, and financial leverage.",
            "significance": "Enables corporate executives, credit agencies, and equity investors to diagnose the root operational drivers behind financial performance."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='50' width='130' height='60' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='85' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>Profit Margin</text><text x='85' y='92' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>Net Inc / Sales</text><text x='165' y='85' font-family='sans-serif' font-size='16' font-weight='700' fill='#617087'>*</text><rect x='185' y='50' width='140' height='60' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='255' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#786CE5' text-anchor='middle'>Asset Turnover</text><text x='255' y='92' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>Sales / Total Assets</text><text x='340' y='85' font-family='sans-serif' font-size='16' font-weight='700' fill='#617087'>*</text><rect x='360' y='50' width='150' height='60' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='435' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#28A994' text-anchor='middle'>Equity Multiplier</text><text x='435' y='92' font-family='monospace' font-size='8' fill='#19283D' text-anchor='middle'>Assets / Equity</text><text x='525' y='85' font-family='sans-serif' font-size='16' font-weight='700' fill='#617087'>=</text><rect x='545' y='40' width='130' height='80' rx='6' fill='#E9E8F8' stroke='#F2C75C'/><text x='610' y='75' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>ROE</text><text x='610' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#369B72' text-anchor='middle'>Return on Equity</text></svg>",
            "explanation": "Illustrates the three multiplicative components of the DuPont identity generating Return on Equity (ROE).",
            "caption": "Figure E3.4: Three-Step DuPont Decomposition of Return on Equity"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Short-Term Liquidity Ratios (Current and Quick Ratios)",
                "explanation": "Current Ratio (Current Assets / Current Liabilities, benchmark 2:1) and Quick Ratio ((Current Assets - Inventory) / Current Liabilities, benchmark 1:1) evaluate immediate debt solvency.",
                "terminology": "Current Ratio, Quick Ratio, Acid-Test, Working Capital Buffer.",
                "example": "A firm with $200k current assets and $100k current liabilities maintains a healthy 2.0 current ratio."
            },
            {
                "point_no": 2,
                "heading": "Long-Term Solvency and Leverage Ratios",
                "explanation": "Debt-Equity Ratio (Total Debt / Shareholders' Net Worth) and Interest Coverage Ratio (EBIT / Interest) evaluate corporate capital gearing and debt repayment safety margins.",
                "terminology": "Debt-Equity Ratio, Gearing, Interest Coverage Ratio, Bankruptcy Buffer.",
                "example": "An interest coverage ratio of 6.0 indicates EBIT can cover annual debt interest six times over."
            },
            {
                "point_no": 3,
                "heading": "DuPont Tier 1: Operating Net Profit Margin",
                "explanation": "Calculated as Net Income / Sales; measures the percentage of revenue converted into profit after deducting all operating expenses, interest, and taxes.",
                "terminology": "Net Profit Margin, Operating Efficiency, Cost Control.",
                "example": "Pricing power allows a luxury manufacturer to command a high 22% net profit margin."
            },
            {
                "point_no": 4,
                "heading": "DuPont Tier 2: Total Asset Turnover (Asset Velocity)",
                "explanation": "Calculated as Sales / Total Assets; measures asset utilization efficiency in generating commercial sales volume.",
                "terminology": "Asset Turnover, Asset Velocity, Capital Intensity.",
                "example": "A retail supermarket operating on thin 2% margins achieves high ROE via high 5.0x asset turnover."
            },
            {
                "point_no": 5,
                "heading": "DuPont Tier 3: Financial Leverage Equity Multiplier",
                "explanation": "Calculated as Total Assets / Shareholders' Equity; measures the degree to which assets are funded by debt rather than equity capital.",
                "terminology": "Equity Multiplier, Financial Leverage, Balance Sheet Gearing.",
                "example": "Margin = 10%, Turnover = 1.5, Multiplier = 2.0 results in ROE = 10% * 1.5 * 2.0 = 30.0%."
            }
        ],
        "conclusion": "The DuPont framework isolates whether corporate return on equity is driven by operational profitability, asset turnover velocity, or financial debt leverage."
    },
    {
        "id": "exam_fm_q4",
        "subject_id": "mim501",
        "question_no": 4,
        "title": "Explain Discounted Cash Flow (DCF) Methods: Net Present Value (NPV) vs Internal Rate of Return (IRR) Conflicts.",
        "intro": {
            "definition": "Capital budgeting DCF techniques evaluate long-term capital investments by discounting prospective future cash flows to present value terms using the cost of capital.",
            "background": "Developed by Joel Dean (1951) to supersede crude payback periods with mathematically rigorous present value techniques.",
            "significance": "Guides multi-million dollar corporate asset investments, ensuring long-term shareholder wealth creation."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='280' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='170' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Net Present Value (NPV)</text><text x='170' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>NPV = PV(Inflows) - Outlay</text><text x='170' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Reinvests at WACC (Realistic &amp; Superior)</text><rect x='390' y='30' width='280' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='530' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Internal Rate of Return (IRR)</text><text x='530' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>Discount Rate 'r' where NPV = 0</text><text x='530' y='92' font-family='sans-serif' font-size='8' fill='#EF846B' text-anchor='middle'>Reinvests at Project's Own IRR (Flawed)</text></svg>",
            "explanation": "Contrasts NPV and IRR evaluation methods and highlights their fundamental reinvestment rate assumptions.",
            "caption": "Figure E4.4: Discounted Cash Flow Criteria Comparison: NPV vs IRR"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Net Present Value (NPV) Decision Rule",
                "explanation": "NPV equals the sum of discounted future operating cash inflows minus the initial capital expenditure outlay; accept all projects where NPV > 0.",
                "terminology": "Net Present Value, Hurdle Rate Discounting, Value Additivity.",
                "example": "A project requiring $100k generating $125k PV of inflows has an NPV of +$25k (Accept)."
            },
            {
                "point_no": 2,
                "heading": "Internal Rate of Return (IRR) Break-Even Benchmark",
                "explanation": "IRR is the internal break-even discount rate where the present value of cash inflows equals the initial investment outlay (NPV = 0); accept if IRR > Cost of Capital (k).",
                "terminology": "Internal Rate of Return (IRR), Hurdle Rate Comparison, Break-Even Discount Rate.",
                "example": "A project with IRR = 16% evaluated against a 10% cost of capital is accepted."
            },
            {
                "point_no": 3,
                "heading": "Roots of Conflict: Scale, Timing, and Unequal Life Disparities",
                "explanation": "In mutually exclusive projects, NPV and IRR rankings can conflict due to differences in initial capital investment scale, cash flow timing patterns, or project lifespans.",
                "terminology": "Mutually Exclusive Projects, Scale Disparity, Cash Flow Skewness.",
                "example": "A small project with 40% IRR may yield only $5k NPV, while a larger project with 20% IRR yields $50k NPV."
            },
            {
                "point_no": 4,
                "heading": "Reinvestment Rate Assumption Difference",
                "explanation": "NPV assumes cash flows are reinvested at the realistic firm Cost of Capital (WACC), whereas IRR mathematically assumes reinvestment at the project's own internal rate of return.",
                "terminology": "Reinvestment Rate Assumption, WACC Reinvestment, IRR Flaw.",
                "example": "Assuming a 35% project can reinvest all intermediate cash flows at 35% is unrealistic in competitive markets."
            },
            {
                "point_no": 5,
                "heading": "Theoretical Supremacy of the NPV Metric",
                "explanation": "When ranking conflicts arise between mutually exclusive proposals, the NPV recommendation must always be followed because it directly measures absolute dollar additions to shareholder wealth.",
                "terminology": "NPV Supremacy, Wealth Addition, Shareholder Maximization.",
                "example": "Always choose the project yielding the highest absolute positive NPV ($50k vs $5k)."
            }
        ],
        "conclusion": "NPV is the theoretically superior investment metric because it reflects realistic WACC reinvestment rates and directly measures absolute additions to shareholder wealth."
    },
    {
        "id": "exam_fm_q5",
        "subject_id": "mim501",
        "question_no": 5,
        "title": "Explain Capital Rationing and Project Selection using the Profitability Index (PI).",
        "intro": {
            "definition": "Capital rationing is the operational financial condition where a firm has a fixed ceiling on total capital expenditure funds, preventing it from accepting all positive NPV projects.",
            "background": "Arises from internal managerial constraints (soft rationing) or external market credit borrowing ceilings (hard rationing).",
            "significance": "Requires sophisticated ranking algorithms (Profitability Index) to maximize total aggregate NPV under constrained investment budgets."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='80' rx='6' fill='#FFF2EB' stroke='#EF846B'/><text x='120' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>Capital Budget Cap</text><text x='120' y='75' font-family='monospace' font-size='11' font-weight='700' fill='#D65F64' text-anchor='middle'>Budget = $1,000,000</text><text x='120' y='92' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Cannot fund all projects</text><path d='M 215 70 L 295 70' stroke='#377FE6' stroke-width='2'/><rect x='300' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='390' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Profitability Index</text><text x='390' y='75' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>PI = PV / Outlay</text><text x='390' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Ranks Efficiency per $1</text><path d='M 485 70 L 555 70' stroke='#28A994' stroke-width='2'/><rect x='560' y='30' width='110' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='615' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>Max NPV</text><text x='615' y='85' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Optimal Portfolio</text></svg>",
            "explanation": "Illustrates project prioritization via Profitability Index (PI) ranking to maximize total portfolio NPV within a constrained capital ceiling.",
            "caption": "Figure E5.4: Capital Rationing Portfolio Optimization via Profitability Index"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Internal (Soft) vs External (Hard) Capital Rationing",
                "explanation": "Soft rationing is imposed internally by executive management to control corporate expansion pace; hard rationing is imposed externally by capital markets refusing credit.",
                "terminology": "Soft Rationing, Hard Rationing, Budget Ceiling, Debt Covenants.",
                "example": "Board limits total annual capital expenditure to $10M despite having access to more debt."
            },
            {
                "point_no": 2,
                "heading": "Profitability Index (Benefit-Cost Ratio) Formula",
                "explanation": "Profitability Index measures capital efficiency by calculating present value of cash inflows per dollar of capital outlay: PI = PV of Cash Inflows / Initial Outlay.",
                "terminology": "Profitability Index (PI), Benefit-Cost Ratio, Capital Efficiency.",
                "example": "A project with $120k PV of inflows and $100k outlay has a PI of 1.20."
            },
            {
                "point_no": 3,
                "heading": "Ranking Divisible Projects by Highest PI",
                "explanation": "When projects can be accepted partially (divisible), ranking proposals in descending order of PI and funding downwards guarantees maximum aggregate portfolio NPV.",
                "terminology": "Divisible Projects, PI Ranking, Linear Programming Optimization.",
                "example": "Project A (PI=1.4) and Project B (PI=1.3) are fully funded before Project C (PI=1.1)."
            },
            {
                "point_no": 4,
                "heading": "Indivisible Projects and Feasible Combinations",
                "explanation": "When projects cannot be accepted partially, simple PI ranking may leave unallocated idle funds; management must evaluate all feasible combinations to maximize total absolute NPV.",
                "terminology": "Indivisible Projects, Integer Programming, Exhaustive Combination Method.",
                "example": "Selecting two projects that exhaust $1M with $300k total NPV over one project with $250k NPV."
            },
            {
                "point_no": 5,
                "heading": "Opportunity Cost of Capital Rationing Constraints",
                "explanation": "Artificial internal capital ceilings reject positive NPV investments, preventing the firm from achieving its maximum potential shareholder wealth.",
                "terminology": "Opportunity Cost, Foregone Wealth, Sub-optimal Investment.",
                "example": "Rejecting a project with +$50k NPV due to budget constraints forfeits $50k of market equity value."
            }
        ],
        "conclusion": "The Profitability Index optimizes capital allocation under rationing constraints by identifying project combinations that maximize total shareholder wealth per dollar invested."
    },
    {
        "id": "exam_fm_q6",
        "subject_id": "mim501",
        "question_no": 6,
        "title": "Explain Operating Leverage, Financial Leverage, and Combined Leverage Analysis.",
        "intro": {
            "definition": "Leverage analysis is the financial evaluation of how fixed operating overheads and fixed financing charges magnify percentage variations in corporate operating profits (EBIT) and earnings per share (EPS).",
            "background": "Developed in managerial finance to quantify enterprise business risk (operating costs) and capital financial risk (debt obligations).",
            "significance": "Underpins capital structure planning, guiding management on the safe debt capacity an enterprise can sustain without risking insolvency."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='120' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>DOL (Operating)</text><text x='120' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>DOL = Contrib / EBIT</text><text x='120' y='92' font-family='sans-serif' font-size='8' fill='#377FE6' text-anchor='middle'>Fixed Operating Overhead</text><path d='M 215 70 L 265 70' stroke='#786CE5' stroke-width='2'/><rect x='270' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='360' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>DFL (Financial)</text><text x='360' y='75' font-family='monospace' font-size='9' fill='#19283D' text-anchor='middle'>DFL = EBIT / (EBIT - I)</text><text x='360' y='92' font-family='sans-serif' font-size='8' fill='#786CE5' text-anchor='middle'>Fixed Debt Interest Cost</text><path d='M 455 70 L 505 70' stroke='#28A994' stroke-width='2'/><rect x='510' y='30' width='160' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='590' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>DCL = DOL * DFL</text><text x='590' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Total Enterprise Risk</text><text x='590' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Magnifies % Change in EPS</text></svg>",
            "explanation": "Illustrates the cascade multiplication of Operating Leverage and Financial Leverage into total Combined Leverage.",
            "caption": "Figure E6.4: Leverage Cascade Architecture and Total Business Risk"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Degree of Operating Leverage (DOL) and Business Risk",
                "explanation": "Measures the percentage change in operating profit (EBIT) resulting from a 1% change in sales volume: DOL = Contribution / EBIT, driven by fixed operating costs.",
                "terminology": "Degree of Operating Leverage (DOL), Fixed Operating Costs, Business Risk, Break-Even.",
                "example": "If DOL = 2.5, a 10% increase in sales generates a 25% surge in operating profit (EBIT)."
            },
            {
                "point_no": 2,
                "heading": "Degree of Financial Leverage (DFL) and Financial Risk",
                "explanation": "Measures the percentage change in Earnings Per Share (EPS) resulting from a 1% change in operating profit: DFL = EBIT / (EBIT - Interest), driven by debt servicing costs.",
                "terminology": "Degree of Financial Leverage (DFL), Fixed Interest Charges, Financial Gearing.",
                "example": "If DFL = 2.0, a 10% increase in EBIT leads to a 20% amplification in EPS."
            },
            {
                "point_no": 3,
                "heading": "Degree of Combined Leverage (DCL) and Total Risk",
                "explanation": "Quantifies the composite sensitivity of EPS to variations in sales revenue: DCL = DOL * DFL = Contribution / (EBIT - Interest).",
                "terminology": "Degree of Combined Leverage (DCL), Total Enterprise Volatility, EPS Sensitivity.",
                "example": "With DOL = 2.0 and DFL = 1.5: DCL = 3.0; a 10% increase in sales yields a 30% jump in EPS."
            },
            {
                "point_no": 4,
                "heading": "Leverage as a Double-Edged Sword",
                "explanation": "Leverage magnifies shareholder returns during periods of expanding demand, but rapidly accelerates corporate losses and insolvency when revenues contract below break-even.",
                "terminology": "Asymmetric Risk, Magnified Losses, Insolvency Acceleration.",
                "example": "During a 15% revenue decline, high DCL causes a catastrophic 45% collapse in EPS."
            },
            {
                "point_no": 5,
                "heading": "Strategic Risk Balancing (High DOL with Low DFL)",
                "explanation": "Capital structure theory recommends that capital-intensive firms with high fixed operating costs (high DOL) should maintain low debt (low DFL) to prevent excessive combined risk.",
                "terminology": "Trade-off Balance, Conservative Gearing, Capital Intensity.",
                "example": "Automobile manufacturers avoid heavy debt borrowing to absorb cyclical economic downturns."
            }
        ],
        "conclusion": "Leverage analysis balances operating cost structures with debt financing, ensuring total corporate volatility remains within manageable solvency boundaries."
    },
    {
        "id": "exam_fm_q7",
        "subject_id": "mim501",
        "question_no": 7,
        "title": "Explain EBIT-EPS Indifference Point Analysis across Alternative Financing Structures.",
        "intro": {
            "definition": "The EBIT-EPS Indifference Point is the exact level of operating earnings (EBIT) at which two alternative capital financing structures yield identical Earnings Per Share (EPS).",
            "background": "Developed in corporate financial planning to identify the operational profit threshold beyond which debt financing becomes more advantageous than equity financing.",
            "significance": "Provides an analytical decision framework for selecting optimal debt-equity proportions during corporate capital expansions."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><line x1='60' y1='110' x2='640' y2='110' stroke='#617087' stroke-width='2'/><line x1='60' y1='110' x2='60' y2='20' stroke='#617087' stroke-width='2'/><line x1='60' y1='110' x2='600' y2='30' stroke='#377FE6' stroke-width='2'/><text x='580' y='25' font-family='sans-serif' font-size='9' fill='#377FE6'>Equity Plan</text><line x1='200' y1='110' x2='600' y2='15' stroke='#786CE5' stroke-width='2'/><text x='580' y='12' font-family='sans-serif' font-size='9' fill='#786CE5'>Debt Plan (Steeper)</text><circle cx='380' cy='63' r='5' fill='#EF846B'/><text x='380' y='50' font-family='sans-serif' font-size='9' font-weight='700' fill='#EF846B' text-anchor='middle'>Indifference Point</text><text x='640' y='125' font-family='sans-serif' font-size='9' fill='#19283D'>EBIT ($)</text><text x='50' y='20' font-family='sans-serif' font-size='9' fill='#19283D'>EPS ($)</text></svg>",
            "explanation": "Illustrates the intersection point where alternative debt and equity financing plans yield identical EPS; beyond this point, debt generates higher EPS.",
            "caption": "Figure E7.4: Graphical EBIT-EPS Indifference Point Chart"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Mathematical Formulation of the Indifference Point",
                "explanation": "Equates the EPS equations of Plan 1 and Plan 2: [(EBIT - I1) * (1 - T) - PD1] / N1 = [(EBIT - I2) * (1 - T) - PD2] / N2, solving for the indifferent EBIT value.",
                "terminology": "Indifference Point Equation, Operating Profit (EBIT), Interest (I), Share Count (N).",
                "example": "Solving the equation between an all-equity plan and a 50% debt plan yields an indifference EBIT of $40,000."
            },
            {
                "point_no": 2,
                "heading": "Financial Breakeven Point vs Indifference Point",
                "explanation": "Financial breakeven is the minimum EBIT required to cover fixed financial interest and preferred dividends (EPS = 0); the indifference point compares two competing plans.",
                "terminology": "Financial Breakeven Point, Fixed Financial Charges, EPS Zero Point.",
                "example": "If annual interest is $20,000, financial breakeven is exactly $20,000."
            },
            {
                "point_no": 3,
                "heading": "Decision Rule: Operations Above the Indifference Point",
                "explanation": "If projected EBIT is expected to remain consistently higher than the indifference point, the high-debt plan is preferred because financial leverage elevates EPS.",
                "terminology": "Financial Leverage Benefit, EPS Magnification, High-Debt Strategy.",
                "example": "When projected EBIT is $60,000 (above $40,000 indifference), the debt plan yields higher EPS."
            },
            {
                "point_no": 4,
                "heading": "Decision Rule: Operations Below the Indifference Point",
                "explanation": "If projected operating earnings fall below the indifference threshold, the all-equity plan is preferred to avoid heavy fixed interest obligations.",
                "terminology": "Conservative Equity Strategy, Downside Insulation, Interest Burden.",
                "example": "During recessions with EBIT at $25,000, equity financing maintains positive EPS while debt causes losses."
            },
            {
                "point_no": 5,
                "heading": "Incorporation of Preference Share Capital",
                "explanation": "When preferred shares are evaluated, preferred dividends must be divided by (1 - T) in the equation because preferred dividends are not tax-deductible.",
                "terminology": "Preference Dividend Tax Adjustment, Non-Deductibility, After-Tax Payout.",
                "example": "A $7,000 preference dividend at 30% tax requires $10,000 of pre-tax EBIT to service."
            }
        ],
        "conclusion": "EBIT-EPS analysis establishes an empirical profit threshold guiding management to employ debt leverage when operating profits reliably exceed the indifference benchmark."
    },
    {
        "id": "exam_fm_q8",
        "subject_id": "mim501",
        "question_no": 8,
        "title": "Explain Capital Structure Theories: Net Income (NI), Net Operating Income (NOI), and Modigliani-Miller (MM) Hypothesis.",
        "intro": {
            "definition": "Capital structure theories examine whether the proportion of debt versus equity financing affects overall Weighted Average Cost of Capital (WACC) and total enterprise market value.",
            "background": "Founded by David Durand (1952) with the NI and NOI approaches, and revolutionized by Nobel laureates Franco Modigliani and Merton Miller (1958).",
            "significance": "Underpins modern corporate finance, determining whether an optimal capital structure exists that minimizes capital costs and maximizes firm value."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='120' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Net Income (NI)</text><text x='120' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Durand (Relevant)</text><text x='120' y='92' font-family='sans-serif' font-size='8' fill='#369B72' text-anchor='middle'>Debt increases firm value</text><rect x='250' y='30' width='180' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='340' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Net Operating Income</text><text x='340' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Durand (Irrelevant)</text><text x='340' y='92' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>WACC remains constant</text><rect x='470' y='30' width='190' height='80' rx='6' fill='#E9E8F8' stroke='#28A994'/><text x='565' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#1B6F61' text-anchor='middle'>MM Hypothesis (1958)</text><text x='565' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Capital structure irrelevant</text><text x='565' y='92' font-family='sans-serif' font-size='8' fill='#28A994' text-anchor='middle'>Arbitrage Restores Parity</text></svg>",
            "explanation": "Contrasts the Net Income (relevance), Net Operating Income (irrelevance), and Modigliani-Miller Arbitrage theories of capital structure.",
            "caption": "Figure E8.4: Capital Structure Paradigms and Firm Valuation Effects"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Net Income (NI) Approach: Relevance Theory",
                "explanation": "David Durand argued that because debt is cheaper than equity (Kd < Ke) and risk is perceived as constant, increasing debt gearing continuously lowers overall WACC and raises firm market value.",
                "terminology": "Net Income Approach, Capital Gearing, Value Accretion, Constant Ke.",
                "example": "A firm borrowing 90% debt theoretically minimizes its WACC under the NI hypothesis."
            },
            {
                "point_no": 2,
                "heading": "Net Operating Income (NOI) Approach: Irrelevance Theory",
                "explanation": "Durand's counter-theory posited that higher debt elevates financial risk, causing equity investors to demand higher return (Ke rises), perfectly offsetting the cheap debt advantage and keeping WACC constant.",
                "terminology": "NOI Approach, Offsetting Risk Premium, Constant WACC, Value Invariance.",
                "example": "Any cost reduction from cheap debt is negated by equity holders demanding higher returns."
            },
            {
                "point_no": 3,
                "heading": "Traditional Theory and the U-Shaped WACC Curve",
                "explanation": "Proponents (Ezra Solomon) showed that moderate debt lowers WACC up to an optimum point; beyond this optimal gearing, bankruptcy risks escalate both Kd and Ke, creating a U-shaped WACC curve.",
                "terminology": "Traditional Theory, Optimal Capital Structure, U-Shaped WACC, Bankruptcy Distress.",
                "example": "Maintaining a conservative 40% debt structure minimizes overall capital cost."
            },
            {
                "point_no": 4,
                "heading": "Modigliani-Miller (MM) Hypothesis without Taxes",
                "explanation": "In 1958, MM proved that in perfect frictionless markets (zero taxes, zero transaction costs), a firm's total value is determined by its operating assets, making capital structure completely irrelevant.",
                "terminology": "MM Proposition I, Law of One Price, Frictionless Markets, Asset Earning Power.",
                "example": "Two identical operational firms must trade at identical total enterprise market values."
            },
            {
                "point_no": 5,
                "heading": "The Arbitrage Mechanism Restoring Valuation Parity",
                "explanation": "MM demonstrated that if an overvalued levered firm trades at a premium, investors engage in arbitrage by selling levered shares and taking on personal homemade leverage, driving market prices back to parity.",
                "terminology": "Arbitrage Process, Homemade Leverage, Market Equilibrium, Value Parity.",
                "example": "Investors borrowing on personal account restore price equilibrium between levered and unlevered firms."
            }
        ],
        "conclusion": "Capital structure theory demonstrates that in frictionless markets debt is irrelevant via arbitrage, while real-world tax shields and distress costs establish an optimal debt ratio."
    },
    {
        "id": "exam_fm_q9",
        "subject_id": "mim501",
        "question_no": 9,
        "title": "Explain James E. Walter's Dividend Model and Optimal Payout Policies across Growth, Normal, and Declining Firms.",
        "intro": {
            "definition": "Walter's model is a theoretical valuation framework proving that corporate dividend policy directly affects enterprise share price based on the relationship between internal return (r) and the cost of capital (k).",
            "background": "Formulated by James E. Walter in 1956 to counter dividend irrelevance theories, demonstrating that dividends are relevant to share valuation.",
            "significance": "Provides clear strategic guidance on whether corporate net earnings should be paid out as dividends or retained for compounding."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><rect x='20' y='30' width='190' height='80' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='115' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Growth Firm (r &gt; k)</text><text x='115' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Internal Return &gt; Cost of Cap</text><text x='115' y='92' font-family='sans-serif' font-size='8' font-weight='700' fill='#369B72' text-anchor='middle'>Optimal Payout: 0%</text><rect x='245' y='30' width='190' height='80' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='340' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Normal Firm (r = k)</text><text x='340' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Internal Return = Cost of Cap</text><text x='340' y='92' font-family='sans-serif' font-size='8' font-weight='700' fill='#786CE5' text-anchor='middle'>Optimal Payout: Indifferent</text><rect x='470' y='30' width='190' height='80' rx='6' fill='#F7F8FC' stroke='#EF846B'/><text x='565' y='55' font-family='sans-serif' font-size='11' font-weight='700' fill='#EF846B' text-anchor='middle'>Declining Firm (r &lt; k)</text><text x='565' y='75' font-family='sans-serif' font-size='8' fill='#19283D' text-anchor='middle'>Internal Return &lt; Cost of Cap</text><text x='565' y='92' font-family='sans-serif' font-size='8' font-weight='700' fill='#D65F64' text-anchor='middle'>Optimal Payout: 100%</text></svg>",
            "explanation": "Illustrates Walter's optimal dividend payout mandates across Growth (0%), Normal (Indifferent), and Declining (100%) enterprise profiles.",
            "caption": "Figure E9.4: Walter's Model Optimal Payout Policies by Firm Growth Profile"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Mathematical Formulation of Walter's Valuation Model",
                "explanation": "Share price is determined by discounting dividends plus the present value of retained earnings: P = [ D + (r / k) * (E - D) ] / k, where D is dividend, E is earnings, r is internal return, and k is cost of capital.",
                "terminology": "Walter's Formula, Internal Rate of Return (r), Cost of Capital (k), EPS (E), DPS (D).",
                "example": "With E=$10, D=$4, r=15%, k=10%: P = [4 + (0.15/0.10)*(10 - 4)] / 0.10 = $130."
            },
            {
                "point_no": 2,
                "heading": "Growth Firms (r > k): Zero Dividend Payout Strategy",
                "explanation": "When internal investment return exceeds the cost of capital, shareholders maximize wealth when the firm retains 100% of profits (0% payout) to compound earnings internally.",
                "terminology": "Growth Firm, Internal Compounding, Zero Payout, Share Price Maximization.",
                "example": "Setting D = 0 in the above example elevates share price to $150, confirming the 0% payout rule."
            },
            {
                "point_no": 3,
                "heading": "Declining Firms (r < k): 100% Dividend Distribution Strategy",
                "explanation": "When internal return is inferior to market returns, retaining earnings destroys capital; wealth is maximized by distributing 100% of earnings as cash dividends.",
                "terminology": "Declining Firm, Capital Destruction, 100% Payout Ratio, Cash Distribution.",
                "example": "If r = 8% and k = 10%, paying a 100% dividend yields the highest theoretical share price."
            },
            {
                "point_no": 4,
                "heading": "Normal Firms (r = k): Dividend Indifference",
                "explanation": "When internal return equals the market cost of capital, dividend payout policy has zero impact on share price; investors earn identical returns whether profits are paid or retained.",
                "terminology": "Normal Firm, Indifferent Payout, Invariance.",
                "example": "Share price remains completely constant whether payout is 0%, 50%, or 100%."
            },
            {
                "point_no": 5,
                "heading": "Critical Assumptions and Practical Limitations",
                "explanation": "Assumes 100% internal financing (no external debt/equity issues) and constant r and k, which oversimplifies real-world market imperfections.",
                "terminology": "Internal Equity Financing, Perpetual Returns, Constant Cost of Capital.",
                "example": "In practice, diminishing marginal returns cause internal return (r) to decline as investment expands."
            }
        ],
        "conclusion": "Walter's model proves that dividend policy is relevant to share price, prescribing retention for high-growth firms and full distribution for declining enterprises."
    },
    {
        "id": "exam_fm_q10",
        "subject_id": "mim501",
        "question_no": 10,
        "title": "Explain Working Capital Management: Operating Cycle, Baumol Cash Model, and EOQ Inventory Optimization.",
        "intro": {
            "definition": "Working capital management is the operational financial discipline of managing current assets and liabilities to maintain daily solvency while maximizing profitability.",
            "background": "Developed by corporate financial controllers to prevent technical insolvency stemming from liquidity traps during revenue expansions.",
            "significance": "Balances the trade-off between liquidity (safety buffer) and profitability (avoiding idle cash drag on return on capital)."
        },
        "diagram": {
            "svg": "<svg viewBox='0 0 700 140' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:6px;border:1px solid #E5E9F1;'><circle cx='80' cy='70' r='40' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><text x='80' y='68' font-family='sans-serif' font-size='10' font-weight='700' fill='#377FE6' text-anchor='middle'>Cash</text><text x='80' y='82' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Capital</text><path d='M 125 60 L 195 40' stroke='#377FE6' stroke-width='2'/><circle cx='240' cy='40' r='35' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><text x='240' y='42' font-family='sans-serif' font-size='9' font-weight='700' fill='#786CE5' text-anchor='middle'>Raw Mat</text><path d='M 280 40 L 360 40' stroke='#786CE5' stroke-width='2'/><circle cx='400' cy='40' r='35' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><text x='400' y='42' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994' text-anchor='middle'>WIP &amp; FG</text><path d='M 440 45 L 510 65' stroke='#28A994' stroke-width='2'/><circle cx='550' cy='70' r='40' fill='#E9E8F8' stroke='#F2C75C' stroke-width='2'/><text x='550' y='68' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>Receivables</text><text x='550' y='82' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Debtors Book</text><path d='M 510 85 L 125 85' stroke='#369B72' stroke-width='2' stroke-dasharray='4,4'/><text x='320' y='105' font-family='sans-serif' font-size='9' font-weight='700' fill='#369B72' text-anchor='middle'>Cash Collection from Customers (Completes Cycle)</text></svg>",
            "explanation": "Illustrates the continuous cash-to-cash operating cycle moving from procurement through manufacturing and customer collections.",
            "caption": "Figure E10.4: Enterprise Cash-to-Cash Operating Cycle Architecture"
        },
        "points": [
            {
                "point_no": 1,
                "heading": "Operating Cycle Length and Formula",
                "explanation": "The Net Operating Cycle measures the time required to convert raw materials into cash: Operating Cycle = Raw Material Days + WIP Days + Finished Goods Days + Debtors Days - Creditors Deferral Days.",
                "terminology": "Operating Cycle, Cash Conversion Cycle, Gross vs Net Working Capital, Velocity.",
                "example": "A cycle of 45 days means the firm must finance 45 days of operational expenses."
            },
            {
                "point_no": 2,
                "heading": "Baumol's Optimum Cash Balance Model",
                "explanation": "Adapts inventory lot sizing to cash management, balancing transaction fees of converting marketable securities against interest opportunity costs: C* = sqrt(2 * T * F / i).",
                "terminology": "Baumol Model, Cash Lot Size (C*), Transaction Cost (F), Opportunity Cost (i).",
                "example": "With $1M annual cash needs, $50 transfer fee, and 8% interest rate: optimal transfer lot is $35,355."
            },
            {
                "point_no": 3,
                "heading": "Miller-Orr Stochastic Cash Control Model",
                "explanation": "Accommodates random daily cash fluctuations by establishing Upper (H), Return (Z), and Lower (L) boundaries based on daily variance: Z = cuberoot(3 * F * Var / 4i) + L.",
                "terminology": "Miller-Orr Model, Cash Boundaries, Cash Variance, Automatic Rebalancing.",
                "example": "When cash balance touches the upper limit H, excess cash is automatically swept into securities."
            },
            {
                "point_no": 4,
                "heading": "Economic Order Quantity (EOQ) Inventory Optimization",
                "explanation": "Pinpoints the exact replenishment order quantity that minimizes the total annual cost of ordering and inventory holding: EOQ = sqrt(2 * D * S / H).",
                "terminology": "EOQ, Annual Demand (D), Ordering Cost (S), Carrying Cost (H), Minimum Total Cost.",
                "example": "At EOQ, total annual ordering costs exactly equal total annual carrying costs."
            },
            {
                "point_no": 5,
                "heading": "ABC Analysis for Selective Inventory Control",
                "explanation": "Classifies stock based on annual consumption value: Category A (70% value, 10% volume, stringent control); Category B (20% value, 20% volume); Category C (10% value, 70% volume).",
                "terminology": "ABC Analysis, Pareto Principle (80/20 Rule), Selective Inventory Control.",
                "example": "Maintaining tight physical lockup and daily reconciliation on Category A components."
            }
        ],
        "conclusion": "Working capital management optimizes the cash-to-cash operating cycle using mathematical models to guarantee daily solvency without dragging profitability."
    }
]
