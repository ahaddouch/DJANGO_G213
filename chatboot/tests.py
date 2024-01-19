from django.test import TestCase
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone

class ChatModelTest(TestCase):
    def setUp(self):
        # Crée un utilisateur pour les tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_chat(self):
        # Teste la création d'un objet Chat
        chat = Chat.objects.create(user=self.user, message='Test message', response='Test response', created_at=timezone.now())
        
        # Vérifie que l'objet Chat a été créé correctement
        self.assertEqual(chat.user, self.user)
        self.assertEqual(chat.message, 'Test message')
        self.assertEqual(chat.response, 'Test response')

    def test_update_chat(self):
        # Crée un objet Chat pour les tests
        chat = Chat.objects.create(user=self.user, message='Initial message', response='Initial response', created_at=timezone.now())

        # Modifie l'objet Chat
        chat.message = 'Updated message'
        chat.response = 'Updated response'
        chat.save()

        # Récupère l'objet Chat depuis la base de données pour s'assurer que les modifications ont été enregistrées
        updated_chat = Chat.objects.get(pk=chat.pk)
        
        # Vérifie que l'objet Chat a été correctement mis à jour
        self.assertEqual(updated_chat.message, 'Updated message')
        self.assertEqual(updated_chat.response, 'Updated response')

    def test_delete_chat(self):
        # Crée un objet Chat pour les tests
        chat = Chat.objects.create(user=self.user, message='To be deleted', response='Delete me', created_at=timezone.now())

        # Supprime l'objet Chat
        chat.delete()

        # Vérifie que l'objet Chat a été correctement supprimé de la base de données
        with self.assertRaises(Chat.DoesNotExist):
            Chat.objects.get(pk=chat.pk)
