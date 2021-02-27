import json

import serializers as serializers
from django.shortcuts import render
from django.forms import model_to_dict
from django.http import HttpResponse

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lesson1.models import Student, Course
from lesson1.serializers import StudentSerializer, CourseSerializer


def get_students(request):
    students = Student.objects.all()    #list of objects
    list_student = []
    for i in students:
        list_student.append(model_to_dict(i))   #convert objects to dict
    json_data = json.dumps({'list': list_student})   #convert to json
    return HttpResponse(json_data)

@api_view(['GET'])
def get_drf_students(request):
    students = Student.objects.all()
    data = StudentSerializer(students, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_drf_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(data={'result': 'Student does not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = StudentSerializer(student).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_drf_courses(request):
    courses = Course.objects.all()
    data = CourseSerializer(courses, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_drf_course(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response(data={'result': 'Course does not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CourseSerializer(course).data
    return Response(data=data, status=status.HTTP_200_OK)