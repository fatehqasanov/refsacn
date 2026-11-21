package com.example.refscan.ui.reference

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.ExitToApp
import androidx.compose.material.icons.filled.Search
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp

import com.example.refscan.domain.Reference
import com.example.refscan.ui.auth.AuthViewModel

@Composable
fun ReferenceListScreen(
    viewModel: ReferenceListViewModel,
    authViewModel: AuthViewModel,
    onAddClicked: () -> Unit,
    onReferenceClicked: (String) -> Unit
) {
    val uiState by viewModel.uiState.collectAsState()

    ReferenceListContent(
        uiState = uiState,
        userEmail = authViewModel.currentUserEmail ?: "fatehqasanov@gmail.com",
        onSearchQueryChanged = viewModel::onSearchQueryChanged,
        onClearSearch = viewModel::clearSearch,
        onStatusFilterChanged = viewModel::onStatusFilterChanged,
        onAddClicked = onAddClicked,
        onReferenceClicked = onReferenceClicked,
        onDeleteReference = viewModel::deleteReference,
        onLogoutClicked = authViewModel::logout
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReferenceListContent(
    uiState: ReferenceListUiState,
    userEmail: String,
    onSearchQueryChanged: (String) -> Unit,
    onClearSearch: () -> Unit,
    onStatusFilterChanged: (String) -> Unit,
    onAddClicked: () -> Unit,
    onReferenceClicked: (String) -> Unit,
    onDeleteReference: (String) -> Unit,
    onLogoutClicked: () -> Unit
) {
    var itemToDelete by remember { mutableStateOf<Reference?>(null) }

    if (itemToDelete != null) {
        AlertDialog(
            onDismissRequest = { itemToDelete = null },
            title = { Text("Delete Reference?") },
            text = { Text("Are you sure you want to delete '${itemToDelete?.projectName}' reference note?") },
            confirmButton = {
                TextButton(onClick = {
                    itemToDelete?.let { onDeleteReference(it.id) }
                    itemToDelete = null
                }) {
                    Text("Delete", color = MaterialTheme.colorScheme.error)
                }
            },
            dismissButton = {
                TextButton(onClick = { itemToDelete = null }) {
                    Text("Cancel")
                }
            }
        )
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("RefScan Material References", fontWeight = FontWeight.Bold) },
                actions = {
                    IconButton(onClick = onLogoutClicked) {
                        Icon(Icons.Default.ExitToApp, contentDescription = "Log out")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer,
                    titleContentColor = MaterialTheme.colorScheme.onPrimaryContainer
                )
            )
        },
        floatingActionButton = {
            FloatingActionButton(onClick = onAddClicked, containerColor = MaterialTheme.colorScheme.primary) {
                Icon(Icons.Default.Add, contentDescription = "Add Reference")
            }
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(16.dp)
        ) {
            // E1: Search Input Bar
            OutlinedTextField(
                value = uiState.searchQuery,
                onValueChange = onSearchQueryChanged,
                placeholder = { Text("Search by note or level...") },
                leadingIcon = { Icon(Icons.Default.Search, contentDescription = null) },
                trailingIcon = {
                    if (uiState.searchQuery.isNotEmpty()) {
                        IconButton(onClick = onClearSearch) {
                            Icon(Icons.Default.Clear, contentDescription = "Clear search")
                        }
                    }
                },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true
            )

            Spacer(modifier = Modifier.height(12.dp))

            // E7: Statistics Header Card
            Card(
                modifier = Modifier.fillMaxWidth(),
                colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.secondaryContainer)
            ) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(16.dp),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Column {
                        Text(text = "Logged in: $userEmail", style = MaterialTheme.typography.labelMedium)
                        Text(text = "Total References: ${uiState.references.size}", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                    }
                    Text(
                        text = uiState.statsSummary,
                        style = MaterialTheme.typography.bodyMedium,
                        fontWeight = FontWeight.SemiBold,
                        color = MaterialTheme.colorScheme.primary
                    )
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // E5: Status Filter Chips
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                FilterChip(
                    selected = uiState.statusFilter == "all",
                    onClick = { onStatusFilterChanged("all") },
                    label = { Text("All (${uiState.references.size})") }
                )
                FilterChip(
                    selected = uiState.statusFilter == "active",
                    onClick = { onStatusFilterChanged("active") },
                    label = { Text("Active (${uiState.activeCount})") }
                )
                FilterChip(
                    selected = uiState.statusFilter == "archived",
                    onClick = { onStatusFilterChanged("archived") },
                    label = { Text("Archived (${uiState.archivedCount})") }
                )
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Content List / E3 Empty / Loading / Error States
            when {
                uiState.isLoading -> {
                    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                        CircularProgressIndicator()
                    }
                }
                uiState.error != null -> {
                    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                        Text(text = "Error: ${uiState.error}", color = MaterialTheme.colorScheme.error)
                    }
                }
                uiState.filteredReferences.isEmpty() -> {
                    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                        if (uiState.searchQuery.isNotEmpty()) {
                            Text(text = "No matching material references found for '${uiState.searchQuery}'", style = MaterialTheme.typography.bodyMedium)
                        } else {
                            Text(text = "No references added yet. Tap '+' to create your first texture log!", style = MaterialTheme.typography.bodyMedium)
                        }
                    }
                }
                else -> {
                    LazyColumn(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        items(uiState.filteredReferences) { item ->
                            ReferenceItemCard(
                                reference = item,
                                onClick = { onReferenceClicked(item.id) },
                                onDelete = { itemToDelete = item }
                            )
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun ReferenceItemCard(
    reference: Reference,
    onClick: () -> Unit,
    onDelete: () -> Unit
) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onClick() },
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
    ) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            // Color Badge Preview
            val defaultColor = MaterialTheme.colorScheme.primary
            val parsedColor = remember(reference.colorHex) {
                try {
                    val hex = reference.colorHex.removePrefix("#")
                    val colorInt = hex.toLong(16)
                    if (hex.length == 6) {
                        Color(colorInt or 0xFF000000)
                    } else {
                        defaultColor
                    }
                } catch (e: Exception) {
                    defaultColor
                }
            }

            Box(
                modifier = Modifier
                    .size(40.dp)
                    .background(parsedColor, shape = CircleShape)
            )

            Spacer(modifier = Modifier.width(16.dp))

            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = reference.projectName,
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.Bold
                )
                Text(
                    text = reference.note,
                    style = MaterialTheme.typography.bodyMedium,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
                Spacer(modifier = Modifier.height(4.dp))
                Row(verticalAlignment = Alignment.CenterVertically) {
                    repeat(reference.rating) {
                        Icon(
                            Icons.Default.Star,
                            contentDescription = null,
                            modifier = Modifier.size(14.dp),
                            tint = Color(0xFFFFB800)
                        )
                    }
                    Spacer(modifier = Modifier.width(8.dp))
                    Surface(
                        shape = RoundedCornerShape(4.dp),
                        color = if (reference.status == "active") MaterialTheme.colorScheme.primaryContainer else MaterialTheme.colorScheme.surfaceVariant
                    ) {
                        Text(
                            text = reference.status.uppercase(),
                            modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp),
                            style = MaterialTheme.typography.labelSmall
                        )
                    }
                }
            }

            IconButton(onClick = onDelete) {
                Icon(Icons.Default.Delete, contentDescription = "Delete item", tint = MaterialTheme.colorScheme.error)
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun ReferenceListPreview() {
    MaterialTheme {
        ReferenceListContent(
            uiState = ReferenceListUiState(
                references = listOf(
                    Reference("1", "uid", "p1", "Cyberpunk Alley Level", "Wet asphalt roughness & puddle reflection", "#1A2B3C", 5, "active"),
                    Reference("2", "uid", "p2", "Overgrown Ruin Environment", "Mossy stone brick normal map notes", "#2A7B3C", 4, "archived")
                ),
                isLoading = false
            ),
            userEmail = "fatehqasanov@gmail.com",
            onSearchQueryChanged = {},
            onClearSearch = {},
            onStatusFilterChanged = {},
            onAddClicked = {},
            onReferenceClicked = {},
            onDeleteReference = {},
            onLogoutClicked = {}
        )
    }
}