package com.example.refscan.ui.reference

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.refscan.domain.ReferenceRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class ReferenceListViewModel(
    private val repository: ReferenceRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(ReferenceListUiState())
    val uiState: StateFlow<ReferenceListUiState> = _uiState.asStateFlow()

    init {
        observeReferences()
    }

    private fun observeReferences() {
        viewModelScope.launch {
            repository.observeMyReferences()
                .catch { e ->
                    _uiState.update { it.copy(isLoading = false, error = e.localizedMessage) }
                }
                .collect { list ->
                    _uiState.update { it.copy(references = list, isLoading = false, error = null) }
                }
        }
    }

    fun onSearchQueryChanged(query: String) {
        _uiState.update { it.copy(searchQuery = query) }
    }

    fun clearSearch() {
        _uiState.update { it.copy(searchQuery = "") }
    }

    fun onStatusFilterChanged(status: String) {
        _uiState.update { it.copy(statusFilter = status) }
    }

    fun deleteReference(id: String) {
        viewModelScope.launch {
            repository.deleteReference(id)
        }
    }
}