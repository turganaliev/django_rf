from rest_framework import serializers

from lesson1.models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'id name age course'.split()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'id name grade university'.split()