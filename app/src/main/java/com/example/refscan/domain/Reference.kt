package com.example.refscan.domain

import com.google.firebase.Timestamp
import com.google.firebase.firestore.DocumentId
import com.google.firebase.firestore.ServerTimestamp

data class Reference(
    @DocumentId val id: String = "",
    val ownerId: String = "",
    val projectId: String = "",
    val projectName: String = "",
    val note: String = "",
    val colorHex: String = "#1A2B3C",
    val rating: Int = 3,
    val status: String = "active",
    @ServerTimestamp val createdAt: Timestamp? = null,
    @ServerTimestamp val updatedAt: Timestamp? = null
)

data class ReferenceInput(
    val projectId: String = "",
    val projectName: String = "",
    val note: String = "",
    val colorHex: String = "#1A2B3C",
    val rating: Int = 3,
    val status: String = "active"
)