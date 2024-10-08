# Generated by Django 4.2.15 on 2024-08-26 20:28

from django.db import migrations


def students_and_teachers_o2m_to_m2m(apps, schema_editor):
    Teacher = apps.get_model('school', 'Teacher')
    Student = apps.get_model('school', 'Student')

    for student in Student.objects.all():
        teacher = Teacher.objects.get(id=student.teacher_id)
        student.teachers.add(teacher)


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student_teachers_alter_student_group_and_more'),
    ]

    operations = [
        migrations.RunPython(students_and_teachers_o2m_to_m2m)
    ]
