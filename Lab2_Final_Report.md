# Lab 2 Final Report: Cloud Data CRUD & Server-Side Access Control

**Course:** Mobile Application in the Cloud — Lab 2  
**App Name:** RefScan  
**Team Members & Workload Distribution:**  
1. **Fateh Hasanlı** (Student ID: 57322 | Email: `fatehqasanov@gmail.com`) — **60% Workload** (Tech Lead, Data Layer, Auth & Form Logic)  
2. **Ibrokhimov Odiljon** (Student ID: 52857 | Email: `52857@student.polsl.pl`) — **40% Workload** (QA/DevOps, List UI, Security Rules & Extensions)  

**Tech Stack:** Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore (EU Region) · Git/GitHub  
**GitHub Repository:** [https://github.com/fatehqasanov/refsacn](https://github.com/fatehqasanov/refsacn)  
**Git Tag:** `lab2`  

---

## Requirements Checklist (R1 – R10)

| Requirement | Description | Status |
| :--- | :--- | :---: |
| **R1** | Sprint planning on board, Retro issue closed, DoD in README | ✅ **DONE** |
| **R2** | Cloud database (Firestore EU), main + reference collection (3+ records) | ✅ **DONE** |
| **R3** | Data model with `ownerId`, server timestamps, $\ge 4$ domain fields | ✅ **DONE** |
| **R4** | 3-Layer architecture (Repository interface, ViewModel, pure Validator) | ✅ **DONE** |
| **R5** | Live list query filtered by `ownerId`, loading & error states, logout | ✅ **DONE** |
| **R6** | Create/Edit form, reference picker, 3+ validation rules, cross-field rule | ✅ **DONE** |
| **R7** | Delete with confirmation dialog naming item being deleted | ✅ **DONE** |
| **R8** | Server-side Security Rules in `firestore.rules` with 8 tested scenarios | ✅ **DONE** |
| **R9** | Implemented 4 Extensions (E1 Search, E3 Empty states, E5 Status toggle, E7 Stats) | ✅ **DONE** |
| **R10** | Team process, commits/PRs from BOTH Fateh & Odiljon, tag `lab2` | ✅ **DONE** |

---

## Tech Stack & Definition of Done

### Tech Stack Table
- **App Framework:** Kotlin + Jetpack Compose
- **Backend & Auth:** Firebase Authentication
- **Cloud Database:** Cloud Firestore (EU Region - `europe-west1`)
- **Security:** Firestore Security Rules (`firestore.rules`)
- **Testing Frameworks:** JUnit 4, Kotlin Coroutines Test Framework

### Definition of Done (DoD)
> *"A story is done when it is merged to main through a reviewed PR with at least one approval, works on the device of both team members (Fateh Hasanlı and Ibrokhimov Odiljon), does not crash on invalid input or screen rotation, and its linked GitHub issue is closed."*

---

## Cloud Data Model (R2 & R3)

**Main Collection:** `references`  
**Reference Collection (Read-Only):** `projects` (Holds 3+ pre-seeded records)

| Collection | Field Name | Type | Set By | Description |
| :--- | :--- | :--- | :--- | :--- |
| `users` | `uid` | String (doc id) | Firebase Auth | User account identifier |
| `users` | `email` | String | User / Auth | e.g. `fatehqasanov@gmail.com` |
| `projects` | `id` | String (doc id) | Admin / Seed | e.g. `proj_1` (Reference collection) |
| `projects` | `title` | String | Admin / Seed | e.g. `Cyberpunk Alley Level` |
| `references` | `id` | String (doc id) | Firestore | Unique reference ID |
| `references` | `ownerId` | String | App (Auth session) | Foreign key to `users.uid` |
| `references` | `projectId` | String | User Input | Foreign key to `projects.id` |
| `references` | `note` | String | User Input | Material reference description |
| `references` | `colorHex` | String | User Input | Surface color hex code (`#RRGGBB`) |
| `references` | `rating` | Int | User Input | Importance rating (1 to 5 stars) |
| `references` | `status` | String | User Input | `"active"` or `"archived"` |
| `references` | `createdAt` | Timestamp | Server Clock | `FieldValue.serverTimestamp()` |
| `references` | `updatedAt` | Timestamp | Server Clock | `FieldValue.serverTimestamp()` |

---

## R8 — Server-Side Access Control Scenarios Matrix

Rules code defined in [`firestore.rules`](file:///C:/Users/fateh/AndroidStudioProjects/RefScan/firestore.rules):

| # | Scenario Description | Expected | Verification Method | Result |
| :-: | :--- | :-: | :--- | :-: |
| **1** | Read own record | Allowed | App snapshot query / Rules Playground | ✅ **ALLOWED** |
| **2** | Read same record as a different user | Denied | Rules Playground simulated as User B | ✅ **DENIED** |
| **3** | Read without being signed in | Denied | Unauthenticated API request call | ✅ **DENIED** |
| **4** | Create record whose `ownerId` is another user | Denied | Rules Playground create request with fake UID | ✅ **DENIED** |
| **5** | Create record breaking logical rule (empty note) | Denied | Rules Playground validation check | ✅ **DENIED** |
| **6** | Update own record, changing its `ownerId` | Denied | Rules Playground update request | ✅ **DENIED** |
| **7** | Create record in reference collection (`projects`) | Denied | Write request to `/projects/new` | ✅ **DENIED** |
| **8** | Read reference record as signed-in user | Allowed | App dropdown query / Rules Playground | ✅ **ALLOWED** |

---

## R9 — Implemented Extensions (4 Completed)

1. **E1: Search** — Text field filters the list by `note` and `projectName` (case-insensitive) with a clear button.
2. **E3: Empty & No-Results States** — Distinct hint shown when list is empty vs. when a search query yields no hits.
3. **E5: Status Toggle & Filtering** — Toggle chips filter list between "All", "Active", and "Archived" with status tags.
4. **E7: Statistics Header** — Header card displays live computed metrics (`"2 active · 1 archived"`).

---

## Phase 6 — Micro-Retrospective ("Retro – Lab 2")

- **What Went Well:** Smooth collaboration between Fateh Hasanlı and Ibrokhimov Odiljon with commits authored by both members.
- **What Did Not Go Well:** Initial Security Rules denied update operations due to timestamp comparison syntax; resolved by enforcing `request.time` equality.
- **Action Items for Lab 3:** Implement unit tests for `ReferenceValidator` using JUnit 4 and set up Firebase Local Emulator Suite.

---
*Report generated for Lab 2 submission • RefScan Android App • Authors: Fateh Hasanlı (57322) & Ibrokhimov Odiljon (52857)*
