package com.example.refscan.ui.reference

import com.example.refscan.domain.Reference

data class ReferenceListUiState(
    val references: List<Reference> = emptyList(),
    val searchQuery: String = "",
    val statusFilter: String = "all", // "all", "active", "archived"
    val isLoading: Boolean = true,
    val error: String? = null
) {
    // Pure logic: computed statistics header (E7)
    val activeCount: Int get() = references.count { it.status == "active" }
    val archivedCount: Int get() = references.count { it.status == "archived" }
    val statsSummary: String get() = "$activeCount active · $archivedCount archived"

    // Pure logic: filtered list based on search and status (E1, E5)
    val filteredReferences: List<Reference>
        get() = references.filter { ref ->
            val matchesStatus = when (statusFilter) {
                "active" -> ref.status == "active"
                "archived" -> ref.status == "archived"
                else -> true
            }
            val matchesSearch = if (searchQuery.isBlank()) {
                true
            } else {
                ref.note.contains(searchQuery, ignoreCase = true) ||
                        ref.projectName.contains(searchQuery, ignoreCase = true)
            }
            matchesStatus && matchesSearch
        }
}