from django.db import models

# models 모듈의 Model 클래스를 확장하여 만든 클래스 #p.150
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)  #월,일,시,분,초를 자동으로 기록할 수 있게 해주는 필드
    updated_at = models.DateTimeField(auto_now=True)    #게시물 수정 시 수정 시각 저장

    #포스트의 제목과 번호를 출력하기
    # 포스트를 생성하면 pk의 값이 포스트에 부여됨 #p.153
    def __str__(self):
        return f'[{self.pk}]{self.title}'
