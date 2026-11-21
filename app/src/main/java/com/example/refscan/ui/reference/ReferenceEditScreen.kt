package com.example.refscan.ui.reference

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.refscan.domain.Project

@Composable
fun ReferenceEditScreen(
    viewModel: ReferenceEditViewModel,
    onDone: () -> Unit
) {
    val uiState by viewModel.uiState.collectAsState()

    LaunchedEffect(uiState.isSaved) {
        if (uiState.isSaved) {
            onDone()
        }
    }

    ReferenceEditContent(
        uiState = uiState,
        onProjectSelected = viewModel::onProjectSelected,
        onNoteChanged = viewModel::onNoteChanged,
        onColorHexChanged = viewModel::onColorHexChanged,
        onRatingChanged = viewModel::onRatingChanged,
        onStatusChanged = viewModel::onStatusChanged,
        onSaveClicked = viewModel::save,
        onBackClicked = onDone
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReferenceEditContent(
    uiState: ReferenceEditUiState,
    onProjectSelected: (Project) -> Unit,
    onNoteChanged: (String) -> Unit,
    onColorHexChanged: (String) -> Unit,
    onRatingChanged: (Int) -> Unit,
    onStatusChanged: (String) -> Unit,
    onSaveClicked: () -> Unit,
    onBackClicked: () -> Unit
) {
    var dropdownExpanded by remember { mutableStateOf(false) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(if (uiState.referenceId == null) "Create Material Reference" else "Edit Reference") },
                navigationIcon = {
                    IconButton(onClick = onBackClicked) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer,
                    titleContentColor = MaterialTheme.colorScheme.onPrimaryContainer
                )
            )
        }
    ) { padding ->
        if (uiState.isLoading) {
            Surface(modifier = Modifier.fillMaxSize()) {
                Column(
                    modifier = Modifier.fillMaxSize(),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    CircularProgressIndicator()
                }
            }
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .padding(16.dp)
                    .verticalScroll(rememberScrollState())
            ) {
                // Project Selector (Reference Collection Dropdown)
                Text("Target Game Project", style = MaterialTheme.typography.labelLarge, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(4.dp))
                
                OutlinedTextField(
                    value = uiState.selectedProjectName.ifEmpty { "Select Project..." },
                    onValueChange = {},
                    readOnly = true,
                    enabled = false,
                    isError = uiState.projectError != null,
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { dropdownExpanded = true }
                )
                
                DropdownMenu(
                    expanded = dropdownExpanded,
                    onDismissRequest = { dropdownExpanded = false }
                ) {
                    uiState.projects.forEach { project ->
                        DropdownMenuItem(
                            text = { Text("${project.title} (${project.engine})") },
                            onClick = {
                                onProjectSelected(project)
                                dropdownExpanded = false
                            }
                        )
                    }
                }
                
                if (uiState.projectError != null) {
                    Text(uiState.projectError, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall)
                }

                Spacer(modifier = Modifier.height(16.dp))

                // Material Note Input
                OutlinedTextField(
                    value = uiState.note,
                    onValueChange = onNoteChanged,
                    label = { Text("Material Reference Note") },
                    placeholder = { Text("e.g. Wet asphalt roughness & puddle reflection") },
                    isError = uiState.noteError != null || uiState.crossFieldError != null,
                    modifier = Modifier.fillMaxWidth(),
                    minLines = 3
                )
                if (uiState.noteError != null) {
                    Text(uiState.noteError, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall)
                }

                Spacer(modifier = Modifier.height(16.dp))

                // Color Hex Code Input
                OutlinedTextField(
                    value = uiState.colorHex,
                    onValueChange = onColorHexChanged,
                    label = { Text("Surface Color Hex Code (#RRGGBB)") },
                    placeholder = { Text("#1A2B3C") },
                    isError = uiState.colorHexError != null,
                    modifier = Modifier.fillMaxWidth(),
                    singleLine = true
                )
                if (uiState.colorHexError != null) {
                    Text(uiState.colorHexError, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall)
                }

                Spacer(modifier = Modifier.height(16.dp))

                // Rating Picker (1-5 stars)
                Text("Texture Importance Rating", style = MaterialTheme.typography.labelLarge, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(4.dp))
                Row(verticalAlignment = Alignment.CenterVertically) {
                    (1..5).forEach { star ->
                        IconButton(onClick = { onRatingChanged(star) }) {
                            Icon(
                                Icons.Default.Star,
                                contentDescription = "$star stars",
                                tint = if (star <= uiState.rating) Color(0xFFFFB800) else Color.LightGray,
                                modifier = Modifier.size(32.dp)
                            )
                        }
                    }
                }
                if (uiState.ratingError != null) {
                    Text(uiState.ratingError, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall)
                }

                Spacer(modifier = Modifier.height(16.dp))

                // Status Chips
                Text("Reference Status", style = MaterialTheme.typography.labelLarge, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(4.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    FilterChip(
                        selected = uiState.status == "active",
                        onClick = { onStatusChanged("active") },
                        label = { Text("Active") }
                    )
                    FilterChip(
                        selected = uiState.status == "archived",
                        onClick = { onStatusChanged("archived") },
                        label = { Text("Archived") }
                    )
                }

                // Cross-field error display
                if (uiState.crossFieldError != null) {
                    Spacer(modifier = Modifier.height(16.dp))
                    Text(uiState.crossFieldError, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall)
                }

                // General Error
                if (uiState.generalError != null) {
                    Spacer(modifier = Modifier.height(16.dp))
                    Text(uiState.generalError, color = MaterialTheme.colorScheme.error)
                }

                Spacer(modifier = Modifier.height(32.dp))

                Button(
                    onClick = onSaveClicked,
                    enabled = !uiState.isSaving,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    if (uiState.isSaving) {
                        CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.onPrimary)
                    } else {
                        Text(if (uiState.referenceId == null) "Create Reference" else "Update Reference")
                    }
                }
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun ReferenceEditPreview() {
    MaterialTheme {
        ReferenceEditContent(
            uiState = ReferenceEditUiState(
                selectedProjectName = "Cyberpunk Alley Level",
                note = "Wet asphalt roughness & puddle reflection",
                colorHex = "#1A2B3C",
                rating = 4,
                status = "active",
                projects = listOf(Project("1", "Cyberpunk Alley Level", "Unreal Engine 5"))
            ),
            onProjectSelected = {},
            onNoteChanged = {},
            onColorHexChanged = {},
            onRatingChanged = {},
            onStatusChanged = {},
            onSaveClicked = {},
            onBackClicked = {}
        )
    }
}