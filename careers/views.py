from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

    @extend_schema(
        summary="Listar todos os Posts",
        description="Retorna uma lista de todos os posts existentes, ordenados do mais recente para o mais antigo.",
        responses={
            200: OpenApiResponse(response=PostSerializer(many=True), description="Lista de posts retornada com sucesso."),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Criar um novo Post",
        description="Cria um novo objeto de post com os dados fornecidos pelo usuário.",
        responses={
            201: OpenApiResponse(response=PostSerializer, description="Post criado com sucesso."),
            400: OpenApiResponse(description="Dados inválidos foram enviados."),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Obter um Post específico",
        description="Retorna os detalhes de um post específico, buscando pelo seu ID numérico.",
        responses={
            200: OpenApiResponse(response=PostSerializer, description="Detalhes do post retornados com sucesso."),
            404: OpenApiResponse(description="Post não encontrado."),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Atualizar um Post (parcialmente)",
        description="Atualiza um ou mais campos (título e/ou conteúdo) de um post existente.",
        responses={
            200: OpenApiResponse(response=PostSerializer, description="Post atualizado com sucesso."),
            400: OpenApiResponse(description="Dados inválidos foram enviados."),
            404: OpenApiResponse(description="Post não encontrado."),
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Deletar um Post",
        description="Remove permanentemente um post do banco de dados.",
        responses={
            204: OpenApiResponse(response=None, description="Post deletado com sucesso. Nenhum conteúdo retornado."),
            404: OpenApiResponse(description="Post não encontrado."),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)