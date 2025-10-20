from django.contrib import admin
from django.urls import path
from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
    TodoReopenView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # 1. Coloque a lista de tarefas no caminho raiz
    path("", TodoListView.as_view(), name="todo_list"),
    # 2. Mantenha o create
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>/", TodoCompleteView.as_view(), name="todo_complete"),
    path("reopen/<int:pk>/", TodoReopenView.as_view(), name="todo_reopen"),
]
