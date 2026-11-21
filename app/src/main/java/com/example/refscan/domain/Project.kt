package com.example.refscan.domain

import com.google.firebase.firestore.DocumentId

data class Project(
    @DocumentId val id: String = "",
    val title: String = "",
    val engine: String = ""
)