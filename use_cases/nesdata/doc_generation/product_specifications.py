from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_product_specification_sheets(session, output_dir='/tmp/product_specifications/'):
    """Generate product specification sheets PDFs"""
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    products_data = [
        {
            'filename': 'NesKafe_Product_Specifications_2023.pdf',
            'product_line': 'NesKafe Coffee Products',
            'category': 'Coffee',
            'products': [
                {
                    'name': 'NesKafe Classic',
                    'sku': 'NK-CL-200',
                    'size': '200g jar',
                    'ingredients': ['100% Pure Coffee', 'Natural Coffee Extract', 'Coffee Beans (Arabica 60%, Robusta 40%)'],
                    'nutritional': {'calories': 2, 'protein': 0.3, 'carbs': 0.5, 'fat': 0, 'sodium': 1, 'caffeine': 65},
                    'allergens': ['None'],
                    'shelf_life': '24 months',
                    'storage': 'Store in cool, dry place. Keep jar tightly sealed.',
                    'certifications': ['ISO 22000', 'Rainforest Alliance Certified', 'Fair Trade'],
                    'origin': 'Beans sourced from Brazil, Vietnam, Colombia'
                },
                {
                    'name': 'NesKafe Gold',
                    'sku': 'NK-GD-150',
                    'size': '150g jar',
                    'ingredients': ['100% Premium Coffee', 'Freeze-Dried Coffee', '100% Arabica Beans', 'Natural Flavoring'],
                    'nutritional': {'calories': 2, 'protein': 0.4, 'carbs': 0.3, 'fat': 0, 'sodium': 1, 'caffeine': 75},
                    'allergens': ['None'],
                    'shelf_life': '30 months',
                    'storage': 'Store in cool, dry place below 25°C. Avoid direct sunlight.',
                    'certifications': ['Organic Certified', 'Carbon Neutral', 'UTZ Certified'],
                    'origin': 'Single-origin premium Arabica from Colombian highlands'
                }
            ]
        },
        {
            'filename': 'PureLife_Water_Technical_Specs.pdf',
            'product_line': 'PureLife Water Products',
            'category': 'Water',
            'products': [
                {
                    'name': 'PureLife Natural',
                    'sku': 'PL-NT-500',
                    'size': '500ml bottle',
                    'ingredients': ['Purified Water', 'Added Minerals (Calcium Chloride, Magnesium Sulfate, Potassium Bicarbonate)'],
                    'nutritional': {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0, 'sodium': 2, 'calcium': 15, 'magnesium': 4},
                    'allergens': ['None'],
                    'shelf_life': '18 months',
                    'storage': 'Store in cool, dry place. Avoid extreme temperatures.',
                    'certifications': ['NSF Certified', 'FDA Approved', 'ISO 14001'],
                    'source': 'Natural spring water from protected watersheds, 7-stage purification'
                },
                {
                    'name': 'PureLife Sparkling',
                    'sku': 'PL-SP-330',
                    'size': '330ml can',
                    'ingredients': ['Carbonated Purified Water', 'Natural Minerals', 'CO2'],
                    'nutritional': {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0, 'sodium': 8, 'calcium': 22, 'magnesium': 6},
                    'allergens': ['None'],
                    'shelf_life': '12 months',
                    'storage': 'Store upright in cool place. Best served chilled.',
                    'certifications': ['SQF Certified', 'BRC Grade A', 'Recyclable Package'],
                    'source': 'Premium mineral water with natural carbonation enhancement'
                }
            ]
        },
        {
            'filename': 'ChocoBars_Ingredients_Nutritional_Info.pdf',
            'product_line': 'ChocoBars Chocolate Products',
            'category': 'Chocolate',
            'products': [
                {
                    'name': 'ChocoBars Dark',
                    'sku': 'CB-DK-85',
                    'size': '85g bar',
                    'ingredients': ['Cocoa Mass', 'Sugar', 'Cocoa Butter', 'Vanilla Extract', 'Soy Lecithin (Emulsifier)'],
                    'nutritional': {'calories': 170, 'protein': 3.2, 'carbs': 12.8, 'fat': 12.1, 'sugar': 10.5, 'fiber': 2.8, 'sodium': 5},
                    'allergens': ['Soy', 'May contain Milk, Tree Nuts'],
                    'shelf_life': '18 months',
                    'storage': 'Store in cool, dry place at 16-18°C. Avoid direct sunlight.',
                    'certifications': ['Fair Trade Certified', 'Rainforest Alliance', 'Non-GMO Project Verified'],
                    'cocoa_content': '70% minimum cocoa solids from Ecuador and Madagascar'
                },
                {
                    'name': 'ChocoBars Milk',
                    'sku': 'CB-MK-90',
                    'size': '90g bar',
                    'ingredients': ['Sugar', 'Cocoa Butter', 'Milk Powder', 'Cocoa Mass', 'Lactose', 'Vanilla', 'Soy Lecithin'],
                    'nutritional': {'calories': 185, 'protein': 2.8, 'carbs': 18.5, 'fat': 11.2, 'sugar': 17.8, 'calcium': 62, 'sodium': 28},
                    'allergens': ['Milk', 'Soy', 'May contain Tree Nuts, Peanuts'],
                    'shelf_life': '15 months',
                    'storage': 'Store below 20°C in dry conditions. Refrigerate in hot climates.',
                    'certifications': ['ISO 22000', 'Sustainable Cocoa Program', 'Kosher Certified'],
                    'cocoa_content': '35% cocoa solids, Alpine milk powder'
                }
            ]
        },
        {
            'filename': 'BabyFirst_Formula_Safety_Guidelines.pdf',
            'product_line': 'BabyFirst Baby Food Products',
            'category': 'Baby Food',
            'products': [
                {
                    'name': 'BabyFirst Formula',
                    'sku': 'BF-FM-400',
                    'size': '400g canister',
                    'ingredients': ['Demineralized Whey', 'Vegetable Oils', 'Lactose', 'Milk Proteins', 'Vitamins A,D,E,K,C', 'B-Complex', 'Iron', 'Calcium', 'DHA', 'ARA'],
                    'nutritional': {'calories': 66, 'protein': 1.4, 'carbs': 7.2, 'fat': 3.6, 'dha': 17, 'ara': 25, 'iron': 1.2, 'calcium': 52},
                    'allergens': ['Milk', 'May contain Soy'],
                    'shelf_life': '24 months unopened, 3 weeks after opening',
                    'storage': 'Store in cool, dry place. Refrigerate after opening. Use within 1 hour after preparation.',
                    'certifications': ['FDA Approved', 'EU Infant Formula Regulation', 'HACCP Certified', 'Organic Certified'],
                    'age_range': '0-6 months (Stage 1)',
                    'safety_note': 'Follow preparation instructions exactly. Consult pediatrician before use.'
                },
                {
                    'name': 'BabyFirst Organic',
                    'sku': 'BF-OR-350',
                    'size': '350g canister',
                    'ingredients': ['Organic Lactose', 'Organic Vegetable Oils', 'Organic Whey Protein', 'Organic Milk Proteins', 'Organic Vitamins', 'Organic Minerals', 'Probiotics'],
                    'nutritional': {'calories': 68, 'protein': 1.5, 'carbs': 7.4, 'fat': 3.7, 'probiotics': '10^6 CFU', 'omega3': 45, 'calcium': 58},
                    'allergens': ['Milk'],
                    'shelf_life': '18 months unopened, 3 weeks after opening',
                    'storage': 'Store in cool, dry place below 25°C. Use sterilized equipment.',
                    'certifications': ['USDA Organic', 'EU Organic', 'Non-GMO Verified', 'Clean Label Project'],
                    'age_range': '0-12 months (Stages 1&2)',
                    'safety_note': 'Prepared formula must be used within 2 hours. Discard leftover formula.'
                }
            ]
        },
        {
            'filename': 'PetLove_Product_Certifications.pdf',
            'product_line': 'PetLove Pet Care Products', 
            'category': 'Pet Care',
            'products': [
                {
                    'name': 'PetLove Dry Food',
                    'sku': 'PL-DF-2K',
                    'size': '2kg bag',
                    'ingredients': ['Chicken Meal', 'Brown Rice', 'Chicken Fat', 'Beet Pulp', 'Fish Oil', 'Vitamins E,A,D3', 'Minerals', 'Probiotics', 'Antioxidants'],
                    'nutritional': {'protein': 28, 'fat': 15, 'fiber': 4, 'moisture': 10, 'calcium': 1.2, 'phosphorus': 1.0, 'omega6': 2.8, 'omega3': 0.5},
                    'allergens': ['None - Grain Friendly Formula'],
                    'shelf_life': '18 months unopened, 6 weeks after opening',
                    'storage': 'Store in cool, dry place. Keep bag sealed. Use airtight container after opening.',
                    'certifications': ['AAFCO Approved', 'Made in USA', 'No Artificial Colors/Flavors', 'Quality Tested'],
                    'life_stage': 'Adult dogs (1-7 years)',
                    'feeding_guide': '1 cup per 25 lbs body weight daily, divided into 2 meals'
                },
                {
                    'name': 'PetLove Premium',
                    'sku': 'PL-PR-1.5K',
                    'size': '1.5kg bag',
                    'ingredients': ['Deboned Salmon', 'Sweet Potato', 'Peas', 'Salmon Meal', 'Canola Oil', 'Flaxseed', 'Natural Flavors', 'Vitamins', 'Chelated Minerals'],
                    'nutritional': {'protein': 32, 'fat': 18, 'fiber': 3.5, 'moisture': 10, 'calcium': 1.8, 'phosphorus': 1.2, 'dha': 0.8, 'glucosamine': 400, 'chondroitin': 100},
                    'allergens': ['Fish - Grain Free Formula'],
                    'shelf_life': '15 months unopened, 4 weeks after opening',
                    'storage': 'Store in original bag in cool, dry location. Avoid temperature fluctuations.',
                    'certifications': ['AAFCO Premium', 'Wild-Caught Salmon', 'Limited Ingredient', 'Holistic Veterinarian Approved'],
                    'life_stage': 'All life stages - puppy to senior',
                    'feeding_guide': 'Weight-based feeding chart included. Transition gradually over 7 days.'
                }
            ]
        }
    ]
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'ProductTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=20,
        alignment=1,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=10,
        spaceBefore=15,
        textColor=colors.darkred,
        fontName='Helvetica-Bold'
    )
    
    product_header_style = ParagraphStyle(
        'ProductHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=25,
        textColor=colors.darkgreen,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=colors.darkgreen,
        borderPadding=5
    )
    
    for product_spec in products_data:
        doc = SimpleDocTemplate(
            os.path.join(output_dir, product_spec['filename']), 
            pagesize=letter,
            rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72
        )
        
        story = []
        
        # Title and Header
        story.append(Paragraph("PRODUCT SPECIFICATION SHEET", title_style))
        story.append(Paragraph(f"{product_spec['product_line']}", title_style))
        story.append(Spacer(1, 20))
        
        # Document Info
        doc_info_data = [
            ['Document Version:', '2023.1'],
            ['Category:', product_spec['category']],
            ['Issue Date:', datetime.now().strftime('%B %d, %Y')],
            ['Valid Until:', 'December 31, 2024'],
            ['Document Control:', 'QA-SPEC-2023']
        ]
        
        doc_table = Table(doc_info_data, colWidths=[1.5*inch, 2*inch])
        doc_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        
        story.append(doc_table)
        story.append(Spacer(1, 30))
        
        # Process each product in the specification
        for i, product in enumerate(product_spec['products']):
            if i > 0:
                story.append(Spacer(1, 20))
            
            # Product Header
            story.append(Paragraph(f"{product['name']} - {product['sku']}", product_header_style))
            
            # Basic Product Information
            story.append(Paragraph("PRODUCT INFORMATION", section_style))
            
            basic_info_data = [
                ['Product Name:', product['name']],
                ['SKU Code:', product['sku']],
                ['Package Size:', product['size']],
                ['Shelf Life:', product['shelf_life']],
                ['Storage Conditions:', product['storage']]
            ]
            
            basic_table = Table(basic_info_data, colWidths=[1.5*inch, 4*inch])
            basic_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ]))
            
            story.append(basic_table)
            story.append(Spacer(1, 15))
            
            # Ingredients
            story.append(Paragraph("INGREDIENTS", section_style))
            ingredients_text = "• " + "<br/>• ".join(product['ingredients'])
            story.append(Paragraph(ingredients_text, styles['Normal']))
            story.append(Spacer(1, 15))
            
            # Nutritional Information - Using safe get method
            story.append(Paragraph("NUTRITIONAL INFORMATION (per serving)", section_style))
            
            # Helper function to safely get nutritional values
            def get_nutrition_value(nutrition_dict, key, default=0):
                return nutrition_dict.get(key, default)
            
            # Create nutritional table based on product type
            if product_spec['category'] == 'Coffee':
                nutrition_data = [
                    ['Nutrient', 'Per Cup (6 fl oz)', 'Daily Value %'],
                    ['Calories', f"{get_nutrition_value(product['nutritional'], 'calories')}", '<1%'],
                    ['Protein', f"{get_nutrition_value(product['nutritional'], 'protein')}g", '1%'],
                    ['Total Carbohydrates', f"{get_nutrition_value(product['nutritional'], 'carbs')}g", '<1%'],
                    ['Total Fat', f"{get_nutrition_value(product['nutritional'], 'fat')}g", '0%'],
                    ['Sodium', f"{get_nutrition_value(product['nutritional'], 'sodium')}mg", '<1%'],
                    ['Caffeine', f"{get_nutrition_value(product['nutritional'], 'caffeine')}mg", 'N/A']
                ]
            elif product_spec['category'] == 'Water':
                nutrition_data = [
                    ['Mineral', 'Per Bottle', 'Daily Value %'],
                    ['Calories', f"{get_nutrition_value(product['nutritional'], 'calories')}", '0%'],
                    ['Total Fat', f"{get_nutrition_value(product['nutritional'], 'fat')}g", '0%'],
                    ['Sodium', f"{get_nutrition_value(product['nutritional'], 'sodium')}mg", '<1%'],
                    ['Calcium', f"{get_nutrition_value(product['nutritional'], 'calcium')}mg", '2%'],
                    ['Magnesium', f"{get_nutrition_value(product['nutritional'], 'magnesium')}mg", '1%']
                ]
            elif product_spec['category'] == 'Chocolate':
                nutrition_data = [
                    ['Nutrient', 'Per 30g serving', 'Daily Value %'],
                    ['Calories', f"{get_nutrition_value(product['nutritional'], 'calories')}", '9%'],
                    ['Protein', f"{get_nutrition_value(product['nutritional'], 'protein')}g", '6%'],
                    ['Total Carbohydrates', f"{get_nutrition_value(product['nutritional'], 'carbs')}g", '5%'],
                    ['Total Fat', f"{get_nutrition_value(product['nutritional'], 'fat')}g", '16%'],
                    ['Sugars', f"{get_nutrition_value(product['nutritional'], 'sugar')}g", 'N/A'],
                    ['Dietary Fiber', f"{get_nutrition_value(product['nutritional'], 'fiber')}g", '10%'],
                    ['Sodium', f"{get_nutrition_value(product['nutritional'], 'sodium')}mg", '<1%']
                ]
            elif product_spec['category'] == 'Baby Food':
                nutrition_data = [
                    ['Nutrient', 'Per 100ml prepared', 'Infant Daily Value'],
                    ['Energy', f"{get_nutrition_value(product['nutritional'], 'calories')} kcal", 'N/A'],
                    ['Protein', f"{get_nutrition_value(product['nutritional'], 'protein')}g", 'N/A'],
                    ['Carbohydrates', f"{get_nutrition_value(product['nutritional'], 'carbs')}g", 'N/A'],
                    ['Fat', f"{get_nutrition_value(product['nutritional'], 'fat')}g", 'N/A'],
                    ['DHA', f"{get_nutrition_value(product['nutritional'], 'dha')}mg", 'N/A'],
                    ['Iron', f"{get_nutrition_value(product['nutritional'], 'iron')}mg", 'N/A'],
                    ['Calcium', f"{get_nutrition_value(product['nutritional'], 'calcium')}mg", 'N/A']
                ]
            elif product_spec['category'] == 'Pet Care':
                nutrition_data = [
                    ['Nutrient', 'Guaranteed Analysis', 'Min/Max'],
                    ['Crude Protein', f"{get_nutrition_value(product['nutritional'], 'protein')}%", 'Minimum'],
                    ['Crude Fat', f"{get_nutrition_value(product['nutritional'], 'fat')}%", 'Minimum'],
                    ['Crude Fiber', f"{get_nutrition_value(product['nutritional'], 'fiber')}%", 'Maximum'],
                    ['Moisture', f"{get_nutrition_value(product['nutritional'], 'moisture')}%", 'Maximum'],
                    ['Calcium', f"{get_nutrition_value(product['nutritional'], 'calcium')}%", 'Minimum'],
                    ['Phosphorus', f"{get_nutrition_value(product['nutritional'], 'phosphorus')}%", 'Minimum']
                ]
            
            nutrition_table = Table(nutrition_data, colWidths=[1.8*inch, 1.5*inch, 1.2*inch])
            nutrition_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ]))
            
            story.append(nutrition_table)
            story.append(Spacer(1, 15))
            
            # Allergen Information
            story.append(Paragraph("ALLERGEN INFORMATION", section_style))
            allergen_text = f"<b>Contains:</b> {', '.join(product['allergens'])}"
            if any('May contain' in allergen for allergen in product['allergens']):
                allergen_text += "<br/><b>Warning:</b> Manufactured in facilities that process multiple allergens."
            story.append(Paragraph(allergen_text, styles['Normal']))
            story.append(Spacer(1, 15))
            
            # Certifications and Quality
            story.append(Paragraph("CERTIFICATIONS & QUALITY STANDARDS", section_style))
            cert_text = "• " + "<br/>• ".join(product['certifications'])
            story.append(Paragraph(cert_text, styles['Normal']))
            story.append(Spacer(1, 15))
            
            # Product-specific information
            if product_spec['category'] == 'Coffee':
                story.append(Paragraph("COFFEE SPECIFICATIONS", section_style))
                coffee_specs = f"""
                <b>Bean Origin:</b> {product['origin']}
                <br/><b>Processing Method:</b> Freeze-dried instant coffee technology
                <br/><b>Roast Profile:</b> Medium roast for optimal flavor balance
                <br/><b>Grind Size:</b> Fine powder for instant dissolution
                <br/><b>Preparation:</b> Add 1-2 teaspoons to 6 fl oz hot water (175-185°F)
                """
                story.append(Paragraph(coffee_specs, styles['Normal']))
                
            elif product_spec['category'] == 'Water':
                story.append(Paragraph("WATER SOURCE & TREATMENT", section_style))
                water_specs = f"""
                <b>Source:</b> {product['source']}
                <br/><b>Treatment Process:</b> Multi-stage filtration and purification
                <br/><b>Quality Testing:</b> 200+ quality tests performed daily
                <br/><b>pH Level:</b> 6.5 - 8.5 (optimal drinking range)
                <br/><b>TDS (Total Dissolved Solids):</b> 150-300 ppm
                """
                story.append(Paragraph(water_specs, styles['Normal']))
                
            elif product_spec['category'] == 'Chocolate':
                story.append(Paragraph("CHOCOLATE SPECIFICATIONS", section_style))
                chocolate_specs = f"""
                <b>Cocoa Content:</b> {product['cocoa_content']}
                <br/><b>Bean Variety:</b> Premium Trinitario and Nacional varieties
                <br/><b>Conching Time:</b> 72 hours for smooth texture
                <br/><b>Tempering:</b> Traditional European tempering process
                <br/><b>Quality Grade:</b> Premium confectionery grade
                """
                story.append(Paragraph(chocolate_specs, styles['Normal']))
                
            elif product_spec['category'] == 'Baby Food':
                story.append(Paragraph("SAFETY & PREPARATION GUIDELINES", section_style))
                safety_info = f"""
                <b>Age Recommendation:</b> {product['age_range']}
                <br/><b>Safety Note:</b> {product['safety_note']}
                <br/><b>Preparation Instructions:</b>
                <br/>1. Wash hands and sterilize all equipment
                <br/>2. Boil water and cool to 70°C (158°F)
                <br/>3. Add powder to water (not water to powder)
                <br/>4. Mix thoroughly and test temperature before feeding
                <br/>5. Use prepared formula within 2 hours
                <br/><b>Medical Consultation:</b> Always consult pediatrician before use
                """
                story.append(Paragraph(safety_info, styles['Normal']))
                
            elif product_spec['category'] == 'Pet Care':
                story.append(Paragraph("FEEDING GUIDELINES", section_style))
                feeding_info = f"""
                <b>Life Stage:</b> {product['life_stage']}
                <br/><b>Feeding Instructions:</b> {product['feeding_guide']}
                <br/><b>Transition Period:</b> Gradually mix with current food over 7 days
                <br/><b>Fresh Water:</b> Always provide clean, fresh water
                <br/><b>Feeding Schedule:</b> Divide daily amount into 2-3 meals
                <br/><b>Storage After Opening:</b> Use airtight container, consume within 6 weeks
                """
                story.append(Paragraph(feeding_info, styles['Normal']))
            
            story.append(Spacer(1, 20))
        
        # Footer compliance information
        story.append(Spacer(1, 30))
        compliance_info = f"""
        <b>REGULATORY COMPLIANCE</b>
        <br/>This product specification sheet complies with applicable food safety regulations including FDA, USDA, and international standards. 
        All nutritional information is based on average values from regular testing. 
        <br/><br/>
        <b>QUALITY ASSURANCE</b>
        <br/>Products are manufactured under strict quality control systems including HACCP, GMP, and ISO 22000 standards. 
        Regular third-party audits ensure compliance with all safety and quality requirements.
        <br/><br/>
        <i>For technical inquiries or additional product information, contact: technical.support@company.com</i>
        <br/><i>Document prepared by: Product Development & Quality Assurance Team</i>
        """
        
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=colors.grey
        )
        story.append(Paragraph(compliance_info, footer_style))
        
        # Build the PDF
        doc.build(story)
        session.file.put(f'{output_dir}/*', stage_location='@DOCUMENTS/product_specifications/', auto_compress=False, overwrite=True)
    print('Created product specification documents and uploaded them to stage @DOCUMENTS/product_specifications/')