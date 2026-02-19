from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from core.models import Comment
import json

# render the main page
def home(request):
    return render(request, 'core/home.html')

# handle the api of messege (get list,create messege,delete the messege)
def comments_api(request):
    if request.method == "GET":
        # 取得留言，倒序排列
        comments = Comment.objects.order_by("-created_at")
        # 將 QuerySet 轉成可 JSON 化的 list
        data = []
        for c in comments:
            data.append({
                "id": c.id,
                "author": c.author,
                "content": c.content,
                "created_at": c.created_at.isoformat(),
            })
        return JsonResponse({"comments": data}, json_dumps_params={'ensure_ascii': False})

    elif request.method == "POST":
        # 前端要帶 CSRF token
        body = json.loads(request.body)
        Comment.objects.create(
            author=body.get("author", "Anonymous"),
            content=body.get("content", "")
        )
        return JsonResponse({"status": "ok"})

    elif request.method == "DELETE":
        body = json.loads(request.body)
        comment_id = body.get("id")
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({"status": "deleted"})
        except Comment.DoesNotExist:
            return JsonResponse({"status": "not found"}, status=404)

    return JsonResponse({"error": "method not allowed"}, status=405)
