from django.views.generic import ListView, DetailView

from .models import Product


class GameListView(ListView):
    template_name = "games/game_list.html"
    model = Product
    paginate_by = 8
    context_object_name = "games"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(category="Hry | PC").order_by("title")

        return data


class GameDetailView(DetailView):
    template_name = "games/game_detail.html"
    model = Product
    context_object_name = "game"
