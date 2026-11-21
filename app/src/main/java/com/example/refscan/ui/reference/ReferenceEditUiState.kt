package com.example.refscan.ui.reference

import com.example.refscan.domain.Project

data class ReferenceEditUiState(
    val referenceId: String? = null,
    val selectedProjectId: String = "",
    val selectedProjectName: String = "",
    val note: String = "",
    val colorHex: String = "#1A2B3C",
    val rating: Int = 3,
    val status: String = "active",
    val projects: List<Project> = emptyList(),
    
    val projectError: String? = null,
    val noteError: String? = null,
    val colorHexError: String? = null,
    val ratingError: String? = null,
    val crossFieldError: String? = null,
    val generalError: String? = null,
    
    val isLoading: Boolean = false,
    val isSaving: Boolean = false,
    val isSaved: Boolean = false
)