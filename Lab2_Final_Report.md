# Lab 2 Final Technical & Implementation Report: Cloud Data CRUD & Server-Side Access Control

**Course:** Mobile Application in the Cloud — Lab 2  
**App Name:** RefScan  
**Tech Stack:** Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore · Git/GitHub  
**GitHub Repository:** [https://github.com/fatehqasanov/refsacn](https://github.com/fatehqasanov/refsacn) | **Git Tag:** `lab2`  

---

## 1. Team Members & Division of Responsibilities

This project was developed collaboratively by a team of two students:

-- **Fateh Hasanli** (Student ID: 57322 | Email: `fatehqasanov@gmail.com`) — **Product Owner & Tech Lead**
  - Architecture & Data Layer setup (`ReferenceRepository`, `FirebaseReferenceRepository`).
  - Firebase Authentication & Form ViewModels (`AuthViewModel`, `ReferenceEditViewModel`).
  - Domain models (`Reference`, `Project`) & pure Kotlin validation rules (`ReferenceValidator`).
- **Ibrokhimov Odiljon** (Student ID: 52857 | Email: `52857@student.polsl.pl`) — **QA / DevOps & Developer**
  - Live Reference List UI (`ReferenceListScreen` and item cards).
  - Server-side Security Rules (`firestore.rules`) and scenario testing.
  - Implemented extensions (E1 Search, E3 Empty States, E5 Status Filter, E7 Statistics Header).
  - GitHub Board management, PR reviews, and release tag `lab2`.

---

## 2. Application Context & Domain Problem

> *"Game artists and level designers walking outside or traveling cannot use desktop task managers to instantly capture, tag, and organize real-world material textures and color references for their active game projects."*

**Why RefScan Fits Mobile Better Than Desktop:** Desktop task management tools (such as Jira or Trello) are designed for sprint planning at an office desk. RefScan relies on smartphone portability so environment artists can record surface material roughness, color hex codes, and texture notes immediately while observing physical real-world locations.

---

## 3. Technical Stack & Definition of Done

### Technical Configuration
- **App Framework:** Kotlin + Jetpack Compose (Modern declarative UI)
- **Authentication:** Firebase Authentication (Email & Password session management)
- **Cloud Database:** Cloud Firestore (EU Region: `europe-west1`)
- **Backend Security:** Firestore Security Rules (`firestore.rules`)
- **Testing Utilities:** JUnit 4 and Kotlin Coroutines Test framework

### Definition of Done (DoD)
> *"A feature or user story is considered Done when it is merged into main through a reviewed Pull Request with at least one approval, runs without crashing on the devices of both team members (Fateh Hasanlı and Ibrokhimov Odiljon), handles invalid input gracefully with user-friendly error messages, and has its corresponding GitHub issue closed."*

---

## 4. Cloud Firestore Data Model Specification

The cloud backend uses two collections: `references` (the main collection that users create, edit, and delete) and `projects` (a read-only reference collection that holds pre-seeded game project titles):

| Collection | Field Name | Type | Set By | Description & Rules |
| :--- | :--- | :--- | :--- | :--- |
| `users` | `uid` | String (doc id) | Firebase Auth | Matches authenticated user UID |
| `users` | `email` | String | User / Auth | User account email address |
| `projects` | `id` | String (doc id) | Admin / Seed | Pre-seeded reference collection ID |
| `projects` | `title` | String | Admin / Seed | e.g. `"Cyberpunk Alley Level"` |
| `references` | `id` | String (doc id) | Firestore | Unique reference document ID |
| `references` | `ownerId` | String | App (Auth Session) | Foreign key matching `users.uid` |
| `references` | `projectId` | String | User Input | Foreign key matching `projects.id` |
| `references` | `note` | String | User Input | Texture description (1 to 200 chars) |
| `references` | `colorHex` | String | User Input | Surface color hex format (`#RRGGBB`) |
| `references` | `rating` | Int | User Input | Importance rating (1 to 5 stars) |
| `references` | `status` | String | User Input | `"active"` or `"archived"` |
| `references` | `createdAt` | Timestamp | Server Clock | `FieldValue.serverTimestamp()` |
| `references` | `updatedAt` | Timestamp | Server Clock | `FieldValue.serverTimestamp()` |

---

## 5. 3-Layer Architecture & Data Isolation

The application strictly enforces a 3-layer architecture to ensure clean separation of concerns:
1. **Data Layer:** `ReferenceRepository` interface and `FirebaseReferenceRepository` handle all direct communication with Cloud Firestore using coroutine extensions (`await()`) and realtime snapshot flows (`callbackFlow`).
2. **Logic Layer:** `ReferenceValidator` contains pure Kotlin validation functions (zero UI or Android framework dependencies). `ReferenceListViewModel` and `ReferenceEditViewModel` manage UI state via `StateFlow`.
3. **UI Layer:** Jetpack Compose screens (`ReferenceListScreen` and `ReferenceEditScreen`) only display state and forward user interactions to the ViewModel.

---

## 6. Server-Side Access Control & Security Scenarios (R8)

Security rules are defined as code in [`firestore.rules`](file:///C:/Users/fateh/AndroidStudioProjects/RefScan/firestore.rules) and committed to the repository:

| # | Scenario Description | Expected Behavior | Verification Method | Result |
| :-: | :--- | :-: | :--- | :-: |
| **1** | Read own record | Allowed | App snapshot query / Rules Playground | ✅ **ALLOWED** |
| **2** | Read same record as a different user | Denied | Rules Playground simulated as User B | ✅ **DENIED** |
| **3** | Read without being signed in | Denied | Unauthenticated request call | ✅ **DENIED** |
| **4** | Create record whose `ownerId` is another user | Denied | Rules Playground create request with fake UID | ✅ **DENIED** |
| **5** | Create record breaking logical rule (empty note) | Denied | Rules Playground validation check | ✅ **DENIED** |
| **6** | Update own record, changing its `ownerId` | Denied | Rules Playground update request | ✅ **DENIED** |
| **7** | Create record in reference collection (`projects`) | Denied | Write request to `/projects/new` | ✅ **DENIED** |
| **8** | Read reference record as signed-in user | Allowed | App dropdown query / Rules Playground | ✅ **ALLOWED** |

---

## 7. Phase 6 — Micro-Retrospective ("Retro – Lab 2")

- **What Went Well:** Excellent teamwork and task distribution between Fateh Hasanlı and Ibrokhimov Odiljon with commits authored by both team members in the repository.
- **What Did Not Go Well:** Initial Security Rules blocked update requests due to strict timestamp comparisons; resolved by comparing `request.time`.
- **Action Items for Lab 3:** Implement unit test suites for `ReferenceValidator` and `AuthValidator` using JUnit 4, and configure Firebase Local Emulator Suite.

---
*Report generated for Lab 2 submission • RefScan Android App • Authors: Fateh Hasanlı (57322) & Ibrokhimov Odiljon (52857)*
