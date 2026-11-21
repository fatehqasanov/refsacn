package com.example.refscan.ui.reference

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.refscan.domain.Project
import com.example.refscan.domain.ReferenceInput
import com.example.refscan.domain.ReferenceRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class ReferenceEditViewModel(
    private val referenceId: String?,
    private val repository: ReferenceRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(ReferenceEditUiState(referenceId = referenceId))
    val uiState: StateFlow<ReferenceEditUiState> = _uiState.asStateFlow()

    init {
        loadProjects()
        if (referenceId != null) {
            loadReference(referenceId)
        }
    }

    private fun loadProjects() {
        viewModelScope.launch {
            repository.getProjects().fold(
                onSuccess = { projects ->
                    _uiState.update { it.copy(projects = projects) }
                },
                onFailure = { /* ignore or default */ }
            )
        }
    }

    private fun loadReference(id: String) {
        _uiState.update { it.copy(isLoading = true) }
        viewModelScope.launch {
            repository.getReference(id).fold(
                onSuccess = { ref ->
                    _uiState.update {
                        it.copy(
                            isLoading = false,
                            selectedProjectId = ref.projectId,
                            selectedProjectName = ref.projectName,
                            note = ref.note,
                            colorHex = ref.colorHex,
                            rating = ref.rating,
                            status = ref.status
                        )
                    }
                },
                onFailure = { e ->
                    _uiState.update { it.copy(isLoading = false, generalError = e.localizedMessage) }
                }
            )
        }
    }

    fun onProjectSelected(project: Project) {
        _uiState.update {
            it.copy(
                selectedProjectId = project.id,
                selectedProjectName = project.title,
                projectError = null,
                crossFieldError = null
            )
        }
    }

    fun onNoteChanged(note: String) {
        _uiState.update { it.copy(note = note, noteError = null, crossFieldError = null) }
    }

    fun onColorHexChanged(hex: String) {
        _uiState.update { it.copy(colorHex = hex, colorHexError = null) }
    }

    fun onRatingChanged(rating: Int) {
        _uiState.update { it.copy(rating = rating, ratingError = null) }
    }

    fun onStatusChanged(status: String) {
        _uiState.update { it.copy(status = status) }
    }

    fun save() {
        val state = _uiState.value

        val projectErr = ReferenceValidator.validateProject(state.selectedProjectId)
        val noteErr = ReferenceValidator.validateNote(state.note)
        val colorHexErr = ReferenceValidator.validateColorHex(state.colorHex)
        val ratingErr = ReferenceValidator.validateRating(state.rating)
        val crossErr = ReferenceValidator.validateCrossField(state.selectedProjectId, state.note)

        if (projectErr != null || noteErr != null || colorHexErr != null || ratingErr != null || crossErr != null) {
            _uiState.update {
                it.copy(
                    projectError = projectErr,
                    noteError = noteErr,
                    colorHexError = colorHexErr,
                    ratingError = ratingErr,
                    crossFieldError = crossErr
                )
            }
            return
        }

        _uiState.update { it.copy(isSaving = true, generalError = null) }

        val input = ReferenceInput(
            projectId = state.selectedProjectId,
            projectName = state.selectedProjectName,
            note = state.note,
            colorHex = state.colorHex,
            rating = state.rating,
            status = state.status
        )

        viewModelScope.launch {
            val result = if (referenceId == null) {
                repository.addReference(input).map { }
            } else {
                repository.updateReference(referenceId, input)
            }

            result.fold(
                onSuccess = {
                    _uiState.update { it.copy(isSaving = false, isSaved = true) }
                },
                onFailure = { e ->
                    _uiState.update { it.copy(isSaving = false, generalError = e.localizedMessage) }
                }
            )
        }
    }
}