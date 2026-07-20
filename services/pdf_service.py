import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)


def create_report(result):

    filename = f"{result['name']}.pdf"

    filepath = os.path.join(REPORT_DIR, filename)

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filepath)

    story = []

    story.append(
        Paragraph(
            f"<b>ChemAI Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Name:</b> {result['name']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Formula:</b> {result['formula']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Molecular Weight:</b> {result['molecular_weight']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>IUPAC:</b> {result['iupac_name']}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>AI Explanation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            result["ai_explanation"],
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Safety</b>",
            styles["Heading2"]
        )
    )

    for key, value in result["safety"].items():

        story.append(
            Paragraph(
                f"{key}: {value}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    return filepath