package com.example.refscan.ui.auth

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.refscan.domain.AuthRepository
import com.google.firebase.FirebaseNetworkException
import com.google.firebase.auth.FirebaseAuthInvalidCredentialsException
import com.google.firebase.auth.FirebaseAuthInvalidUserException
import com.google.firebase.auth.FirebaseAuthUserCollisionException
import com.google.firebase.auth.FirebaseAuthWeakPasswordException
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.flow.update
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
            _uiState.update {
                it.copy(emailError = emailError, passwordError = passwordError)
            }
            return
        }

        _uiState.update { it.copy(isLoading = true, generalError = null) }

        viewModelScope.launch {
            authRepository.login(email, password).fold(
                onSuccess = {
                    _uiState.update { it.copy(isLoading = false) }
                },
                onFailure = { exception ->
                    val errorMessage = mapFirebaseAuthException(exception)
                    _uiState.update { it.copy(isLoading = false, generalError = errorMessage) }
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
                it.copy(
                    emailError = emailError,
                    passwordError = passwordError,
                    confirmPasswordError = confirmError
                )
            }
            return
        }

        _uiState.update { it.copy(isLoading = true, generalError = null) }

        viewModelScope.launch {
            authRepository.register(email, password).fold(
                onSuccess = {
                    _uiState.update { it.copy(isLoading = false) }
                },
                onFailure = { exception ->
                    val errorMessage = mapFirebaseAuthException(exception)
                    _uiState.update { it.copy(isLoading = false, generalError = errorMessage) }
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
    
    val currentUserEmail: String?
        get() = authRepository.getCurrentUser()?.email

    fun clearErrors() {
        _uiState.update { it.copy(emailError = null, passwordError = null, confirmPasswordError = null, generalError = null) }
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