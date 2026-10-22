package com.example.refscan.ui.home

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.refscan.ui.auth.AuthViewModel

@Composable
fun HomeScreen(
    viewModel: AuthViewModel
) {
    HomeScreenContent(
        userEmail = viewModel.currentUserEmail ?: "Unknown User",
        onLogoutClicked = viewModel::logout
    )
}

@Composable
fun HomeScreenContent(
    userEmail: String,
    onLogoutClicked: () -> Unit
) {
    Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(24.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(text = "RefScan", style = MaterialTheme.typography.displayMedium, color = MaterialTheme.colorScheme.primary)

            Spacer(modifier = Modifier.height(16.dp))

            Text(text = "Logged in as $userEmail", style = MaterialTheme.typography.headlineSmall)

            Spacer(modifier = Modifier.height(32.dp))

            Button(onClick = onLogoutClicked) {
                Text("Log out")
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun HomeScreenPreview() {
    MaterialTheme {
        HomeScreenContent(
            userEmail = "fatehqasanov@gmail.com",
            onLogoutClicked = {}
        )
    }
}