from django.contrib import admin
from .models import Post, Comment
# from .models import Post = import models.Post
# .models에서 post와 comment 모델을 불러온 거임.


# Register your models here.: 우리가 만든 모델을 추가해야 함.
admin.site.register(Post)
admin.site.register(Comment)

# .models에서 .은 같은 라인의 다른 파일 의미, ..은 상위폴더 의미