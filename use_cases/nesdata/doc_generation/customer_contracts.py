from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime, timedelta
import os

def create_customer_contracts(session, output_dir='/tmp/customer_contracts/'):
    """Generate customer contract agreement PDFs"""

    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    contracts_data = [
        {
            'filename': f'{output_dir}/ClickAndBuy_Solutions_Master_Agreement_2023.pdf',
            'customer_name': 'ClickAndBuy Solutions',
            'customer_id': 'CUST-001',
            'contract_type': 'Master Distribution Agreement',
            'effective_date': '2023-01-01',
            'expiry_date': '2025-12-31',
            'credit_limit': 250000,
            'payment_terms': '30 days net',
            'volume_commitment': 50000,
            'territory': 'Downtown Metro Area, Exclusive',
            'discount_tier': 'Tier 2 - 8% base discount',
            'promotional_support': '$25,000 quarterly',
            'key_products': ['NesKafe Classic', 'PureLife Natural', 'ChocoBars Milk'],
            'minimum_orders': 'Monthly minimum $15,000',
            'delivery_terms': 'FOB Destination, 5-7 business days',
            'rebate_structure': '2% additional rebate on >$200K annual volume'
        },
        {
            'filename': f'{output_dir}/EuroMart_Paris_Distribution_Contract.pdf',
            'customer_name': 'EuroMart Paris',
            'customer_id': 'CUST-047',
            'contract_type': 'Regional Distribution Agreement',
            'effective_date': '2023-03-15',
            'expiry_date': '2026-03-14',
            'credit_limit': 500000,
            'payment_terms': '45 days net',
            'volume_commitment': 120000,
            'territory': 'Germany, Austria, Switzerland - Non-exclusive',
            'discount_tier': 'Tier 1 - 12% base discount',
            'promotional_support': '$50,000 semi-annually',
            'key_products': ['NesKafe Gold', 'CreamyDelight Vanilla', 'ChocoWafers Crispy'],
            'minimum_orders': 'Monthly minimum €35,000',
            'delivery_terms': 'Ex Works, Customer arranged logistics',
            'rebate_structure': '3% volume rebate on >€500K annual, 5% on >€800K'
        },
        {
            'filename': f'{output_dir}/SuperShop_Premium_Terms_Conditions.pdf',
            'customer_name': 'SuperShop Premium',
            'customer_id': 'CUST-023',
            'contract_type': 'Wholesale Supply Agreement',
            'effective_date': '2022-07-01',
            'expiry_date': '2024-06-30',
            'credit_limit': 1000000,
            'payment_terms': '60 days net',
            'volume_commitment': 200000,
            'territory': 'Multi-state distribution rights (CA, NV, AZ)',
            'discount_tier': 'Premium Tier - 15% base discount',
            'promotional_support': '$75,000 quarterly + co-op advertising',
            'key_products': ['DeluxeChoc Premium', 'BabyFirst Formula', 'PetLove Premium'],
            'minimum_orders': 'Bi-weekly minimum $50,000',
            'delivery_terms': 'FOB Origin, expedited shipping available',
            'rebate_structure': 'Tiered: 2% at $1M, 4% at $1.5M, 6% at $2M+'
        },
        {
            'filename': f'{output_dir}/Online_Retailers_Partnership_Agreement.pdf',
            'customer_name': 'E-Commerce Hub',
            'customer_id': 'CUST-089',
            'contract_type': 'Digital Commerce Partnership',
            'effective_date': '2023-06-01',
            'expiry_date': '2025-05-31',
            'credit_limit': 100000,
            'payment_terms': '15 days net (accelerated for digital)',
            'volume_commitment': 30000,
            'territory': 'Online sales - North America, non-exclusive',
            'discount_tier': 'Digital Tier - 10% base discount',
            'promotional_support': '$15,000 quarterly + digital marketing support',
            'key_products': ['NesKafe Instant', 'PureLife Flavored', 'MorningCrunch Honey'],
            'minimum_orders': 'Weekly minimum $8,000',
            'delivery_terms': 'Drop-ship model, direct to consumer',
            'rebate_structure': '1.5% digital commerce rebate + 0.5% data sharing bonus'
        },
        {
            'filename': f'{output_dir}/HyperMall_Enterprise_Contract.pdf',
            'customer_name': 'HyperMall North',
            'customer_id': 'CUST-012',
            'contract_type': 'Enterprise Retail Agreement',
            'effective_date': '2023-02-01',
            'expiry_date': '2026-01-31',
            'credit_limit': 500000,
            'payment_terms': '30 days net with 2% early payment discount (10 days)',
            'volume_commitment': 150000,
            'territory': 'Northern Region - 25 store locations',
            'discount_tier': 'Enterprise Tier - 14% base discount',
            'promotional_support': '$40,000 quarterly + in-store promotion rights',
            'key_products': ['Full product portfolio access'],
            'minimum_orders': 'Monthly minimum $40,000 across all locations',
            'delivery_terms': 'FOB Destination with white glove delivery service',
            'rebate_structure': '3% volume rebate + 1% loyalty bonus after year 2'
        }
    ]
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1,  # Center alignment
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=12,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )
    
    for contract in contracts_data:
        # Create PDF document
        doc = SimpleDocTemplate(contract['filename'], pagesize=letter,
                              rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        
        story = []
        
        # Title
        title = Paragraph(f"{contract['contract_type']}", title_style)
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Contract header info
        header_data = [
            ['Contract ID:', f"CNTR-{contract['customer_id'].split('-')[1]}-2023"],
            ['Customer Name:', contract['customer_name']],
            ['Customer ID:', contract['customer_id']],
            ['Effective Date:', contract['effective_date']],
            ['Expiry Date:', contract['expiry_date']],
            ['Document Date:', datetime.now().strftime('%Y-%m-%d')]
        ]
        
        header_table = Table(header_data, colWidths=[2*inch, 3*inch])
        header_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ]))
        
        story.append(header_table)
        story.append(Spacer(1, 20))
        
        # Commercial Terms Section
        story.append(Paragraph("COMMERCIAL TERMS & CONDITIONS", heading_style))
        
        commercial_data = [
            ['Credit Limit:', f"${contract['credit_limit']:,}"],
            ['Payment Terms:', contract['payment_terms']],
            ['Annual Volume Commitment:', f"{contract['volume_commitment']:,} units"],
            ['Territory Rights:', contract['territory']],
            ['Discount Structure:', contract['discount_tier']],
            ['Minimum Order Requirements:', contract['minimum_orders']],
            ['Delivery Terms:', contract['delivery_terms']],
        ]
        
        commercial_table = Table(commercial_data, colWidths=[2.5*inch, 3.5*inch])
        commercial_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ]))
        
        story.append(commercial_table)
        story.append(Spacer(1, 20))
        
        # Product Portfolio Section
        story.append(Paragraph("PRODUCT PORTFOLIO & REBATES", heading_style))
        
        product_text = f"""
        <b>Key Products:</b> {', '.join(contract['key_products'])}
        <br/><br/>
        <b>Promotional Support:</b> {contract['promotional_support']}
        <br/><br/>
        <b>Rebate Structure:</b> {contract['rebate_structure']}
        """
        
        story.append(Paragraph(product_text, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Performance Requirements
        story.append(Paragraph("PERFORMANCE REQUIREMENTS", heading_style))
        
        performance_requirements = f"""
        1. <b>Volume Commitments:</b> Customer agrees to purchase minimum {contract['volume_commitment']:,} units annually across agreed product categories.
        
        2. <b>Payment Performance:</b> Adherence to {contract['payment_terms']} payment terms. Late payments may result in credit limit reduction.
        
        3. <b>Inventory Management:</b> Maintain adequate stock levels to prevent out-of-stock situations exceeding 5% of time.
        
        4. <b>Brand Standards:</b> Comply with brand merchandising and marketing guidelines as provided by supplier.
        
        5. <b>Reporting:</b> Provide monthly sales reports and quarterly inventory reports within 5 business days of period end.
        """
        
        story.append(Paragraph(performance_requirements, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Pricing and Discounts
        story.append(Paragraph("PRICING STRUCTURE", heading_style))
        
        pricing_text = f"""
        <b>Base Discount Level:</b> {contract['discount_tier']}
        <br/><br/>
        <b>Volume Rebates:</b> {contract['rebate_structure']}
        <br/><br/>
        <b>Price Protection:</b> 60-day advance notice on price increases. Promotional pricing honored through promotion period.
        <br/><br/>
        <b>Payment Discounts:</b> Early payment discounts available as specified in payment terms.
        """
        
        story.append(Paragraph(pricing_text, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Territory and Exclusivity
        story.append(Paragraph("TERRITORY & DISTRIBUTION RIGHTS", heading_style))
        
        territory_text = f"""
        <b>Assigned Territory:</b> {contract['territory']}
        <br/><br/>
        <b>Distribution Rights:</b> Customer authorized to distribute products within assigned territory through agreed channels.
        <br/><br/>
        <b>Online Sales:</b> E-commerce activities must comply with territorial restrictions and brand guidelines.
        """
        
        story.append(Paragraph(territory_text, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Contract Terms
        story.append(Paragraph("CONTRACT ADMINISTRATION", heading_style))
        
        admin_text = f"""
        <b>Term:</b> {contract['effective_date']} through {contract['expiry_date']}
        <br/><br/>
        <b>Renewal:</b> Auto-renewal for successive one-year periods unless 90-day written notice provided.
        <br/><br/>
        <b>Termination:</b> Either party may terminate with 60-day notice for material breach after 30-day cure period.
        <br/><br/>
        <b>Governing Law:</b> This agreement governed by laws of jurisdiction where supplier is domiciled.
        """
        
        story.append(Paragraph(admin_text, styles['Normal']))
        story.append(Spacer(1, 30))
        
        # Signature block
        signature_data = [
            ['SUPPLIER:', 'CUSTOMER:'],
            ['', ''],
            ['_________________________', '_________________________'],
            ['Authorized Signature', 'Authorized Signature'],
            ['', ''],
            ['_________________________', '_________________________'],
            ['Print Name & Title', 'Print Name & Title'],
            ['', ''],
            ['Date: _______________', 'Date: _______________']
        ]
        
        signature_table = Table(signature_data, colWidths=[3*inch, 3*inch])
        signature_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        
        story.append(signature_table)
        
        # Build PDF
        doc.build(story)
        session.file.put(f'{output_dir}/*', stage_location='@DOCUMENTS/customer_contracts/', auto_compress=False, overwrite=True)
    print('Created customer contract documents and uploaded them to stage @DOCUMENTS/customer_contracts/')

