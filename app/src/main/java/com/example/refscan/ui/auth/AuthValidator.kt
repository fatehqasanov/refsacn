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