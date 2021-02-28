from rest_framework import serializers

from lesson1.models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'id name age course'.split()


class CourseSerializer(serializers.ModelSerializer):
    count = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Course
        fields = 'id name grade university count'.split()