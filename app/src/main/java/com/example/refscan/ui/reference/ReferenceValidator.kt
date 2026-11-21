package com.example.refscan.ui.reference

object ReferenceValidator {
    private val HEX_COLOR_REGEX = "^#[0-9A-Fa-f]{6}\$".toRegex()

    fun validateProject(projectId: String): String? {
        if (projectId.isBlank()) return "Please select a target game project"
        return null
    }

    fun validateNote(note: String): String? {
        if (note.isBlank()) return "Note cannot be empty"
        if (note.length > 200) return "Maximum 200 characters allowed"
        return null
    }

    fun validateColorHex(colorHex: String): String? {
        if (colorHex.isBlank()) return "Color hex code is required"
        if (!HEX_COLOR_REGEX.matches(colorHex)) return "Format must be valid Hex (e.g. #1A2B3C)"
        return null
    }

    fun validateRating(rating: Int): String? {
        if (rating < 1 || rating > 5) return "Rating must be between 1 and 5 stars"
        return null
    }

    // Cross-field validation rule
    fun validateCrossField(projectId: String, note: String): String? {
        if (projectId.isNotBlank() && note.trim().length < 5) {
            return "Please provide a descriptive note (min 5 chars) for the selected project"
        }
        return null
    }
}