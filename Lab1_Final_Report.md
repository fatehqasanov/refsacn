# Lab 1 Final Report: Walking Skeleton & Firebase Authentication

**Course:** Mobile Application in the Cloud — Lab 1  
**App Name:** RefScan  
**Student Name:** Fateh Hasanlı  
**Student ID:** 57322  
**Role:** Solo Developer (PO, Tech Lead, Developer, QA/DevOps)  
**Tech Stack:** Kotlin · Jetpack Compose · Firebase Authentication · Cloud Firestore · Git/GitHub  

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

## Phase 1 — Team & Roles

Since this is a solo-developer project, all responsibilities across product, architecture, implementation, and quality assurance are managed individually:

| Role | Responsibility | Assigned Person |
| :--- | :--- | :--- |
| **Product Owner (PO)** | Product vision, problem statement, user story writing, and backlog prioritization. | Fateh Hasanlı (ID: 57322) |
| **Tech Lead** | Architecture design, data model specification, state management, and Firebase setup. | Fateh Hasanlı (ID: 57322) |
| **Developer** | Kotlin & Jetpack Compose implementation, UI screens, ViewModel, and Firebase Auth calls. | Fateh Hasanlı (ID: 57322) |
| **QA / DevOps** | Git configuration, branch protection, pull request reviews, and board management. | Fateh Hasanlı (ID: 57322) |

---

## Phase 2 — Product Definition & Cloud Data Model

### 1. Problem Statement
> *"Game artists and level designers walking outside or traveling cannot use desktop task managers to instantly capture, tag, and organize real-world material textures and color references for their active game projects."*

### 2. MVP Features & Sprint Breakdown
- **User Authentication (Sprint 1 - Complete):** Register, Log In, Log Out, and Auto-Login session persistence using Firebase Authentication.
- **Project List Screen (Sprint 1):** View and manage active game projects or environmental levels.
- **Reference Detail & Edit Screen (Sprint 1):** View, add, and update real-world notes, material tags, and color hex codes linked to a project.
- **Camera & Cloud Storage Upload (Sprint 3 / Later):** Capture direct photo references using the phone camera and sync to Firebase Cloud Storage.

### 3. Cloud Firestore Data Model (Max 3 Collections)

```
[users] (Collection)
 └── uid (Doc ID - String matching Firebase Auth UID)
      ├── email: String
      ├── displayName: String
      └── createdAt: Timestamp

[projects] (Collection)
 └── projectId (Doc ID - String)
      ├── ownerId: String (foreign key -> users.uid)
      ├── title: String
      ├── engine: String
      └── createdAt: Timestamp

[references] (Collection)
 └── referenceId (Doc ID - String)
      ├── projectId: String (foreign key -> projects.projectId)
      ├── ownerId: String (foreign key -> users.uid)
      ├── note: String
      ├── colorHex: String
      └── createdAt: Timestamp
```

---

## Phase 3 — Repository Architecture & Workflow Setup

### 1. GitHub Board Columns & Workflow
- **Columns:** `Backlog` | `Sprint 1` | `In Progress` | `In Review` | `Done`
- **Automation:** Issues automatically move to `Done` upon merging linked Pull Requests.

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

## Layer-by-Layer Code Structure & Snippets

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

#### `AuthValidator.kt` (Pure Kotlin Validation)
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

#### `AuthUiState.kt`
```kotlin
package com.example.refscan.ui.auth

data class AuthUiState(
    val email: String = "",
    val password: String = "",
    val confirmPassword: String = "",
    val emailError: String? = null,
    val passwordError: String? = null,
    val confirmPasswordError: String? = null,
    val generalError: String? = null,
    val isLoading: Boolean = false
)
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

### 3. UI Layer & Navigation (`com.example.refscan.ui.navigation`)

#### `AppNavHost.kt`
```kotlin
package com.example.refscan.ui.navigation

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.refscan.ui.auth.AuthViewModel
import com.example.refscan.ui.auth.LoginScreen
import com.example.refscan.ui.auth.RegisterScreen
import com.example.refscan.ui.home.HomeScreen

@Composable
fun AppNavHost(viewModel: AuthViewModel) {
    val navController = rememberNavController()
    val isLoggedIn by viewModel.isLoggedIn.collectAsState()

    LaunchedEffect(isLoggedIn) {
        if (isLoggedIn) {
            navController.navigate("home") {
                popUpTo(0) { inclusive = true }
            }
        } else {
            navController.navigate("login") {
                popUpTo(0) { inclusive = true }
            }
        }
    }

    NavHost(
        navController = navController,
        startDestination = if (isLoggedIn) "home" else "login"
    ) {
        composable("login") {
            LoginScreen(
                viewModel = viewModel,
                onNavigateToRegister = { navController.navigate("register") }
            )
        }
        composable("register") {
            RegisterScreen(
                viewModel = viewModel,
                onNavigateToLogin = {
                    navController.navigate("login") { popUpTo("login") { inclusive = true } }
                }
            )
        }
        composable("home") {
            HomeScreen(viewModel = viewModel)
        }
    }
}
```

---

## UI Screenshots & Screen Wireframe Representations

### 1. Login Screen
- **Components:** App Logo / Title, Email Text Field (`KeyboardType.Email`), Masked Password Text Field (`PasswordVisualTransformation`), "Log in" Button with `CircularProgressIndicator` during loading, "No account? Register" text link, and error message text.

```
+-------------------------------------------------------+
|                       RefScan                         |
|                       Log In                          |
|                                                       |
|  [ Email Address                            ]         |
|  [ Password (••••••••)                      ]         |
|                                                       |
|  [                   LOG IN                         ] |
|                                                       |
|                 No account? Register                  |
+-------------------------------------------------------+
```

### 2. Register Screen
- **Components:** Registration Title, Email Field, Password Field, Confirm Password Field, field-level error messages below each input, "Create account" Loading Button, and link back to Login.

```
+-------------------------------------------------------+
|                      Register                         |
|                                                       |
|  [ Email Address                            ]         |
|  [ Password                                 ]         |
|  [ Confirm Password                         ]         |
|                                                       |
|  [               CREATE ACCOUNT                     ] |
|                                                       |
|            Already have an account? Log in            |
+-------------------------------------------------------+
```

### 3. Home Screen (Authenticated Session)
- **Components:** Title "RefScan", user session greeting (`Logged in as <email>`), and "Log out" button.

```
+-------------------------------------------------------+
|                       RefScan                         |
|                                                       |
|            Logged in as student@polsl.pl              |
|                                                       |
|  [                  LOG OUT                         ] |
+-------------------------------------------------------+
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
*Report generated and formatted for Lab 1 submission • RefScan Android App • Student ID: 57322*
