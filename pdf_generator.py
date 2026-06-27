from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(data, filename="startup_report.pdf"):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Startup Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Startup Name:</b> {data['name']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Industry:</b> {data['industry']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Startup Idea:</b> {data['idea']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Target Customers:</b> {data['customer']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Revenue Model:</b> {data['revenue']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Description:</b> {data['description']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Business Details</b>", styles["Heading2"]))

    story.append(Paragraph(f"Target Market: {data['target_market']}", styles["BodyText"]))
    story.append(Paragraph(f"Investment: {data['investment']}", styles["BodyText"]))
    story.append(Paragraph(f"Development Time: {data['development_time']}", styles["BodyText"]))
    story.append(Paragraph(f"Market Potential: {data['market_potential']}", styles["BodyText"]))
    story.append(Paragraph(f"Category: {data['category']}", styles["BodyText"]))
    story.append(Paragraph(f"Startup Score: {data['score']}/100", styles["BodyText"]))
    story.append(Paragraph(f"Success Meter: {data['success_level']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>SWOT Analysis</b>", styles["Heading2"]))

    story.append(Paragraph(f"Strength: {data['strength']}", styles["BodyText"]))
    story.append(Paragraph(f"Weakness: {data['weakness']}", styles["BodyText"]))
    story.append(Paragraph(f"Opportunity: {data['opportunity']}", styles["BodyText"]))
    story.append(Paragraph(f"Threat: {data['threat']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Startup Roadmap</b>", styles["Heading2"]))

    for step in data["roadmap"]:
        story.append(Paragraph(step, styles["BodyText"]))

    story.append(Paragraph("<br/><b>AI Business Tips</b>", styles["Heading2"]))

    for tip in data["business_tips"]:
        story.append(Paragraph("• " + tip, styles["BodyText"]))

    pdf.build(story)

    return filename