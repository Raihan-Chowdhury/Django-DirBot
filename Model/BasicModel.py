class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
        
    objects = models.Manager()

    class Meta:
        ordering = ['-created']
        managed = True
        db_table = 'Post'
