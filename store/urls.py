from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router=SimpleRouter()
router.register('products',views.ProductViewSet)
router.register('collections',views.CollectionViewSet)
router.urls

# URLConf
urlpatterns = router.urls