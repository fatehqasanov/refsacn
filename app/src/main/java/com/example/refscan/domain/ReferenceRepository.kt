package com.example.refscan.domain

import kotlinx.coroutines.flow.Flow

interface ReferenceRepository {
    fun observeMyReferences(): Flow<List<Reference>>
    suspend fun getReference(id: String): Result<Reference>
    suspend fun getProjects(): Result<List<Project>>
    suspend fun addReference(input: ReferenceInput): Result<String>
    suspend fun updateReference(id: String, input: ReferenceInput): Result<Unit>
    suspend fun deleteReference(id: String): Result<Unit>
}