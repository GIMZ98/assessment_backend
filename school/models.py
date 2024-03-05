from django.db import models

# School
class School(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20)

# Assessment Areas
class AssessmentArea(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20)

# Awards
class Award(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=50)

# Class
class Class(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20)

# Student
class Student(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    fullName = models.CharField(max_length=50)

# Subject
class Subject(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    subject = models.CharField(max_length=20)
    subject_score = models.IntegerField()

# Answer
class Answer(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    answer = models.CharField(max_length=100)

# Category
class Category(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=100)

# Correct Answer
class CorrectAnswer(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    answer = models.CharField(max_length=100)

# Summary
class Summary(models.Model):
    school_id = models.ForeignKey("School", to_field="id", on_delete=models.PROTECT, null=True)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.IntegerField()
    assessment_area_id = models.ForeignKey("AssessmentArea", to_field="id", on_delete=models.PROTECT, null=True)
    award_id = models.ForeignKey("Award", to_field="id", on_delete=models.PROTECT, null=True)
    class_id = models.ForeignKey("Class", to_field="id", on_delete=models.PROTECT, null=True)
    correct_answer_percentage_per_class = models.IntegerField()
    correct_answer = models.CharField(max_length=100)
    student_id = models.ForeignKey("Student", to_field="id", on_delete=models.PROTECT, null=True)
    participant = models.IntegerField()
    student_score = models.IntegerField()
    subject_id = models.ForeignKey("Subject", to_field="id", on_delete=models.PROTECT, null=True)
    category_id = models.ForeignKey("Category", to_field="id", on_delete=models.PROTECT, null=True)
    year_level_name = models.CharField(max_length=20)
    answer_id = models.ForeignKey("Answer", to_field="id", on_delete=models.PROTECT, null=True)
    correct_answer_id = models.ForeignKey("CorrectAnswer", to_field="id", on_delete=models.PROTECT, null=True)
