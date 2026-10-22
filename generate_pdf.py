import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, HRFlowable, Image as RLImage

pdf_path = r"C:\Users\fateh\AndroidStudioProjects\RefScan\Lab1_Final_Report.pdf"

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
    spaceAfter=10
)

h2_style = ParagraphStyle(
    'H2',
    parent=styles['Heading2'],
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#4338CA'),
    spaceBefore=14,
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
add_p('Lab 1 Final Report: Walking Skeleton &amp; Firebase Authentication', title_style)
add_p('<b>Course:</b> Mobile Application in the Cloud — Lab 1<br/>'
      '<b>App Name:</b> RefScan<br/>'
      '<b>Student Name:</b> Fateh Hasanlı | <b>Student ID:</b> 57322<br/>'
      '<b>Account Email:</b> fatehqasanov@gmail.com<br/>'
      '<b>Role:</b> Solo Developer (PO, Tech Lead, Developer, QA/DevOps)<br/>'
      '<b>Tech Stack:</b> Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore · Git/GitHub<br/>'
      '<b>GitHub Repository:</b> <font color="#4338CA"><u>https://github.com/fatehqasanov/refsacn</u></font>', body_style)

story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB'), spaceAfter=10))

# Executive Summary
add_p('Executive Summary &amp; Deliverables Checklist', h2_style)
table_data = [
    [Paragraph('<b>Phase</b>', body_style), Paragraph('<b>Section</b>', body_style), Paragraph('<b>Status</b>', body_style)],
    [Paragraph('Phase 1', body_style), Paragraph('Team Roles &amp; Responsibilities', body_style), Paragraph('<font color="#16A34A"><b>COMPLETE</b></font>', body_style)],
    [Paragraph('Phase 2', body_style), Paragraph('Product Problem Statement, MVP &amp; Cloud Data Model', body_style), Paragraph('<font color="#16A34A"><b>COMPLETE</b></font>', body_style)],
    [Paragraph('Phase 3', body_style), Paragraph('GitHub Repository, Board Setup &amp; Rulesets', body_style), Paragraph('<font color="#16A34A"><b>COMPLETE</b></font>', body_style)],
    [Paragraph('Phase 4', body_style), Paragraph('Android Project Setup (Compose) &amp; Firebase Integration', body_style), Paragraph('<font color="#16A34A"><b>COMPLETE</b></font>', body_style)],
    [Paragraph('Phase 5', body_style), Paragraph('3-Layer Firebase Authentication Feature Implementation', body_style), Paragraph('<font color="#16A34A"><b>COMPLETE</b></font>', body_style)],
    [Paragraph('Phase 6', body_style), Paragraph('Architecture Diagram, PR Review &amp; Micro-Retrospective', body_style), Paragraph('<font color="#16A34A"><b>COMPLETE</b></font>', body_style)],
]
t = Table(table_data, colWidths=[70, 350, 80])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(t)
story.append(Spacer(1, 8))

# Repository Information
add_p('Repository &amp; Git Information', h2_style)
add_p('• <b>Repository Link:</b> https://github.com/fatehqasanov/refsacn<br/>'
      '• <b>Default Branch:</b> main (Protected with mandatory Pull Request reviews)<br/>'
      '• <b>Feature Branch:</b> feature/auth<br/>'
      '• <b>Git Commit Log Highlights:</b><br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;- <code>e261544</code> — feat(auth): Implement 3-layer Firebase Authentication feature<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;- <code>818c092</code> — docs: Add Lab 1 final report document<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;- <code>6a605fd</code> — refactor(ui): Extract stateless UI content components and update report with rendered screen layouts', body_style)

# Phase 1
add_p('Phase 1 — Team &amp; Roles', h2_style)
add_p('Since this is a solo-developer project, all responsibilities are held individually by <b>Fateh Hasanlı (ID: 57322, Email: fatehqasanov@gmail.com)</b>:', body_style)

roles_data = [
    [Paragraph('<b>Role</b>', body_style), Paragraph('<b>Responsibility</b>', body_style), Paragraph('<b>Assigned Person</b>', body_style)],
    [Paragraph('Product Owner (PO)', body_style), Paragraph('Product vision, problem statement, user story writing, and backlog prioritization.', body_style), Paragraph('Fateh Hasanlı (57322)', body_style)],
    [Paragraph('Tech Lead', body_style), Paragraph('Architecture design, data model specification, state management, and Firebase setup.', body_style), Paragraph('Fateh Hasanlı (57322)', body_style)],
    [Paragraph('Developer', body_style), Paragraph('Kotlin &amp; Jetpack Compose implementation, UI screens, ViewModel, and Firebase Auth calls.', body_style), Paragraph('Fateh Hasanlı (57322)', body_style)],
    [Paragraph('QA / DevOps', body_style), Paragraph('Git configuration, branch protection, pull request reviews, and board management.', body_style), Paragraph('Fateh Hasanlı (57322)', body_style)],
]
rt = Table(roles_data, colWidths=[110, 270, 120])
rt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(rt)
story.append(Spacer(1, 8))

# Phase 2
add_p('Phase 2 — Product Definition &amp; Cloud Data Model', h2_style)
add_p('1. Target Audience &amp; Problem Statement', h3_style)
add_p('<i>"Game artists and level designers walking outside or traveling cannot use desktop task managers to instantly capture, tag, and organize real-world material textures and color references for their active game projects."</i>', quote_style)
add_p('<b>Why a Mobile App?</b> RefScan leverages smartphone portability to log real-world reference observations, surface material tags, and color palettes directly from physical locations.', body_style)

add_p('2. MVP Features &amp; Sprint Breakdown', h3_style)
add_p('• <b>User Authentication (Sprint 1 - Complete):</b> Register, Log In, Log Out, and Auto-Login session persistence using Firebase Authentication (<code>fatehqasanov@gmail.com</code>).<br/>'
      '• <b>Project List Screen (Sprint 1):</b> View and manage active game environment levels or project titles.<br/>'
      '• <b>Reference Detail &amp; Edit Screen (Sprint 1):</b> View, add, and update material notes, surface tags, and color hex codes linked to a project.<br/>'
      '• <b>Camera &amp; Cloud Storage Upload (Sprint 3 / Later):</b> Capture direct texture photo references using the phone camera and sync to Firebase Cloud Storage.', body_style)

add_p('3. Cloud Firestore Data Model (Max 3 Collections)', h3_style)
schema_text = '''[users] (Collection)
 └── uid (Doc ID - String matching Firebase Auth UID)
      ├── email: String (e.g. fatehqasanov@gmail.com)
      ├── displayName: String
      └── createdAt: Timestamp

[projects] (Collection)
 └── projectId (Doc ID - String)
      ├── ownerId: String (foreign key -> users.uid)
      ├── title: String (e.g. "Cyberpunk Alley Level")
      ├── engine: String (e.g. "Unreal Engine 5")
      └── createdAt: Timestamp

[references] (Collection)
 └── referenceId (Doc ID - String)
      ├── projectId: String (foreign key -> projects.projectId)
      ├── ownerId: String (foreign key -> users.uid)
      ├── note: String (e.g. "Wet asphalt roughness & puddle reflection")
      ├── colorHex: String (e.g. "#1A2B3C")
      └── createdAt: Timestamp'''
story.append(Preformatted(schema_text, code_style))

# Phase 4 & 5 Architecture & Code
add_p('Phase 4 &amp; 5 — Technical Implementation &amp; 3-Layer Architecture', h2_style)
add_p('1. Architecture &amp; Data Flow', h3_style)
add_p('The application strictly isolates concerns into 3 distinct layers:<br/>'
      '• <b>Data Layer:</b> <code>AuthRepository</code> (interface) and <code>FirebaseAuthRepository</code> handle all direct interactions with the Firebase SDK using coroutines (<code>await()</code>) and <code>callbackFlow</code>.<br/>'
      '• <b>Logic Layer:</b> <code>AuthValidator</code> (pure Kotlin validation rules) and <code>AuthViewModel</code> manage UI state via <code>StateFlow</code> and map Firebase exceptions to user-friendly string messages.<br/>'
      '• <b>UI Layer:</b> Jetpack Compose screens (<code>LoginScreen</code>, <code>RegisterScreen</code>, <code>HomeScreen</code>) and <code>AppNavHost</code> consume the ViewModel state and handle navigation stack resets upon auth transitions.', body_style)

# Code Snippets
add_p('2. Core Code Implementation', h3_style)
auth_repo_code = '''// AuthRepository.kt (Domain Layer Interface)
package com.example.refscan.domain

import com.google.firebase.auth.FirebaseUser
import kotlinx.coroutines.flow.Flow

interface AuthRepository {
    val authState: Flow<FirebaseUser?>
    suspend fun login(email: String, password: String): Result<Unit>
    suspend fun register(email: String, password: String): Result<Unit>
    suspend fun logout(): Result<Unit>
    fun getCurrentUser(): FirebaseUser?
}'''
story.append(Preformatted(auth_repo_code, code_style))

firebase_repo_code = '''// FirebaseAuthRepository.kt (Data Layer Implementation)
package com.example.refscan.data

import com.example.refscan.domain.AuthRepository
import com.google.firebase.Firebase
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.FirebaseUser
import com.google.firebase.auth.auth
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.tasks.await

class FirebaseAuthRepository : AuthRepository {
    private val auth: FirebaseAuth = Firebase.auth

    override val authState: Flow<FirebaseUser?> = callbackFlow {
        val listener = FirebaseAuth.AuthStateListener { trySend(it.currentUser) }
        auth.addAuthStateListener(listener)
        awaitClose { auth.removeAuthStateListener(listener) }
    }

    override suspend fun login(email: String, password: String): Result<Unit> = runCatching {
        auth.signInWithEmailAndPassword(email, password).await()
    }

    override suspend fun register(email: String, password: String): Result<Unit> = runCatching {
        auth.createUserWithEmailAndPassword(email, password).await()
    }

    override suspend fun logout(): Result<Unit> = runCatching { auth.signOut() }
    override fun getCurrentUser(): FirebaseUser? = auth.currentUser
}'''
story.append(Preformatted(firebase_repo_code, code_style))

# UI Screenshots Section
add_p('3. In-App Screenshots (Compose UI Rendering)', h2_style)
add_p('The following screenshots show the actual application screens rendered directly from the Jetpack Compose components:', body_style)

img_login = r"C:\Users\fateh\AndroidStudioProjects\RefScan\login_screenshot.png"
img_reg = r"C:\Users\fateh\AndroidStudioProjects\RefScan\register_screenshot.png"
img_home = r"C:\Users\fateh\AndroidStudioProjects\RefScan\home_screenshot.png"

# Side by side screenshot images table (Width: 150pt, Height: 316pt each)
screenshot_table_data = [
    [
        Paragraph('<b>Figure 1: Login Screen</b>', body_style),
        Paragraph('<b>Figure 2: Register Screen</b>', body_style),
        Paragraph('<b>Figure 3: Home Screen</b>', body_style)
    ],
    [
        RLImage(img_login, width=150, height=316),
        RLImage(img_reg, width=150, height=316),
        RLImage(img_home, width=150, height=316)
    ]
]

st = Table(screenshot_table_data, colWidths=[165, 165, 165])
st.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,0), 4),
    ('TOPPADDING', (0,1), (-1,1), 4),
]))
story.append(st)
story.append(Spacer(1, 12))

# Phase 6
add_p('Phase 6 — Micro-Retrospective ("Retro – Lab 1")', h2_style)
add_p('• <b>What Went Well:</b> The 3-layer architecture cleanly decoupled pure Kotlin validation (<code>AuthValidator</code>) from UI composables and Firebase SDK calls. <code>callbackFlow</code> provided real-time auth state updates directly to Jetpack Compose navigation.<br/>'
      '• <b>What Did Not Go Well:</b> Initial Gradle build issues due to Kotlin 2.0 Compose compiler plugin requirements and missing SDK platform dependencies.<br/>'
      '• <b>Action Items for Lab 2:</b> Integrate Cloud Firestore SDK to persist user profile details upon registration, write unit tests for <code>AuthValidator</code>, and enhance Material 3 UI styling.', body_style)

doc.build(story)
print('PDF generated with EMBEDDED PNG SCREENSHOTS successfully at:', pdf_path)
