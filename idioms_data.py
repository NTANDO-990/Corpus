from fpdf import FPDF

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "FAMILY LAW LEVEL 2: Marriage in & out of Community of Property", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, text)
        self.ln()

pdf = PDF()
pdf.add_page()

# Questions section
pdf.chapter_title("🔍 QUESTIONS")

questions = """Section A 
Which of the following is a key characteristic of a marriage in community of property?
A. Each spouse retains separate estates
B. There is a complete separation of assets and liabilities
C. All assets and liabilities are shared equally
D. Each spouse can enter contracts without the other’s consent
	2.	What is the legal consequence of not signing an antenuptial contract before marriage?
A. The marriage is void
B. The marriage is automatically out of community of property
C. The marriage is automatically in community of property
D. The marriage must be registered with the High Court
	3.	Which of the following is TRUE about a marriage out of community of property with accrual?
A. All debts are shared
B. Spouses share income during marriage
C. Property acquired during the marriage is subject to division at divorce
D. The joint estate begins immediately after marriage
	4.	The accrual system:
A. Shares the entire estate from the start of the marriage
B. Applies only to assets owned before marriage
C. Automatically applies unless expressly excluded in the antenuptial contract
D. Cannot be used in South African law
	5.	In a marriage out of community of property without accrual, each spouse:
A. Shares property but not debt
B. Is responsible for their own assets and liabilities
C. Must share a bank account
D. Has equal say in the joint estate

Section B
6.	Define a marriage in community of property.
	7.	List two advantages and two disadvantages of being married in community of property.
	8.	What is the purpose of an antenuptial contract?
    
    
Section C
9.	Scenario:
Sipho and Lerato got married without signing an antenuptial contract.
 Five years later, Sipho starts a company and incurs a large amount of debt. 
 His creditors want to attach Lerato’s car, which she paid for with her own salary.
	•	Advise whether the creditors can do this and explain why.
	10.	Scenario:
Tshepo and Anna are married out of community of property with accrual.

	•	Tshepo had R500,000 worth of assets at the start of the marriage.
	•	Anna had no assets.
	•	At divorce, Tshepo’s estate is worth R1 million, and Anna’s estate is worth R2 million.
	•	Calculate the accrual and determine what Tshepo is entitled to.
    
Section D
11.	A marriage out of community of property with accrual means spouses share everything equally from the beginning.
	12.	An antenuptial contract must be signed in front of a notary and registered at the Deeds Office.
	13.	Spouses in a marriage in community of property cannot freely contract without each other’s consent.
	14.	The accrual system protects the spouse who earned less during the marriage.
	15.	A marriage in community of property has no effect on debts incurred before marriage."""  # [Insert the full questions text from previous message here]

pdf.chapter_body(questions)

# Answers section
pdf.chapter_title("✅ ANSWER KEY")

answers = """Seaction A
1.	C. All assets and liabilities are shared equally
	2.	C. The marriage is automatically in community of property
	3.	C. Property acquired during the marriage is subject to division at divorce
	4.	C. Automatically applies unless expressly excluded in the antenuptial contract
	5.	B. Is responsible for their own assets and liabilities
    
    Section B
    6.	Definition:
A marriage in community of property means that both spouses share a joint estate.
 All assets and debts accumulated before and during the marriage become jointly owned unless specifically excluded 
 (e.g., inheritances with conditions).
	7.	Advantages:

	•	Simpler estate planning and administration
	•	Both spouses benefit equally from assets acquired
Disadvantages:
	•	One spouse’s debt affects both
	•	Limited financial independence

	8.	Purpose of ANC:
An antenuptial contract allows spouses to exclude the community of property and profit/loss regime. It also gives the option to include or exclude the accrual system, providing financial independence during the marriage.

Section C
Answer:
Yes, the creditors can attach Lerato’s car. Since Sipho and Lerato did not sign an antenuptial contract, they are married in community of property. All assets (including Lerato’s car) form part of the joint estate and are thus vulnerable to claims by Sipho’s creditors.
	10.	Answer:

	•	Tshepo’s accrual: R1,000,000 – R500,000 = R500,000
	•	Anna’s accrual: R2,000,000 – R0 = R2,000,000
	•	Difference in accrual: R2,000,000 – R500,000 = R1,500,000
	•	Tshepo is entitled to half the difference: R750,000
    
Section D
11.	False
	12.	True
	13.	True
	14.	True
	15.	False"""  # [Insert the full answers text from previous message here]

pdf.chapter_body(answers)

# Save PDF
pdf.output("Family_Law_Level_2_Quiz.pdf")