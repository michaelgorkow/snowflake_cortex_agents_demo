from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from datetime import datetime
import os

def create_marketing_campaign_documents(session, output_dir='/tmp/marketing_campaigns'):
    """Generate marketing campaign brief and results PDFs"""
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    campaigns_data = [
        {
            'filename': 'Coffee_Lovers_Campaign_Brief_Results.pdf',
            'campaign_name': 'Coffee Lovers Special',
            'campaign_id': 'CAMP-001',
            'category': 'Coffee',
            'period': 'March - May 2022',
            'budget': 500000,
            'discount': 15,
            'objective': 'Increase coffee category market share by 12% and drive trial of premium NesKafe Gold',
            'target_audience': 'Coffee enthusiasts aged 25-45, household income $50K+, urban/suburban',
            'key_products': ['NesKafe Classic', 'NesKafe Gold', 'NesKafe Cappuccino'],
            'channels': ['Digital advertising', 'In-store displays', 'Sampling programs', 'Social media'],
            'kpis': {
                'sales_lift': {'target': 25, 'actual': 32},
                'market_share': {'target': 12, 'actual': 14.8},
                'brand_awareness': {'target': 15, 'actual': 18},
                'roi': {'target': 3.2, 'actual': 4.1}
            },
            'results_summary': 'Campaign exceeded all targets with 32% sales lift vs 25% target. Strong performance in digital channels with 68% of incremental sales attributed to online activation.',
            'lessons_learned': 'Premium positioning messaging resonated well. Sampling drove higher conversion rates than anticipated. Recommend extending sampling component in future campaigns.',
            'media_spend': {
                'Digital': 180000,
                'In-store': 150000,
                'Sampling': 120000,
                'Traditional': 50000
            }
        },
        {
            'filename': 'Summer_Hydration_Campaign_Analysis.pdf',
            'campaign_name': 'Summer Hydration',
            'campaign_id': 'CAMP-002',
            'category': 'Water',
            'period': 'June - August 2022',
            'budget': 750000,
            'discount': 10,
            'objective': 'Position PureLife as premium hydration choice during peak summer season, target 20% volume increase',
            'target_audience': 'Active lifestyle consumers aged 18-55, health-conscious, outdoor enthusiasts',
            'key_products': ['PureLife Natural', 'PureLife Sparkling', 'PureLife Flavoured'],
            'channels': ['Outdoor advertising', 'Sports partnerships', 'Influencer marketing', 'Retail promotions'],
            'kpis': {
                'volume_growth': {'target': 20, 'actual': 28},
                'new_customers': {'target': 15000, 'actual': 22400},
                'engagement_rate': {'target': 4.5, 'actual': 6.2},
                'cost_per_acquisition': {'target': 12.50, 'actual': 9.80}
            },
            'results_summary': 'Outstanding performance with 28% volume growth driven by successful sports partnerships and influencer collaborations. Weather patterns favored campaign timing.',
            'lessons_learned': 'Influencer partnerships delivered exceptional ROI. Sports venue activations created strong brand association. Weather dependency noted for future planning.',
            'media_spend': {
                'Sports Partnerships': 250000,
                'Influencer Marketing': 200000,
                'Outdoor/OOH': 180000,
                'Digital': 120000
            }
        },
        {
            'filename': 'Holiday_Treats_ROI_Report.pdf',
            'campaign_name': 'Holiday Treats',
            'campaign_id': 'CAMP-004',
            'category': 'Chocolate',
            'period': 'November - December 2022',
            'budget': 1000000,
            'discount': 25,
            'objective': 'Maximize holiday season chocolate sales, establish gift-giving positioning, achieve $4M incremental revenue',
            'target_audience': 'Holiday shoppers, gift-buyers, families with children, premium chocolate consumers',
            'key_products': ['ChocoBars Dark', 'DeluxeChoc Premium', 'SweetTreats Caramel', 'CreamyBites Hazelnut'],
            'channels': ['TV advertising', 'Holiday packaging', 'Gift sets', 'E-commerce promotions'],
            'kpis': {
                'incremental_revenue': {'target': 4000000, 'actual': 5200000},
                'gift_set_sales': {'target': 25000, 'actual': 31500},
                'premium_mix': {'target': 35, 'actual': 42},
                'customer_satisfaction': {'target': 8.5, 'actual': 8.9}
            },
            'results_summary': 'Exceptional holiday performance with $5.2M incremental revenue vs $4M target. Premium gift sets drove margin expansion and brand elevation.',
            'lessons_learned': 'Holiday packaging crucial for gift positioning. TV advertising created strong emotional connection. E-commerce fulfillment challenges during peak periods.',
            'media_spend': {
                'TV Advertising': 400000,
                'Holiday Packaging': 250000,
                'Digital/E-commerce': 200000,
                'In-store Displays': 150000
            }
        },
        {
            'filename': 'Digital_Marketing_Strategy_2023.pdf',
            'campaign_name': 'Integrated Digital Strategy 2023',
            'campaign_id': 'STRAT-2023',
            'category': 'Multi-Category',
            'period': 'January - December 2023',
            'budget': 2500000,
            'discount': 'Variable by campaign',
            'objective': 'Establish omnichannel digital presence, increase online sales by 45%, improve customer data collection',
            'target_audience': 'Digital-native consumers across all product categories, emphasis on mobile-first experience',
            'key_products': ['Full portfolio with rotating focus'],
            'channels': ['Social media', 'Search marketing', 'Programmatic display', 'Email marketing', 'Mobile apps'],
            'kpis': {
                'online_sales_growth': {'target': 45, 'actual': 52},
                'digital_attribution': {'target': 30, 'actual': 38},
                'email_list_growth': {'target': 100000, 'actual': 135000},
                'mobile_conversion': {'target': 3.2, 'actual': 4.1}
            },
            'results_summary': '2023 digital transformation exceeded expectations with 52% online growth. Mobile-first approach and personalization drove superior performance.',
            'lessons_learned': 'Data-driven personalization delivers significant lift. Mobile optimization critical. Cross-category campaigns more efficient than single-product focus.',
            'media_spend': {
                'Search Marketing': 800000,
                'Social Media': 600000,
                'Programmatic Display': 500000,
                'Email/CRM': 300000,
                'Mobile/App': 300000
            }
        }
    ]
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CampaignTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        alignment=1,
        textColor=colors.darkred,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=20,
        textColor=colors.darkblue,
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
    
    for campaign in campaigns_data:
        doc = SimpleDocTemplate(
            os.path.join(output_dir, campaign['filename']), 
            pagesize=letter,
            rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72
        )
        
        story = []
        
        # Title and Header
        story.append(Paragraph(f"CAMPAIGN ANALYSIS REPORT", title_style))
        story.append(Paragraph(f"{campaign['campaign_name']}", title_style))
        story.append(Spacer(1, 20))
        
        # Executive Summary Box
        exec_summary_data = [
            ['Campaign ID:', campaign['campaign_id']],
            ['Category:', campaign['category']],
            ['Period:', campaign['period']],
            ['Total Budget:', f"${campaign['budget']:,}"],
            ['Report Date:', datetime.now().strftime('%B %d, %Y')]
        ]
        
        exec_table = Table(exec_summary_data, colWidths=[1.5*inch, 3*inch])
        exec_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        
        story.append(exec_table)
        story.append(Spacer(1, 25))
        
        # Campaign Objectives
        story.append(Paragraph("CAMPAIGN OBJECTIVES", section_style))
        story.append(Paragraph(campaign['objective'], styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Target Audience
        story.append(Paragraph("TARGET AUDIENCE", section_style))
        story.append(Paragraph(campaign['target_audience'], styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Key Products
        story.append(Paragraph("FEATURED PRODUCTS", section_style))
        products_text = "• " + "<br/>• ".join(campaign['key_products'])
        story.append(Paragraph(products_text, styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Marketing Channels
        story.append(Paragraph("MARKETING CHANNELS", section_style))
        channels_text = "• " + "<br/>• ".join(campaign['channels'])
        story.append(Paragraph(channels_text, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Performance Results
        story.append(Paragraph("PERFORMANCE RESULTS", section_style))
        
        # KPI Results Table
        kpi_data = [
            ['Key Performance Indicator', 'Target', 'Actual', 'vs Target']
        ]
        
        for kpi, values in campaign['kpis'].items():
            kpi_name = kpi.replace('_', ' ').title()
            target = values['target']
            actual = values['actual']
            
            if isinstance(target, (int, float)) and isinstance(actual, (int, float)):
                if target != 0:
                    vs_target = f"{((actual - target) / target * 100):+.1f}%"
                    if actual >= target:
                        status = "✓ Above Target"
                    else:
                        status = "⚠ Below Target"
                else:
                    vs_target = "N/A"
                    status = "N/A"
            else:
                vs_target = "N/A"
                status = "N/A"
            
            # Format values appropriately
            if kpi in ['sales_lift', 'market_share', 'brand_awareness', 'volume_growth', 'premium_mix', 'online_sales_growth', 'digital_attribution']:
                target_str = f"{target}%"
                actual_str = f"{actual}%"
            elif kpi in ['roi', 'engagement_rate', 'mobile_conversion']:
                target_str = f"{target:.1f}"
                actual_str = f"{actual:.1f}"
            elif kpi in ['cost_per_acquisition']:
                target_str = f"${target:.2f}"
                actual_str = f"${actual:.2f}"
            elif kpi in ['incremental_revenue']:
                target_str = f"${target:,}"
                actual_str = f"${actual:,}"
            elif kpi in ['customer_satisfaction']:
                target_str = f"{target}/10"
                actual_str = f"{actual}/10"
            else:
                target_str = f"{target:,}"
                actual_str = f"{actual:,}"
            
            kpi_data.append([kpi_name, target_str, actual_str, vs_target])
        
        kpi_table = Table(kpi_data, colWidths=[2.5*inch, 1*inch, 1*inch, 1.2*inch])
        kpi_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ]))
        
        story.append(kpi_table)
        story.append(Spacer(1, 20))
        
        # Media Spend Breakdown
        story.append(Paragraph("MEDIA SPEND ALLOCATION", section_style))
        
        spend_data = [['Channel', 'Budget', 'Percentage']]
        total_spend = sum(campaign['media_spend'].values())
        
        for channel, amount in campaign['media_spend'].items():
            percentage = (amount / total_spend) * 100
            spend_data.append([channel, f"${amount:,}", f"{percentage:.1f}%"])
        
        spend_data.append(['TOTAL', f"${total_spend:,}", "100.0%"])
        
        spend_table = Table(spend_data, colWidths=[2*inch, 1.5*inch, 1*inch])
        spend_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
            ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ]))
        
        story.append(spend_table)
        story.append(Spacer(1, 25))
        
        # Results Summary
        story.append(Paragraph("EXECUTIVE SUMMARY", section_style))
        story.append(Paragraph(campaign['results_summary'], styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Key Learnings
        story.append(Paragraph("KEY LEARNINGS & RECOMMENDATIONS", section_style))
        story.append(Paragraph(campaign['lessons_learned'], styles['Normal']))
        story.append(Spacer(1, 25))
        
        # ROI Analysis
        if 'roi' in campaign['kpis']:
            story.append(Paragraph("RETURN ON INVESTMENT ANALYSIS", section_style))
            
            roi_actual = campaign['kpis']['roi']['actual']
            roi_analysis = f"""
            <b>Campaign ROI:</b> {roi_actual:.1f}x
            <br/>
            <b>Investment:</b> ${campaign['budget']:,}
            <br/>
            <b>Estimated Return:</b> ${int(campaign['budget'] * roi_actual):,}
            <br/>
            <b>Net Benefit:</b> ${int(campaign['budget'] * (roi_actual - 1)):,}
            <br/><br/>
            This campaign generated <b>${roi_actual:.1f}</b> in value for every dollar invested, 
            indicating strong performance and justifying continued investment in similar initiatives.
            """
            story.append(Paragraph(roi_analysis, styles['Normal']))
        
        story.append(Spacer(1, 30))
        
        # Footer
        footer_text = f"""
        <i>This report was generated on {datetime.now().strftime('%B %d, %Y')} by the Marketing Analytics Team.<br/>
        For questions or additional analysis, contact: marketing.analytics@company.com</i>
        """
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=colors.grey,
            alignment=1
        )
        story.append(Paragraph(footer_text, footer_style))
        
        # Build the PDF
        doc.build(story)
        session.file.put(f'{output_dir}/*', stage_location='@DOCUMENTS/marketing_campaigns/', auto_compress=False, overwrite=True)
    print('Created marketing campaign documents and uploaded them to stage @DOCUMENTS/marketing_campaigns/')