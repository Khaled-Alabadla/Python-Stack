from django.db import models

class CourseManager(models.Manager):
    def create_course(self, name, description):
        course = self.create(name=name)
        CourseDescription.objects.create(course=course, description=description)
        return course
    
    def validate_course(self, name, description):
        
        errors = {}
        if len(name) < 5:
            errors['name'] = 'Course name must be at least 5 characters long.'
        if len(description) < 15:
            errors['description'] = 'Course description must be at least 15 characters long.'
        return errors
    
    def delete_course(self, pk):
        course = self.get(pk=pk)
        course.delete()
        return True
class Course(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    objects = CourseManager()

    def __str__(self):
        return self.name
    
class CourseDescription(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.name} Description"
    
class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.course.name} at {self.date}"
