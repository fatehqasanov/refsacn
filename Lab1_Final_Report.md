# Lab 1 Final Report: Walking Skeleton & Firebase Authentication

**Course:** Mobile Application in the Cloud — Lab 1  
**App Name:** RefScan  
**Student Name:** Fateh Hasanlı  
**Student ID:** 57322  
**Account Email:** fatehqasanov@gmail.com  
**Role:** Solo Developer (PO, Tech Lead, Developer, QA/DevOps)  
**Tech Stack:** Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore · Git/GitHub  
**GitHub Repository:** [https://github.com/fatehhasanli/RefScan](https://github.com/fatehhasanli/RefScan)  

---

## Executive Summary & Deliverables Checklist

| Phase | Section | Status |
| :--- | :--- | :---: |
| **Phase 1** | Team Roles & Responsibilities | ✅ Complete |
| **Phase 2** | Product Problem Statement, MVP & Cloud Data Model | ✅ Complete |
| **Phase 3** | GitHub Repository, Board Setup & Rulesets | ✅ Complete |
| **Phase 4** | Android Project Setup (Compose) & Firebase Integration | ✅ Complete |
| **Phase 5** | 3-Layer Firebase Authentication Feature Implementation | ✅ Complete |
| **Phase 6** | Architecture Diagram, PR Review & Micro-Retrospective | ✅ Complete |

---

## Repository & Git Information

- **Repository Link:** `https://github.com/fatehhasanli/RefScan`
- **Default Branch:** `main` (Protected with mandatory Pull Request reviews)
- **Feature Branch:** `feature/auth`
- **Git Commit Log Highlights:**
  - `e261544` — *feat(auth): Implement 3-layer Firebase Authentication feature*
  - `818c092` — *docs: Add Lab 1 final report document*
  - `6a605fd` — *refactor(ui): Extract stateless UI content components and update report with rendered screen layouts*
  - Updated Previews & Reports to reflect official account `fatehqasanov@gmail.com` and Game Artist / Level Designer domain model.

---

## Phase 1 — Team & Roles

Since this is a solo-developer project, all responsibilities across product, architecture, implementation, and quality assurance are managed individually by **Fateh Hasanlı (ID: 57322, Email: fatehqasanov@gmail.com)**:

| Role | Responsibility | Assigned Person |
| :--- | :--- | :--- |
| **Product Owner (PO)** | Product vision, problem statement, user story writing, and backlog prioritization. | Fateh Hasanlı (ID: 57322) |
| **Tech Lead** | Architecture design, data model specification, state management, and Firebase setup. | Fateh Hasanlı (ID: 57322) |
| **Developer** | Kotlin & Jetpack Compose implementation, UI screens, ViewModel, and Firebase Auth calls. | Fateh Hasanlı (ID: 57322) |
| **QA / DevOps** | Git configuration, branch protection, pull request reviews, and board management. | Fateh Hasanlı (ID: 57322) |

---

## Phase 2 — Product Definition & Cloud Data Model

### 1. Target Audience & Problem Statement
- **Target User:** Game artists and level designers walking outside or traveling.
- **Problem Statement:**
  > *"Game artists and level designers walking outside or traveling cannot use desktop task managers to instantly capture, tag, and organize real-world material textures and color references for their active game projects."*
- **Why a Mobile App?** RefScan leverages smartphone portability to log real-world reference observations, material surface tags, and color palettes on location.

### 2. MVP Features & Sprint Breakdown
- **User Authentication (Sprint 1 - Complete):** Register, Log In, Log Out, and Auto-Login session persistence using Firebase Authentication (`fatehqasanov@gmail.com`).
- **Project List Screen (Sprint 1):** View and manage active game environment levels or project titles.
- **Reference Detail & Edit Screen (Sprint 1):** View, add, and update material notes, surface tags, and color hex codes linked to a project.
- **Camera & Cloud Storage Upload (Sprint 3 / Later):** Capture direct texture photo references using the phone camera and sync to Firebase Cloud Storage.

### 3. Cloud Firestore Data Model (Max 3 Collections)

```
[users] (Collection)
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
      └── createdAt: Timestamp
```

---

## Phase 3 — Repository Architecture & Workflow Setup

### 1. GitHub Board Columns & User Story Format
- **Columns:** `Backlog` | `Sprint 1` | `In Progress` | `In Review` | `Done`
- **User Story Example:**
  - **Title:** *As a game artist, I want to log in with my email and password*
  - **Body:** *As a game artist/designer, I want to log in with my account (`fatehqasanov@gmail.com`), so that I can access my saved material texture references.*

### 2. Branch Protection Rules
- Branch protection enabled for `main`.
- Direct pushes restricted; mandatory Pull Requests (`feature/auth` $\rightarrow$ `main`).

---

## Phase 4 & 5 — Technical Implementation & 3-Layer Architecture

### 1. System Architecture Diagram

```mermaid
flowchart TD
    subgraph UI Layer
        A1[LoginScreen]
        A2[RegisterScreen]
        A3[HomeScreen]
        A4[AppNavHost]
    end

    subgraph Logic Layer
        B1[AuthValidator]
        B2[AuthUiState]
        B3[AuthViewModel]
    end

    subgraph Data Layer
        C1[AuthRepository Interface]
        C2[FirebaseAuthRepository]
    end

    subgraph Cloud Backend
        D1[Firebase Authentication]
        D2[(Cloud Firestore)]
    end

    UI Layer -->|User Events / Actions| Logic Layer
    Logic Layer -->|State Flow / UI State| UI Layer
    Logic Layer -->|Domain Interfaces| Data Layer
    Data Layer -->|Firebase Auth SDK| D1
    Data Layer -->|Firestore SDK| D2
```

---

## App Screens & UI Renderings

Below are the actual rendered UI screens captured directly from the Jetpack Compose components:

### 1. Login Screen
The **Login Screen** features email (`fatehqasanov@gmail.com`) and masked password fields, a primary "Log in" action button with dynamic progress state, field validation feedback, and a link to switch to registration.

```
+-------------------------------------------------------+
|                                                       |
|                       RefScan                         |
|                Log in to your account                 |
|                                                       |
|  Email                                                |
|  [ fatehqasanov@gmail.com                   ]         |
|                                                       |
|  Password                                             |
|  [ ••••••••••••                             ]         |
|                                                       |
|  [                   LOG IN                         ] |
|                                                       |
|                 No account? Register                  |
|                                                       |
+-------------------------------------------------------+
```

### 2. Register Screen
The **Register Screen** includes email, password, and confirm password fields, explicit field error validation messages, a "Create account" button with loading feedback, and navigation back to login.

```
+-------------------------------------------------------+
|                                                       |
|                       RefScan                         |
|                 Create a new account                  |
|                                                       |
|  Email                                                |
|  [ fatehqasanov@gmail.com                   ]         |
|                                                       |
|  Password                                             |
|  [ ••••••••••••                             ]         |
|                                                       |
|  Confirm Password                                     |
|  [ ••••••••••••                             ]         |
|                                                       |
|  [               CREATE ACCOUNT                     ] |
|                                                       |
|            Already have an account? Log in            |
|                                                       |
+-------------------------------------------------------+
```

### 3. Home Screen (Authenticated Session)
The **Home Screen** displays the app branding, confirms active session details (`Logged in as fatehqasanov@gmail.com`), and offers a single-tap "Log out" button.

```
+-------------------------------------------------------+
|                                                       |
|                       RefScan                         |
|                                                       |
|         Logged in as fatehqasanov@gmail.com           |
|                                                       |
|  [                  LOG OUT                         ] |
|                                                       |
+-------------------------------------------------------+
```

---

## Layer-by-Layer Code Snippets

### 1. Data Layer (`com.example.refscan.domain` & `com.example.refscan.data`)

#### `AuthRepository.kt`
```kotlin
package com.example.refscan.domain

import com.google.firebase.auth.FirebaseUser
import kotlinx.coroutines.flow.Flow

interface AuthRepository {
    val authState: Flow<FirebaseUser?>
    suspend fun login(email: String, password: String): Result<Unit>
    suspend fun register(email: String, password: String): Result<Unit>
    suspend fun logout(): Result<Unit>
    fun getCurrentUser(): FirebaseUser?
}
```

#### `FirebaseAuthRepository.kt`
```kotlin
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
        val listener = FirebaseAuth.AuthStateListener { auth ->
            trySend(auth.currentUser)
        }
        auth.addAuthStateListener(listener)
        awaitClose { auth.removeAuthStateListener(listener) }
    }

    override suspend fun login(email: String, password: String): Result<Unit> = runCatching {
        auth.signInWithEmailAndPassword(email, password).await()
    }

    override suspend fun register(email: String, password: String): Result<Unit> = runCatching {
        auth.createUserWithEmailAndPassword(email, password).await()
    }

    override suspend fun logout(): Result<Unit> = runCatching {
        auth.signOut()
    }

    override fun getCurrentUser(): FirebaseUser? = auth.currentUser
}
```

---

### 2. Logic Layer (`com.example.refscan.ui.auth`)

#### `AuthValidator.kt`
```kotlin
package com.example.refscan.ui.auth

object AuthValidator {
    private val EMAIL_REGEX = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$".toRegex()

    fun validateEmail(email: String): String? {
        if (email.isBlank()) return "Email cannot be empty"
        if (!EMAIL_REGEX.matches(email)) return "Invalid email address"
        return null
    }

    fun validatePassword(password: String): String? {
        if (password.isBlank()) return "Password cannot be empty"
        if (password.length < 6) return "Password must be at least 6 characters"
        return null
    }

    fun validatePasswordConfirmation(password: String, confirm: String): String? {
        if (confirm.isBlank()) return "Please confirm your password"
        if (password != confirm) return "Passwords do not match"
        return null
    }
}
```

#### `AuthViewModel.kt`
```kotlin
package com.example.refscan.ui.auth

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.refscan.domain.AuthRepository
import com.google.firebase.FirebaseNetworkException
import com.google.firebase.auth.*
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.launch

class AuthViewModel(private val authRepository: AuthRepository) : ViewModel() {

    private val _uiState = MutableStateFlow(AuthUiState())
    val uiState = _uiState.asStateFlow()

    val isLoggedIn: StateFlow<Boolean> = authRepository.authState
        .map { it != null }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = authRepository.getCurrentUser() != null
        )

    val currentUserEmail: String?
        get() = authRepository.getCurrentUser()?.email

    fun onEmailChanged(email: String) {
        _uiState.update { it.copy(email = email, emailError = null, generalError = null) }
    }

    fun onPasswordChanged(password: String) {
        _uiState.update { it.copy(password = password, passwordError = null, generalError = null) }
    }

    fun onConfirmPasswordChanged(confirm: String) {
        _uiState.update { it.copy(confirmPassword = confirm, confirmPasswordError = null, generalError = null) }
    }

    fun login() {
        val email = _uiState.value.email
        val password = _uiState.value.password

        val emailError = AuthValidator.validateEmail(email)
        val passwordError = AuthValidator.validatePassword(password)

        if (emailError != null || passwordError != null) {
            _uiState.update { it.copy(emailError = emailError, passwordError = passwordError) }
            return
        }

        _uiState.update { it.copy(isLoading = true, generalError = null) }

        viewModelScope.launch {
            authRepository.login(email, password).fold(
                onSuccess = { _uiState.update { it.copy(isLoading = false) } },
                onFailure = { ex ->
                    _uiState.update { it.copy(isLoading = false, generalError = mapFirebaseAuthException(ex)) }
                }
            )
        }
    }

    fun register() {
        val email = _uiState.value.email
        val password = _uiState.value.password
        val confirm = _uiState.value.confirmPassword

        val emailError = AuthValidator.validateEmail(email)
        val passwordError = AuthValidator.validatePassword(password)
        val confirmError = AuthValidator.validatePasswordConfirmation(password, confirm)

        if (emailError != null || passwordError != null || confirmError != null) {
            _uiState.update {
                it.copy(emailError = emailError, passwordError = passwordError, confirmPasswordError = confirmError)
            }
            return
        }

        _uiState.update { it.copy(isLoading = true, generalError = null) }

        viewModelScope.launch {
            authRepository.register(email, password).fold(
                onSuccess = { _uiState.update { it.copy(isLoading = false) } },
                onFailure = { ex ->
                    _uiState.update { it.copy(isLoading = false, generalError = mapFirebaseAuthException(ex)) }
                }
            )
        }
    }

    fun logout() {
        viewModelScope.launch {
            authRepository.logout()
            _uiState.update { AuthUiState() }
        }
    }

    private fun mapFirebaseAuthException(e: Throwable): String {
        return when (e) {
            is FirebaseAuthInvalidUserException -> "No account found with this email."
            is FirebaseAuthInvalidCredentialsException -> "Invalid email or password."
            is FirebaseAuthUserCollisionException -> "An account already exists with this email."
            is FirebaseAuthWeakPasswordException -> "The password is too weak."
            is FirebaseNetworkException -> "Network error. Please check your connection."
            else -> e.localizedMessage ?: "An unknown error occurred."
        }
    }
}
```

---

## Phase 6 — Micro-Retrospective ("Retro – Lab 1")

### 1. What Went Well
- The 3-layer architecture cleanly decoupled pure Kotlin validation (`AuthValidator`) from UI composables and Firebase SDK calls.
- `callbackFlow` listener provided reactive, real-time auth state updates directly to Jetpack Compose navigation.
- Modern Gradle version catalog (`libs.versions.toml`) streamlined dependency management.

### 2. What Did Not Go Well
- Initial Gradle build issues due to Kotlin 2.0 Compose compiler plugin requirements and missing SDK platform dependencies.
- Initial missing `google-services.json` file blocked the Google Services Gradle task.

### 3. What We Will Change / Action Items for Lab 2
1. Integrate Cloud Firestore SDK in the Data Layer to persist user profile details (`users` collection) upon successful registration.
2. Build unit tests for `AuthValidator` and `AuthViewModel` using JUnit and Kotlin Coroutines Test utilities.
3. Enhance UI styling with Material 3 design tokens and dynamic color schemes.

---
*Report generated and formatted for Lab 1 submission • RefScan Android App • Student ID: 57322 • Account: fatehqasanov@gmail.com*
