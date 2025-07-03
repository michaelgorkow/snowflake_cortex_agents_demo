from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_financial_report_content(report, title_style, section_style, subsection_style, styles):
    """Create content for Annual Financial Report"""
    story = []
    
    # Title and Header
    story.append(Paragraph("ANNUAL FINANCIAL REPORT", title_style))
    story.append(Paragraph("2023", title_style))
    story.append(Spacer(1, 30))
    
    # Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", section_style))
    exec_summary = """
    Fiscal year 2023 demonstrated resilient performance despite challenging macroeconomic conditions. 
    Total revenue reached $2.8 billion, representing 8.2% growth over 2022. Gross margin improved to 
    42.3% driven by strategic pricing initiatives and supply chain optimization efforts. 
    <br/><br/>
    Operating income increased 12.1% to $456 million, with EBITDA reaching $632 million (22.6% margin). 
    The company maintained strong cash flow generation with $487 million in operating cash flow, 
    enabling continued investment in innovation and market expansion.
    <br/><br/>
    Key performance highlights include successful product launches in the premium segments, 
    expansion into new geographic markets, and significant progress on sustainability initiatives 
    that are increasingly important to consumers and stakeholders.
    """
    story.append(Paragraph(exec_summary, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Financial Highlights
    story.append(Paragraph("FINANCIAL HIGHLIGHTS", section_style))
    
    financial_data = [
        ['Metric', '2023', '2022', 'Change'],
        ['Total Revenue', '$2.8B', '$2.6B', '+8.2%'],
        ['Gross Profit', '$1.18B', '$1.04B', '+13.5%'],
        ['Gross Margin', '42.3%', '40.1%', '+2.2pp'],
        ['Operating Income', '$456M', '$407M', '+12.1%'],
        ['Operating Margin', '16.3%', '15.7%', '+0.6pp'],
        ['EBITDA', '$632M', '$571M', '+10.7%'],
        ['EBITDA Margin', '22.6%', '22.0%', '+0.6pp'],
        ['Net Income', '$342M', '$298M', '+14.8%'],
        ['EPS (Diluted)', '$3.42', '$2.98', '+14.8%'],
        ['Operating Cash Flow', '$487M', '$431M', '+13.0%'],
        ['Free Cash Flow', '$358M', '$312M', '+14.7%']
    ]
    
    financial_table = Table(financial_data, colWidths=[2*inch, 1.2*inch, 1.2*inch, 1*inch])
    financial_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(financial_table)
    story.append(Spacer(1, 25))
    
    # Revenue Analysis by Category
    story.append(Paragraph("REVENUE ANALYSIS BY PRODUCT CATEGORY", section_style))
    
    category_revenue = [
        ['Product Category', '2023 Revenue', '% of Total', 'YoY Growth', 'Key Drivers'],
        ['Coffee', '$7M', '30.0%', '+1.07%', 'Premium positioning, new product launches'],
        ['Chocolate', '$17M', '23.0%', '+1.3%', 'Holiday seasons, gift packaging'],
        ['Water', '$9M', '19.0%', '+3.8%', 'Health trends, summer campaigns'],
        ['Dairy', '$12M', '14.0%', '+1.3%', 'Ice cream innovations, seasonal growth'],
        ['Baby Food', '$10M', '9.0%', '-2.1%', 'Organic segment expansion'],
        ['Cereals', '$9M', '6.0%', '+0.06%', 'Healthy options, back-to-school'],
        ['Pet Care', '$6M', '4.0%', '-1.8%', 'Rapid category growth, premiumization']
    ]
    
    category_table = Table(category_revenue, colWidths=[1.3*inch, 1*inch, 0.8*inch, 0.8*inch, 1.8*inch])
    category_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (3, -1), 'CENTER'),
    ]))
    
    story.append(category_table)
    story.append(Spacer(1, 25))
    
    # Regional Performance
    story.append(Paragraph("REGIONAL PERFORMANCE ANALYSIS", section_style))
    
    regional_analysis = """
    <b>North America:</b> Delivered strong 9.4% growth to $1.12B, driven by successful product 
    innovations and market share gains in coffee and chocolate categories. E-commerce channel 
    expansion contributed 15% of regional growth.
    <br/><br/>
    <b>Europe:</b> Achieved 7.8% growth to $896M despite challenging economic conditions. 
    Premium product mix improvement and successful cost management initiatives offset 
    inflationary pressures.
    <br/><br/>
    <b>Asia Pacific:</b> Outstanding 12.1% growth to $504M supported by market expansion 
    and increasing consumer adoption of Western-style products. China and Southeast Asia 
    markets showed exceptional performance.
    <br/><br/>
    <b>Latin America:</b> Solid 6.2% growth to $196M with strong performance in Brazil 
    and Mexico. Local product adaptations and expanded distribution drove market penetration.
    <br/><br/>
    <b>Middle East & Africa:</b> Emerging markets delivered 8.9% growth to $84M, reflecting 
    successful market entry strategies and partnership development.
    """
    story.append(Paragraph(regional_analysis, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Cost Structure Analysis
    story.append(Paragraph("COST STRUCTURE & MARGIN ANALYSIS", section_style))
    
    cost_analysis = """
    <b>Cost of Goods Sold:</b> Represented 57.7% of revenue, down from 59.9% in 2022. 
    Improvement driven by strategic pricing actions (+$89M impact), supply chain efficiencies 
    (+$34M), and favorable product mix shift toward higher-margin segments (+$28M).
    <br/><br/>
    <b>Operating Expenses:</b> Increased 6.1% to $726M, below revenue growth rate, demonstrating 
    operational leverage. Key investments included digital transformation ($45M), innovation 
    capabilities ($38M), and market expansion ($29M).
    <br/><br/>
    <b>Key Cost Pressures:</b> Raw material inflation (+$67M), labor cost increases (+$34M), 
    and logistics expenses (+$28M) were successfully offset through pricing actions and 
    efficiency programs.
    """
    story.append(Paragraph(cost_analysis, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Cash Flow & Capital Allocation
    story.append(Paragraph("CASH FLOW & CAPITAL ALLOCATION", section_style))
    
    cashflow_data = [
        ['Cash Flow Components', '2023', '2022', 'Change'],
        ['Operating Cash Flow', '$487M', '$431M', '+$56M'],
        ['Capital Expenditures', '$129M', '$119M', '+$10M'],
        ['Free Cash Flow', '$358M', '$312M', '+$46M'],
        ['Dividends Paid', '$89M', '$76M', '+$13M'],
        ['Share Repurchases', '$125M', '$95M', '+$30M'],
        ['Acquisitions', '$67M', '$45M', '+$22M'],
        ['Debt Reduction', '$45M', '$78M', '-$33M']
    ]
    
    cashflow_table = Table(cashflow_data, colWidths=[2.5*inch, 1.2*inch, 1.2*inch, 1*inch])
    cashflow_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkorange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(cashflow_table)
    story.append(Spacer(1, 20))
    
    # Outlook and Strategy
    story.append(Paragraph("2024 OUTLOOK & STRATEGIC PRIORITIES", section_style))
    
    outlook = """
    Looking ahead to 2024, we expect continued revenue growth of 6-8% driven by innovation 
    pipeline launches, geographic expansion, and premium positioning strategies. We anticipate 
    some margin pressure from ongoing inflationary impacts but expect to maintain EBITDA 
    margins above 22% through operational excellence initiatives.
    <br/><br/>
    <b>Strategic Priorities:</b>
    <br/>• Innovation acceleration in health & wellness segments
    <br/>• Digital transformation and e-commerce expansion
    <br/>• Sustainability leadership and ESG commitments
    <br/>• Operational efficiency and cost optimization
    <br/>• Strategic partnerships and selective acquisitions
    <br/>• Talent development and organizational capability building
    """
    story.append(Paragraph(outlook, styles['Normal']))
    
    return story

def create_operational_report_content(report, title_style, section_style, subsection_style, styles):
    """Create content for Supply Chain Cost Analysis Report"""
    story = []
    
    # Title and Header
    story.append(Paragraph("SUPPLY CHAIN COST ANALYSIS", title_style))
    story.append(Paragraph("Q4 2023", title_style))
    story.append(Spacer(1, 30))
    
    # Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", section_style))
    exec_summary = """
    Q4 2023 supply chain operations faced significant headwinds from continued inflationary 
    pressures, logistics challenges, and seasonal demand fluctuations. Total supply chain 
    costs increased 8.4% year-over-year, with raw materials (+12.3%) and transportation 
    (+15.7%) representing the primary drivers.
    <br/><br/>
    Despite these challenges, operational excellence initiatives delivered $23M in cost 
    savings through automation, process optimization, and strategic sourcing. The supply 
    chain team successfully maintained 98.7% order fulfillment rates while managing 
    holiday season peak demand.
    """
    story.append(Paragraph(exec_summary, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Cost Component Analysis
    story.append(Paragraph("SUPPLY CHAIN COST BREAKDOWN", section_style))
    
    cost_breakdown = [
        ['Cost Component', 'Q4 2023', 'Q4 2022', 'YoY Change', '% of Total'],
        ['Raw Materials', '$187M', '$167M', '+12.3%', '45.2%'],
        ['Manufacturing', '$98M', '$94M', '+4.3%', '23.7%'],
        ['Packaging', '$56M', '$52M', '+7.7%', '13.5%'],
        ['Transportation', '$41M', '$35M', '+15.7%', '9.9%'],
        ['Warehousing', '$23M', '$21M', '+9.5%', '5.6%'],
        ['Quality & Compliance', '$9M', '$8M', '+6.3%', '2.2%'],
        ['Total Supply Chain Costs', '$414M', '$382M', '+8.4%', '100.0%']
    ]
    
    cost_table = Table(cost_breakdown, colWidths=[1.8*inch, 1*inch, 1*inch, 0.8*inch, 0.8*inch])
    cost_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(cost_table)
    story.append(Spacer(1, 25))
    
    # Raw Material Cost Analysis
    story.append(Paragraph("RAW MATERIAL COST PRESSURES", section_style))
    
    raw_material_analysis = """
    <b>Coffee Beans:</b> Prices increased 18.2% due to adverse weather conditions in key 
    growing regions and supply chain disruptions. Brazilian frost and Colombian rainfall 
    patterns significantly impacted arabica bean availability.
    <br/><br/>
    <b>Cocoa:</b> Cost inflation of 14.7% driven by West African supply constraints and 
    increased global demand. Sustainability certification requirements adding premium costs.
    <br/><br/>
    <b>Milk & Dairy:</b> Input costs rose 11.3% reflecting feed cost inflation and energy 
    price increases affecting dairy farming operations.
    <br/><br/>
    <b>Packaging Materials:</b> Aluminum and plastic resin costs increased 9.8% and 7.2% 
    respectively. Sustainable packaging initiatives requiring premium materials.
    <br/><br/>
    <b>Sugar:</b> Global sugar prices up 6.4% due to reduced crop yields in key producing regions.
    """
    story.append(Paragraph(raw_material_analysis, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Transportation & Logistics
    story.append(Paragraph("TRANSPORTATION & LOGISTICS CHALLENGES", section_style))
    
    logistics_analysis = """
    <b>Freight Costs:</b> Ocean freight rates remained elevated at $4,200 per container, 
    up 22% from Q4 2022. Port congestion and carrier capacity constraints continued to 
    impact delivery schedules and costs.
    <br/><br/>
    <b>Trucking:</b> Domestic transportation costs increased 12.4% driven by driver shortages, 
    fuel price volatility, and increased demand during holiday shipping season.
    <br/><br/>
    <b>Warehouse Operations:</b> Labor costs rose 8.7% due to tight labor markets and 
    seasonal wage premiums. Automation investments partially offset impact.
    <br/><br/>
    <b>Last-Mile Delivery:</b> E-commerce fulfillment costs up 14.2% reflecting increased 
    customer expectations for faster delivery and higher fuel costs.
    """
    story.append(Paragraph(logistics_analysis, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Cost Mitigation Initiatives
    story.append(Paragraph("COST MITIGATION & EFFICIENCY PROGRAMS", section_style))
    
    mitigation_data = [
        ['Initiative', 'Investment', 'Annual Savings', 'Payback Period'],
        ['Automation Projects', '$15M', '$8.2M', '1.8 years'],
        ['Strategic Sourcing', '$2M', '$12.1M', '2 months'],
        ['Process Optimization', '$5M', '$6.7M', '9 months'],
        ['Energy Efficiency', '$8M', '$3.4M', '2.4 years'],
        ['Waste Reduction', '$3M', '$4.8M', '7 months'],
        ['Digital Supply Chain', '$12M', '$7.9M', '1.5 years'],
        ['Total Programs', '$45M', '$43.1M', '1.0 year']
    ]
    
    mitigation_table = Table(mitigation_data, colWidths=[1.8*inch, 1*inch, 1*inch, 1*inch])
    mitigation_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(mitigation_table)
    story.append(Spacer(1, 25))
    
    # Q1 2024 Outlook
    story.append(Paragraph("Q1 2024 SUPPLY CHAIN OUTLOOK", section_style))
    
    outlook = """
    <b>Expected Challenges:</b>
    <br/>• Continued raw material inflation estimated at 6-8%
    <br/>• Seasonal transportation constraints in Northern regions
    <br/>• Energy cost volatility impacting manufacturing
    <br/>• Labor cost pressures in key distribution centers
    <br/><br/>
    <b>Planned Initiatives:</b>
    <br/>• Long-term supplier agreements to stabilize raw material costs
    <br/>• Additional automation deployments in 3 facilities
    <br/>• Alternative transportation routing optimization
    <br/>• Renewable energy projects to reduce utility cost exposure
    <br/><br/>
    <b>Cost Projections:</b> Supply chain costs expected to increase 5-7% in Q1 2024, 
    with mitigation efforts limiting impact to below revenue growth rate.
    """
    story.append(Paragraph(outlook, styles['Normal']))
    
    return story

def create_sustainability_report_content(report, title_style, section_style, subsection_style, styles):
    """Create content for Sustainability & ESG Report"""
    story = []
    
    # Title and Header
    story.append(Paragraph("SUSTAINABILITY & ESG REPORT", title_style))
    story.append(Paragraph("2023", title_style))
    story.append(Spacer(1, 30))
    
    # Executive Message
    story.append(Paragraph("EXECUTIVE MESSAGE", section_style))
    exec_message = """
    2023 marked a transformative year in our sustainability journey. We accelerated our 
    commitments to environmental stewardship, social responsibility, and governance excellence 
    while maintaining strong business performance. Our integrated approach to ESG creates 
    long-term value for all stakeholders.
    <br/><br/>
    Key achievements include 35% reduction in carbon emissions intensity, 100% sustainably 
    sourced cocoa and coffee, and $50M invested in community development programs. These 
    accomplishments demonstrate our commitment to leading positive change in the food and 
    beverage industry.
    """
    story.append(Paragraph(exec_message, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Environmental Performance
    story.append(Paragraph("ENVIRONMENTAL PERFORMANCE", section_style))
    
    environmental_data = [
        ['Environmental Metric', '2023', '2022', 'Target 2025', 'Progress'],
        ['Carbon Emissions (Scope 1&2)', '245k tCO2e', '312k tCO2e', '180k tCO2e', '68% to target'],
        ['Water Usage Intensity', '2.1 m³/ton', '2.4 m³/ton', '1.8 m³/ton', '75% to target'],
        ['Waste to Landfill', '2,340 tons', '3,120 tons', '1,500 tons', '93% to target'],
        ['Renewable Energy %', '67%', '52%', '85%', '79% to target'],
        ['Sustainable Packaging', '78%', '61%', '95%', '82% to target'],
        ['Recyclable Materials', '89%', '84%', '100%', '89% to target']
    ]
    
    env_table = Table(environmental_data, colWidths=[1.8*inch, 1*inch, 1*inch, 1*inch, 1*inch])
    env_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(env_table)
    story.append(Spacer(1, 25))
    
    # Climate Action Initiatives
    story.append(Paragraph("CLIMATE ACTION & DECARBONIZATION", section_style))
    
    climate_initiatives = """
    <b>Renewable Energy Transition:</b> Installed 15 MW of solar capacity across 8 facilities, 
    bringing total renewable energy to 67% of consumption. Additional 25 MW planned for 2024 
    with estimated $12M annual savings and 45k tCO2e reduction.
    <br/><br/>
    <b>Energy Efficiency:</b> Implemented LED lighting upgrades, HVAC optimization, and 
    equipment modernization across 12 manufacturing sites. Combined initiatives delivered 
    18% energy intensity improvement and $8.7M cost savings.
    <br/><br/>
    <b>Transportation Optimization:</b> Deployed route optimization algorithms and increased 
    rail transport usage, reducing logistics emissions by 22%. Electric vehicle pilot 
    program launched in 3 urban markets.
    <br/><br/>
    <b>Carbon Offsetting:</b> Invested $4.2M in verified carbon offset projects including 
    reforestation (Brazil), renewable energy (India), and methane capture (USA). 
    Offset 38k tCO2e while supporting community development.
    """
    story.append(Paragraph(climate_initiatives, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Sustainable Sourcing
    story.append(Paragraph("SUSTAINABLE SOURCING & SUPPLY CHAIN", section_style))
    
    sourcing_progress = """
    <b>Cocoa Sustainability:</b> Achieved 100% sustainably sourced cocoa through direct 
    farmer partnerships and certification programs. Invested $18M in farmer training, 
    infrastructure development, and premium payments benefiting 45,000 farming families.
    <br/><br/>
    <b>Coffee Sustainability:</b> Reached 100% sustainable coffee sourcing with 78% 
    directly traded. Farmer support programs improved yields by 23% and quality scores by 
    15%. Water conservation projects implemented in 12 growing regions.
    <br/><br/>
    <b>Water Stewardship:</b> Reduced water intensity by 12.5% through process improvements 
    and recycling systems. Launched watershed protection projects in 5 high-risk regions, 
    partnering with local communities and NGOs.
    <br/><br/>
    <b>Packaging Innovation:</b> Introduced plant-based packaging for 15 product lines, 
    representing 23% of portfolio. Reduced packaging weight by 8.4% while maintaining 
    product protection and shelf life.
    """
    story.append(Paragraph(sourcing_progress, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Social Impact
    story.append(Paragraph("SOCIAL IMPACT & COMMUNITY DEVELOPMENT", section_style))
    
    social_data = [
        ['Social Impact Area', 'Investment', 'Beneficiaries', 'Key Outcomes'],
        ['Education Programs', '$12M', '85,000 children', 'School infrastructure, teacher training'],
        ['Healthcare Access', '$8M', '120,000 people', 'Mobile clinics, nutrition programs'],
        ['Women Empowerment', '$6M', '15,000 women', 'Microfinance, leadership development'],
        ['Youth Employment', '$4M', '3,200 youth', 'Skills training, job placement'],
        ['Emergency Relief', '$3M', '50,000 families', 'Disaster response, food security'],
        ['Total Community Investment', '$33M', '273,200 people', 'Sustainable development impact']
    ]
    
    social_table = Table(social_data, colWidths=[1.5*inch, 0.8*inch, 1*inch, 2*inch])
    social_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkorange),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightyellow),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
    ]))
    
    story.append(social_table)
    story.append(Spacer(1, 25))
    
    # Governance & Ethics
    story.append(Paragraph("GOVERNANCE & BUSINESS ETHICS", section_style))
    
    governance_content = """
    <b>Board Diversity:</b> Achieved 45% gender diversity and 35% ethnic diversity on Board 
    of Directors. Independent directors represent 78% of board composition with enhanced 
    oversight of ESG matters through dedicated sustainability committee.
    <br/><br/>
    <b>Supply Chain Compliance:</b> Conducted 1,247 supplier audits with 96% compliance rate. 
    Implemented blockchain traceability for high-risk commodities covering 67% of supply base. 
    Zero tolerance policy for child labor with comprehensive monitoring systems.
    <br/><br/>
    <b>Data Privacy & Security:</b> Invested $15M in cybersecurity infrastructure with 
    zero material data breaches. GDPR compliance across all European operations with 
    enhanced customer data protection protocols.
    <br/><br/>
    <b>Ethics Training:</b> 100% employee completion of annual ethics training with specialized 
    modules for anti-corruption, fair competition, and responsible marketing. Anonymous 
    reporting system received 47 inquiries with 100% investigated and resolved.
    """
    story.append(Paragraph(governance_content, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Economic Impact & Innovation
    story.append(Paragraph("ECONOMIC IMPACT & SUSTAINABLE INNOVATION", section_style))
    
    innovation_content = """
    <b>R&D Investment:</b> Allocated $78M (2.8% of revenue) to sustainable innovation 
    including plant-based alternatives, nutrition enhancement, and circular economy solutions. 
    Filed 23 patents related to sustainable technologies.
    <br/><br/>
    <b>Local Economic Impact:</b> Contributed $890M to local economies through wages, taxes, 
    and local sourcing. Created 2,340 new jobs globally with 68% in developing markets, 
    prioritizing local hiring and skills development.
    <br/><br/>
    <b>Sustainable Products:</b> Launched 12 products with improved nutritional profiles 
    and sustainable ingredients. Sustainable product lines now represent 34% of portfolio 
    with 28% higher growth rates than conventional products.
    <br/><br/>
    <b>Cost Efficiency:</b> Sustainability initiatives generated $43M in operational savings 
    through waste reduction, energy efficiency, and process optimization, demonstrating 
    positive correlation between environmental and financial performance.
    """
    story.append(Paragraph(innovation_content, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # 2024 Commitments
    story.append(Paragraph("2024 SUSTAINABILITY COMMITMENTS", section_style))
    
    commitments_2024 = """
    <b>Environmental Targets:</b>
    <br/>• Achieve 75% renewable energy across all operations
    <br/>• Reduce water intensity by additional 15%
    <br/>• Eliminate single-use plastics in 50% of product lines
    <br/>• Plant 500,000 trees through reforestation partnerships
    <br/><br/>
    <b>Social Impact Goals:</b>
    <br/>• Invest $40M in community development programs
    <br/>• Support 100,000 smallholder farmers with sustainable practices
    <br/>• Achieve 50% women in leadership positions
    <br/>• Provide skills training to 5,000 young people
    <br/><br/>
    <b>Innovation Priorities:</b>
    <br/>• Launch 15 products with enhanced nutritional profiles
    <br/>• Develop fully biodegradable packaging solutions
    <br/>• Establish circular economy pilot programs
    <br/>• Create $100M green innovation fund
    """
    story.append(Paragraph(commitments_2024, styles['Normal']))
    return story

def create_financial_operational_reports(session, output_dir='/tmp/financial_reports/'):
    """Generate financial and operational reports PDFs"""
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    reports_data = [
        {
            'filename': 'Annual_Financial_Report_2023.pdf',
            'report_type': 'Annual Financial Report',
            'period': '2023',
            'content_type': 'financial'
        },
        {
            'filename': 'Supply_Chain_Cost_Analysis_Q4_2023.pdf',
            'report_type': 'Supply Chain Cost Analysis',
            'period': 'Q4 2023',
            'content_type': 'operational'
        },
        {
            'filename': 'Sustainability_ESG_Report_2023.pdf',
            'report_type': 'Sustainability & ESG Report',
            'period': '2023',
            'content_type': 'sustainability'
        }
    ]
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=30,
        alignment=1,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=25,
        textColor=colors.darkred,
        fontName='Helvetica-Bold'
    )
    
    subsection_style = ParagraphStyle(
        'SubsectionHeading',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=10,
        spaceBefore=15,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )
    
    for report in reports_data:
        doc = SimpleDocTemplate(
            os.path.join(output_dir, report['filename']), 
            pagesize=letter,
            rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72
        )
        
        story = []
        
        if report['content_type'] == 'financial':
            story.extend(create_financial_report_content(report, title_style, section_style, subsection_style, styles))
        elif report['content_type'] == 'operational':
            story.extend(create_operational_report_content(report, title_style, section_style, subsection_style, styles))
        elif report['content_type'] == 'sustainability':
            story.extend(create_sustainability_report_content(report, title_style, section_style, subsection_style, styles))
        
        # Build the PDF
        doc.build(story)
        session.file.put(f'{output_dir}/*', stage_location='@DOCUMENTS/financial_operations_reports/', auto_compress=False, overwrite=True)
    print('Created financial operations documents and uploaded them to stage @DOCUMENTS/financial_operations_reports/')