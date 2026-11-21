# Financial Management (MIM501) Lessons Generator
from generator.helper import create_topic

def get_fm_modules():
    return [
        {
            "module_no": 1,
            "title": "Introduction: Concepts, Scope, Functions & Cost of Capital",
            "hours": 6,
            "marks": 15,
            "topics": [
                create_topic(
                    "fm_m1_t1",
                    "Nature, Scope, Objectives of Financial Management, and Weighted Average Cost of Capital (WACC)",
                    ["Profit vs Wealth Maximization", "Three Executive Financial Decisions (Financing, Investing, Dividend)", "Cost of Specific Capital (Debt, Preference, Equity)", "Weighted Average Cost of Capital (WACC) Calculation"],
                    "Financial Management is the managerial discipline concerned with the planning, procuring, allocating, and controlling of corporate financial resources to maximize shareholder economic wealth.",
                    "Evolved from descriptive corporate financing during the early 20th century to analytical decision-making grounded in modern portfolio and capital structure theory.",
                    "Provides the financial governance framework for strategic resource deployment, investor valuation, and corporate solvency.",
                    ["Differentiate Wealth Maximization from short-sighted Profit Maximization.", "Analyze the triad of core corporate financial decisions (Investing, Financing, Dividend).", "Compute individual component costs of Debt (Kd), Preference (Kp), and Equity (Ke).", "Calculate Weighted Average Cost of Capital (WACC) using market and book value weights."],
                    "Corporate value equals the sum of discounted future free cash flows. Lowering WACC directly amplifies enterprise market value.",
                    [
                        ("Wealth Maximization", "Maximizing the net present value of equity shareholder market capitalization."),
                        ("Cost of Capital", "Minimum expected rate of return required by providers of capital to justify investment."),
                        ("WACC", "Composite overall cost of capital weighted proportionally across equity, debt, and preferred capital."),
                        ("Tax Shield on Debt", "Interest on debt is tax-deductible, reducing effective cost of debt: Kd = I(1 - t) / Net Proceeds.")
                    ],
                    "1. Time Value of Money: Wealth maximization accounts for cash flow timing and duration, unlike simple accounting profit.\n2. Risk Recognition: Higher discount rates are applied to riskier prospective cash flow streams.",
                    "Capital Raising (Debt/Equity) -> Investment in Productive Assets -> Operating Cash Flow Generation -> Value Maximization.",
                    [
                        "1. Finance executive evaluates capital needs based on long-term corporate growth plans.",
                        "2. Target capital structure balances low-cost debt against financial bankruptcy risk.",
                        "3. Specific costs of debt, equity, and retained earnings are computed.",
                        "4. WACC serves as the hurdle benchmark discount rate for all capital budgeting decisions."
                    ],
                    ["Criterion", "Profit Maximization", "Wealth Maximization"],
                    [
                        ["Primary Objective", "Maximizing short-term accounting net profit", "Maximizing market price of equity shares (NPV)"],
                        ["Time Value of Money", "Ignores cash flow timing and duration", "Strictly incorporates time value of money"],
                        ["Risk Consideration", "Ignores business and financial risk factors", "Explicitly incorporates risk and uncertainty premiums"],
                        ["Longevity & Ethics", "May incentivize hazardous cost-cutting", "Focuses on sustainable long-term enterprise survival"]
                    ],
                    "// WACC Formula\nKo = (We * Ke) + (Wd * Kd * (1 - T)) + (Wp * Kp)\nWhere W = Weight of source, K = Specific cost, T = Corporate tax rate",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Financing</text><text x='110' y='85' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Debt vs Equity</text><text x='110' y='105' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Capital Structure</text><text x='110' y='125' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Minimizes WACC</text><path d='M 195 90 L 245 90' stroke='#377FE6' stroke-width='2'/><rect x='250' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='330' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Investing</text><text x='330' y='85' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Capital Budgeting</text><text x='330' y='105' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Working Capital</text><text x='330' y='125' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>ROIC &gt; WACC</text><path d='M 415 90 L 465 90' stroke='#786CE5' stroke-width='2'/><rect x='470' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='550' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Dividend</text><text x='550' y='85' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Payout vs Retained</text><text x='550' y='105' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Internal Financing</text><text x='550' y='125' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Signaling Value</text><path d='M 635 90 L 685 90' stroke='#28A994' stroke-width='2'/><rect x='690' y='30' width='85' height='120' rx='8' fill='#E9E8F8' stroke='#F2C75C'/><text x='732' y='75' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>Wealth</text><text x='732' y='95' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72' text-anchor='middle'>Max</text><text x='732' y='120' font-family='sans-serif' font-size='8' fill='#617087' text-anchor='middle'>Share Price</text></svg>""",
                    "Figure 1.1: Triad of Financial Management Decisions Driving Shareholder Wealth Maximization",
                    "Numerical Demonstration of After-Tax Cost of Debt vs Equity",
                    "Given: 10% Debentures issued at par ($100), Corporate Tax rate t = 30%.\nPre-tax Kd = 10%.\nAfter-tax Cost of Debt: Kd(after-tax) = 10% * (1 - 0.30) = 7.0%.\nIf Cost of Equity Ke = 14%, and Capital Structure is 40% Debt and 60% Equity:\nWACC = (0.40 * 7.0%) + (0.60 * 14.0%) = 2.8% + 8.4% = 11.2%.",
                    [
                        "Financial management centers on three interlinked decisions: Investing, Financing, and Dividend.",
                        "Wealth Maximization is superior to Profit Maximization as it accounts for time value of money and risk.",
                        "Debt provides a valuable corporate tax shield because interest payments are tax-deductible expenses.",
                        "Cost of Equity (Ke) can be determined using Dividend Growth or Capital Asset Pricing Model (CAPM).",
                        "WACC represents the minimum hurdle return a firm must generate on its aggregate asset investments.",
                        "Market value weights provide a more accurate reflection of current opportunity costs than historical book values."
                    ],
                    "Financial management governs corporate capital allocation to maximize equity market value through optimal WACC management.",
                    "Wealth Maximization, Cost of Debt, Cost of Equity, WACC, Hurdle Rate, Tax Shield.",
                    "Capital Raising -> Component Cost Calculation -> WACC Weighting -> Hurdle Rate Deployment.",
                    "Overlooking the tax deductibility of debt interest, leading to inflated after-tax cost of debt calculations."
                )
            ]
        },
        {
            "module_no": 2,
            "title": "Analysis and Interpretation of Corporate Final Accounts",
            "hours": 6,
            "marks": 15,
            "topics": [
                create_topic(
                    "fm_m2_t1",
                    "Financial Ratio Analysis and DuPont Decomposition System",
                    ["Liquidity Ratios (Current, Quick)", "Solvency & Leverage Ratios (Debt-Equity, Interest Coverage)", "Activity / Turnover Ratios (Inventory, Debtors, Working Capital)", "Profitability Ratios (Gross, Net, ROI, ROE)", "Three-Tier DuPont Decomposition"],
                    "Financial ratio analysis is the quantitative evaluation of an enterprise's liquidity, operational efficiency, solvency, and profitability through mathematical relationships extracted from final balance sheets and profit & loss statements.",
                    "Refined by financial analysts and codified by the DuPont Corporation in 1919 to diagnose operational drivers behind Return on Equity (ROE).",
                    "Essential for commercial credit scoring, equity stock valuation, corporate governance, and debt covenant monitoring.",
                    ["Compute and interpret short-term liquidity ratios (Current, Quick, Cash Ratio).", "Assess long-term capital solvency using Debt-to-Equity and Interest Coverage Ratios.", "Evaluate operational activity using Inventory Turnover and Debtors Collection Period.", "Decompose Return on Equity (ROE) using the three-step DuPont analysis model."],
                    "Ratios establish standardized metrics enabling benchmark comparison across temporal trends and industry peer groups.",
                    [
                        ("Current Ratio", "Current Assets / Current Liabilities; measures immediate solvency (Benchmark: 2:1)."),
                        ("Quick / Acid-Test Ratio", "(Current Assets - Inventory - Prepaid Expenses) / Current Liabilities (Benchmark: 1:1)."),
                        ("Debt-Equity Ratio", "Total Long-Term Debt / Shareholders' Net Worth; measures financial leverage."),
                        ("Interest Coverage Ratio", "EBIT / Annual Interest Expense; measures ability to service debt obligations."),
                        ("DuPont Model", "ROE = Profit Margin * Asset Turnover * Financial Leverage Multiplier.")
                    ],
                    "1. Liquidity vs Profitability Tradeoff: Excessive idle liquid cash buffers safety but degrades overall asset turnover and ROE.\n2. Financial Leverage Amplification: Debt magnifies ROE during profitable periods, but accelerates insolvency during revenue downturns.",
                    "Raw Financial Statements -> Ratio Computation -> Cross-Sectional & Time-Series Benchmarking -> DuPont Diagnosis.",
                    [
                        "1. Certified Balance Sheet and Income Statement data extracted.",
                        "2. Liquidity, activity, leverage, and profitability ratios compiled.",
                        "3. DuPont decomposition reveals whether ROE is driven by margin, efficiency, or debt leverage.",
                        "4. Corrective actions target weak inventory velocity, excessive collection delays, or high gearing."
                    ],
                    ["Ratio Category", "Key Indicator", "Formula", "Analytical Significance"],
                    [
                        ["Liquidity", "Current Ratio", "Current Assets / Current Liabilities", "Short-term debt repayment safety buffer"],
                        ["Solvency", "Debt-Equity Ratio", "Total Debt / Net Worth", "Long-term creditor capital protection cushion"],
                        ["Activity", "Inventory Turnover", "Cost of Goods Sold / Average Inventory", "Efficiency of inventory conversion to sales"],
                        ["Profitability", "ROE (DuPont)", "Net Profit Margin * Asset Turnover * Equity Multiplier", "Ultimate profitability generated per dollar of equity"]
                    ],
                    "// DuPont 3-Step Identity\nROE = (Net Income / Sales) * (Sales / Total Assets) * (Total Assets / Equity)\nROE = Net Profit Margin * Asset Turnover * Equity Multiplier",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='60' width='140' height='70' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='100' y='90' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Net Profit Margin</text><text x='100' y='110' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>Net Income / Sales</text><text x='190' y='100' font-family='sans-serif' font-size='16' font-weight='700' fill='#617087'>*</text><rect x='215' y='60' width='150' height='70' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='290' y='90' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Asset Turnover</text><text x='290' y='110' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>Sales / Total Assets</text><text x='385' y='100' font-family='sans-serif' font-size='16' font-weight='700' fill='#617087'>*</text><rect x='410' y='60' width='160' height='70' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='490' y='90' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>Equity Multiplier</text><text x='490' y='110' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>Total Assets / Equity</text><text x='590' y='100' font-family='sans-serif' font-size='16' font-weight='700' fill='#617087'>=</text><rect x='615' y='45' width='155' height='100' rx='8' fill='#E9E8F8' stroke='#F2C75C'/><text x='692' y='85' font-family='sans-serif' font-size='13' font-weight='700' fill='#19283D' text-anchor='middle'>Return on Equity</text><text x='692' y='110' font-family='sans-serif' font-size='14' font-weight='700' fill='#369B72' text-anchor='middle'>ROE</text></svg>""",
                    "Figure 2.1: DuPont Three-Tier System Decomposing Return on Equity (ROE)",
                    "DuPont Breakdown Analysis for an Industrial Enterprise",
                    "Company A: Margin = 8%, Asset Turnover = 1.5x, Equity Multiplier = 2.0x.\nROE = 0.08 * 1.5 * 2.0 = 24.0%.\nDiagnosis: Strong ROE achieved through balanced operational profitability, efficient plant asset utilization, and moderate conservative debt leverage.",
                    [
                        "Liquidity ratios examine the firm's capacity to fulfill immediate short-term obligations.",
                        "Standard benchmarks are 2:1 for Current Ratio and 1:1 for Quick (Acid-Test) Ratio.",
                        "Solvency ratios (Debt-Equity, Interest Coverage) assess long-term insolvency and bankruptcy resistance.",
                        "The DuPont framework demonstrates that ROE is driven by: Operating Margin * Asset Velocity * Financial Leverage.",
                        "Inventory Turnover and Debtors Collection Period measure the efficiency of operational working capital cycles.",
                        "High financial leverage boosts ROE only when Return on Capital Employed (ROCE) exceeds interest rates on debt."
                    ],
                    "Ratio analysis and DuPont decomposition transform static financial statements into actionable diagnostics of corporate operational health.",
                    "Ratio Analysis, Current Ratio, Quick Ratio, Debt-Equity Ratio, ROE, DuPont Analysis.",
                    "Statement Extraction -> Ratio Compilation -> Trend Benchmarking -> DuPont Root Cause Analysis.",
                    "Including inventory and prepaid expenses in the quick ratio numerator; quick assets strictly exclude illiquid stock."
                )
            ]
        },
        {
            "module_no": 3,
            "title": "Capital Budgeting",
            "hours": 4,
            "marks": 10,
            "topics": [
                create_topic(
                    "fm_m3_t1",
                    "Capital Budgeting Evaluation Techniques: Payback Period, ARR, NPV, IRR, and PI",
                    ["Non-Discounted Methods (Payback, Accounting Rate of Return)", "Discounted Cash Flow (DCF) Methods", "Net Present Value (NPV) Criterion", "Internal Rate of Return (IRR) & Interpolation", "Profitability Index (PI) & Capital Rationing", "NPV vs IRR Conflicts"],
                    "Capital Budgeting is the long-term strategic decision-making process for evaluating, selecting, and committing capital outlays to investment projects whose economic benefits extend beyond one fiscal year.",
                    "Formulated in modern financial economics by Joel Dean (1951) to replace ad-hoc managerial intuition with discounted cash flow rigor.",
                    "Determines long-term corporate growth, fixed asset expansion, technological competitiveness, and firm survival.",
                    ["Calculate non-discounted metrics: Traditional Payback Period and Accounting Rate of Return (ARR).", "Compute Net Present Value (NPV) utilizing appropriate weighted average discount rates.", "Calculate Internal Rate of Return (IRR) via financial interpolation.", "Resolve mutually exclusive project selection conflicts between NPV and IRR."],
                    "Accept projects where NPV > 0, IRR > Cost of Capital (k), and Profitability Index (PI) > 1.0.",
                    [
                        ("Net Present Value (NPV)", "Present value of future operating cash inflows minus initial capital outlay: PV(Inflows) - Initial Outlay."),
                        ("Internal Rate of Return (IRR)", "Discount rate that equates the present value of future cash inflows to initial investment (NPV = 0)."),
                        ("Payback Period", "Time span required for cumulative cash inflows to equal the initial capital investment outlay."),
                        ("Profitability Index (PI)", "Ratio of present value of inflows to initial cash outlay (Benefit-Cost Ratio).")
                    ],
                    "1. NPV Supremacy: When NPV and IRR give conflicting recommendations for mutually exclusive projects, the NPV decision rules because it assumes cash reinvestment at the cost of capital.\n2. Cash Flow Focus: Capital budgeting decisions rely on incremental after-tax cash flows, not accounting profits.",
                    "Project Outlay (CF0) -> Annual Incremental Cash Inflows (CF1..n) -> Discounting at WACC -> NPV / IRR / PI Calculation -> Accept/Reject.",
                    [
                        "1. Project proposals compiled and incremental after-tax cash flows projected.",
                        "2. Cash flows discounted using corporate hurdle cost of capital (k).",
                        "3. NPV calculated; independent projects with positive NPV accepted.",
                        "4. Mutually exclusive projects ranked by highest absolute NPV.",
                        "5. Capital rationing allocates constrained budgets according to highest Profitability Index (PI)."
                    ],
                    ["Evaluation Technique", "Discounted Cash Flow?", "Decision Criterion", "Reinvestment Rate Assumption"],
                    [
                        ["Payback Period", "No (Traditional)", "Accept if Payback < Target Period", "None (ignores cash after payback)"],
                        ["Accounting Rate of Return (ARR)", "No (Uses P&L Profit)", "Accept if ARR > Target Return", "None (accounting profit based)"],
                        ["Net Present Value (NPV)", "Yes", "Accept if NPV > 0", "Cost of Capital (WACC) - Highly Realistic"],
                        ["Internal Rate of Return (IRR)", "Yes", "Accept if IRR > Cost of Capital (k)", "Equal to project's own IRR - Often Unrealistic"]
                    ],
                    "// Core Mathematical Equations\nNPV = SUM [ CF_t / (1 + k)^t ] - CF_0\nIRR: Discount rate 'r' where SUM [ CF_t / (1 + r)^t ] = CF_0\nPI = PV of Inflows / Initial Outlay",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='120' rx='8' fill='#FFF2EB' stroke='#EF846B'/><text x='110' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#EF846B' text-anchor='middle'>Year 0: Outflow</text><text x='110' y='95' font-family='monospace' font-size='13' font-weight='700' fill='#D65F64' text-anchor='middle'>-$100,000</text><text x='110' y='125' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Initial Capital Outlay</text><path d='M 195 90 L 265 90' stroke='#377FE6' stroke-width='2'/><rect x='270' y='30' width='230' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='385' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Years 1-5: Cash Inflows</text><text x='385' y='85' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>Discounted at WACC (k = 10%)</text><text x='385' y='105' font-family='monospace' font-size='10' fill='#28A994' text-anchor='middle'>PV(Inflows) = $125,400</text><text x='385' y='125' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>CF_t / (1 + k)^t</text><path d='M 505 90 L 575 90' stroke='#28A994' stroke-width='2'/><rect x='580' y='30' width='190' height='120' rx='8' fill='#E9E8F8' stroke='#28A994'/><text x='675' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#1B6F61' text-anchor='middle'>Decision Output</text><text x='675' y='85' font-family='monospace' font-size='11' font-weight='700' fill='#369B72' text-anchor='middle'>NPV = +$25,400</text><text x='675' y='105' font-family='monospace' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>PI = 1.254 | IRR &gt; k</text><text x='675' y='130' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72' text-anchor='middle'>STATUS: ACCEPT</text></svg>""",
                    "Figure 3.1: Discounted Cash Flow (DCF) Capital Budgeting Timeline",
                    "Interpolation Formula for Calculating IRR Manually",
                    "Given: At discount rate L = 12%, NPV_L = +$4,500. At discount rate H = 16%, NPV_H = -$2,500.\nIRR = L + [ NPV_L / (NPV_L - NPV_H) ] * (H - L)\nIRR = 12% + [ 4500 / (4500 - (-2500)) ] * (16% - 12%)\nIRR = 12% + [ 4500 / 7000 ] * 4% = 12% + 2.57% = 14.57%.",
                    [
                        "Capital budgeting evaluates long-term investment decisions with multi-year cash flow horizons.",
                        "Traditional Payback Period ignores cash flows occurring after the payback threshold.",
                        "NPV is the gold standard criterion; accept all independent projects with NPV > 0.",
                        "IRR is the internal break-even discount rate where project NPV equals exactly zero.",
                        "In mutually exclusive project conflicts, NPV takes precedence due to realistic reinvestment rate assumptions.",
                        "Profitability Index (PI = PV of Inflows / Outlay) is the optimal metric under capital rationing constraints."
                    ],
                    "Capital budgeting deploys discounted cash flow methodologies to ensure long-term corporate capital yields returns exceeding the cost of capital.",
                    "Capital Budgeting, Payback Period, Net Present Value, Internal Rate of Return, Profitability Index, DCF.",
                    "Cash Flow Projection -> Hurdle Rate Discounting -> NPV/IRR Evaluation -> Mutually Exclusive Selection.",
                    "Confusing accounting profit with operating cash flow; capital budgeting strictly requires after-tax cash flows (PAT + Depreciation)."
                )
            ]
        },
        {
            "module_no": 4,
            "title": "Leverage Analysis & Capital Structure Theories",
            "hours": 6,
            "marks": 15,
            "topics": [
                create_topic(
                    "fm_m4_t1",
                    "Operating, Financial, and Combined Leverage, EBIT-EPS Analysis, and Capital Structure Theories",
                    ["Operating Leverage (DOL) & Fixed Costs", "Financial Leverage (DFL) & Debt Servicing", "Combined Leverage (DCL)", "EBIT-EPS Indifference Point Analysis", "Capital Structure Theories: NI, NOI, Traditional & Modigliani-Miller (MM)"],
                    "Leverage analysis examines the sensitivity of operating profit (EBIT) and earnings per share (EPS) to percentage variations in sales volume, while capital structure theories investigate whether debt-equity financing proportions impact enterprise valuation.",
                    "Founded by Franco Modigliani and Merton Miller in their seminal 1958 paper demonstrating capital structure irrelevance in perfect markets.",
                    "Guides corporate debt capacity determination, credit ratings management, and financial solvency optimization.",
                    ["Calculate Degree of Operating Leverage (DOL), Financial Leverage (DFL), and Combined Leverage (DCL).", "Determine the EBIT-EPS Indifference Point across alternative capital financing structures.", "Compare the Net Income (NI) Approach with the Net Operating Income (NOI) Approach.", "Explain the Modigliani-Miller (MM) Hypothesis with and without corporate taxes."],
                    "Operating leverage arises from fixed operating costs; financial leverage arises from fixed debt interest costs. Combined leverage reflects total enterprise risk.",
                    [
                        ("Degree of Operating Leverage (DOL)", "% Change in EBIT / % Change in Sales = Contribution / EBIT."),
                        ("Degree of Financial Leverage (DFL)", "% Change in EPS / % Change in EBIT = EBIT / (EBIT - Interest)."),
                        ("Degree of Combined Leverage (DCL)", "DOL * DFL = Contribution / (EBIT - Interest); measures total risk."),
                        ("Indifference Point", "EBIT level at which two competing capital structures produce identical Earnings Per Share (EPS)."),
                        ("MM Arbitrage Process", "Investors substitute personal leverage for corporate leverage to restore valuation parity.")
                    ],
                    "1. Leverage Double-Edged Sword: When revenues exceed the break-even point, leverage magnifies shareholder EPS; when sales drop, leverage rapidly causes losses.\n2. Tax Shield Value: Corporate taxes render debt attractive up to the point where bankruptcy distress costs outweigh interest tax savings.",
                    "Sales -> (Less Variable Cost) -> Contribution -> (Less Fixed Operating Cost) -> EBIT -> (Less Interest) -> EBT -> EPS.",
                    [
                        "1. Operational cost structure sets Degree of Operating Leverage (DOL).",
                        "2. Debt issuance creates fixed interest obligations setting Degree of Financial Leverage (DFL).",
                        "3. Multiplying DOL by DFL yields total combined volatility of earnings per share.",
                        "4. Management uses EBIT-EPS analysis to select equity vs debt financing based on projected sales."
                    ],
                    ["Theory", "Proponent", "Impact of Debt on Firm Value (V)", "Impact of Debt on WACC (Ko)"],
                    [
                        ["Net Income (NI) Approach", "David Durand", "Higher debt increases firm value", "WACC decreases continuously with debt"],
                        ["Net Operating Income (NOI)", "David Durand", "Debt proportion has NO effect on firm value", "WACC remains completely constant"],
                        ["Traditional Theory", "Solomon, Ezra", "Increases value up to optimum debt level", "U-shaped WACC with distinct minimum point"],
                        ["Modigliani-Miller (No Tax)", "Modigliani & Miller (1958)", "Capital structure is irrelevant (Arbitrage)", "WACC remains constant across all gearing"]
                    ],
                    "// Mathematical Formulas\nDOL = Contribution / EBIT\nDFL = EBIT / (EBIT - I)\nDCL = Contribution / (EBIT - I)\nIndifference: [(EBIT - I1)(1 - t)] / N1 = [(EBIT - I2)(1 - t)] / N2",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='210' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='135' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Operating Leverage</text><text x='50' y='80' font-family='sans-serif' font-size='10' fill='#19283D'>Driven by Fixed Operating Costs</text><text x='50' y='105' font-family='monospace' font-size='11' fill='#19283D'>DOL = %Δ EBIT / %Δ Sales</text><text x='50' y='130' font-family='sans-serif' font-size='9' fill='#617087'>Business / Operational Risk</text><path d='M 245 90 L 295 90' stroke='#377FE6' stroke-width='2'/><rect x='300' y='30' width='210' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='405' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Financial Leverage</text><text x='320' y='80' font-family='sans-serif' font-size='10' fill='#19283D'>Driven by Fixed Debt Interest</text><text x='320' y='105' font-family='monospace' font-size='11' fill='#19283D'>DFL = %Δ EPS / %Δ EBIT</text><text x='320' y='130' font-family='sans-serif' font-size='9' fill='#617087'>Financial / Bankruptcy Risk</text><path d='M 515 90 L 565 90' stroke='#786CE5' stroke-width='2'/><rect x='570' y='30' width='200' height='120' rx='8' fill='#E9E8F8' stroke='#28A994'/><text x='670' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#1B6F61' text-anchor='middle'>Combined Leverage</text><text x='590' y='85' font-family='monospace' font-size='11' font-weight='700' fill='#19283D'>DCL = DOL * DFL</text><text x='590' y='110' font-family='sans-serif' font-size='10' fill='#19283D'>Total Enterprise Volatility</text><text x='590' y='135' font-family='sans-serif' font-size='9' font-weight='700' fill='#28A994'>Magnifies % Change in EPS</text></svg>""",
                    "Figure 4.1: Cascade Structure of Operating, Financial, and Combined Leverage",
                    "EBIT-EPS Indifference Point Calculation",
                    "Option 1: All Equity (100,000 shares, No interest).\nOption 2: 50% Debt (50,000 shares, $20,000 annual interest). Tax rate = 30%.\nEquation: [EBIT * (1 - 0.3)] / 100,000 = [(EBIT - 20,000) * (1 - 0.3)] / 50,000\nSimplifying: 0.7 EBIT / 100,000 = 0.7 (EBIT - 20,000) / 50,000\nEBIT / 2 = EBIT - 20,000 => EBIT = $40,000.\nInterpretation: At EBIT of $40,000, both financing options produce identical EPS of $0.28.",
                    [
                        "Operating leverage measures business risk arising from fixed operating overhead costs.",
                        "Financial leverage measures financial risk arising from fixed interest obligations on debt.",
                        "Combined Leverage (DCL = DOL * DFL) quantifies the net percentage variation in EPS for a 1% change in sales.",
                        "The EBIT-EPS indifference point identifies the exact operating profit where competing financing plans yield equal EPS.",
                        "Traditional theory posits an optimal capital structure with a distinct minimum WACC.",
                        "Modigliani-Miller (1958) demonstrated capital structure irrelevance in perfect frictionless markets via the arbitrage process."
                    ],
                    "Leverage and capital structure theories govern how corporate fixed cost structures and debt proportions influence firm valuation.",
                    "Operating Leverage, Financial Leverage, Combined Leverage, EBIT-EPS, Indifference Point, MM Hypothesis.",
                    "Fixed Cost Incurrence -> DOL/DFL Magnification -> Indifference Analysis -> Capital Structure Optimization.",
                    "Assuming high financial leverage is always advantageous; if operating profit drops below interest obligations, EPS turns negative."
                )
            ]
        },
        {
            "module_no": 5,
            "title": "Investment Decisions & Risk Appraisal",
            "hours": 6,
            "marks": 15,
            "topics": [
                create_topic(
                    "fm_m5_t1",
                    "Risk and Uncertainty in Capital Budgeting: RADR, Certainty Equivalents, and Decision Tree Analysis",
                    ["Risk vs Uncertainty", "Risk-Adjusted Discount Rate (RADR) Method", "Certainty Equivalent (CE) Approach", "Probability Distribution and Expected Net Present Value", "Decision Tree Analysis in Sequential Capital Commitments"],
                    "Risk appraisal in capital budgeting encompasses quantitative techniques used to evaluate investment projects when prospective future operating cash flows exhibit statistical dispersion or probability distributions rather than certainty.",
                    "Originated in decision science and modern finance theory (Markowitz, Hertz, Raiffa) to replace single-point deterministic cash flow estimates.",
                    "Guards capital-intensive investments against catastrophic losses in volatile macroeconomic and competitive environments.",
                    ["Distinguish risk (quantifiable probabilities) from uncertainty (unquantifiable contingencies).", "Apply the Risk-Adjusted Discount Rate (RADR) method to elevate hurdle rates for riskier projects.", "Execute the Certainty Equivalent (CE) approach converting uncertain cash flows to guaranteed equivalents.", "Construct and evaluate sequential decision trees for multi-phase investment commitments."],
                    "Higher investment risk demands either a higher discount rate (RADR) or conservative downward scaling of cash flows (Certainty Equivalent).",
                    [
                        ("Risk", "Decision state where future outcomes are unknown but follow known statistical probability distributions."),
                        ("Uncertainty", "Decision state where future outcomes have zero known mathematical probabilities."),
                        ("RADR", "Discount rate composed of risk-free rate (Rf) plus a risk premium (Rp): k = Rf + Rp."),
                        ("Certainty Equivalent (α)", "Factor (0 to 1) converting risky expected cash flows into equivalent riskless cash sums."),
                        ("Decision Tree", "Graphical network charting sequential investment decisions, chance forks, and payoff branches.")
                    ],
                    "1. Method Divergence: RADR adjusts the denominator (discount rate); the Certainty Equivalent method adjusts the numerator (cash flow).\n2. Rolling Back Decision Trees: Decision trees are evaluated backwards from terminal payoff nodes to root decision nodes using expected values.",
                    "Risk Identification -> Probability Estimation -> RADR / CE Application -> Sequential Decision Tree Modeling -> Final Go/No-Go.",
                    [
                        "1. Project cash flow forecasts modeled across economic scenarios (Boom, Normal, Recession).",
                        "2. Standard deviation and coefficient of variation quantify risk dispersion.",
                        "3. RADR elevates the discount rate benchmark based on project beta or variance.",
                        "4. Alternatively, alpha coefficients reduce expected inflows to risk-free equivalents discounted at Rf.",
                        "5. Multi-stage projects employ decision trees to value abandonment and expansion options."
                    ],
                    ["Appraisal Method", "Mechanism of Adjustment", "Formula", "Theoretical Strength"],
                    [
                        ["Risk-Adjusted Discount Rate (RADR)", "Adjusts denominator (Discount rate k)", "NPV = SUM [ E(CF_t) / (1 + Rf + Rp)^t ] - Outlay", "Simple to understand; aligns with market return premiums"],
                        ["Certainty Equivalent (CE)", "Adjusts numerator (Cash inflows)", "NPV = SUM [ (α_t * CF_t) / (1 + Rf)^t ] - Outlay", "Separates risk perception from time value of money"],
                        ["Decision Tree Analysis", "Maps sequential decision and chance nodes", "Fold-back algorithm using Expected Monetary Value", "Accounts for flexibility, staging, and future management options"]
                    ],
                    "// RADR Equation\nDiscount Rate k = Risk-Free Rate (Rf) + Project Risk Premium (Rp)\nNPV_RADR = SUM [ E(CF_t) / (1 + k)^t ] - CF_0",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='40' y='70' width='80' height='40' rx='4' fill='#377FE6'/><text x='80' y='95' font-family='sans-serif' font-size='10' font-weight='700' fill='#FFF' text-anchor='middle'>Decision</text><path d='M 120 90 L 220 50' stroke='#377FE6' stroke-width='2'/><path d='M 120 90 L 220 130' stroke='#377FE6' stroke-width='2'/><circle cx='230' cy='50' r='12' fill='#786CE5'/><text x='230' y='54' font-family='sans-serif' font-size='10' fill='#FFF' text-anchor='middle'>1</text><circle cx='230' cy='130' r='12' fill='#786CE5'/><text x='230' y='134' font-family='sans-serif' font-size='10' fill='#FFF' text-anchor='middle'>2</text><path d='M 242 45 L 360 30' stroke='#28A994' stroke-width='2'/><path d='M 242 55 L 360 70' stroke='#28A994' stroke-width='2'/><text x='290' y='30' font-family='sans-serif' font-size='9' fill='#19283D'>Boom (p=0.6)</text><text x='290' y='75' font-family='sans-serif' font-size='9' fill='#19283D'>Slump (p=0.4)</text><rect x='365' y='15' width='180' height='30' rx='4' fill='#F7F8FC' stroke='#28A994'/><text x='455' y='35' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>Payoff: +$80,000</text><rect x='365' y='55' width='180' height='30' rx='4' fill='#F7F8FC' stroke='#D65F64'/><text x='455' y='75' font-family='monospace' font-size='10' fill='#D65F64' text-anchor='middle'>Payoff: -$20,000</text><rect x='580' y='35' width='190' height='110' rx='8' fill='#E9E8F8' stroke='#786CE5'/><text x='675' y='65' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>Expected Value</text><text x='675' y='90' font-family='monospace' font-size='10' fill='#19283D' text-anchor='middle'>EMV = (0.6*80k) + (0.4*-20k)</text><text x='675' y='115' font-family='monospace' font-size='12' font-weight='700' fill='#369B72' text-anchor='middle'>EMV = $40,000</text></svg>""",
                    "Figure 5.1: Decision Tree Architecture with Probability Nodes and Expected Value Payoffs",
                    "Comparing RADR and Certainty Equivalent Computations",
                    "Expected Cash Inflow Year 1: $100,000.\nRisk-free rate Rf = 6%, Risk premium Rp = 4% (RADR = 10%).\nMethod 1 (RADR): PV = $100,000 / (1 + 0.10)^1 = $90,909.\nMethod 2 (CE): If Certainty Equivalent coefficient α = 0.95: Guaranteed Cash Flow = 0.95 * $100,000 = $95,000.\nDiscounted at risk-free rate Rf = 6%: PV = $95,000 / (1 + 0.06)^1 = $89,622.",
                    [
                        "Risk entails quantifiable probability distributions; uncertainty involves unknowable outcomes.",
                        "RADR increases the discount rate benchmark (Rf + Rp), demanding higher compensation for volatility.",
                        "The Certainty Equivalent approach converts uncertain cash flows to guaranteed sums discounted at the risk-free rate.",
                        "The Certainty Equivalent method is theoretically superior because it separates risk aversion from the time value of money.",
                        "Decision trees model sequential multi-period decisions using decision nodes and chance outcome forks.",
                        "Backward induction (rollback technique) calculates Expected Monetary Value (EMV) to choose optimal branches."
                    ],
                    "Risk appraisal methodologies incorporate statistical volatility into capital budgeting via discount rate adjustments and sequential decision tree logic.",
                    "Risk, Uncertainty, RADR, Certainty Equivalent, Decision Tree, Expected Monetary Value.",
                    "Scenario Analysis -> Probability Weighting -> RADR/CE Adjustment -> Decision Tree Rollback.",
                    "Discounting Certainty Equivalent cash flows using the risk-adjusted rate instead of the risk-free rate (double-counting risk)."
                )
            ]
        },
        {
            "module_no": 6,
            "title": "Dividend Policies",
            "hours": 6,
            "marks": 15,
            "topics": [
                create_topic(
                    "fm_m6_t1",
                    "Dividend Theories: Walter's Model, Gordon's Model, MM Dividend Irrelevance, and Corporate Policies",
                    ["Relevance vs Irrelevance Theories", "James E. Walter's Valuation Formula", "Myron J. Gordon's Dividend Growth Model", "Modigliani-Miller (MM) Dividend Irrelevance Hypothesis", "Determinants of Corporate Dividend Policy"],
                    "Dividend policy is the executive financial decision determining the proportion of corporate net profits distributed to equity shareholders as cash dividends versus retained within the enterprise for reinvestment.",
                    "Formulated into modern mathematical models by James E. Walter (1956), Myron Gordon (1959), and Modigliani & Miller (1961).",
                    "Affects corporate stock prices, shareholder satisfaction, enterprise internal growth capacity, and capital market signaling.",
                    ["Formulate and calculate share prices using Walter's valuation model.", "Analyze Gordon's 'Bird-in-the-Hand' dividend model.", "Explain Modigliani and Miller's dividend irrelevance proof and arbitrage mechanism.", "Evaluate market determinants influencing corporate dividend policy."],
                    "When return on internal investment (r) exceeds the cost of capital (k), the firm maximizes value by retaining 100% of earnings; if r < k, it should distribute 100%.",
                    [
                        ("Dividend Payout Ratio", "Percentage of net profit distributed as dividends: DPS / EPS."),
                        ("Retention Ratio (b)", "Percentage of net profit retained within the firm: 1 - Payout Ratio."),
                        ("Walter's Model", "P = [ D + (r / k) * (E - D) ] / k; relates internal return (r) to cost of capital (k)."),
                        ("Bird-in-the-Hand Theory", "Gordon's premise that investors prefer immediate certain dividends over uncertain future capital gains."),
                        ("MM Irrelevance Theorem", "Dividend policy does not impact share price in perfect capital markets with fixed investment policy.")
                    ],
                    "1. Walter's Growth Dictum: Growth firms (r > k) should retain all profits (0% payout); declining firms (r < k) should distribute all profits (100% payout).\n2. Clientele Effect: Different shareholder demographics gravitate toward firms with matching dividend payout habits.",
                    "Net Profit -> Investment Opportunity Assessment -> Retention vs Dividend Decision -> Market Price Reaction.",
                    [
                        "1. Board evaluates internal rate of return (r) on available capital projects.",
                        "2. If r > k, earnings are retained to maximize enterprise growth.",
                        "3. If r < k, earnings are distributed to enable shareholders to earn higher returns elsewhere.",
                        "4. Walter and Gordon formulas determine theoretical market share price.",
                        "5. Stable dividend policies communicate positive managerial confidence to stock markets."
                    ],
                    ["Theory Type", "Model", "Core Assumption", "Optimal Dividend Payout Policy"],
                    [
                        ["Relevance", "Walter's Model", "All financing done internally; perpetual earnings", "If r > k: 0% Payout; If r < k: 100% Payout; If r = k: Indifferent"],
                        ["Relevance", "Gordon's Model", "r and k are constant; investors are risk-averse", "Higher payout elevates share price by lowering investor risk perception"],
                        ["Irrelevance", "Modigliani-Miller (MM)", "Perfect markets, zero taxes, fixed investments", "Payout ratio has ZERO impact on enterprise valuation (Arbitrage restores parity)"]
                    ],
                    "// Walter's Model Formula\nP = [ D + (r / k) * (E - D) ] / k\nWhere P = Share Price, D = DPS, E = EPS, r = Internal Return, k = Cost of Capital",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='140' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Growth Firm (r &gt; k)</text><text x='50' y='80' font-family='sans-serif' font-size='10' fill='#19283D'>Internal Return &gt; Cost of Capital</text><text x='50' y='105' font-family='monospace' font-size='11' font-weight='700' fill='#369B72'>Optimal Payout: 0%</text><text x='50' y='130' font-family='sans-serif' font-size='9' fill='#617087'>Retain all earnings for compounding</text><rect x='290' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='400' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Normal Firm (r = k)</text><text x='310' y='80' font-family='sans-serif' font-size='10' fill='#19283D'>Internal Return = Cost of Capital</text><text x='310' y='105' font-family='monospace' font-size='11' font-weight='700' fill='#786CE5'>Optimal Payout: Any %</text><text x='310' y='130' font-family='sans-serif' font-size='9' fill='#617087'>Share price remains completely indifferent</text><rect x='550' y='30' width='220' height='120' rx='8' fill='#F7F8FC' stroke='#EF846B'/><text x='660' y='55' font-family='sans-serif' font-size='12' font-weight='700' fill='#EF846B' text-anchor='middle'>Declining Firm (r &lt; k)</text><text x='570' y='80' font-family='sans-serif' font-size='10' fill='#19283D'>Internal Return &lt; Cost of Capital</text><text x='570' y='105' font-family='monospace' font-size='11' font-weight='700' fill='#D65F64'>Optimal Payout: 100%</text><text x='570' y='130' font-family='sans-serif' font-size='9' fill='#617087'>Distribute all cash to shareholders</text></svg>""",
                    "Figure 6.1: Walter's Model Optimal Payout Policy Across Growth, Normal, and Declining Firms",
                    "Numerical Demonstration of Walter's Model Share Valuation",
                    "Given: EPS = $10, DPS = $4, Cost of Capital k = 10% (0.10), Internal Return r = 15% (0.15).\nP = [ D + (r / k) * (E - D) ] / k\nP = [ 4 + (0.15 / 0.10) * (10 - 4) ] / 0.10\nP = [ 4 + 1.5 * 6 ] / 0.10 = [ 4 + 9 ] / 0.10 = 13 / 0.10 = $130.\nIf Payout is 0% (D = 0): P = [ 0 + 1.5 * 10 ] / 0.10 = 15 / 0.10 = $150 (Confirms 0% payout maximizes price when r > k).",
                    [
                        "Dividend decisions balance immediate shareholder payouts against internal retained earnings growth.",
                        "Walter's model demonstrates that optimal dividend payout depends on the relationship between r and k.",
                        "For growth firms (r > k), zero dividend payout maximizes market share valuation.",
                        "Gordon's model posits that investors discount capital gains at higher rates than current dividends.",
                        "Modigliani and Miller argue that dividend policy is irrelevant to firm value in frictionless capital markets.",
                        "Real-world policies prioritize stable dividend trajectories to avoid negative market signaling."
                    ],
                    "Dividend theories evaluate how distributing versus retaining net earnings affects corporate equity valuation and investor signaling.",
                    "Dividend Policy, Walter's Model, Gordon's Model, MM Dividend Irrelevance, Signaling, Clientele Effect.",
                    "Earnings Generation -> Opportunity Assessment (r vs k) -> Payout Decision -> Market Price Adjustment.",
                    "Believing paying high dividends is always good; if a high-growth firm pays dividends instead of reinvesting at r > k, shareholder wealth decreases."
                )
            ]
        },
        {
            "module_no": 7,
            "title": "Management of Working Capital",
            "hours": 6,
            "marks": 15,
            "topics": [
                create_topic(
                    "fm_m7_t1",
                    "Working Capital Cycle, Cash Models (Baumol & Miller-Orr), Receivables, and Inventory (EOQ & ABC)",
                    ["Gross vs Net Working Capital", "Operating Cycle Analysis & Formula", "Cash Management Models (Baumol, Miller-Orr)", "Receivables Management & Credit Policy", "Inventory Optimization (EOQ & ABC Analysis)"],
                    "Working capital management is the operational financial discipline of planning and controlling current assets and current liabilities to ensure operational liquidity while maximizing profitability.",
                    "Pioneered by corporate financial controllers to avoid technical insolvency stemming from operational cash crunches during business expansion.",
                    "Protects daily solvency, guarantees timely payment to suppliers and labor, optimizes inventory investment, and avoids costly short-term emergency borrowing.",
                    ["Compute Gross and Net Working Capital.", "Calculate the Operating Cycle length in days: Inventory Period + Debtors Period - Creditors Period.", "Apply the Baumol and Miller-Orr models for optimum cash balances.", "Calculate Economic Order Quantity (EOQ) and classify inventory using ABC Analysis."],
                    "The Operating Cycle reflects the time elapsed from raw material procurement to final customer cash collection. Shortening this cycle releases trapped liquidity.",
                    [
                        ("Net Working Capital (NWC)", "Current Assets minus Current Liabilities; represents margin of long-term safety."),
                        ("Operating Cycle", "Gross Operating Cycle minus Creditors deferral period: (Raw Material + WIP + Finished Goods + Debtors) - Creditors."),
                        ("Baumol's Cash Model", "Determines optimal cash conversion lot: C* = sqrt(2 * T * F / i)."),
                        ("Miller-Orr Model", "Sets upper, lower, and return cash balance boundaries using daily cash flow variance."),
                        ("EOQ", "Economic Order Quantity minimizing sum of ordering and holding costs: sqrt(2 * D * S / H)."),
                        ("ABC Analysis", "Classifies inventory: A (high value, low quantity), B (moderate), C (low value, high quantity).")
                    ],
                    "1. Liquidity-Profitability Dilemma: Conservative working capital policies maximize liquidity but drag profitability; aggressive policies maximize profits but risk default.\n2. Negative Working Capital: Efficient retailers (e.g., supermarkets) operate on negative working capital by collecting instant cash from shoppers while deferring supplier payments.",
                    "Cash -> Raw Materials -> Work-in-Progress -> Finished Goods -> Accounts Receivable (Debtors) -> Cash Collected.",
                    [
                        "1. Firm purchases raw materials on trade credit.",
                        "2. Materials processed into finished goods through manufacturing.",
                        "3. Goods sold on credit terms generating Accounts Receivable.",
                        "4. Cash collected from debtors; suppliers paid at maturity.",
                        "5. Excess operating cash invested in short-term marketable securities."
                    ],
                    ["Component", "Optimization Objective", "Mathematical Model Applied"],
                    [
                        ["Cash", "Minimize idle cash while preventing payment default", "Baumol Model / Miller-Orr Stochastic Model"],
                        ["Receivables", "Optimize trade credit terms to boost sales without bad debts", "Credit Policy Evaluation (Marginal Profit vs Default Risk)"],
                        ["Inventory", "Minimize stockout risk and inventory holding carrying costs", "Economic Order Quantity (EOQ) & ABC Selective Control"],
                        ["Payables", "Maximize interest-free trade credit period without vendor friction", "Creditors Turnover / Cash Discount Valuation"]
                    ],
                    "// Mathematical Models\nOperating Cycle = RM_days + WIP_days + FG_days + Debtors_days - Creditors_days\nEOQ = sqrt(2 * Annual Demand * Order Cost / Holding Cost)\nBaumol Cash C* = sqrt(2 * Annual Cash * Transaction Cost / Interest Rate)",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><circle cx='100' cy='90' r='50' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><text x='100' y='85' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Cash</text><text x='100' y='105' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Working Cap</text><path d='M 155 80 L 235 55' stroke='#377FE6' stroke-width='2'/><circle cx='290' cy='50' r='50' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><text x='290' y='45' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Raw Material</text><text x='290' y='65' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Inventory</text><path d='M 345 50 L 445 50' stroke='#786CE5' stroke-width='2'/><circle cx='500' cy='50' r='50' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><text x='500' y='45' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>WIP &amp; FG</text><text x='500' y='65' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Production</text><path d='M 555 55 L 635 80' stroke='#28A994' stroke-width='2'/><circle cx='690' cy='90' r='50' fill='#E9E8F8' stroke='#F2C75C' stroke-width='2'/><text x='690' y='85' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>Receivables</text><text x='690' y='105' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Debtors Book</text><path d='M 645 110 L 155 110' stroke='#369B72' stroke-width='2' stroke-dasharray='4,4'/><text x='400' y='135' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72' text-anchor='middle'>Cash Collected from Debtors (Completes Operating Cycle)</text></svg>""",
                    "Figure 7.1: Continuous Cash-to-Cash Operating Cycle in Enterprise Management",
                    "Economic Order Quantity (EOQ) Numerical Calculation",
                    "Annual Demand D = 10,000 units, Ordering Cost S = $50 per order, Holding Cost H = $4 per unit/year.\nEOQ = sqrt( (2 * 10,000 * 50) / 4 ) = sqrt( 1,000,000 / 4 ) = sqrt( 250,000 ) = 500 units.\nNumber of orders per year = 10,000 / 500 = 20 orders.\nTotal Ordering Cost = 20 * $50 = $1,000; Total Carrying Cost = (500 / 2) * $4 = $1,000.\nTotal Annual Inventory Cost = $2,000 (Notice that Ordering and Carrying costs are exactly equal at EOQ).",
                    [
                        "Working capital management balances liquidity preservation against corporate profitability.",
                        "The Operating Cycle measures the velocity of cash conversion from inventory purchase to debtor realization.",
                        "Baumol's cash model balances transaction conversion costs against interest opportunity costs.",
                        "The Miller-Orr model accommodates random daily cash flow variations through upper and lower control bands.",
                        "Economic Order Quantity (EOQ) pinpoints the order lot size where ordering costs equal carrying costs.",
                        "ABC inventory classification applies selective control: Category A receives stringent management scrutiny."
                    ],
                    "Working capital management maintains daily operational solvency across cash, receivables, inventory, and payables cycles.",
                    "Working Capital, Operating Cycle, Baumol Model, Miller-Orr, Receivables, EOQ, ABC Analysis.",
                    "Procurement -> Operating Cycle Conversion -> Optimization Models -> Working Capital Solvency.",
                    "Overstating working capital requirements by ignoring interest-free trade credit spontaneously provided by suppliers."
                )
            ]
        }
    ]
