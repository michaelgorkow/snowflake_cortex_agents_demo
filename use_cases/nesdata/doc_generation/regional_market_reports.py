
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_regional_market_reports(session, output_dir='/tmp/regional_market_reports/'):
    """Generate regional market analysis reports PDFs"""
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    reports_data = [
        {
            'filename': 'North_America_Market_Analysis_2023.pdf',
            'region': 'North America',
            'countries': ['United States', 'Canada', 'Mexico'],
            'market_size': 4500,  # Million USD
            'growth_rate': 6.8,
            'our_market_share': 12.4,
            'period': '2023'
        },
        {
            'filename': 'Europe_APAC_Market_Trends_Q4_2023.pdf',
            'region': 'Europe & Asia Pacific',
            'countries': ['Germany', 'France', 'UK', 'Japan', 'China', 'Australia'],
            'market_size': 6200,  # Million USD
            'growth_rate': 4.2,
            'our_market_share': 8.7,
            'period': 'Q4 2023'
        },
        {
            'filename': 'Latin_America_Consumer_Insights_2023.pdf',
            'region': 'Latin America',
            'countries': ['Brazil', 'Argentina', 'Chile', 'Colombia', 'Peru'],
            'market_size': 1800,  # Million USD
            'growth_rate': 8.9,
            'our_market_share': 15.2,
            'period': '2023'
        },
        {
            'filename': 'Global_Competitive_Landscape_Report.pdf',
            'region': 'Global',
            'countries': ['All Major Markets'],
            'market_size': 15400,  # Million USD
            'growth_rate': 5.7,
            'our_market_share': 11.2,
            'period': '2023'
        }
    ]
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=25,
        alignment=1,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=20,
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
        
        if report['region'] == 'North America':
            story.extend(create_north_america_content(report, title_style, section_style, subsection_style, styles))
        elif report['region'] == 'Europe & Asia Pacific':
            story.extend(create_europe_apac_content(report, title_style, section_style, subsection_style, styles))
        elif report['region'] == 'Latin America':
            story.extend(create_latin_america_content(report, title_style, section_style, subsection_style, styles))
        elif report['region'] == 'Global':
            story.extend(create_global_competitive_content(report, title_style, section_style, subsection_style, styles))
        
        # Build the PDF
        doc.build(story)
        session.file.put(f'{output_dir}/*', stage_location='@DOCUMENTS/regional_market_reports/', auto_compress=False, overwrite=True)
    print('Created regional market documents and uploaded them to stage @DOCUMENTS/regional_market_reports/')

def create_north_america_content(report, title_style, section_style, subsection_style, styles):
    """Create content for North America Market Analysis"""
    story = []
    
    # Title and Header
    story.append(Paragraph("NORTH AMERICA MARKET ANALYSIS", title_style))
    story.append(Paragraph("2023 Annual Review", title_style))
    story.append(Spacer(1, 30))
    
    # Market Overview
    story.append(Paragraph("MARKET OVERVIEW", section_style))
    
    market_overview_data = [
        ['Market Metric', 'Value', 'YoY Change'],
        ['Total Market Size', '$4.5 Billion', '+6.8%'],
        ['Our Market Share', '12.4%', '+0.8pp'],
        ['Our Revenue', '$19.3 Million', '+13.2%'],
        ['Market Growth Rate', '6.8%', '+1.2pp vs 2022'],
        ['Consumer Spending Growth', '4.1%', 'Above inflation'],
        ['Number of Active Customers', '2.3 Million', '+8.7%']
    ]
    
    overview_table = Table(market_overview_data, colWidths=[2.5*inch, 1.5*inch, 1.2*inch])
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(overview_table)
    story.append(Spacer(1, 25))
    
    # Market Dynamics
    story.append(Paragraph("MARKET DYNAMICS & TRENDS", section_style))
    
    market_dynamics = """
    <b>Consumer Behavior Shifts:</b> Health and wellness trends continue to drive premium 
    product adoption, with organic and natural segments growing 15.3% year-over-year. 
    Convenience remains paramount, with single-serve and on-the-go formats capturing 
    42% of category growth.
    <br/><br/>
    <b>E-commerce Acceleration:</b> Online sales reached 18.7% of total category sales, 
    up from 14.2% in 2022. Direct-to-consumer channels showing 34% growth, driven by 
    subscription models and personalized nutrition offerings.
    <br/><br/>
    <b>Sustainability Focus:</b> 68% of consumers willing to pay premium for sustainable 
    packaging and ethically sourced ingredients. Carbon-neutral and recyclable packaging 
    becoming key differentiators, especially among Gen Z and Millennial demographics.
    <br/><br/>
    <b>Inflation Impact:</b> Despite 8.2% food inflation, category resilience demonstrated 
    through successful pricing strategies and value perception maintenance. Premium 
    segments outperformed expectations with limited elasticity impact.
    """
    story.append(Paragraph(market_dynamics, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Competitive Landscape
    story.append(Paragraph("COMPETITIVE LANDSCAPE", section_style))
    
    competitor_data = [
        ['Company', 'Market Share', 'Change vs 2022', 'Key Strengths', 'Strategic Focus'],
        ['Our Company', '12.4%', '+0.8pp', 'Innovation, Premium positioning', 'Digital transformation'],
        ['Competitor A', '18.7%', '-0.3pp', 'Scale, Distribution', 'Cost optimization'],
        ['Competitor B', '15.2%', '+0.5pp', 'Brand portfolio, Marketing', 'Health & wellness'],
        ['Competitor C', '11.8%', '-0.2pp', 'Manufacturing efficiency', 'Automation'],
        ['Competitor D', '9.3%', '+0.7pp', 'Innovation speed', 'Plant-based products'],
        ['Others', '32.6%', '-0.5pp', 'Niche segments', 'Specialty channels']
    ]
    
    competitor_table = Table(competitor_data, colWidths=[1*inch, 0.8*inch, 0.8*inch, 1.3*inch, 1.3*inch])
    competitor_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
    ]))
    
    story.append(competitor_table)
    story.append(Spacer(1, 25))
    
    # Category Performance
    story.append(Paragraph("CATEGORY PERFORMANCE ANALYSIS", section_style))
    
    category_performance = """
    <b>Coffee Segment:</b> Strongest performer with 14.2% growth, driven by premium 
    single-origin offerings and cold brew innovations. Our market share in coffee 
    increased to 16.8%, benefiting from successful "Coffee Lovers Special" campaign 
    and new product launches.
    <br/><br/>
    <b>Chocolate & Confectionery:</b> Holiday season drove exceptional Q4 performance 
    (+22.1%), with gift packaging and premium assortments leading growth. Year-round 
    performance steady at 7.3% growth, supported by health-conscious dark chocolate trend.
    <br/><br/>
    <b>Water & Beverages:</b> Flavored and functional water segments expanded 19.4%, 
    while traditional bottled water faced pressure (-2.1%). Sparkling and enhanced 
    water categories showing robust consumer adoption.
    <br/><br/>
    <b>Baby Food:</b> Organic segment growth of 21.7% offset conventional declines. 
    Demographic trends favor continued category expansion, with millennial parents 
    prioritizing premium nutrition and clean ingredients.
    """
    story.append(Paragraph(category_performance, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Regional Insights
    story.append(Paragraph("REGIONAL INSIGHTS", section_style))
    
    regional_breakdown = [
        ['Sub-Region', 'Market Share', 'Growth Rate', 'Key Trends'],
        ['United States', '13.1%', '+7.2%', 'Health trends, E-commerce, Premium positioning'],
        ['Canada', '11.8%', '+5.9%', 'Sustainability focus, French-language marketing'],
        ['Mexico', '10.2%', '+8.4%', 'Middle-class expansion, Modern trade growth']
    ]
    
    regional_table = Table(regional_breakdown, colWidths=[1.5*inch, 1*inch, 1*inch, 2.5*inch])
    regional_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
    ]))
    
    story.append(regional_table)
    story.append(Spacer(1, 25))
    
    # Opportunities & Challenges
    story.append(Paragraph("OPPORTUNITIES & CHALLENGES", section_style))
    
    opportunities = """
    <b>Growth Opportunities:</b>
    <br/>• Plant-based and alternative protein segments showing 28% annual growth
    <br/>• Hispanic consumer segment expanding 12% annually, under-indexed in our portfolio
    <br/>• Functional foods and beverages with health claims gaining mainstream acceptance
    <br/>• Direct-to-consumer and subscription models showing superior margins
    <br/>• Foodservice recovery creating distribution expansion opportunities
    <br/><br/>
    <b>Key Challenges:</b>
    <br/>• Supply chain inflation pressuring margins across all categories
    <br/>• Increased promotional intensity from private label and value competitors
    <br/>• Regulatory changes in health claims and nutritional labeling requirements
    <br/>• Talent acquisition challenges in digital marketing and data analytics
    <br/>• Consumer price sensitivity in economic uncertainty environment
    """
    story.append(Paragraph(opportunities, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Market Forecast
    story.append(Paragraph("2024 MARKET FORECAST", section_style))
    
    forecast_data = [
        ['Forecast Metric', '2024E', 'Change vs 2023'],
        ['Total Market Growth', '+5.2%', 'Moderation from 2023'],
        ['Our Market Share Target', '13.1%', '+0.7pp gain'],
        ['E-commerce Penetration', '22.5%', '+3.8pp increase'],
        ['Premium Segment Growth', '+11.3%', 'Continued outperformance'],
        ['Innovation Pipeline Impact', '+$45M', 'New product contributions'],
        ['Market Consolidation Risk', 'Medium', 'M&A activity expected']
    ]
    
    forecast_table = Table(forecast_data, colWidths=[2.5*inch, 1.5*inch, 1.8*inch])
    forecast_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkorange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(forecast_table)
    story.append(Spacer(1, 20))
    
    # Strategic Recommendations
    recommendations = """
    <b>Strategic Recommendations for 2024:</b>
    <br/>1. Accelerate health & wellness product innovation with clean label positioning
    <br/>2. Expand e-commerce capabilities and direct-to-consumer offerings
    <br/>3. Increase marketing investment in Hispanic and Gen Z consumer segments  
    <br/>4. Develop strategic partnerships for plant-based product development
    <br/>5. Implement dynamic pricing strategies to optimize margin in inflationary environment
    """
    story.append(Paragraph(recommendations, styles['Normal']))
    
    return story

def create_europe_apac_content(report, title_style, section_style, subsection_style, styles):
    """Create content for Europe & APAC Market Trends"""
    story = []
    
    # Title and Header
    story.append(Paragraph("EUROPE & ASIA PACIFIC", title_style))
    story.append(Paragraph("Market Trends Report - Q4 2023", title_style))
    story.append(Spacer(1, 30))
    
    # Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", section_style))
    executive_summary = """
    Q4 2023 performance across Europe and Asia Pacific markets demonstrated resilience 
    despite challenging macroeconomic conditions. Combined market size of $6.2 billion 
    grew 4.2% year-over-year, with Asia Pacific (+7.8%) significantly outperforming 
    Europe (+1.9%) due to continued economic recovery and consumer spending normalization.
    <br/><br/>
    Our market share reached 8.7%, representing a 0.4 percentage point gain driven by 
    successful product localizations and strategic distribution partnerships. Premium 
    positioning and health-focused products showed particular strength across both regions.
    """
    story.append(Paragraph(executive_summary, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Regional Performance Split
    story.append(Paragraph("REGIONAL PERFORMANCE BREAKDOWN", section_style))
    
    regional_performance = [
        ['Region', 'Market Size', 'YoY Growth', 'Our Share', 'Our Revenue', 'Key Drivers'],
        ['Europe', '$3.8B', '+1.9%', '9.2%', '$16.2M', 'Premium coffee, Sustainability'],
        ['Asia Pacific', '$2.4B', '+7.8%', '7.9%', '$9.2M', 'Health trends, Urbanization'],
        ['Combined', '$6.2B', '+4.2%', '8.7%', '$25.4M', 'Innovation, Local adaptation']
    ]
    
    regional_table = Table(regional_performance, colWidths=[1*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.8*inch])
    regional_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (4, -1), 'CENTER'),
    ]))
    
    story.append(regional_table)
    story.append(Spacer(1, 25))
    
    # Europe Deep Dive
    story.append(Paragraph("EUROPE MARKET ANALYSIS", section_style))
    
    europe_analysis = """
    <b>Market Conditions:</b> European markets faced headwinds from energy costs, 
    inflation (averaging 6.4%), and consumer sentiment challenges. However, premium 
    segments showed resilience with only 2.1% volume decline while maintaining 
    price realization of +8.3%.
    <br/><br/>
    <b>Sustainability Leadership:</b> European consumers leading global sustainability 
    adoption, with 78% willing to pay premium for eco-friendly packaging. Our 
    plant-based and organic product lines achieved 23.4% growth in the region.
    <br/><br/>
    <b>Country Performance:</b>
    <br/>• Germany: Market share 11.2% (+0.6pp), strong coffee and chocolate performance
    <br/>• France: Market share 8.9% (+0.3pp), premium positioning success
    <br/>• UK: Market share 7.4% (-0.1pp), Brexit-related supply chain challenges
    <br/>• Others: Market share 9.8% (+0.5pp), Eastern Europe expansion
    <br/><br/>
    <b>Regulatory Environment:</b> New EU regulations on health claims and packaging 
    sustainability creating both challenges and opportunities. Early adoption of 
    compliance measures providing competitive advantages.
    """
    story.append(Paragraph(europe_analysis, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Asia Pacific Deep Dive
    story.append(Paragraph("ASIA PACIFIC MARKET ANALYSIS", section_style))
    
    apac_analysis = """
    <b>Growth Dynamics:</b> APAC markets demonstrated robust growth with urbanization, 
    middle-class expansion, and Western lifestyle adoption driving category demand. 
    E-commerce penetration reached 31.2%, the highest globally.
    <br/><br/>
    <b>Localization Success:</b> Tailored product formulations for local taste preferences 
    showing superior performance. Green tea flavored products and reduced-sugar 
    variants particularly successful in health-conscious markets.
    <br/><br/>
    <b>Country Performance:</b>
    <br/>• China: Market share 6.8% (+1.2pp), rapid urban expansion and premium adoption
    <br/>• Japan: Market share 12.1% (+0.8pp), aging population driving health trends
    <br/>• Australia: Market share 14.3% (+0.4pp), sustainability and local sourcing focus
    <br/>• Southeast Asia: Market share 5.9% (+1.8pp), emerging market penetration
    <br/><br/>
    <b>Digital Commerce:</b> Mobile-first commerce strategies essential, with 67% of 
    purchases through mobile platforms. Social commerce and live-streaming sales 
    channels showing remarkable growth rates.
    """
    story.append(Paragraph(apac_analysis, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Competitive Intelligence
    story.append(Paragraph("COMPETITIVE INTELLIGENCE", section_style))
    
    competitive_moves = """
    <b>Major Competitive Developments:</b>
    <br/>• Regional Competitor X launched plant-based protein line in 8 European markets
    <br/>• Global Player Y acquired specialty coffee roaster with €200M investment
    <br/>• Local Leader Z expanded manufacturing capacity in Thailand and Vietnam
    <br/>• Tech-enabled Startup W gained 2.1% share through direct-to-consumer model
    <br/><br/>
    <b>Price Competition:</b> Increased promotional intensity in traditional retail 
    channels, with average promotion depth increasing 2.3pp. However, premium 
    segments maintaining pricing discipline with selective promotional strategies.
    <br/><br/>
    <b>Innovation Race:</b> Accelerating product launch cycles with average time-to-market 
    reducing from 18 to 14 months. Sustainability and health positioning becoming 
    table stakes for new product success.
    """
    story.append(Paragraph(competitive_moves, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Consumer Insights
    story.append(Paragraph("CONSUMER BEHAVIOR INSIGHTS", section_style))
    
    consumer_insights = [
        ['Consumer Trend', 'Europe Impact', 'APAC Impact', 'Business Implications'],
        ['Health & Wellness', 'High', 'Very High', 'Functional products, Clean labels'],
        ['Sustainability', 'Very High', 'Medium', 'Eco packaging, Ethical sourcing'],
        ['Convenience', 'Medium', 'High', 'On-the-go formats, E-commerce'],
        ['Premiumization', 'High', 'Very High', 'Quality positioning, Brand building'],
        ['Digital Engagement', 'Medium', 'Very High', 'Social commerce, Influencer marketing'],
        ['Local Preferences', 'Medium', 'Very High', 'Product localization, Cultural adaptation']
    ]
    
    consumer_table = Table(consumer_insights, colWidths=[1.3*inch, 0.9*inch, 0.9*inch, 2.1*inch])
    consumer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
    ]))
    
    story.append(consumer_table)
    story.append(Spacer(1, 25))
    
    # Q1 2024 Outlook
    story.append(Paragraph("Q1 2024 MARKET OUTLOOK", section_style))
    
    outlook_2024 = """
    <b>Europe Forecast:</b> Cautious optimism with 2.5-3.5% growth expected as 
    economic conditions stabilize. Energy cost normalization and improved consumer 
    confidence should support volume recovery while maintaining pricing gains.
    <br/><br/>
    <b>APAC Forecast:</b> Continued robust growth of 6-8% driven by ongoing 
    urbanization and middle-class expansion. China reopening effects and increased 
    travel/hospitality demand creating additional tailwinds.
    <br/><br/>
    <b>Strategic Focus Areas:</b>
    <br/>• Accelerate sustainability innovations in Europe
    <br/>• Expand digital commerce capabilities in APAC
    <br/>• Develop region-specific health and wellness propositions
    <br/>• Strengthen local manufacturing and supply chain resilience
    <br/>• Invest in emerging market penetration strategies
    """
    story.append(Paragraph(outlook_2024, styles['Normal']))
    
    return story

def create_latin_america_content(report, title_style, section_style, subsection_style, styles):
    """Create content for Latin America Consumer Insights"""
    story = []
    
    # Title and Header
    story.append(Paragraph("LATIN AMERICA", title_style))
    story.append(Paragraph("Consumer Insights & Market Analysis 2023", title_style))
    story.append(Spacer(1, 30))
    
    # Market Snapshot
    story.append(Paragraph("MARKET SNAPSHOT", section_style))
    
    market_snapshot = """
    Latin America represents our fastest-growing region with 8.9% market growth and 
    15.2% market share, reflecting successful localization strategies and expanding 
    middle-class demographics. Total addressable market of $1.8 billion provides 
    significant runway for continued expansion across five key countries.
    <br/><br/>
    Strong consumer affinity for premium brands, combined with increasing disposable 
    incomes and urbanization trends, created favorable conditions for category 
    expansion and share gains throughout 2023.
    """
    story.append(Paragraph(market_snapshot, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Country Analysis
    story.append(Paragraph("COUNTRY-BY-COUNTRY ANALYSIS", section_style))
    
    country_data = [
        ['Country', 'Market Size', 'Our Share', 'Our Revenue', 'Growth Rate', 'Key Success Factors'],
        ['Brazil', '$720M', '18.4%', '+12.1%', '', 'Local partnerships, Coffee culture'],
        ['Mexico', '$490M', '14.2%', '+7.8%', '', 'Modern trade expansion, Premium positioning'],
        ['Argentina', '$280M', '12.8%', '+6.2%', '', 'Inflation hedging, Local production'],
        ['Colombia', '$190M', '16.9%', '+11.4%', '', 'Coffee heritage, Direct sourcing'],
        ['Chile', '$120M', '13.7%', '+8.9%', '', 'Health trends, Sustainability focus']
    ]

    country_data = [
        ['Country', 'Market Size', 'Our Share', 'Our Revenue', 'Growth Rate', 'Key Success Factors'],
        ['Brazil', '$28.3M', '18.4%', '$5.2M', '+12.1%', 'Local partnerships, Coffee culture'],
        ['Mexico', '$19.7M', '14.2%', '$2.8M', '+7.8%', 'Modern trade expansion, Premium positioning'],
        ['Argentina', '$14.1M', '12.8%', '$1.8M', '+6.2%', 'Inflation hedging, Local production'],
        ['Colombia', '$10.7M', '16.9%', '$1.8M', '+11.4%', 'Coffee heritage, Direct sourcing'],
        ['Chile', '$8.0M', '13.7%', '$1.1M', '+8.9%', 'Health trends, Sustainability focus']
    ]
    
    country_table = Table(country_data, colWidths=[1*inch, 0.9*inch, 0.8*inch, 0.8*inch, 2*inch])
    country_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (3, -1), 'CENTER'),
    ]))
    
    story.append(country_table)
    story.append(Spacer(1, 25))
    
    # Consumer Demographics
    story.append(Paragraph("CONSUMER DEMOGRAPHICS & BEHAVIOR", section_style))
    
    demographics = """
    <b>Age Demographics:</b> 58% of our consumers aged 25-45, representing the core 
    middle-class segment with growing purchasing power. Millennial parents (28-38) 
    driving premium baby food and health-conscious product adoption.
    <br/><br/>
    <b>Income Segmentation:</b> Upper-middle class ($25K-50K household income) 
    represents 34% of volume but 52% of revenue, demonstrating premium positioning 
    success. Lower-middle class accessibility programs showing strong penetration.
    <br/><br/>
    <b>Geographic Distribution:</b> Urban consumers (78% of sales) leading premium 
    adoption, while rural markets (22%) showing rapid modern trade penetration and 
    brand awareness growth of 23% annually.
    <br/><br/>
    <b>Cultural Preferences:</b> Strong preference for authentic flavors and local 
    ingredient integration. Family-oriented purchasing decisions with 67% of buyers 
    considering children's preferences in product selection.
    """
    story.append(Paragraph(demographics, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Channel Evolution
    story.append(Paragraph("RETAIL CHANNEL EVOLUTION", section_style))
    
    channel_evolution = """
    <b>Modern Trade Growth:</b> Supermarkets and hypermarkets expanded 15.3% 
    year-over-year, now representing 52% of category sales. International retail 
    chains driving standardization and premium shelf space allocation.
    <br/><br/>
    <b>Traditional Trade Resilience:</b> Mom-and-pop stores maintain 31% share 
    through proximity convenience and credit relationships. Our traditional trade 
    programs achieved 89% distribution coverage across target outlets.
    <br/><br/>
    <b>E-commerce Emergence:</b> Online sales reached 8.4% of total, growing 45% 
    annually. Mobile commerce and social selling particularly strong among 
    urban millennials, with WhatsApp commerce gaining traction.
    <br/><br/>
    <b>Cash-and-Carry:</b> B2B wholesale channel serving small retailers growing 
    12.7%, providing efficient distribution network for market penetration.
    """
    story.append(Paragraph(channel_evolution, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Economic Factors
    story.append(Paragraph("ECONOMIC ENVIRONMENT IMPACT", section_style))
    
    economic_factors = [
        ['Economic Factor', 'Impact Level', 'Business Response', 'Outcome'],
        ['Currency Volatility', 'High', 'Local sourcing, Hedging strategies', 'Margin protection'],
        ['Inflation (avg 18.4%)', 'Very High', 'Dynamic pricing, Pack optimization', 'Market share gains'],
        ['Interest Rates', 'Medium', 'Working capital optimization', 'Cash flow positive'],
        ['Employment Growth', 'Positive', 'Expanded distribution', 'Volume growth'],
        ['Government Policies', 'Mixed', 'Regulatory compliance', 'License to operate'],
        ['Trade Agreements', 'Positive', 'Supply chain optimization', 'Cost advantages']
    ]
    
    economic_table = Table(economic_factors, colWidths=[1.3*inch, 1*inch, 1.5*inch, 1.2*inch])
    economic_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkorange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
    ]))
    
    story.append(economic_table)
    story.append(Spacer(1, 25))
    
    # Innovation & Localization
    story.append(Paragraph("PRODUCT INNOVATION & LOCALIZATION", section_style))
    
    innovation_success = """
    <b>Flavor Localization:</b> Dulce de leche, tropical fruit, and coffee-based 
    variations achieved 34% higher trial rates than global formulations. Local 
    taste preferences significantly impacting product development roadmap.
    <br/><br/>
    <b>Pack Size Optimization:</b> Smaller, affordable pack sizes (targeting $0.50-$1.50 
    price points) expanded market accessibility while maintaining unit profitability 
    through improved manufacturing efficiency.
    <br/><br/>
    <b>Cultural Integration:</b> Holiday and celebration-themed products achieved 
    67% higher seasonal sales than standard offerings. Regional festival tie-ins 
    and cultural celebrations driving emotional brand connection.
    <br/><br/>
    <b>Health Positioning:</b> Functional benefits communication adapted for local 
    health consciousness trends. Natural ingredients and "menos artificial" 
    positioning resonating strongly with health-aware consumers.
    """
    story.append(Paragraph(innovation_success, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Competitive Landscape
    story.append(Paragraph("COMPETITIVE DYNAMICS", section_style))
    
    competitive_landscape = """
    <b>Local Champions:</b> Regional players maintain strong positions through 
    cultural connection and price competitiveness. Our strategy focuses on 
    premium positioning while respecting local market dynamics.
    <br/><br/>
    <b>International Expansion:</b> Global competitors increasing investment in 
    region, particularly in Brazil and Mexico. Market consolidation expected 
    as scale advantages become more important.
    <br/><br/>
    <b>Private Label Growth:</b> Retailer brands gaining 2.3pp share annually, 
    primarily in basic segments. Premium differentiation strategy effectively 
    defending against private label encroachment.
    <br/><br/>
    <b>Innovation Speed:</b> Faster product launch cycles necessitated by 
    competitive intensity. Time-to-market reduced from 12 to 8 months through 
    regional innovation centers and local manufacturing partnerships.
    """
    story.append(Paragraph(competitive_landscape, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Growth Strategy
    story.append(Paragraph("2024 GROWTH STRATEGY", section_style))
    
    growth_strategy = """
    <b>Market Expansion:</b>
    <br/>• Enter 3 new countries (Peru, Ecuador, Uruguay) with targeted product portfolio
    <br/>• Expand distribution to 15,000 additional traditional trade outlets
    <br/>• Launch e-commerce platforms in Brazil and Mexico
    <br/><br/>
    <b>Product Innovation:</b>
    <br/>• Introduce 8 locally-adapted product variations
    <br/>• Develop affordable premium tier for emerging middle class
    <br/>• Expand functional food offerings with health benefits
    <br/><br/>
    <b>Operational Excellence:</b>
    <br/>• Establish regional manufacturing hub in Brazil
    <br/>• Implement currency hedging strategy across all markets  
    <br/>• Develop local supplier partnerships for key ingredients
    <br/><br/>
    <b>Expected Outcomes:</b> 10-12% revenue growth with market share expansion 
    to 16.8% across target markets.
    """
    story.append(Paragraph(growth_strategy, styles['Normal']))
    
    return story

def create_global_competitive_content(report, title_style, section_style, subsection_style, styles):
    """Create content for Global Competitive Landscape Report"""
    story = []
    
    # Title and Header
    story.append(Paragraph("GLOBAL COMPETITIVE LANDSCAPE", title_style))
    story.append(Paragraph("Strategic Intelligence Report 2023", title_style))
    story.append(Spacer(1, 30))
    
    # Global Market Overview
    story.append(Paragraph("GLOBAL MARKET OVERVIEW", section_style))
    
    global_overview = """
    The global food and beverage market reached $15.4 billion in 2023, growing 5.7% 
    year-over-year despite macroeconomic challenges. Market consolidation accelerated 
    with $12.8 billion in M&A activity, while innovation cycles shortened to meet 
    rapidly evolving consumer preferences.
    <br/><br/>
    Our company achieved 11.2% global market share, ranking #4 globally and maintaining 
    strong positions across all key categories. Strategic focus on premium positioning, 
    sustainability leadership, and digital transformation delivered market-beating 
    growth rates across most regions.
    """
    story.append(Paragraph(global_overview, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Competitive Positioning
    story.append(Paragraph("GLOBAL COMPETITIVE POSITIONING", section_style))
    
    competitive_positioning = [
        ['Rank', 'Company', 'Market Share', 'Revenue', 'Key Strengths', 'Strategic Focus'],
        ['1', 'Global Leader Alpha', '22.3%', '$3.4B', 'Scale, Distribution', 'Cost leadership'],
        ['2', 'International Beta', '18.7%', '$2.9B', 'Brand portfolio', 'Innovation'],
        ['3', 'Multinational Gamma', '14.1%', '$2.2B', 'Manufacturing', 'Efficiency'],
        ['4', 'Our Company', '11.2%', '$1.7B', 'Premium positioning', 'Differentiation'],
        ['5', 'Regional Delta', '8.9%', '$1.4B', 'Local expertise', 'Market penetration'],
        ['6-10', 'Others Combined', '24.8%', '$3.8B', 'Niche focus', 'Specialization']
    ]
    
    positioning_table = Table(competitive_positioning, colWidths=[0.5*inch, 1.2*inch, 0.8*inch, 0.7*inch, 1.2*inch, 1.1*inch])
    positioning_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('BACKGROUND', (0, 4), (-1, 4), colors.lightblue),  # Highlight our company
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 4), (-1, 4), 'Helvetica-Bold'),  # Bold our company row
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (2, 0), (3, -1), 'CENTER'),
    ]))
    
    story.append(positioning_table)
    story.append(Spacer(1, 25))
    
    # Competitive Intelligence
    story.append(Paragraph("COMPETITIVE INTELLIGENCE & STRATEGIC MOVES", section_style))
    
    competitive_intelligence = """
    <b>Global Leader Alpha:</b> Announced $2.1B acquisition of specialty beverage company, 
    expanding portfolio into functional drinks and plant-based nutrition. Focus on 
    cost synergies and manufacturing consolidation. Price competition strategy in 
    developing markets pressuring category profitability.
    <br/><br/>
    <b>International Beta:</b> Launched innovation accelerator program with $500M 
    investment in emerging technologies. Partnership with tech companies for 
    personalized nutrition and direct-to-consumer platforms. Sustainability 
    commitments exceeding industry standards creating competitive advantages.
    <br/><br/>
    <b>Multinational Gamma:</b> Divested non-core assets worth $1.8B to focus on 
    core categories. Significant automation investments reducing labor costs by 
    15% across manufacturing network. Aggressive pricing strategy gaining share 
    in price-sensitive segments.
    <br/><br/>
    <b>Regional Delta:</b> Expanding globally through strategic partnerships and 
    licensing agreements. Strong digital marketing capabilities and influencer 
    partnerships driving brand awareness among younger demographics. Disruptive 
    innovation in packaging and convenience formats.
    """
    story.append(Paragraph(competitive_intelligence, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Market Share Dynamics
    story.append(Paragraph("MARKET SHARE EVOLUTION & TRENDS", section_style))
    
    share_dynamics = """
    <b>Share Gains & Losses (2023 vs 2022):</b>
    <br/>• Our Company: +0.7pp (successful premium strategy and innovation pipeline)
    <br/>• International Beta: +0.5pp (sustainability leadership and brand building)
    <br/>• Regional Delta: +0.8pp (digital disruption and convenience innovation)
    <br/>• Global Leader Alpha: -0.3pp (price competition impact on margins)
    <br/>• Multinational Gamma: -0.4pp (portfolio rationalization effects)
    <br/><br/>
    <b>Category Leadership Analysis:</b>
    <br/>• Coffee: Beta leads (24.1%), we rank #3 (16.8%)
    <br/>• Chocolate: Alpha leads (28.4%), we rank #2 (19.2%)
    <br/>• Water: Alpha leads (31.2%), we rank #4 (12.7%)
    <br/>• Baby Food: We lead (22.1%), Beta #2 (18.9%)
    <br/>• Dairy: Gamma leads (26.8%), we rank #3 (15.4%)
    """
    story.append(Paragraph(share_dynamics, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Innovation Landscape
    story.append(Paragraph("INNOVATION & TECHNOLOGY LANDSCAPE", section_style))
    
    innovation_trends = [
        ['Innovation Area', 'Market Impact', 'Our Position', 'Competitive Threat', 'Investment Priority'],
        ['Plant-based Products', 'High', 'Following', 'Medium', 'High'],
        ['Functional Foods', 'Very High', 'Leading', 'Low', 'Very High'],
        ['Sustainable Packaging', 'High', 'Leading', 'Medium', 'High'],
        ['Personalized Nutrition', 'Medium', 'Developing', 'High', 'Medium'],
        ['Digital Commerce', 'Very High', 'Competitive', 'High', 'Very High'],
        ['Alternative Proteins', 'Medium', 'Exploring', 'Medium', 'Medium'],
        ['Clean Label', 'High', 'Leading', 'Low', 'High']
    ]
    
    innovation_table = Table(innovation_trends, colWidths=[1.2*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1*inch])
    innovation_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(innovation_table)
    story.append(Spacer(1, 25))
    
    # Threat Assessment
    story.append(Paragraph("COMPETITIVE THREAT ASSESSMENT", section_style))
    
    threat_assessment = """
    <b>High Priority Threats:</b>
    <br/>• Beta's sustainability leadership creating consumer preference advantages
    <br/>• Delta's digital-native approach disrupting traditional retail relationships
    <br/>• Private label growth in key retailers pressuring mainstream positioning
    <br/>• New entrant startups with venture capital backing in niche segments
    <br/><br/>
    <b>Medium Priority Concerns:</b>
    <br/>• Alpha's scale advantages in raw material procurement during inflation
    <br/>• Gamma's automation creating cost advantages in price-competitive segments
    <br/>• Regional players strengthening through strategic partnerships
    <br/><br/>
    <b>Emerging Risks:</b>
    <br/>• Technology companies entering food/beverage through platform business models
    <br/>• Direct-to-consumer brands bypassing traditional retail distribution
    <br/>• Regulatory changes favoring local/sustainable production methods
    """
    story.append(Paragraph(threat_assessment, styles['Normal']))
    story.append(Spacer(1, 25))
    
    # Strategic Recommendations
    story.append(Paragraph("STRATEGIC RECOMMENDATIONS", section_style))
    
    recommendations = """
    <b>Defensive Strategies:</b>
    <br/>1. Accelerate sustainability initiatives to match Beta's leadership position
    <br/>2. Strengthen retailer partnerships with exclusive product developments
    <br/>3. Enhance cost competitiveness through supply chain optimization
    <br/>4. Protect core categories through innovation and marketing investment
    <br/><br/>
    <b>Offensive Opportunities:</b>
    <br/>1. Leverage baby food category leadership for portfolio cross-selling
    <br/>2. Expand premium positioning to additional categories and regions
    <br/>3. Develop strategic partnerships in plant-based and functional foods
    <br/>4. Acquire innovative startups to access new technologies and consumer insights
    <br/><br/>
    <b>Investment Priorities:</b>
    <br/>1. Digital transformation and e-commerce capabilities ($150M)
    <br/>2. Sustainable packaging and clean label innovations ($100M)
    <br/>3. Market expansion in high-growth regions ($75M)
    <br/>4. Manufacturing automation and efficiency ($125M)
    """
    story.append(Paragraph(recommendations, styles['Normal']))
    return story