
from rest_framework import status
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse



class CursosTestCase(APITestCase):
    
    def setUp(self):
        self.list_url =  reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1',
            descricao='Curso de Teste 1',
            nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2',
            descricao='Curso de Teste 2',
            nivel='I'
        )
        
    def test_listar_cursos(self):
        """
        Testa a funcionalidade de listar os cursos.

        Este caso de teste verifica se o endpoint da API para listar os cursos retorna uma resposta com um código de status 200. Ele também verifica se a resposta contém o número esperado de cursos.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    def test_criar_curso(self):
        """
        Testa a funcionalidade de criar um novo curso.

        Este caso de teste verifica se o endpoint da API para criar um novo curso retorna uma resposta com um código de status 201. Ele verifica se o curso foi criado com sucesso.
        """
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso de Teste 3',
            'nivel': 'A'
        }
        response = self.client.post(path=self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
           
    def test_excluir_curso(self):
        """
        Testa se a requisição DELETE não permitida pra curso.
        """
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_editar_curso(self):
        """
        Testa a funcionalidade de editar um curso existente.

        Este caso de teste verifica se o endpoint da API para editar um curso retorna uma resposta com um código de status 200. Ele verifica se o curso foi editado com sucesso.
        """
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso de Teste 1 alterado',
            'nivel': 'B'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.curso_1.refresh_from_db()
    