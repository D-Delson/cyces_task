from rest_framework import serializers

class DashBoardSerializer(serializers.Serializer):
    total_applications = serializers.IntegerField()
    total_job_posts = serializers.IntegerField()