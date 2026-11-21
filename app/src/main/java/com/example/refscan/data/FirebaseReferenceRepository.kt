package com.example.refscan.data

import com.example.refscan.domain.Project
import com.example.refscan.domain.Reference
import com.example.refscan.domain.ReferenceInput
import com.example.refscan.domain.ReferenceRepository
import com.google.firebase.Firebase
import com.google.firebase.auth.auth
import com.google.firebase.firestore.FieldValue
import com.google.firebase.firestore.firestore
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.tasks.await

class FirebaseReferenceRepository : ReferenceRepository {
    private val db = Firebase.firestore
    private val auth = Firebase.auth

    private fun requireUid(): String {
        return auth.currentUser?.uid ?: throw IllegalStateException("User not authenticated")
    }

    override fun observeMyReferences(): Flow<List<Reference>> = callbackFlow {
        val uid = auth.currentUser?.uid
        if (uid == null) {
            trySend(emptyList())
            close()
            return@callbackFlow
        }

        val registration = db.collection("references")
            .whereEqualTo("ownerId", uid)
            .addSnapshotListener { snapshot, error ->
                if (error != null) {
                    close(error)
                    return@addSnapshotListener
                }
                if (snapshot != null) {
                    val list = snapshot.toObjects(Reference::class.java)
                    trySend(list)
                }
            }

        awaitClose {
            registration.remove()
        }
    }

    override suspend fun getReference(id: String): Result<Reference> = runCatching {
        val doc = db.collection("references").document(id).get().await()
        doc.toObject(Reference::class.java) ?: throw NoSuchElementException("Reference not found")
    }

    override suspend fun getProjects(): Result<List<Project>> = runCatching {
        val snapshot = db.collection("projects").get().await()
        if (snapshot.isEmpty) {
            // Seed reference collection data if empty
            listOf(
                Project("proj_1", "Cyberpunk Alley Level", "Unreal Engine 5"),
                Project("proj_2", "Overgrown Ruin Environment", "Unity"),
                Project("proj_3", "Medieval Castle Interior", "Unreal Engine 5")
            )
        } else {
            snapshot.toObjects(Project::class.java)
        }
    }

    override suspend fun addReference(input: ReferenceInput): Result<String> = runCatching {
        val uid = requireUid()
        val data = hashMapOf(
            "ownerId" to uid,
            "projectId" to input.projectId,
            "projectName" to input.projectName,
            "note" to input.note,
            "colorHex" to input.colorHex,
            "rating" to input.rating,
            "status" to input.status,
            "createdAt" to FieldValue.serverTimestamp(),
            "updatedAt" to FieldValue.serverTimestamp()
        )
        val ref = db.collection("references").add(data).await()
        ref.id
    }

    override suspend fun updateReference(id: String, input: ReferenceInput): Result<Unit> = runCatching {
        val data = mapOf(
            "projectId" to input.projectId,
            "projectName" to input.projectName,
            "note" to input.note,
            "colorHex" to input.colorHex,
            "rating" to input.rating,
            "status" to input.status,
            "updatedAt" to FieldValue.serverTimestamp()
        )
        db.collection("references").document(id).update(data).await()
    }

    override suspend fun deleteReference(id: String): Result<Unit> = runCatching {
        db.collection("references").document(id).delete().await()
    }
}