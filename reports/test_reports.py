
from reports.report_generator import generate_csv, generate_pdf

# Generate CSV
csv_data = generate_csv()

with open("trust_ai_report.csv", "wb") as file:
    file.write(csv_data)

print("CSV report generated successfully!")

# Generate PDF
pdf_data = generate_pdf()

with open("trust_ai_report.pdf", "wb") as file:
    file.write(pdf_data)

print("PDF report generated successfully!")

print("Both reports are ready!")
