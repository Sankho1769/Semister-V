# Entrepreneurship (MIM 502) Lessons Generator
from generator.helper import create_topic

def get_ent_modules():
    return [
        {
            "module_no": 1,
            "title": "Introduction to Entrepreneurship",
            "hours": 10,
            "marks": 20,
            "topics": [
                create_topic(
                    "ent_m1_t1",
                    "Concept of Entrepreneurship and Role in Economic Development",
                    ["Definitions & Evolution", "Economic Impact & Employment", "Innovation as Driver (Schumpeter)", "Entrepreneurial Ecosystems"],
                    "Entrepreneurship is the dynamic process of identifying economic opportunities, assembling resources, assuming calculated financial risks, and introducing innovations to create value.",
                    "The term originates from the French 'entreprendre' (to undertake). Joseph Schumpeter formulated modern theory identifying the entrepreneur as the agent of 'creative destruction'.",
                    "Serves as the primary catalyst for GDP growth, job creation, regional balanced development, and industrial modernization.",
                    ["Define entrepreneurship across economic, psychological, and behavioral perspectives.", "Analyze Joseph Schumpeter's theory of innovation and creative destruction.", "Evaluate the macro role of entrepreneurship in capital formation and employment.", "Identify the core pillars of an entrepreneurial ecosystem."],
                    "Entrepreneurship converts latent ideas into market realities by organizing land, labor, and capital under conditions of uncertainty.",
                    [
                        ("Creative Destruction", "Schumpeterian process where market innovations dismantle outdated business models."),
                        ("Capital Formation", "Mobilization of idle savings into productive industrial investments."),
                        ("Opportunity Recognition", "Discerning unmet consumer needs and viable market arbitrage gaps."),
                        ("Calculated Risk", "Bearing manageable uncertainty backed by empirical research and mitigation plans.")
                    ],
                    "1. Wealth Generation: New ventures create added economic output rather than redistributing static assets.\n2. Regional Balance: Small-scale enterprises disperse industrial activity away from saturated metropolises.",
                    "Unmet Market Need -> Opportunity Discovery -> Resource Marshalling -> Innovation Launch -> Economic Surplus.",
                    [
                        "1. Entrepreneur detects market inefficiency or technological advancement.",
                        "2. Feasibility studies validate commercial potential and consumer willingness to pay.",
                        "3. Seed capital and skilled human talent are assembled.",
                        "4. Enterprise launched; competitive disruption reallocates market market share.",
                        "5. Profits generated are reinvested into enterprise expansion and tax bases."
                    ],
                    ["Economic Dimension", "Traditional Enterprise", "Entrepreneurial Venture"],
                    [
                        ["Primary Goal", "Sustained stability & subsistence profits", "Rapid scalable growth & market disruption"],
                        ["Risk Tolerance", "Risk-averse, minimal uncertainty", "Calculated risk-taker seeking exponential upside"],
                        ["Approach to Market", "Follows existing supply & demand patterns", "Creates new markets via product or process innovation"],
                        ["Resource Strategy", "Constrained strictly to currently owned assets", "Leverages external capital, partnerships, and intellectual property"]
                    ],
                    "// Conceptual Model of Economic Impact\nCapital Investment ($) -> Local Supplier Linkages -> Household Disposable Income -> Aggregate Demand Expansion",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='40' width='150' height='100' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='105' y='75' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Innovation</text><text x='105' y='105' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>New Goods &amp; Methods</text><path d='M 185 90 L 235 90' stroke='#377FE6' stroke-width='2'/><rect x='240' y='40' width='150' height='100' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='315' y='75' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Venture Launch</text><text x='315' y='105' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Capital Formation</text><path d='M 395 90 L 445 90' stroke='#786CE5' stroke-width='2'/><rect x='450' y='40' width='150' height='100' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='525' y='75' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Job Creation</text><text x='525' y='105' font-family='sans-serif' font-size='10' fill='#617087' text-anchor='middle'>Income Generation</text><path d='M 605 90 L 655 90' stroke='#28A994' stroke-width='2'/><rect x='660' y='40' width='120' height='100' rx='8' fill='#E9E8F8' stroke='#F2C75C'/><text x='720' y='75' font-family='sans-serif' font-size='11' font-weight='700' fill='#19283D' text-anchor='middle'>GDP Growth</text><text x='720' y='105' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Macro Expansion</text></svg>""",
                    "Figure 1.1: Transmission Mechanism from Entrepreneurial Innovation to GDP Growth",
                    "Schumpeter's Five Types of Innovation in Action",
                    "1. Introduction of new good (Electric vehicles)\n2. Introduction of new method of production (Assembly line robotics)\n3. Opening of new market (Fintech in rural unbanked regions)\n4. Conquest of new source of raw material (Synthetic battery chemistries)\n5. Carrying out new organization of industry (Aggregator platform business models)",
                    [
                        "Entrepreneurship is fundamentally an economic driver powered by calculated risk and innovation.",
                        "Joseph Schumpeter coined the paradigm of 'Creative Destruction' where new firms replace obsolete incumbents.",
                        "Entrepreneurs drive capital formation by converting public savings into active industrial production.",
                        "Micro, Small, and Medium Enterprises (MSMEs) account for over 40% of industrial employment in developing nations.",
                        "Entrepreneurial ecosystems integrate universities, venture capital, government policy, and infrastructure.",
                        "Reduces wealth concentration through distributed grassroots commercial activity."
                    ],
                    "Entrepreneurship acts as the engine of macro-economic development, driving capital mobilization, technological advancement, and employment.",
                    "Creative Destruction, Innovation, Capital Formation, Opportunity Recognition, MSME.",
                    "Opportunity Detection -> Resource Synthesis -> Venture Inception -> Macroeconomic Multiplier.",
                    "Confusing traditional small business owners (subsistence-driven) with growth-oriented innovative entrepreneurs."
                )
            ]
        },
        {
            "module_no": 2,
            "title": "Introduction to Entrepreneur",
            "hours": 6,
            "marks": 20,
            "topics": [
                create_topic(
                    "ent_m2_t1",
                    "Characteristics, Behavioral Traits, and Types of Entrepreneurs (Clarence Danhof Classification)",
                    ["Core Personality Traits", "Clarence Danhof Taxonomy (Innovating, Imitative, Fabian, Drone)", "Arthur Cole Classification", "Entrepreneur vs Intrapreneur vs Manager"],
                    "An entrepreneur is an individual who conceives an innovative business idea, takes operational initiative, marshals resources, and bears financial and legal risks to capture economic rewards.",
                    "Pioneered in economic literature by Richard Cantillon (1755), modernized by Clarence Danhof through empirical industrial classification in agriculture.",
                    "Vital for identifying human capital suited for venture creation, policy formulation, and incubation targeting.",
                    ["Profile psychological attributes: internal locus of control, high need for achievement, resilience.", "Categorize entrepreneurs using Clarence Danhof's 4-tier model.", "Distinguish between Entrepreneurs, Intrapreneurs, and Professional Managers.", "Analyze gender-specific and social entrepreneurship models."],
                    "Entrepreneurs operate across diverse archetypes ranging from radical innovators to cautious, tradition-bound survivalists.",
                    [
                        ("Innovating Entrepreneur", "Introduces radically new products, technologies, or business models to open untapped markets."),
                        ("Imitative / Adoptive Entrepreneur", "Replicates proven successful innovations with modifications tailored to emerging local markets."),
                        ("Fabian Entrepreneur", "Excessively cautious and skeptical; adopts innovations only when survival is threatened."),
                        ("Drone Entrepreneur", "Resistant to all change, adhering rigidly to customary traditional methods even at financial ruin."),
                        ("Intrapreneur", "Corporate employee who drives innovative venture creation utilizing company infrastructure.")
                    ],
                    "1. Risk Asymmetry: Entrepreneurs bear full personal financial risk; intrapreneurs operate with corporate safety nets.\n2. Locus of Control: Successful entrepreneurs exhibit high internal locus of control, believing effort determines outcomes.",
                    "Idea Conceptualization -> Risk Assessment -> Resource Organization -> Enterprise Governance.",
                    [
                        "1. Psychological traits motivate independent venture action.",
                        "2. Environmental pressures categorize entrepreneur into Danhof's framework.",
                        "3. Innovators initiate paradigm shifts; imitative entrepreneurs popularize them globally.",
                        "4. Laggards (Fabian and Drone) either adapt under distress or succumb to liquidation."
                    ],
                    ["Characteristic", "Entrepreneur", "Intrapreneur", "Traditional Manager"],
                    [
                        ["Primary Motivation", "Independence, achievement, equity upside", "Corporate recognition, career advancement", "Salary, job security, organizational status"],
                        ["Financial Risk", "High personal financial and career risk", "Zero personal equity loss; corporate risk", "Minimal personal risk"],
                        ["Resource Ownership", "Must acquire and self-fund resources", "Utilizes established corporate assets", "Manages allocated departmental budgets"],
                        ["Focus", "Opportunity discovery & market disruption", "Internal intra-corporate innovation", "Operational efficiency & status quo maintenance"]
                    ],
                    "// Danhof Spectrum in Developing Economies\nGlobal Tech Pioneer (Innovating) -> Local Regional Scaler (Imitative) -> Reluctant Family Firm (Fabian) -> Extinct Handloom Unit (Drone)",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Innovating</text><text x='110' y='90' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Creates new paradigms</text><text x='110' y='110' font-family='sans-serif' font-size='9' fill='#369B72' text-anchor='middle'>Aggressive, High R&amp;D</text><rect x='220' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='300' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Imitative</text><text x='300' y='90' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Adapts proven models</text><text x='300' y='110' font-family='sans-serif' font-size='9' fill='#786CE5' text-anchor='middle'>Crucial for India/Global South</text><rect x='410' y='30' width='160' height='120' rx='8' fill='#FFF2EB' stroke='#EF846B'/><text x='490' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#EF846B' text-anchor='middle'>Fabian</text><text x='490' y='90' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Skeptical and cautious</text><text x='490' y='110' font-family='sans-serif' font-size='9' fill='#EF846B' text-anchor='middle'>Adopts only under threat</text><rect x='600' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#D65F64'/><text x='680' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#D65F64' text-anchor='middle'>Drone</text><text x='680' y='90' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Refuses modernization</text><text x='680' y='110' font-family='sans-serif' font-size='9' fill='#D65F64' text-anchor='middle'>Faces severe extinction</text></svg>""",
                    "Figure 2.1: Clarence Danhof Classification of Entrepreneurial Typology",
                    "Illustrating the Danhof Typology in Real-World Indian Industry",
                    "- Innovating: Space-tech and battery architecture startups developing proprietary IP.\n- Imitative: E-commerce and quick-commerce models customized for Indian logistics constraints.\n- Fabian: Traditional retail shopkeepers adopting UPI payment QR codes only after customer loss.\n- Drone: Artisans refusing digital inventories and losing global handicraft export channels.",
                    [
                        "Clarence Danhof categorized entrepreneurs into: Innovating, Imitative, Fabian, and Drone.",
                        "Imitative entrepreneurs are vital in developing economies by rapidly diffusing proven technologies.",
                        "Key psychological traits: Need for Achievement (n-Ach), risk tolerance, and ambiguity tolerance.",
                        "An intrapreneur exercises entrepreneurial vision inside an existing corporate infrastructure.",
                        "Managers focus on resource optimization; entrepreneurs focus on opportunity creation.",
                        "Drone entrepreneurs adhere to ancestral techniques despite sustained losses, leading to insolvency."
                    ],
                    "Entrepreneurs span diverse behavioral archetypes whose willingness to innovate dictates competitive survival.",
                    "Innovating, Imitative, Fabian, Drone, Intrapreneur, Locus of Control, Risk Tolerance.",
                    "Trait Identification -> Opportunity Seizure -> Typology Execution -> Organizational Maturation.",
                    "Labeling an imitative entrepreneur as 'uncreative'; imitative entrepreneurs adapt complex models to local market realities."
                )
            ]
        },
        {
            "module_no": 3,
            "title": "Entrepreneurial Motivation",
            "hours": 7,
            "marks": 20,
            "topics": [
                create_topic(
                    "ent_m3_t1",
                    "Theories of Entrepreneurial Motivation, McClelland's Acquired Needs, and EDPs",
                    ["David McClelland's Need for Achievement (n-Ach)", "Push vs Pull Motivational Factors", "Rotter's Locus of Control", "Entrepreneurship Development Programmes (EDPs) Objectives & Phases"],
                    "Entrepreneurial motivation refers to the internal psychological drives, cognitive factors, and external stimuli that compel individuals to initiate, direct, and sustain a new commercial enterprise.",
                    "David McClelland (1961) published 'The Achieving Society', pinpointing the Need for Achievement as the primary behavioral determinant of economic entrepreneurship.",
                    "Underpins government training curriculum, venture talent selection, and incubator mentorship models.",
                    ["Analyze David McClelland's Three Needs Theory (Achievement, Power, Affiliation).", "Distinguish 'Push' (necessity-based) from 'Pull' (opportunity-based) motivational drivers.", "Explain the curriculum structure, phases, and evaluation criteria of EDPs.", "Identify key impediments in entrepreneurial motivation."],
                    "Motivation arises from internal aspirations (wealth, autonomy, self-actualization) combined with external catalysts (market incentives, subsidies).",
                    [
                        ("Need for Achievement (n-Ach)", "Drive to excel, achieve against challenging benchmarks, and take personal responsibility for problem-solving."),
                        ("Need for Power (n-Pow)", "Desire to influence, lead, and command authority over organizational resources."),
                        ("Need for Affiliation (n-Aff)", "Desire for warm, friendly interpersonal relationships (least prominent in high-growth founders)."),
                        ("Push Factors", "Compelling external distress drivers (unemployment, underpayment, job dissatisfaction)."),
                        ("Pull Factors", "Alluring market opportunity drivers (financial independence, recognition, market arbitrage).")
                    ],
                    "1. Achievement Supremacy: High n-Ach individuals choose moderately difficult tasks with tangible feedback over high-gamble gambles.\n2. Trainable Competence: McClelland demonstrated in the Kakinada Experiment (India) that entrepreneurial motivation can be systematically developed through structured EDPs.",
                    "Motivational Stimulus -> Goal Formulation -> Enterprise Inception -> Persistence Under Hardship.",
                    [
                        "1. Individual perceives push or pull motivational stimulus.",
                        "2. Need for achievement triggers goal setting and business idea selection.",
                        "3. EDP intervention develops behavioral competencies, financial literacy, and feasibility preparation.",
                        "4. Self-efficacy beliefs reinforce resilience during initial revenue plateaus."
                    ],
                    ["Factor Category", "Motivational Trigger", "Venture Profile", "Typical Longevity"],
                    [
                        ["Pull (Opportunity)", "Desire for autonomy, wealth, innovation", "Tech startups, scalable service firms", "High growth potential, well-capitalized"],
                        ["Push (Necessity)", "Layoffs, lack of employment options, poverty", "Micro-retail, informal subsistence kiosks", "Low growth ceiling, vulnerable to shock"],
                        ["Internal Psychological", "High internal locus of control, n-Ach", "Domain-specialist proprietary ventures", "Resilient, mission-driven leadership"],
                        ["External Institutional", "Subsidies, tax holidays, SEZ benefits", "Manufacturing plants in notified industrial zones", "Tied to ongoing regulatory protection"]
                    ],
                    "// McClelland's Motive Balance in High-Growth Founders\nHigh n-Ach (Problem solving & results) + Moderate n-Pow (Team leadership) + Controlled n-Aff (Tough decisions)",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><circle cx='180' cy='90' r='70' fill='#F7F8FC' stroke='#377FE6' stroke-width='2'/><text x='180' y='75' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Need for</text><text x='180' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Achievement</text><text x='180' y='115' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>n-Ach (Primary)</text><circle cx='400' cy='90' r='70' fill='#F7F8FC' stroke='#786CE5' stroke-width='2'/><text x='400' y='75' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Need for</text><text x='400' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Power</text><text x='400' y='115' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>n-Pow (Leadership)</text><circle cx='620' cy='90' r='70' fill='#F7F8FC' stroke='#28A994' stroke-width='2'/><text x='620' y='75' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Need for</text><text x='620' y='95' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>Affiliation</text><text x='620' y='115' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>n-Aff (Social)</text></svg>""",
                    "Figure 3.1: David McClelland's Acquired Needs Framework in Entrepreneurship",
                    "The Kakinada Experiment: Evidence of EDP Efficacy",
                    "In 1964, David McClelland conducted an intensive training experiment in Kakinada, Andhra Pradesh. Young businesspersons were given psychological achievement stimulation. Post-training tracking showed significantly higher investment rates, business expansion, and job generation compared to the control group, validating that entrepreneurship can be taught.",
                    [
                        "David McClelland identified the Need for Achievement (n-Ach) as the key psychological motivator.",
                        "Entrepreneurs with high n-Ach seek moderate calculated risks and continuous feedback.",
                        "'Pull' motivators produce high-growth scalable enterprises; 'Push' motivators produce subsistence ventures.",
                        "Entrepreneurship Development Programmes (EDPs) consist of 3 phases: Pre-training, Training, and Post-training.",
                        "Post-training support (escort services, credit linkage, licensing) is critical to prevent venture mortality.",
                        "The Kakinada experiment demonstrated that entrepreneurial competencies can be developed systematically."
                    ],
                    "Entrepreneurial motivation synthesizes achievement psychology with external incentives, validated by structured EDP interventions.",
                    "n-Ach, n-Pow, n-Aff, Push Factors, Pull Factors, Kakinada Experiment, EDPs.",
                    "Psychological Motive -> Push/Pull Catalyst -> EDP Skill Ingestion -> Venture Launch.",
                    "Assuming entrepreneurs are high-gamble gamblers; high n-Ach individuals deliberately pursue moderate, calculated risks."
                )
            ]
        },
        {
            "module_no": 4,
            "title": "Project Management",
            "hours": 7,
            "marks": 20,
            "topics": [
                create_topic(
                    "ent_m4_t1",
                    "Project Identification, Feasibility Analysis, and Detailed Project Report (DPR) Formulation",
                    ["Opportunity Scanning & Idea Screening", "Market, Technical & Financial Feasibility", "Detailed Project Report (DPR) Structure", "Project Appraisal Criteria (NPV, IRR, Payback)"],
                    "Project management in entrepreneurship is the disciplined process of identifying viable commercial opportunities, conducting rigorous multi-dimensional feasibility appraisals, and formulating a Detailed Project Report (DPR) for financial and operational execution.",
                    "Originated in industrial engineering and financial analysis to eliminate speculative venture failure and satisfy institutional lending compliance.",
                    "The DPR serves as the master blueprint submitted to banks, financial institutions, and regulatory bodies for loan syndication and statutory approvals.",
                    ["Conduct systematic project screening using SWOT and Porter's Five Forces.", "Execute market, technical, economic, and managerial feasibility analyses.", "Structure a comprehensive Detailed Project Report (DPR).", "Evaluate capital project viability using NPV, IRR, and Break-Even Analysis."],
                    "A project transitions through a defined lifecycle: Identification -> Formulation -> Appraisal -> Implementation -> Monitoring.",
                    [
                        ("Detailed Project Report (DPR)", "Comprehensive document detailing techno-economic, marketing, and financial blueprint of a venture."),
                        ("Technical Feasibility", "Assessment of manufacturing process, plant capacity, equipment availability, and raw material logistics."),
                        ("Financial Feasibility", "Evaluation of capital outlay, projected cash flows, debt-service coverage ratio (DSCR), and break-even point."),
                        ("Economic Appraisal", "Social cost-benefit analysis evaluating public employment and foreign exchange conservation.")
                    ],
                    "1. Debt-Service Coverage Ratio (DSCR): Banks mandate a DSCR of 1.5–2.0 to ensure operating profits can service debt obligations.\n2. Break-Even Margin: Commercial projects must operate significantly above the break-even volume to absorb market shocks.",
                    "Idea Scanning -> Feasibility Study -> DPR Preparation -> Bank Appraisal -> Project Implementation.",
                    [
                        "1. Entrepreneur identifies opportunity through macro-economic and consumer surveys.",
                        "2. Technical specialists verify raw materials, utility consumption, and production engineering.",
                        "3. Financial modelers compile profit and loss projections, cash flow statements, and balance sheets.",
                        "4. DPR submitted to banks (SIDBI, commercial banks) for techno-economic feasibility (TEV) study.",
                        "5. Sanction of term loan and working capital limits enables commercial ground-breaking."
                    ],
                    ["Feasibility Dimension", "Core Parameters Evaluated", "Risk Mitigated"],
                    [
                        ["Market Feasibility", "Demand-supply gap, pricing elasticity, distribution channels", "Unsold inventory, lack of consumer adoption"],
                        ["Technical Feasibility", "Site selection, process technology, power/water access, scalability", "Production bottlenecks, plant shutdowns"],
                        ["Financial Feasibility", "Internal Rate of Return (IRR), DSCR, Payback Period, Net Present Value", "Insolvency, liquidity traps, debt default"],
                        ["Environmental Feasibility", "Pollution control, effluent treatment, statutory green clearances", "Government closure orders, legal penalties"]
                    ],
                    "// Key DPR Metric: Break-Even Point (Units)\nBEP (Units) = Total Fixed Costs / (Selling Price per Unit - Variable Cost per Unit)",
                    """<svg viewBox='0 0 800 180' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='30' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#377FE6'/><text x='110' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Project Idea</text><text x='110' y='90' font-family='sans-serif' font-size='10' fill='#19283D' text-anchor='middle'>Market Scanning</text><text x='110' y='110' font-family='sans-serif' font-size='9' fill='#617087' text-anchor='middle'>Demand-Supply Gap</text><path d='M 195 90 L 245 90' stroke='#377FE6' stroke-width='2'/><rect x='250' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#786CE5'/><text x='330' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#786CE5' text-anchor='middle'>Feasibility Studies</text><text x='330' y='85' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>• Technical Feasibility</text><text x='330' y='105' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>• Market Feasibility</text><text x='330' y='125' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>• Financial Feasibility</text><path d='M 415 90 L 465 90' stroke='#786CE5' stroke-width='2'/><rect x='470' y='30' width='160' height='120' rx='8' fill='#F7F8FC' stroke='#28A994'/><text x='550' y='60' font-family='sans-serif' font-size='12' font-weight='700' fill='#28A994' text-anchor='middle'>DPR Formulation</text><text x='550' y='85' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Detailed Project Report</text><text x='550' y='105' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>Projected P&amp;L / Balance Sheet</text><text x='550' y='125' font-family='sans-serif' font-size='9' fill='#19283D' text-anchor='middle'>DSCR / Break-Even Analysis</text><path d='M 635 90 L 685 90' stroke='#28A994' stroke-width='2'/><rect x='690' y='30' width='85' height='120' rx='8' fill='#E9E8F8' stroke='#F2C75C'/><text x='732' y='80' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>Bank</text><text x='732' y='105' font-family='sans-serif' font-size='10' font-weight='700' fill='#369B72' text-anchor='middle'>Appraisal</text></svg>""",
                    "Figure 4.1: Project Lifecycle from Idea Screening to DPR Bank Appraisal",
                    "Standard Structure of a Detailed Project Report (DPR)",
                    "1. Executive Summary & Promoter Background\n2. Project Description, Capacity & Plant Location\n3. Market Potential, Target Demographics & Competitor Analysis\n4. Technical Blueprint: Machinery, Civil Works, Raw Materials, Utilities\n5. Financial Plan: Total Project Cost, Means of Finance (Debt/Equity)\n6. Financial Projections: Cash Flows, Projected Balance Sheets (5 Years)\n7. Ratio Analysis: DSCR, Current Ratio, Break-Even Point, Payback Period",
                    [
                        "Project management structures commercial initiatives into rigorous sequential phases.",
                        "Feasibility analysis must cover four key domains: Market, Technical, Financial, and Legal/Environmental.",
                        "A Detailed Project Report (DPR) is the authoritative planning document required for bank financing.",
                        "Banks calculate the Debt-Service Coverage Ratio (DSCR) to judge debt repayment capacity.",
                        "Break-Even Analysis determines the exact production volume where revenues equal total operational costs.",
                        "Net Present Value (NPV) and Internal Rate of Return (IRR) are modern discounted cash flow metrics for project appraisal."
                    ],
                    "Project management bridges entrepreneurial vision and commercial viability through empirical feasibility validation and DPR structuring.",
                    "Project Feasibility, DPR, Technical Feasibility, Financial Feasibility, DSCR, Break-Even Analysis, TEV.",
                    "Idea Screening -> Feasibility Verification -> DPR Documentation -> Bank Appraisal -> Execution.",
                    "Relying solely on accounting profit projections without analyzing working capital cash flows, leading to rapid cash crunches."
                )
            ]
        },
        {
            "module_no": 5,
            "title": "Organisation Assistance",
            "hours": 10,
            "marks": 20,
            "topics": [
                create_topic(
                    "ent_m5_t1",
                    "Institutional Support Framework: MSME, SIDBI, SIDO, NSIC, DIC, Venture Capital, and Incubation",
                    ["Institutional Hierarchy (Central vs State)", "MSME Development Act 2006 (Revised Criteria)", "Key Agencies: SIDBI, NSIC, SIDO, DIC", "Startup Funding Stages: Angel Investors vs Venture Capital (VC)", "Business Incubators & Technology Parks"],
                    "Organisation assistance comprises the institutional infrastructure, statutory bodies, financial institutions, and policy schemes established by federal and state governments to nurture, finance, and protect micro, small, and medium enterprises (MSMEs).",
                    "Established under the Ministry of MSME and national industrial development policies to bridge credit, technological, and infrastructure gaps for first-generation entrepreneurs.",
                    "Accelerates industrialization, encourages women's entrepreneurship, boosts export earnings, and insulates nascent startups from predatory competition.",
                    ["State the revised composite criteria for Micro, Small, and Medium Enterprises (MSMED Act).", "Explain the mandates of key apex bodies: SIDBI, SIDO (MSME-DO), NSIC, and DIC.", "Trace the startup equity financing lifecycle from Seed and Angel Capital to Series A/B Venture Capital.", "Evaluate the incubation and acceleration ecosystem."],
                    "Support operates at three levels: Policy (Ministry/SIDO), Grassroots Single-Window Execution (DIC), and Credit Refinancing (SIDBI/NSIC).",
                    [
                        ("MSME Composite Criteria", "Classification combining Investment in Plant & Machinery with Annual Turnover thresholds."),
                        ("SIDBI", "Small Industries Development Bank of India, apex financial institution for MSME credit and venture funds."),
                        ("NSIC", "National Small Industries Corporation; assists MSMEs with machinery hire-purchase, raw material assistance, and marketing."),
                        ("DIC (District Industries Centre)", "District-level single-window facilitation agency for registration, subsidies, and clearances."),
                        ("Angel Investor", "High-net-worth individual providing early seed capital in exchange for convertible debt or equity."),
                        ("Venture Capital (VC)", "Institutional pooled investment fund investing in high-risk, high-growth scalable startups.")
                    ],
                    "1. Composite Criteria: A firm must satisfy both investment AND turnover caps to remain in its designated MSME tier.\n2. Single-Window Scheme: DIC acts as the nodal agency eliminating bureaucratic friction for rural and semi-urban entrepreneurs.",
                    "MSME Registration (Udyam) -> DIC / NSIC Scheme Enrollment -> Bank / SIDBI Credit Evaluation -> Production & Subsidy Disbursal.",
                    [
                        "1. Entrepreneur obtains digital Udyam Registration Certificate.",
                        "2. District Industries Centre (DIC) guides project clearance and state subsidies.",
                        "3. NSIC assists with raw material procurement and government tender exemptions.",
                        "4. SIDBI provides direct financial lending or refinances commercial bank credit.",
                        "5. Incubators provide lab infrastructure, mentorship, and equity investor matchmaking."
                    ],
                    ["Agency / Body", "Jurisdiction", "Primary Mandate / Service Offered"],
                    [
                        ["SIDBI", "National Apex Financial", "Direct lending, refinancing banks, VC Fund-of-Funds"],
                        ["NSIC", "National Commercial / PSU", "Raw material distribution, government tender bidding exemptions"],
                        ["SIDO / MSME-DO", "National Policy & Technical", "Technological assistance, policy formulation, skill training centers"],
                        ["DIC", "District Level Executive", "Single-window clearance, artisan support, state subsidy disbursement"],
                        ["Angel / VC Funds", "Private Institutional Equity", "High-risk growth equity capital, strategic governance, scaling expertise"]
                    ],
                    "// Revised Composite MSME Criteria (2020)\nMicro: Inv <= 1 Cr AND Turnover <= 5 Cr\nSmall: Inv <= 10 Cr AND Turnover <= 50 Cr\nMedium: Inv <= 50 Cr AND Turnover <= 250 Cr",
                    """<svg viewBox='0 0 800 200' xmlns='http://www.w3.org/2000/svg' style='width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid #E5E9F1;'><rect x='300' y='20' width='200' height='40' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='400' y='45' font-family='sans-serif' font-size='12' font-weight='700' fill='#377FE6' text-anchor='middle'>Ministry of MSME (Govt. of India)</text><path d='M 350 60 L 150 90' stroke='#377FE6' stroke-width='2'/><path d='M 400 60 L 400 90' stroke='#786CE5' stroke-width='2'/><path d='M 450 60 L 650 90' stroke='#28A994' stroke-width='2'/><rect x='50' y='90' width='200' height='45' rx='6' fill='#F7F8FC' stroke='#377FE6'/><text x='150' y='115' font-family='sans-serif' font-size='11' font-weight='700' fill='#377FE6' text-anchor='middle'>Financial Support: SIDBI</text><rect x='300' y='90' width='200' height='45' rx='6' fill='#F7F8FC' stroke='#786CE5'/><text x='400' y='115' font-family='sans-serif' font-size='11' font-weight='700' fill='#786CE5' text-anchor='middle'>Marketing &amp; Tech: NSIC / SIDO</text><rect x='550' y='90' width='200' height='45' rx='6' fill='#F7F8FC' stroke='#28A994'/><text x='650' y='115' font-family='sans-serif' font-size='11' font-weight='700' fill='#28A994' text-anchor='middle'>District Level: DIC</text><rect x='100' y='150' width='600' height='35' rx='4' fill='#E9E8F8' stroke='#F2C75C'/><text x='400' y='173' font-family='sans-serif' font-size='10' font-weight='700' fill='#19283D' text-anchor='middle'>Private Equity Ecosystem: Angel Investors -> Incubators -> Venture Capital (VC) Funds</text></svg>""",
                    "Figure 5.1: Multi-Tier Institutional Assistance Ecosystem for MSMEs and Startups",
                    "Startup Capitalization Ladder: Seed to Series B",
                    "- Bootstrapping / FFF (Friends, Family, Fools): Self-funding initial prototypes ($5k - $25k)\n- Angel Investors / Accelerators: Validating product-market fit ($50k - $250k)\n- Venture Capital Series A: Scaling customer acquisition and regional sales ($1M - $5M)\n- Venture Capital Series B: Institutional market expansion and operational automation ($10M+)",
                    [
                        "The MSMED Act revised criteria uses composite investment in plant/machinery AND annual turnover.",
                        "SIDBI acts as the apex financial refinancing body for MSME industrial credit.",
                        "NSIC provides raw material procurement assistance and tender bidding security waivers.",
                        "District Industries Centres (DICs) serve as local single-window nodal agencies for registration and subsidies.",
                        "Angel investors provide early-stage personal capital; Venture Capitalists invest institutional funds in scaling stages.",
                        "Incubators provide physical infrastructure, laboratory access, and regulatory mentorship for emerging ventures."
                    ],
                    "Government institutions and venture capital work collaboratively to remove entry barriers and support nascent enterprises.",
                    "MSME, SIDBI, NSIC, SIDO, DIC, Angel Investor, Venture Capital, Incubation, Udyam.",
                    "Udyam Enrollment -> DIC Clearance -> Financial Refinance (SIDBI) -> Scaling via Venture Capital.",
                    "Confusing Angel Investors (individual high-net-worth angels) with Venture Capitalists (formal institutional fund managers)."
                )
            ]
        }
    ]
