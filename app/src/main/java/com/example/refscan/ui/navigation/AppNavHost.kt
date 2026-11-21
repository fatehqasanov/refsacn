package com.example.refscan.ui.navigation

import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.example.refscan.data.FirebaseReferenceRepository
import com.example.refscan.ui.auth.AuthViewModel
import com.example.refscan.ui.auth.LoginScreen
import com.example.refscan.ui.auth.RegisterScreen
import com.example.refscan.ui.reference.ReferenceEditScreen
import com.example.refscan.ui.reference.ReferenceEditViewModel
import com.example.refscan.ui.reference.ReferenceListScreen
import com.example.refscan.ui.reference.ReferenceListViewModel

@Composable
fun AppNavHost(viewModel: AuthViewModel) {
    val navController = rememberNavController()
    val isLoggedIn by viewModel.isLoggedIn.collectAsState()
    val referenceRepository = remember { FirebaseReferenceRepository() }

    LaunchedEffect(isLoggedIn) {
        if (isLoggedIn) {
            navController.navigate("list") {
                popUpTo(0) { inclusive = true }
            }
        } else {
            navController.navigate("login") {
                popUpTo(0) { inclusive = true }
            }
        }
    }

    NavHost(
        navController = navController,
        startDestination = if (isLoggedIn) "list" else "login"
    ) {
        composable("login") {
            LoginScreen(
                viewModel = viewModel,
                onNavigateToRegister = {
                    navController.navigate("register")
                }
            )
        }
        composable("register") {
            RegisterScreen(
                viewModel = viewModel,
                onNavigateToLogin = {
                    navController.navigate("login") {
                        popUpTo("login") { inclusive = true }
                    }
                }
            )
        }
        composable("list") {
            val listViewModel: ReferenceListViewModel = viewModel {
                ReferenceListViewModel(referenceRepository)
            }
            ReferenceListScreen(
                viewModel = listViewModel,
                authViewModel = viewModel,
                onAddClicked = {
                    navController.navigate("edit")
                },
                onReferenceClicked = { id ->
                    navController.navigate("edit?id=$id")
                }
            )
        }
        composable(
            route = "edit?id={id}",
            arguments = listOf(navArgument("id") {
                type = NavType.StringType
                nullable = true
                defaultValue = null
            })
        ) { entry ->
            val id = entry.arguments?.getString("id")
            val editViewModel: ReferenceEditViewModel = viewModel {
                ReferenceEditViewModel(id, referenceRepository)
            }
            ReferenceEditScreen(
                viewModel = editViewModel,
                onDone = {
                    navController.popBackStack()
                }
            )
        }
    }
}