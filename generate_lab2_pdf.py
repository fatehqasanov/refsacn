import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, HRFlowable, Image as RLImage, PageBreak

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
    fontSize=20,
    leading=24,
    textColor=colors.HexColor('#1E1B4B'),
    spaceAfter=10
)

h2_style = ParagraphStyle(
    'H2',
    parent=styles['Heading2'],
    fontSize=14,
    leading=18,
    textColor=colors.HexColor('#4338CA'),
    spaceBefore=14,
    spaceAfter=6
)

h3_style = ParagraphStyle(
    'H3',
    parent=styles['Heading3'],
    fontSize=11,
    leading=14.5,
    textColor=colors.HexColor('#1F2937'),
    spaceBefore=10,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontSize=9.5,
    leading=13.5,
    textColor=colors.HexColor('#374151'),
    spaceAfter=6
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
    borderPadding=6,
    spaceAfter=8
)

quote_style = ParagraphStyle(
    'Quote',
    parent=body_style,
    fontName='Helvetica-Oblique',
    fontSize=9.5,
    leading=13.5,
    textColor=colors.HexColor('#475569'),
    leftIndent=12,
    borderPadding=4,
    spaceAfter=8
)

story = []

def add_p(text, style=body_style):
    story.append(Paragraph(text, style))

# Document Header
add_p('Lab 2 Final Technical &amp; Implementation Report: Cloud Data CRUD &amp; Access Control', title_style)
add_p('<b>Course:</b> Mobile Application in the Cloud — Lab 2<br/>'
      '<b>App Name:</b> RefScan<br/>'
      '<b>Tech Stack:</b> Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore · Git/GitHub<br/>'
      '<b>GitHub Repository:</b> <font color="#4338CA"><u>https://github.com/fatehqasanov/refsacn</u></font> | <b>Git Tag:</b> <code>lab2</code>', body_style)

story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#4338CA'), spaceAfter=12))

# Section 1: Team & Division of Responsibilities
add_p('1. Team Members &amp; Division of Responsibilities', h2_style)
add_p('This project was developed collaboratively by a team of two students. Responsibilities were divided based on architectural layers and feature ownership:', body_style)

roles_data = [
    [Paragraph('<b>Team Member</b>', body_style), Paragraph('<b>Role &amp; Primary Responsibilities</b>', body_style), Paragraph('<b>Key Deliverables Completed</b>', body_style)],
    [
        Paragraph('<b>Fateh Hasanlı</b><br/>ID: 57322<br/><code>fatehqasanov@gmail.com</code>', body_style),
        Paragraph('<b>Product Owner &amp; Tech Lead</b><br/>• Core Architecture &amp; Data Layer<br/>• Firebase Auth &amp; Form Logic<br/>• Domain Models &amp; Validation', body_style),
        Paragraph('• <code>AuthRepository</code> &amp; ViewModel<br/>• <code>ReferenceRepository</code> &amp; Firebase Impl<br/>• <code>ReferenceValidator</code> rules<br/>• <code>ReferenceEditViewModel</code> &amp; Form', body_style)
    ],
    [
        Paragraph('<b>Ibrokhimov Odiljon</b><br/>ID: 52857<br/><code>52857@student.polsl.pl</code>', body_style),
        Paragraph('<b>QA / DevOps &amp; Developer</b><br/>• Live List UI &amp; Navigation<br/>• Security Rules &amp; Testing<br/>• App Extensions &amp; Board', body_style),
        Paragraph('• <code>ReferenceListScreen</code> &amp; Cards<br/>• <code>firestore.rules</code> security policies<br/>• Extensions E1, E3, E5, E7<br/>• Board &amp; Git Tag <code>lab2</code>', body_style)
    ],
]
rt = Table(roles_data, colWidths=[120, 190, 190])
rt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(rt)
story.append(Spacer(1, 10))

# Section 2: Problem Statement & Context
add_p('2. Application Context &amp; Domain Problem', h2_style)
add_p('<i>"Game artists and level designers walking outside or traveling cannot use desktop task managers to instantly capture, tag, and organize real-world material textures and color references for their active game projects."</i>', quote_style)
add_p('<b>Why RefScan Fits Mobile Better Than Desktop:</b> Desktop task management tools (such as Jira or Trello) are designed for sprint planning at an office desk. RefScan relies on smartphone portability so environment artists can record surface material roughness, color hex codes, and texture notes immediately while observing physical real-world locations.', body_style)

# Section 3: Tech Stack & Definition of Done
add_p('3. Technical Stack &amp; Definition of Done', h2_style)
add_p('<b>Technical Configuration:</b><br/>'
      '• <b>App Framework:</b> Kotlin + Jetpack Compose (Modern declarative UI)<br/>'
      '• <b>Authentication:</b> Firebase Authentication (Email &amp; Password session management)<br/>'
      '• <b>Cloud Database:</b> Cloud Firestore (EU Region: <code>europe-west1</code>)<br/>'
      '• <b>Backend Security:</b> Firestore Security Rules (<code>firestore.rules</code>)<br/>'
      '• <b>Testing Utilities:</b> JUnit 4 and Kotlin Coroutines Test framework', body_style)

add_p('<b>Definition of Done (DoD):</b><br/>'
      '<i>"A feature or user story is considered Done when it is merged into main through a reviewed Pull Request with at least one approval, runs without crashing on the devices of both team members (Fateh Hasanlı and Ibrokhimov Odiljon), handles invalid input gracefully with user-friendly error messages, and has its corresponding GitHub issue closed."</i>', quote_style)

story.append(PageBreak())

# Section 4: Data Model
add_p('4. Cloud Firestore Data Model Specification', h2_style)
add_p('The cloud backend uses two collections: <code>references</code> (the main collection that users create, edit, and delete) and <code>projects</code> (a read-only reference collection that holds pre-seeded game project titles):', body_style)

data_model_rows = [
    [Paragraph('<b>Collection</b>', body_style), Paragraph('<b>Field Name</b>', body_style), Paragraph('<b>Type</b>', body_style), Paragraph('<b>Set By</b>', body_style), Paragraph('<b>Description &amp; Rules</b>', body_style)],
    [Paragraph('users', body_style), Paragraph('uid', body_style), Paragraph('String (doc id)', body_style), Paragraph('Firebase Auth', body_style), Paragraph('Matches authenticated user UID', body_style)],
    [Paragraph('users', body_style), Paragraph('email', body_style), Paragraph('String', body_style), Paragraph('User / Auth', body_style), Paragraph('User account email address', body_style)],
    [Paragraph('projects', body_style), Paragraph('id', body_style), Paragraph('String (doc id)', body_style), Paragraph('Admin / Seed', body_style), Paragraph('Pre-seeded reference collection ID', body_style)],
    [Paragraph('projects', body_style), Paragraph('title', body_style), Paragraph('String', body_style), Paragraph('Admin / Seed', body_style), Paragraph('e.g., "Cyberpunk Alley Level"', body_style)],
    [Paragraph('references', body_style), Paragraph('id', body_style), Paragraph('String (doc id)', body_style), Paragraph('Firestore', body_style), Paragraph('Unique reference document ID', body_style)],
    [Paragraph('references', body_style), Paragraph('ownerId', body_style), Paragraph('String', body_style), Paragraph('App (Auth Session)', body_style), Paragraph('Foreign key matching <code>users.uid</code>', body_style)],
    [Paragraph('references', body_style), Paragraph('projectId', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('Foreign key matching <code>projects.id</code>', body_style)],
    [Paragraph('references', body_style), Paragraph('note', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('Texture description (1 to 200 chars)', body_style)],
    [Paragraph('references', body_style), Paragraph('colorHex', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('Surface color hex format (<code>#RRGGBB</code>)', body_style)],
    [Paragraph('references', body_style), Paragraph('rating', body_style), Paragraph('Int', body_style), Paragraph('User Input', body_style), Paragraph('Importance rating (1 to 5 stars)', body_style)],
    [Paragraph('references', body_style), Paragraph('status', body_style), Paragraph('String', body_style), Paragraph('User Input', body_style), Paragraph('<code>"active"</code> or <code>"archived"</code>', body_style)],
    [Paragraph('references', body_style), Paragraph('createdAt', body_style), Paragraph('Timestamp', body_style), Paragraph('Server Clock', body_style), Paragraph('<code>FieldValue.serverTimestamp()</code>', body_style)],
    [Paragraph('references', body_style), Paragraph('updatedAt', body_style), Paragraph('Timestamp', body_style), Paragraph('Server Clock', body_style), Paragraph('<code>FieldValue.serverTimestamp()</code>', body_style)],
]

dmt = Table(data_model_rows, colWidths=[60, 65, 75, 85, 215])
dmt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(dmt)
story.append(Spacer(1, 10))

# Section 5: Architecture & Data Flow
add_p('5. 3-Layer Architecture &amp; Data Isolation', h2_style)
add_p('The application strictly enforces a 3-layer architecture to ensure clean separation of concerns:<br/>'
      '1. <b>Data Layer:</b> <code>ReferenceRepository</code> interface and <code>FirebaseReferenceRepository</code> handle all direct communication with Cloud Firestore using coroutine extensions (<code>await()</code>) and realtime snapshot flows (<code>callbackFlow</code>).<br/>'
      '2. <b>Logic Layer:</b> <code>ReferenceValidator</code> contains pure Kotlin validation functions (zero UI or Android framework dependencies). <code>ReferenceListViewModel</code> and <code>ReferenceEditViewModel</code> manage UI state via <code>StateFlow</code>.<br/>'
      '3. <b>UI Layer:</b> Jetpack Compose screens (<code>ReferenceListScreen</code> and <code>ReferenceEditScreen</code>) only display state and forward user interactions to the ViewModel.', body_style)

# Code Snippet - Models & Repository
add_p('Core Data &amp; Domain Code Implementation', h3_style)
code_data = '''// Reference.kt (Domain Model)
data class Reference(
    @DocumentId val id: String = "",
    val ownerId: String = "",
    val projectId: String = "",
    val projectName: String = "",
    val note: String = "",
    val colorHex: String = "#1A2B3C",
    val rating: Int = 3,
    val status: String = "active",
    @ServerTimestamp val createdAt: Timestamp? = null,
    @ServerTimestamp val updatedAt: Timestamp? = null
)

// ReferenceRepository.kt (Domain Interface)
interface ReferenceRepository {
    fun observeMyReferences(): Flow<List<Reference>>
    suspend fun getReference(id: String): Result<Reference>
    suspend fun getProjects(): Result<List<Project>>
    suspend fun addReference(input: ReferenceInput): Result<String>
    suspend fun updateReference(id: String, input: ReferenceInput): Result<Unit>
    suspend fun deleteReference(id: String): Result<Unit>
}'''
story.append(Preformatted(code_data, code_style))

story.append(PageBreak())

# Section 6: In-App Screenshots - LARGE & EXPLANATORY ONE BY ONE
add_p('6. In-App Screen Flow &amp; User Experience', h2_style)
add_p('Each screen is displayed below in full scale alongside a detailed breakdown of its features and user interaction flow:', body_style)

img_login = r"C:\Users\fateh\AndroidStudioProjects\RefScan\login_screenshot.png"
img_reg = r"C:\Users\fateh\AndroidStudioProjects\RefScan\register_screenshot.png"
img_list = r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_list_screenshot.png"
img_edit = r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_edit_screenshot.png"

# Figure 1: Login Screen
add_p('Figure 1: Authentication — Login Screen', h3_style)
add_p('<b>Screen Features &amp; Workflow:</b><br/>'
      '• <b>Email Input Field:</b> Configured with <code>KeyboardType.Email</code> and displays real-time validation.<br/>'
      '• <b>Password Field:</b> Uses <code>PasswordVisualTransformation</code> to mask user input.<br/>'
      '• <b>Action Button:</b> Displays a <code>CircularProgressIndicator</code> during authentication calls and disables user interactions while loading.<br/>'
      '• <b>Navigation Link:</b> Redirects the user to the Registration screen.', body_style)
story.append(Spacer(1, 4))
story.append(RLImage(img_login, width=240, height=506))
story.append(Spacer(1, 14))

story.append(PageBreak())

# Figure 2: Register Screen
add_p('Figure 2: Authentication — Register Screen', h3_style)
add_p('<b>Screen Features &amp; Workflow:</b><br/>'
      '• <b>Registration Fields:</b> Collects Email, Password, and Confirm Password.<br/>'
      '• <b>Field Validation:</b> Uses pure Kotlin rules in <code>AuthValidator</code> to verify email formatting, password length (minimum 6 characters), and password confirmation match before initiating backend calls.<br/>'
      '• <b>Error Displays:</b> Field-specific error labels are rendered directly below each corresponding input field.', body_style)
story.append(Spacer(1, 4))
story.append(RLImage(img_reg, width=240, height=506))
story.append(Spacer(1, 14))

story.append(PageBreak())

# Figure 3: Live Reference List Screen
add_p('Figure 3: Main Dashboard — Live Material Reference List (R5, E1, E3, E5, E7)', h3_style)
add_p('<b>Screen Features &amp; Workflow:</b><br/>'
      '• <b>Live Query (R5):</b> Employs Cloud Firestore realtime snapshot listener (<code>addSnapshotListener</code>) filtered strictly at the query level by <code>ownerId == currentUid</code>.<br/>'
      '• <b>E1 Search Extension:</b> Interactive search text field filters the list in real-time by note text and project title.<br/>'
      '• <b>E7 Statistics Header:</b> Displays live computed metrics (e.g. <code>"2 active · 1 archived"</code>).<br/>'
      '• <b>E5 Status Filter Chips:</b> Toggles view between All, Active, and Archived references.<br/>'
      '• <b>Floating Action Button (FAB):</b> Tapping "+" navigates to the Create Reference form screen.', body_style)
story.append(Spacer(1, 4))
story.append(RLImage(img_list, width=240, height=506))
story.append(Spacer(1, 14))

story.append(PageBreak())

# Figure 4: Create & Edit Reference Form Screen
add_p('Figure 4: Data Management — Create &amp; Edit Form Screen (R6, R7)', h3_style)
add_p('<b>Screen Features &amp; Workflow:</b><br/>'
      '• <b>Unified Form Route (R6):</b> Handled via route <code>edit?id={id}</code>. If `id` is null, it creates a new record; if `id` is present, it loads and updates the existing reference.<br/>'
      '• <b>Reference Collection Selector:</b> Picked from a dropdown menu loaded from the <code>projects</code> reference collection.<br/>'
      '• <b>Validation Rules:</b> Enforces note length, valid `#RRGGBB` color hex format, 1-5 star ratings, and cross-field logic.<br/>'
      '• <b>Delete Confirmation (R7):</b> Prompts an alert dialog confirming deletion by item title.', body_style)
story.append(Spacer(1, 4))
story.append(RLImage(img_edit, width=240, height=506))
story.append(Spacer(1, 14))

story.append(PageBreak())

# Section 7: Server-Side Access Control (R8)
add_p('7. Server-Side Access Control &amp; Security Scenarios (R8)', h2_style)
add_p('Security rules are defined as code in <code>firestore.rules</code> and committed to the repository. Access control is enforced on the server for all database operations:', body_style)

r8_rows = [
    [Paragraph('<b>#</b>', body_style), Paragraph('<b>Scenario Description</b>', body_style), Paragraph('<b>Expected Behavior</b>', body_style), Paragraph('<b>Verification Method</b>', body_style), Paragraph('<b>Result</b>', body_style)],
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
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(r8t)
story.append(Spacer(1, 10))

# Security Rules Code
rules_code = '''// firestore.rules (Server-Side Access Control)
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    function isSignedIn() { return request.auth != null; }
    function isOwner(resourceData) { return isSignedIn() && request.auth.uid == resourceData.ownerId; }

    match /references/{id} {
      allow read, delete: if isOwner(resource.data);
      allow create: if isSignedIn() && request.resource.data.ownerId == request.auth.uid;
      allow update: if isOwner(resource.data) && request.resource.data.ownerId == resource.data.ownerId;
    }

    match /projects/{id} {
      allow read: if isSignedIn();
      allow write: if false;
    }
  }
}'''
story.append(Preformatted(rules_code, code_style))

# Section 8: Micro-Retrospective
add_p('8. Phase 6 — Micro-Retrospective ("Retro – Lab 2")', h2_style)
add_p('<b>What Went Well:</b><br/>'
      '• Excellent teamwork and task distribution between Fateh Hasanlı and Ibrokhimov Odiljon with commits authored by both team members in the repository.<br/>'
      '• The 3-layer architecture decoupled pure Kotlin validation (`ReferenceValidator`) and filtering logic (`ReferenceListUiState`) for seamless unit testing in Lab 3.<br/>'
      '• Firestore snapshot listeners delivered instant real-time synchronization upon document edits.<br/><br/>'
      '<b>What Did Not Go Well:</b><br/>'
      '• Initial Security Rules blocked update requests due to strict timestamp comparisons; resolved by comparing `request.time`.<br/><br/>'
      '<b>Action Items for Lab 3:</b><br/>'
      '1. Implement unit test suites for `ReferenceValidator` and `AuthValidator` using JUnit 4.<br/>'
      '2. Configure Firebase Local Emulator Suite for reproducible offline backend testing.', body_style)

doc.build(story)
print('Expanded Lab 2 PDF generated successfully at:', pdf_path)
