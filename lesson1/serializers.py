from rest_framework import serializers

from lesson1.models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'id name age course'.split()


class CourseSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = 'id name grade university count'.split()

    def get_count(self, obj):
        count = Student.objects.filter(course_id=obj.id).count()
        return count