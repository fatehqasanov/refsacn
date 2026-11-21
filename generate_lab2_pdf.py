import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, HRFlowable, Image as RLImage

pdf_path = r"C:\Users\fateh\AndroidStudioProjects\RefScan\Lab2_Final_Report.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontSize=18,
    leading=22,
    textColor=colors.HexColor('#1E1B4B'),
    spaceAfter=8
)

h2_style = ParagraphStyle(
    'H2',
    parent=styles['Heading2'],
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#4338CA'),
    spaceBefore=12,
    spaceAfter=6
)

h3_style = ParagraphStyle(
    'H3',
    parent=styles['Heading3'],
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor('#1F2937'),
    spaceBefore=10,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontSize=9,
    leading=12.5,
    textColor=colors.HexColor('#374151'),
    spaceAfter=5
)

code_style = ParagraphStyle(
    'Code',
    fontName='Courier',
    fontSize=7.5,
    leading=9.5,
    textColor=colors.HexColor('#0F172A'),
    backColor=colors.HexColor('#F8FAFC'),
    borderColor=colors.HexColor('#E2E8F0'),
    borderWidth=0.5,
    borderPadding=5,
    spaceAfter=6
)

quote_style = ParagraphStyle(
    'Quote',
    parent=body_style,
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=12.5,
    textColor=colors.HexColor('#475569'),
    leftIndent=10,
    spaceAfter=6
)

story = []

def add_p(text, style=body_style):
    story.append(Paragraph(text, style))

# Title & Metadata
add_p('Lab 2 Requirements &amp; Implementation Report: Cloud Data CRUD &amp; Access Control', title_style)
add_p('<b>Course:</b> Mobile Application in the Cloud — Lab 2<br/>'
      '<b>App Name:</b> RefScan<br/>'
      '<b>Team Members &amp; Workload Distribution:</b><br/>'
      '&nbsp;&nbsp;1. <b>Fateh Hasanlı</b> (ID: 57322 | Email: <code>fatehqasanov@gmail.com</code>) — <b>60% Workload</b> (Tech Lead, Data Layer, Auth &amp; Form Logic)<br/>'
      '&nbsp;&nbsp;2. <b>Ibrokhimov Odiljon</b> (ID: 52857 | Email: <code>52857@student.polsl.pl</code>) — <b>40% Workload</b> (QA/DevOps, List UI, Security Rules &amp; Extensions)<br/>'
      '<b>Tech Stack:</b> Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore · Git/GitHub<br/>'
      '<b>GitHub Repository:</b> <font color="#4338CA"><u>https://github.com/fatehqasanov/refsacn</u></font> | <b>Git Tag:</b> <code>lab2</code>', body_style)

story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB'), spaceAfter=8))

# Executive Summary / Requirements Checklist
add_p('Requirements Checklist (R1 – R10)', h2_style)
req_data = [
    [Paragraph('<b>Requirement</b>', body_style), Paragraph('<b>Description</b>', body_style), Paragraph('<b>Status</b>', body_style)],
    [Paragraph('R1', body_style), Paragraph('Sprint planning on board, Retro issue closed, DoD in README', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R2', body_style), Paragraph('Cloud database (Firestore EU), main + reference collection (3+ records)', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R3', body_style), Paragraph('Data model with ownerId, server timestamps, >=4 domain fields', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R4', body_style), Paragraph('3-Layer architecture (Repository interface, ViewModel, pure Validator)', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R5', body_style), Paragraph('Live list query filtered by ownerId, loading &amp; error states, logout', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R6', body_style), Paragraph('Create/Edit form, reference picker, 3+ validation rules, cross-field rule', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R7', body_style), Paragraph('Delete with confirmation dialog naming item being deleted', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R8', body_style), Paragraph('Server-side Security Rules in <code>firestore.rules</code> with 8 tested scenarios', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R9', body_style), Paragraph('Implemented 4 Extensions (E1 Search, E3 Empty states, E5 Status toggle, E7 Stats)', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
    [Paragraph('R10', body_style), Paragraph('Team process, commits/PRs from BOTH Fateh &amp; Odiljon, tag <code>lab2</code>', body_style), Paragraph('<font color="#16A34A"><b>DONE</b></font>', body_style)],
]
t = Table(req_data, colWidths=[40, 380, 80])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
]))
story.append(t)
story.append(Spacer(1, 8))

# Tech Stack & Definition of Done
add_p('Tech Stack &amp; Definition of Done', h2_style)
add_p('<b>Tech Stack Table:</b><br/>'
      '• App Framework: Kotlin + Jetpack Compose<br/>'
      '• Backend &amp; Auth: Firebase Authentication<br/>'
      '• Cloud Database: Cloud Firestore (EU Region - europe-west1)<br/>'
      '• Security: Firestore Security Rules (`firestore.rules`)<br/>'
      '• Testing Frameworks: JUnit 4, Kotlin Coroutines Test Framework', body_style)

add_p('<b>Definition of Done (DoD):</b><br/>'
      '<i>"A story is done when it is merged to main through a reviewed PR with at least one approval, works on the device of both team members (Fateh Hasanlı and Ibrokhimov Odiljon), does not crash on invalid input or screen rotation, and its linked GitHub issue is closed."</i>', quote_style)

# Data Model
add_p('Cloud Data Model (R2 &amp; R3)', h2_style)
add_p('<b>Main Collection:</b> <code>references</code> | <b>Reference Collection:</b> <code>projects</code> (Read-Only for users)', body_style)

data_model_rows = [
    [Paragraph('<b>Collection</b>', body_style), Paragraph('<b>Field Name</b>', body_style), Paragraph('<b>Type</b>', body_style), Paragraph('<b>Set By</b>', body_style), Paragraph('<b>Description</b>', body_style)],
    [Paragraph('users', body_style), Paragraph('uid', body_style), Paragraph('String (doc id)', body_style), Paragraph('Firebase Auth', body_style), Paragraph('User account identifier', body_style)],
    [Paragraph('users', body_style), Paragraph('email', body_style), Paragraph('String', body_style), Paragraph('User / Auth', body_style), Paragraph('e.g. fatehqasanov@gmail.com', body_style)],
    [Paragraph('projects', body_style), Paragraph('id', body_style), Paragraph('String (doc id)', body_style), Paragraph('Admin / Seed', body_style), Paragraph('e.g. proj_1 (Reference collection)', body_style)],
    [Paragraph('projects', body_style), Paragraph('title', body_style), Paragraph('String', body_style), Paragraph('Admin / Seed', body_style), Paragraph('e.g. Cyberpunk Alley Level', body_style)],
    [Paragraph('references', body_style), Paragraph('id', body_style), Paragraph('String (doc id)', body_style), Paragraph('Firestore', body_style), Paragraph('Unique reference ID', body_style)],
    [Paragraph('references', body_style), Paragraph('ownerId', body_style), Paragraph('String', body_style), Paragraph('App (Auth session)', body_style), Paragraph('Foreign key to users.uid', body_style)],
    [Paragraph('references', body_style), Paragraph('projectId', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('Foreign key to projects.id', body_style)],
    [Paragraph('references', body_style), Paragraph('note', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('Material reference description (1-200 chars)', body_style)],
    [Paragraph('references', body_style), Paragraph('colorHex', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('Surface color hex (#RRGGBB)', body_style)],
    [Paragraph('references', body_style), Paragraph('rating', body_style), Paragraph('Int', body_style), Paragraph('User Input', body_style), Paragraph('Importance rating (1 to 5 stars)', body_style)],
    [Paragraph('references', body_style), Paragraph('status', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('"active" or "archived"', body_style)],
    [Paragraph('references', body_style), Paragraph('createdAt', body_style), Paragraph('Timestamp', body_style), Paragraph('Server Clock', body_style), Paragraph('FieldValue.serverTimestamp()', body_style)],
    [Paragraph('references', body_style), Paragraph('updatedAt', body_style), Paragraph('Timestamp', body_style), Paragraph('Server Clock', body_style), Paragraph('FieldValue.serverTimestamp()', body_style)],
]

dmt = Table(data_model_rows, colWidths=[65, 65, 80, 80, 210])
dmt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(dmt)
story.append(Spacer(1, 8))

# R8 Server-Side Access Control Matrix
add_p('R8 — Server-Side Access Control Scenarios Matrix', h2_style)
add_p('Enforced on the backend via <code>firestore.rules</code> code committed in the repository:', body_style)

r8_rows = [
    [Paragraph('<b>#</b>', body_style), Paragraph('<b>Scenario Description</b>', body_style), Paragraph('<b>Expected</b>', body_style), Paragraph('<b>Verification Method</b>', body_style), Paragraph('<b>Result</b>', body_style)],
    [Paragraph('1', body_style), Paragraph('Read own record', body_style), Paragraph('Allowed', body_style), Paragraph('App snapshot query / Playground', body_style), Paragraph('<font color="#16A34A"><b>ALLOWED</b></font>', body_style)],
    [Paragraph('2', body_style), Paragraph('Read same record as a different user', body_style), Paragraph('Denied', body_style), Paragraph('Rules Playground as User B', body_style), Paragraph('<font color="#16A34A"><b>DENIED</b></font>', body_style)],
    [Paragraph('3', body_style), Paragraph('Read without being signed in', body_style), Paragraph('Denied', body_style), Paragraph('Unauthenticated request call', body_style), Paragraph('<font color="#16A34A"><b>DENIED</b></font>', body_style)],
    [Paragraph('4', body_style), Paragraph('Create record whose ownerId is another user', body_style), Paragraph('Denied', body_style), Paragraph('Rules Playground create with fake UID', body_style), Paragraph('<font color="#16A34A"><b>DENIED</b></font>', body_style)],
    [Paragraph('5', body_style), Paragraph('Create record breaking logical rule (empty note)', body_style), Paragraph('Denied', body_style), Paragraph('Rules Playground validation check', body_style), Paragraph('<font color="#16A34A"><b>DENIED</b></font>', body_style)],
    [Paragraph('6', body_style), Paragraph('Update own record, changing its ownerId', body_style), Paragraph('Denied', body_style), Paragraph('Rules Playground update request', body_style), Paragraph('<font color="#16A34A"><b>DENIED</b></font>', body_style)],
    [Paragraph('7', body_style), Paragraph('Create a record in reference collection (projects)', body_style), Paragraph('Denied', body_style), Paragraph('Write request to /projects/new', body_style), Paragraph('<font color="#16A34A"><b>DENIED</b></font>', body_style)],
    [Paragraph('8', body_style), Paragraph('Read a reference record as a signed-in user', body_style), Paragraph('Allowed', body_style), Paragraph('App dropdown query / Playground', body_style), Paragraph('<font color="#16A34A"><b>ALLOWED</b></font>', body_style)],
]

r8t = Table(r8_rows, colWidths=[20, 200, 60, 140, 80])
r8t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
]))
story.append(r8t)
story.append(Spacer(1, 8))

# R9 Extensions
add_p('R9 — Implemented Extensions (4 Completed)', h2_style)
ext_rows = [
    [Paragraph('<b>Extension</b>', body_style), Paragraph('<b>Implementation Summary</b>', body_style), Paragraph('<b>Done When Status</b>', body_style)],
    [Paragraph('<b>E1: Search</b>', body_style), Paragraph('Search bar filters real-time list by note and project title (case-insensitive) with clear button', body_style), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', body_style)],
    [Paragraph('<b>E3: Empty &amp; No-Results</b>', body_style), Paragraph('Displays distinct hint to add first item vs. explicit "No matching references found" message', body_style), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', body_style)],
    [Paragraph('<b>E5: Status Toggle</b>', body_style), Paragraph('Filter chips toggle list between "All", "Active", and "Archived" with visual badges', body_style), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', body_style)],
    [Paragraph('<b>E7: Statistics Header</b>', body_style), Paragraph('Header card displays total items and live computed counts ("X active · Y archived")', body_style), Paragraph('<font color="#16A34A"><b>PASSED</b></font>', body_style)],
]
ext_t = Table(ext_rows, colWidths=[110, 310, 80])
ext_t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(ext_t)
story.append(Spacer(1, 10))

# Screenshots Section
add_p('In-App Screenshots (Compose UI Flow)', h2_style)
add_p('Below are the actual in-app mobile screenshots generated from the Jetpack Compose components:', body_style)

img_login = r"C:\Users\fateh\AndroidStudioProjects\RefScan\login_screenshot.png"
img_reg = r"C:\Users\fateh\AndroidStudioProjects\RefScan\register_screenshot.png"
img_list = r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_list_screenshot.png"
img_edit = r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_edit_screenshot.png"

# Grid 2x2 for Screenshots
s1_table_data = [
    [Paragraph('<b>Figure 1: Login Screen</b>', body_style), Paragraph('<b>Figure 2: Register Screen</b>', body_style)],
    [RLImage(img_login, width=150, height=316), RLImage(img_reg, width=150, height=316)],
    [Paragraph('<b>Figure 3: Live Reference List (R5, E1, E3, E5, E7)</b>', body_style), Paragraph('<b>Figure 4: Create/Edit Form (R6, R7)</b>', body_style)],
    [RLImage(img_list, width=150, height=316), RLImage(img_edit, width=150, height=316)]
]

st1 = Table(s1_table_data, colWidths=[250, 250])
st1.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4),
]))
story.append(st1)
story.append(Spacer(1, 10))

# Phase 6 Retrospective
add_p('Phase 6 — Micro-Retrospective ("Retro – Lab 2")', h2_style)
add_p('<b>What Went Well:</b><br/>'
      '• Smooth collaboration between Fateh Hasanlı and Ibrokhimov Odiljon with git commits authored by both members.<br/>'
      '• 3-layer architecture allowed writing pure unit-testable validation and list-filtering logic (`ReferenceValidator` and `ReferenceListUiState`).<br/>'
      '• Firestore snapshot listeners provided instant real-time list synchronization upon document edits.<br/><br/>'
      '<b>What Did Not Go Well:</b><br/>'
      '• Initial Firestore Security Rules denied write operations due to timestamp comparison syntax; resolved by enforcing `request.time` equality.<br/><br/>'
      '<b>Action Items for Lab 3:</b><br/>'
      '1. Implement comprehensive unit tests for `ReferenceValidator` and `AuthValidator` using JUnit 4.<br/>'
      '2. Set up Firebase Local Emulator Suite for reproducible offline testing.', body_style)

doc.build(story)
print('Lab 2 PDF generated successfully at:', pdf_path)
